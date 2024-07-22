print('--------------------- Utils ---------------------')
#@title Utils {display-mode: "form"}
openai.api_key = api_key

def remove_existFiles(folder_path): # remove files end with suffix in a specific folder
  suffix = '.txt'
  for file in glob.glob(f'{folder_path}/*'):
    if file.endswith(suffix):
      os.remove(file)
      print('!Note: The old file {} have been removed.'.format(file))

def remove_existFolder(folder_path): # remove a folder
  if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    print('!Note: The old folder {} have been removed.'.format(folder_path))

def write(content, path): # write content to a file
  with open(path, 'w') as f:
    f.write('{}'.format(content))
  f.close()

def write_domain(domain, path_domain): # write the domain to domain.pddl file
  write(domain_to_string(domain), path_domain)
  print(f'!Note: domain.pddl file has been written to {path_domain}.')

def write_problem(problem, path_problem): # write the problem to problem.pddl file
  write(problem_to_string(problem), path_problem)
  print(f'!Note: problem.pddl file has been written to {path_problem}.')

def task_planner(path_domain, path_problem, output): # run task planner
  path_engine = '/content/downward/fast-downward.py'
  if os.path.exists(path_engine):
    command = 'python ' + path_engine + ' --alias lama-first ' + '--plan-file ' + output + ' ' + path_domain + ' ' + path_problem
    os.system(command + '>/dev/null 2>&1')  # skip outputting intermediate results
    return '/content/' + output
  else:
    print('!Error: Cannot find the executable file fast-downward.py in{}.\n'.format(path_engine))
    sys.exit(0)

def print_plan(path_file): # print the plan in the txt file
  with open(path_file, 'r') as fidin:
    for line in fidin:
      print(line.strip())
  fidin.close()

def read_plan(path_file): # read the plan in the txt file
  with open(path_file, 'r') as fidin:
    plan = [line.strip()[1:-1].split(' ') for line in fidin.readlines() if line.strip()]
  fidin.close()
  return plan[:-1]

def generate_predicate(situation): # generate a predicate
  response = openai.Completion.create(
    engine=gpt_model,
    prompt="tranlate a sentence into a predicate\n\n####\nsentence: The cup is broken.\npredicate: "
            "cup_is_broken\n\n####\nsentence: No water comes out of faucet.\npredicate: "
            "faucet_no_water\n\n####\nsentence: " + situation + "'\npredicate:",
    temperature=0,
    max_tokens=20,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=['\\n', '.'])
  result = response['choices'][0]
  return result['text'][1:]

def objectName_inPlan(path_file): # extract all object names (concrete) from a plan
  plan = read_plan(path_file)
  objects = set()
  for action in plan:
    for index, item in enumerate(action):
      if index!=0 and ('robot' not in item) and ('dining' not in item) and ('kitchen' not in item):
        objects.add(item)
  return list(objects)

def extract_objectName_inSituation(path_file, situation_object): # extract object name (concrete) in a situation
  '''
  situation_object: vacuum
  this function is used to extract object name in the plan (e.g., vacuum_1).
  '''
  objects_name = objectName_inPlan(path_file) # concrete
  situation_object = situation_object.split(' ')[0] # abstract, 'vacuum power cord' --> 'vacuum'
  situation_objectName_concrete = 'None'
  for item in objects_name:
    if situation_object in item:
      situation_objectName_concrete = item
      break
  return situation_objectName_concrete

def extract_objectName_inManipulation(path_file, situation_action):
  '''
  situation_action: grasp_vacuum
  this function is used to extract object name in the plan that is manipulated by robot (e.g., vacuum_1).
  '''
  objects_name = objectName_inPlan(path_file)
  manipulation_objectName_concrete = 'None'
  if '_' in situation_action:
    manipulate_object = situation_action.split('_')[1]
    for item in objects_name:
      if manipulate_object in item:
        manipulation_objectName_concrete = item
        break
  return manipulation_objectName_concrete

