# -*- coding: UTF-8 -*-


print('--------------------- Customized parameters ---------------------')

api_key = '' #@param {type:"string"}
gpt_model = "text-davinci-003" #@param ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]
task_id = 4 #@param ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"] {type:"raw"}
task_id = int(task_id)
task_names = {
    1: 'clean a table using a vacuum cleaner',
    2: 'wash a glass',
    3: 'place food in the refrigerator',
    4: 'provide water for humans to drink',
    5: 'clean a sink',
    6: 'prepare a table for dining',
    7: 'prepare food for a user',
    8: 'make coffee',
    9: 'wash a plate in a sink',
    10: 'provide a user with a coke',
    11: 'provide a user with a burger',
    12: 'clean a glass'}

task_name = task_names[task_id]

#@markdown Here are parameters relevant to LLM:  <br>
ratio_object = "1.0" #@param ["0.5"] {allow-input: true}
ratio_object = float(ratio_object)
ratio_appliance = "1.0" #@param ["0.5"] {allow-input: true}
ratio_appliance = float(ratio_appliance)
prompt_keyword = "sutiable" #@param ["sutiable"] {allow-input: true}
ratio_1object = "0.7" #@param ["0.75"] {allow-input: true}
ratio_1object = float(ratio_1object)


print('--------------------- Setup ---------------------')
# Import third-party packages

import openai
import random
import getpass
import numpy as np
import math
import re
import time
from random import sample
import shutil
import glob
from google.colab import files
import os
import gc
import sys


# Install pddl and its planner

#  Utils
from utils import *

#  Situation dataset
from situation_dataset import *

# Rule-based action translator
from rule_based_translator import *



print('--------------------- PDDL-based task planning ---------------------')

# Define constants for all tasks
from pddl_based_planning import *

# Define actions, domain and problem for tasks
from task1_actions_domain_problem import *

# Write domain and problem, and run planner
from write_domain_planning import *




print('--------------------- Simulate a situation ---------------------')
debug = True #@param {type:"boolean"}
debug_situation_index = 0 #@param {type:"integer"}
situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action = situation_simulator(task_id, debug, debug_situation_index)

'''
process a special situation: object in the situation != object in the manipulation, e.g.,
situation: the outlet_1 is not available;
object in situation: outlet;
object name in situation: outlet_1
object manipulated by robot: vacuum_1;
'''

situation_objectName_concrete = extract_objectName_inSituation(path_plan_init, situation_object)
manipulation_objectName_concrete = extract_objectName_inManipulation(path_plan_init, situation_action)

print('!Note: A situation is randomly simualted:')
if situation_objectName_concrete!='None':
  print('situation (index {}): {}'.format(situation_index, situation.replace(situation_object, situation_objectName_concrete)))
else:
  print('situation({}): {}'.format(situation_index, situation))
print('opposite situation:', situation_opp)
print('corresponding predicate:', situation_predicate)
print('action that exists situation:', situation_action)
print('object in situation:', situation_objectName_concrete)
print('object manipulated by robot:', manipulation_objectName_concrete)

# test
# temp1 = situation
# temp2 = situation_opp
# situation = temp2
# situation_opp = temp1
# print('-'*25)
# print('situation:', situation)
# print('opposite situation:', situation_opp)



print('--------------------- Plan Monitor & Knowledge Extractor ---------------------')

#  Check action feasibility under a situation
#@title Check action feasibility under a situation {display-mode: "form"}
action_index = 0
result_monitor = False  # False: one action cannot be executed
signal_traversed = False  # True: all actions in the checklist are examined

while action_index < len(plan_init) and (not result_monitor) and (not signal_traversed):
  action_encoded = extract_ithAction(action_index, path_plan_init)
  if situation_action not in action_encoded:
    action_index += 1
    print('action {} is executed!'.format(action_encoded))
  else:
    print('!Note: The action feasibility is checking!')
    check_list = plan_init[action_index:]
    counter_check = 0
    for checked_action in check_list:
      counter_check = counter_check + 1
      if '_' in checked_action[0] and 'serve' not in checked_action[0]:  # skip checking actions that don's have objects, such as 'walk'
        checked_action_decoded = action_translator(checked_action, task_id)
        print('unexecuted action (encoded): {}; (decoded): {}'.format(checked_action, checked_action_decoded))
        result_monitor = plan_monitor(situation, checked_action_decoded, 'suitable') # call plan monitor
        if result_monitor:
          print('!Note: The action cannot be executed according to LLM response!')
          break
        else:
          if counter_check == len(check_list):
            signal_traversed = True
      else:
        continue


