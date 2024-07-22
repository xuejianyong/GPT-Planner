import os
from utils import *
import sys


print('--------------------- Write domain and problem, and run planner ---------------------')
#@title Write domain and problem, and run planner {display-mode: "form"}
remove_existFiles('/content')
remove_existFolder('/content/tasks')

# if not os.path.exists('tasks'): # domain and problem files for each task are stored in /content/tasks
#   !mkdir tasks

os.chdir('/content/tasks');
for i in range(1, 13):
  if not os.path.exists(f'task{i}'):
    os.mkdir(f'task{i}')
os.chdir('/content');

key1, key2 = 'domain_' + str(task_id), 'problem_' + str(task_id)
write_domain(names[key1], f'/content/tasks/task{task_id}/domain_intial.pddl')
write_problem(names[key2], f'/content/tasks/task{task_id}/problem_intial.pddl')

# Run fast downward
path_domain = f'/content/tasks/task{task_id}/domain_intial.pddl'
path_problem = f'/content/tasks/task{task_id}/problem_intial.pddl'
try:
  path_plan_init = task_planner(path_domain, path_problem, 'initial_plan.txt')
  print('!Note: A plan {} is generated:'.format('initial_plan.txt'))
  print_plan(path_plan_init)
  plan_init = read_plan(path_plan_init)
except:
  print('!Error: No inital plan is found!')
  sys.exit(0)

# debug_action_translator(task_id, path_plan_init)