def extract_ithAction(step, path_plan): # extract i-th action in the plan
  with open(path_plan, 'r') as fidin:
    plan = [line.strip()[1:-1].split(' ') for line in fidin.readlines() if line.strip()]
  fidin.close()
  return plan[:-1][step]

def llm(prompt):
  sampling_params = {"n": 1,  # sampling number
                      "max_tokens": 32,
                      "temperature": 0,
                      "top_p": 1,
                      "logprobs": 1,
                      "presence_penalty": 0,
                      "frequency_penalty": 0,
                      "stop": ['\\n', '.']}
  raw_response = openai.Completion.create(engine=gpt_model, prompt=prompt, **sampling_params)
  responses = [raw_response['choices'][i]['text'] for i in range(sampling_params['n'])]
  mean_probs = [math.exp(np.mean(raw_response['choices'][i]['logprobs']['token_logprobs'])) for i in range(sampling_params['n'])]
  responses = [sample.strip().lower() for sample in responses]
  return responses, mean_probs

def select_object(task_id, ratio_object):
  utensils = ['dish', 'cleaning bottle', 'cooking pot', 'frying pan', 'trash can', 'cloth napkin', 'paper towel', 'bucket', 'coffee cup', 'colander', 'condiment bottle', 'dish bowl', 'drinking glass', 'measuring cup', 'mug', 'rag', 'wine glass', 'chef knife', 'condiment shaker', 'cutlery fork', 'cutlery knife', 'cutting board', 'dish rack', 'oven tray', 'mat', 'wooden spoon', 'sponge', 'coffee filter', 'wooden chopstick']
  beverages = ['beer', 'milk', 'watermelon juice', 'alcohol', 'coffee', 'orange juice', 'tea', 'wine']
  furnitures = ['bookshelf', 'closet', 'cpu table', 'cupboard', 'desk', 'kitchen cabinet', 'nightstand', 'wooden chair', 'piano bench', 'table cloth', 'coffee table', 'couch', 'dining table', 'kitchen table', 'kitchen counter', 'pantry']
  foods = ['bread', 'cake', 'ice cream', 'noodles', 'oatmeal', 'peanut butter', 'rice', 'salt', 'snack', 'sugar', 'oil', 'pasta', 'chips', 'sauce', 'steak']
  task_objects = {
    1: utensils + furnitures,
    2: utensils + furnitures,
    3: utensils + furnitures + foods,
    4: utensils + furnitures,
    5: utensils + furnitures,
    6: utensils + furnitures,
    7: utensils + furnitures + foods,
    8: utensils + furnitures + beverages,
    9: utensils + furnitures,
    10: utensils + furnitures + beverages,
    11: utensils + furnitures + foods,
    12: utensils + furnitures}
  if task_id in task_objects:
    objects = task_objects[task_id]
  else:
    print('!Error: task_id={} not in task_objects.\n'.format(task_id))
    sys.exit(0)
  objects_selected = sample(objects, round(len(objects) * ratio_object))
  print('!Note: objects that the robot can use in the environment: {}'.format(objects_selected))
  return objects_selected

def select_appliance(task_id, ratio_appliance):
  appliances = ['blender', 'dishwasher', 'freezer', 'microwave', 'refrigerator', 'oven', 'stove', 'washing machine', 'kettle', 'vacuum cleaner', 'toaster', 'air fryer', 'dehumidifier', 'water boiler', 'ice cream maker', 'juicer', 'water filter', 'coffee maker']
  appliances_selected = sample(appliances, round(len(appliances) * ratio_appliance))
  print('!Note: appliances that the robot can use in the environment: {}'.format(appliances_selected))
  return appliances_selected