#  Add action constraint
#@title Add action constraint {display-mode: "form"}
'''
# if plan cannot be executed, augment the robot’s action knowledge with task-oriented common sense
'''
if result_monitor:
  key1, key2, key3 = 'domain_' + str(task_id), 'problem_' + str(task_id), 'dy_init_' + str(task_id)
  path_domain_constraint, path_problem_constraint = plan_modifier_add_constraint(names[key1], names[key2], names[key3], task_id, situation_action, situation_predicate, situation_objectName_concrete, names)
  try:
    path_plan_constraint = task_planner(path_domain_constraint, path_problem_constraint, 'plan_constraint.txt')
    print('!Note: A plan {} is generated.'.format('plan_constraint.txt'))
    print_plan(path_plan_constraint)
    plan_constraint = read_plan(path_plan_constraint)
    exist_plan_constraint = True
  except:
    exist_plan_constraint = False
    print('!Note: No plan is found after constraint is added!')




# Add action effect by using other objects
#@title Add action effect by using other objects {display-mode: "form"}
'''
# if plan under constraint cannot be executed, augment the robot’s action knowledge with task-oriented common sense
'''
if result_monitor and not exist_plan_constraint:
  object_list = select_object(task_id, ratio_object)
  capable_objects = []  # save potentially useful objects
  for item in object_list:
    if llm_object(path_plan_init, situation_object, item, 'suitable'):
      capable_objects.append(item)

  selected_object = None
  if len(capable_objects) == 1:
    selected_object = capable_objects[0]
  elif len(capable_objects) > 1:
    selected_object = llm_object_most(task_name, capable_objects)
  print('selected_object: {}'.format(selected_object))

  if selected_object:
    selected_object = selected_object.replace(' ', '_')
    path_domain_object, path_problem_object = plan_modifier_add_effect_object(task_id, situation_objectName_concrete, selected_object, names)

    try:
      path_plan_object = task_planner(path_domain_object, path_problem_object, 'plan_object.txt')
      print('!Note: A plan {} is generated:'.format('plan_object.txt'))
      print_plan(path_plan_object)
      plan_object = read_plan(path_plan_object)
      exist_plan_object = True
    except:
      exist_plan_object = False
      print('!Note: No plan is found after a new object is added!')
  else:
    exist_plan_object = False
    print('!Note: No new object can be used to solve the situation!')




# Add action effect by using other appliance
#@title Add action effect by using other appliance {display-mode: "form"}
'''
# if plan under constraint cannot be executed, augment the robot’s action knowledge with task-oriented common sense
'''
if result_monitor and not exist_plan_constraint:
  appliance_list = select_appliance(task_id, ratio_appliance)
  capable_appliances = []  # save potentially useful appliances
  for item in appliance_list:
    if llm_appliance(situation, situation_opp, item, task_id):
      capable_appliances.append(item)

  selected_appliance = None
  if len(capable_appliances) == 1:
    selected_appliance = capable_appliances[0]
  elif len(capable_objects) > 1:
    selected_appliance = llm_appliance_most(situation, situation_opp, capable_appliances)
  print('selected_appliance: {}'.format(selected_appliance))

  if selected_appliance:
    selected_appliance = selected_appliance.replace(' ', '_')
    path_domain_appliance, path_problem_appliance = plan_modifier_add_effect_appliance(task_id, situation_predicate, situation_objectName_concrete, selected_appliance, names)

    try:
      path_plan_appliance = task_planner(path_domain_appliance, path_problem_appliance, 'plan_appliance.txt')
      print('!Note: A plan {} is generated:'.format('plan_appliance.txt'))
      print_plan(path_plan_appliance)
      plan_appliance = read_plan(path_plan_appliance)
      exist_plan_appliance = True
    except:
      exist_plan_appliance = False
      print('!Note: No plan is found after a new appliance is added!')
  else:
    exist_plan_appliance = False
    print('!Note: No new appliance can be used to solve the situation!')


print('--------------------- Check result ---------------------')
# @title
if result_monitor:
  if situation_objectName_concrete!='None':
    print('situation (index {}): {}'.format(situation_index, situation.replace(situation_object, situation_objectName_concrete)))
  else:
    print('situation({}): {}'.format(situation_index, situation))
  if exist_plan_constraint:
    print('!Note: A plan_constraint is found to solve the situation!')
    print_plan(path_plan_constraint)
  if exist_plan_object:
    print('!Note: A plan_object is found to solve the situation!')
    print_plan(path_plan_object)
  if exist_plan_appliance:
    print('!Note: A plan_appliance is found to solve the situation!')
    print_plan(path_plan_appliance)
  if not exist_plan_constraint and not exist_plan_object and not exist_plan_appliance:
    print('!Note: No feasible alternative plan to solve the situation!')