def plan_modifier_add_constraint(domain, problem, dy_init, task_id, situation_action, situation_predicate, situation_objectName_concrete, names):
  '''
  task_id: e.g., 1
  situation_action: e.g., turnon_vacuum
  situation_predicate: e.g., power_outage/vaccum_broken
  situation_objectName_concrete: e.g., None/vaccum
  '''
  # define hard constraint
  constraint = situation_predicate
  situation_objectName_abstract = situation_objectName_concrete.split('_')[0]
  if situation_objectName_concrete != 'None':
    names[constraint] = Predicate(constraint, names[situation_objectName_abstract[:4]])
  else:
    names[constraint] = Predicate(constraint, names['othe']) # exist 'unknown' object, e.g., power

  # revise action's precondition by adding hard constraint
  if ~names[constraint] not in gc.get_referents(names[situation_action].precondition)[0]['_operands']:
    gc.get_referents(names[situation_action])[0]['_precondition'] = names[situation_action].precondition & ~names[constraint]

  # revise action's parameters
  if situation_objectName_concrete != 'None' and names[situation_objectName_abstract[:4]] not in names[situation_action].parameters:
    gc.get_referents(names[situation_action])[0]['_parameters'] = names[situation_action].parameters + (names[situation_objectName_abstract[:4]],)
  elif situation_objectName_concrete == 'None' and othe not in names[situation_action].parameters:
    gc.get_referents(names[situation_action])[0]['_parameters'] = names[situation_action].parameters + (othe,)

  # revise domain's predicates
  gc.get_referents(domain)[0]['_predicates'] = domain.predicates.union(frozenset({names[constraint]}))

  # revise problem's initial state
  if situation_objectName_concrete != 'None' and names[constraint](names[situation_objectName_concrete]) not in dy_init:
    dy_init.append(names[constraint](names[situation_objectName_concrete]))
    gc.get_referents(problem)[0]['_init'] = dy_init
  elif situation_objectName_concrete == 'None' and names[constraint](names['other_1']) not in dy_init:
    dy_init.append(names[constraint](names['other_1']))
    gc.get_referents(problem)[0]['_init'] = dy_init

  # revise problem's objects
  if situation_objectName_concrete != 'None' and names[situation_objectName_concrete] not in names[situation_action].parameters:
    gc.get_referents(problem)[0]['_objects'] = problem.objects.union(frozenset({names[situation_objectName_concrete]}))
  elif situation_objectName_concrete == 'None' and other_1 not in names[situation_action].parameters:
    gc.get_referents(problem)[0]['_objects'] = problem.objects.union(frozenset({other_1}))

  print('!Note: The constraint {} has been added in action {}!'.format(~names[constraint], gc.get_referents(names[situation_action])[0]['_name']))
  path_domain_constraint = f'/content/tasks/task{task_id}/domain_constraint.pddl'
  path_problem_constraint = f'/content/tasks/task{task_id}/problem_constraint.pddl'
  write_domain(domain, path_domain_constraint)
  write_problem(problem, path_problem_constraint)
  return path_domain_constraint, path_problem_constraint

def process(action): # remove '_X'; e.g., vacuum_1 -> vacuum
  action_qualified = []
  for index, item in enumerate(action):
    if index >= 1 and '_' in item:
      item = item[:-2]
      action_qualified.append(item)
    else:
      action_qualified.append(item)
  return action_qualified

def debug_action_translator(task_id, path_plan):
  plan = read_plan(path_plan)
  plan_decoded = []
  for i in range(len(plan)):
    action_encoded = extract_ithAction(i, path_plan)
    action_decoded = action_translator(extract_ithAction(i, path_plan), task_id)
    print('task:{}, action:{}\naction_decoded:{}\n'.format(task_name, action_encoded, action_decoded))

def prompt_plan_monitor(prompt_keyword, action_decoded, situation):
  prompt = 'is it ' + prompt_keyword + ' that ' + action_decoded[:-1] + ' if ' + situation[:-1] + '?' + ' Please answer yes or no.'
  return prompt

def plan_monitor(situation, action_decoded, prompt_keyword):
  prompt = prompt_plan_monitor(prompt_keyword, action_decoded, situation)
  try:
      responses, probs = llm(prompt)
      print('raw prompt: {}; response: {}'.format(prompt, responses[0]))
      if 'no' in responses[0]:
        return True
      else:
        return False
  except:
      print('!Error: no response from LLM!')
      sys.exit(0)

def prompt_knowledge_extractor_object(prompt_keyword, action_decoded_temp):
  prompt = 'is it ' + prompt_keyword + ' that ' + action_decoded_temp + '?' + ' Please answer yes or no.'
  return prompt

def llm_object(path_plan, situation_object, item, prompt_keyword):
  plan = read_plan(path_plan)
  plan_decoded = [action_translator(extract_ithAction(i, path_plan), task_id) for i in range(len(plan))]
  result_list = []
  for action_decoded in plan_decoded:
    if (situation_object in action_decoded) and ('find' not in action_decoded) and ('serve' not in action_decoded):
      action_decoded_temp = action_decoded.replace(situation_object, item, 1)[:-1]
      prompt = prompt_knowledge_extractor_object(prompt_keyword, action_decoded_temp)
      try:
        responses, probs = llm(prompt)
        print('raw prompt: {}; response: {}'.format(prompt, responses[0]))
        if 'no' in responses[0]: #save llm's response in result_list
          result_list.append('no')
          break
        else:
          result_list.append('yes')
      except:
        print('!Error: no response in llm (object)!')
        sys.exit(0)
  return 'no' not in result_list and bool(result_list)

def prompt_knowledge_extractor_object_most(candidate_object, task_name):
  prompt = 'there are some objects, such as ' + ', '.join(candidate_object) + \
             '. which object is the most suitable for the task of ' + task_name + '?' + ' if ' + situation[:-1] + '?'
  return prompt

def llm_object_most(task_name, candidate_objects):
  prompt = prompt_knowledge_extractor_object_most(candidate_objects, task_name)
  try:
      responses, probs = llm(prompt)
      print('raw prompt: {}; response: {}'.format(prompt, responses[0]))
  except:
      print('!Error: no response in llm (object_most)!')
      sys.exit(0)
  return next((item for item in candidate_objects if item in responses[0]), None)

def plan_modifier_add_effect_object(task_id, situation_objectName_concrete, selected_object, names):
  key1, key2, key3, key4 = 'domain_' + str(task_id), 'problem_' + str(task_id), 'dy_init_' + str(task_id), 'dy_init_' + str(task_id) + '_content'
  domain = names[key1]
  problem = names[key2]
  dy_init = names[key3]
  dy_init_content = names[key4]

  # revise problem's objects
  gc.get_referents(problem)[0]['_objects'] = problem.objects.union(frozenset({names[selected_object]}))

  # revise problem's initial state
  dy_init_supplement = []
  for item in dy_init_content: # copy initial predicate, e.g, cup - mug
    if situation_objectName_concrete in item:
      index = item.index(situation_objectName_concrete)
      item[index] = item[index].replace(situation_objectName_concrete, selected_object)
      try:
        if len(item) == 2:
          dy_init_supplement.append(names[item[0]](names[item[1]]))
        elif len(item) == 3:
          dy_init_supplement.append(names[item[0]](names[item[1]], names[item[2]]))
        elif len(item) == 4:
          dy_init_supplement.append(names[item[0]](names[item[1]], names[item[2]], names[item[3]]))
        else:
          print('!Error: Cannot convert predicate')
          sys.exit(0)
      except:
        print('!Note: Object\'s class is wrong!')
  dy_init = dy_init + dy_init_supplement
  gc.get_referents(problem)[0]['_init'] = dy_init

  print('!Note: The new object {} has been added!'.format(selected_object))
  path_domain_object = f'/content/tasks/task{task_id}/domain_object.pddl'
  path_problem_object = f'/content/tasks/task{task_id}/problem_object.pddl'
  write_domain(domain, path_domain_object)
  write_problem(problem, path_problem_object)
  return path_domain_object, path_problem_object

def prompt_knowledge_extractor_appliance(situation, candidate_appliance, opp_situation):
  prompt = 'can a ' + candidate_appliance + ' make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '?' + ' Please answer yes or no.'
  return prompt

def llm_appliance(situation, opp_situation, candidate_appliance, task_id):
  prompt = prompt_knowledge_extractor_appliance(situation, candidate_appliance, opp_situation)
  try:
    responses, probs = llm(prompt)
    print('raw prompt: {}; response: {}'.format(prompt, responses[0]))
    if 'no' in responses[0]:
      return False
    else:
      return True
  except:
    print('！Error: No response in llm (appliance)!')
    sys.exit(0)

def prompt_knowledge_extractor_appliance_most(situation, candidate_appliances, opp_situation):
  prompt = 'there are some appliances, such as ' + ', '.join(candidate_appliances) + '. which appliance is the most possible to make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '?'
  return prompt

def llm_appliance_most(situation, opp_situation, candidate_appliances):
  prompt = prompt_knowledge_extractor_appliance_most(situation, candidate_appliances, opp_situation)
  try:
    responses, probs = llm(prompt)
    print('raw prompt: {}; response: {}'.format(prompt, responses[0]))
  except:
    print('！Error: No response in llm (appliance)!')
  return next((item for item in candidate_appliances if item in responses[0]), None)

def plan_modifier_add_effect_appliance(task_id, situation_predicate, situation_objectName_concrete, selected_appliance, names):
  key1, key2, key3 = 'domain_' + str(task_id), 'problem_' + str(task_id), 'dy_init_' + str(task_id)
  domain = names[key1]
  problem = names[key2]
  dy_init = names[key3]

  effect = situation_predicate
  situation_objectName_abstract = situation_objectName_concrete.split('_')[0]
  if situation_objectName_concrete != 'None':
    names[effect] = Predicate(effect, names[situation_objectName_abstract[:4]])
  else:
    names[effect] = Predicate(effect, names['othe']) # exist 'unknown' object, e.g., power

  # revise 'operate' parameters
  if situation_objectName_concrete != 'None' and names[situation_objectName_abstract[:4]] not in names['operate'].parameters:
    gc.get_referents(names['operate'])[0]['_parameters'] = names['operate'].parameters + (names[situation_objectName_abstract[:4]],)
  elif situation_objectName_concrete == 'None' and othe not in names['operate'].parameters:
    gc.get_referents(names['operate'])[0]['_parameters'] = names['operate'].parameters + (othe,)

  # revise 'operate' effect
  if ~names[effect] not in gc.get_referents(names['operate'].effect)[0]['_operands']:
    gc.get_referents(names['operate'])[0]['_effect'] = names['operate'].effect & ~names[effect]

  # revise problem's objects
  gc.get_referents(problem)[0]['_objects'] = problem.objects.union(frozenset({names[selected_appliance]}))


  # revise problem's initial state
  if 'washing_machine' in selected_appliance or 'dehumidifier' in selected_appliance:
    location = 'basement'
  else:
    location = 'kitchen'
  if appliance_at(names[selected_appliance], names[location]) not in dy_init:
    dy_init.append(appliance_at(names[selected_appliance], names[location]))
    gc.get_referents(problem)[0]['_init'] = dy_init

  print('!Note: The new appliance {} has been added!'.format(selected_appliance))
  path_domain_appliance = f'/content/tasks/task{task_id}/domain_appliance.pddl'
  path_problem_appliance = f'/content/tasks/task{task_id}/problem_appliance.pddl'
  write_domain(domain, path_domain_appliance)
  write_problem(problem, path_problem_appliance)
  return path_domain_appliance, path_problem_appliance





