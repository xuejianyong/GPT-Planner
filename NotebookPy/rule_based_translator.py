#@title Rule-based action translator {display-mode: "form"}
def action_translator(action, task_id): # translate action into natural language
  action = process(action) # remove '_X'; e.g., vacuum_1 -> vacuum
  sentence = None # generate a complete sentence

  if task_id == 1:
    if 'walk' in action[0]:
      sentence = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'putdown_vacuum' in action[0]:
      sentence = 'a robot puts down a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_vacuum' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'plug_vacuum' == action[0]:
      sentence = 'a robot plugs a ' + action[2] + ' into a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'turnon_vacuum' in action[0]:
      sentence = 'a robot turns on a ' + action[1] + '.'
    if 'clean_table' in action[0]:
      sentence = 'a robot cleans a ' + action[3] + ' using a ' + action[2] + ' in a ' + action[4] + ' room.'
    if 'turnoff_vacuum' in action[0]:
      sentence = 'a robot turns off a ' + action[1] + '.'
    if 'unplug_vacuum' == action[0]:
      sentence = 'a robot unplugs a ' + action[2] + ' from a ' + action[3] + ' in a ' + action[4] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 2:
    if 'walk' in action[0]:
      sentence = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_glass' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'find_glass' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'find_sink' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_glass' == action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' from a ' + action[3] + ' in a ' + action[3] + ' room.'
    if 'place_glass' == action[0]:
      sentence = 'a robot places a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'find_soap' == action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_soap' == action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'place_soap' == action[0]:
      sentence = 'a robot places a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'find_faucet' == action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'turnon_faucet' == action[0]:
      sentence = 'a robot turns on a ' + action[2] + ' in a ' + action[4] + ' room.'
    if 'wash_glass' == action[0]:
      sentence = 'a robot washs a glass'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 3:
    if 'walk' in action[0]:
      sentence = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_food' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'grasp_food' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' from a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'move_food' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'place_food' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'find_refrigerator' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'open_refrigerator' in action[0]:
      sentence = 'a robot opens a ' + action[2] + ' and places a ' + action[3] + ' in it in a ' + action[4] + ' room.'
    if 'close_refrigerator' in action[0]:
      sentence = 'a robot closes a ' + action[2] + ' in a ' + action[3] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 4:
    if 'walk' in action[0]:
      sentence = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_faucet' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'turnon_faucet' in action[0]:
      sentence = 'a robot turns on a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_cup' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_cup' == action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'fill_cup' in action[0]:
      sentence = 'a robot fills a ' + action[2] + ' with water from a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'move_cup' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'place_cup' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 5:
    if 'walk' in action[0]:
      sentence = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_sink' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_cloth' in action[0]:
      sentence = 'a robot finds a dish ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'grasp_cloth' in action[0]:
      sentence = 'a robot grasps a dish ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_cloth' in action[0]:
      sentence = 'a robot moves a dish ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'place_cloth' in action[0]:
      sentence = 'a robot places a dish ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'find_detergent' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'grasp_detergent' in action[0]:
      sentence = 'a robot grasps a bottle of ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_detergent' in action[0]:
      sentence = 'a robot moves a bottle of ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'squeeze_detergent' in action[0]:
      sentence = 'a robot squeezes a bottle of ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'place_detergent' in action[0]:
      sentence = 'a robot places a bottle of ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'wipe_sink' in action[0]:
      sentence = 'a robot wipes a ' + action[2] + ' in a ' + action[4] + ' room.'
    if 'find_faucet' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'turnon_faucet' in action[0]:
      sentence = 'a robot turns on a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'turnoff_faucet' in action[0]:
      sentence = 'a robot turns on a ' + action[2] + ' in a ' + action[3] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 6:
    if 'walk' in action[0]:
      sentence = 'a robot walks ' + 'from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_plate' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_cupboard' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'open_cupboard' in action[0]:
      sentence = 'a robot opens a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'close_cupboard' in action[0]:
      sentence = 'a robot closes a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_plate' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' from a ' + action[3] + '.'
    if 'move_plate' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'place_plate' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' on a ' + action[3] + ' to a ' + action[4] + ' room.'
    if 'find_fork' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_fork' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + '.'
    if 'move_fork' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'place_fork' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'serve_table' in action[0]:
      sentence = 'a robot has already set the table.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 7:
    if 'walk' in action[0]:
      sentence = 'a robot walks ' + 'from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'open_refrigerator' in action[0]:
      sentence = 'a robot opens a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_food' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'grasp_food' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'move_food' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'open_microwave' in action[0]:
      sentence = 'a robot opens a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'place_food' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'close_microwave' in action[0]:
      sentence = 'a robot closes a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'turnon_microwave' in action[0]:
      sentence = 'a robot turns on a ' + action[2] + ' in a ' + action[4] + ' room.'
    if 'close_refrigerator' in action[0]:
      sentence = 'a robot closes a ' + action[2] + ' in a ' + action[3] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 8:
    if 'walk' in action[0]:
      sentence = 'a robot walks ' + 'from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_bean' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_bean' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_bean' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'open_maker' in action[0]:
      sentence = 'a robot opens a coffee ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'place_bean' in action[0]:
      sentence = 'a robot places a coffee ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'close_maker' in action[0]:
      sentence = 'a robot closes a coffee ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_cup' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_cup' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_cup' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'place_cup' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' in a coffee ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'turnon_maker' in action[0]:
      sentence = 'a robot turns on a coffee ' + action[2] + ' in a ' + action[5] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 9:
    if 'walk' in action[0]:
      sentence = 'a robot walks ' + 'from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_plate' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' from a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'find_plate' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'place_plate' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'find_sink' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_plate' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'wash_plate' in action[0]:
      sentence = 'a robot washs a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 10:
    if 'walk' in action[0]:
      sentence = 'a robot walks ' + 'from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_glass' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_glass' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_glass' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'place_glass' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' on a table in ' + action[4] + ' room.'
    if 'find_coke' in action[0]:
      sentence = 'a robot finds a bottle of ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_coke' in action[0]:
      sentence = 'a robot grasps a bottle of ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_coke' in action[0]:
      sentence = 'a robot moves a bottle of ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room.'
    if 'pour_coke' in action[0]:
      sentence = 'a robot pours a bottle of ' + action[2] + ' into a ' + action[3] + ' in a ' + action[4] + ' room.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 11:
    if 'walk' in action[0]:
      sentence = 'a robot walks ' + 'from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_plate' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_plate' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_plate' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to a ' + action[4] + ' room near a table.'
    if 'place_plate' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' on a table ' + ' in a ' + action[4] + ' room.'
    if 'find_fork' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_fork' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_fork' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to ' + action[4] + ' room.'
    if 'place_fork' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' on a plate in ' + action[3] + ' room.'
    if 'find_chair' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'pull_chair' in action[0]:
      sentence = 'a robot pulls up a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_burger' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_burger' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_burger' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to ' + action[4] + ' room.'
    if 'place_burger' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'serve_burger' in action[0]:
      sentence = 'a robot has already prepared the burger.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence

  if task_id == 12:
    if 'walk' in action[0]:
      sentence = 'a robot walks ' + 'from a ' + action[2] + ' room to a ' + action[3] + ' room.'
    if 'find_table' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'find_glass' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'grasp_glass' in action[0]:
      sentence = 'a robot grasps a ' + action[2] + ' on a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'move_glass' in action[0]:
      sentence = 'a robot moves a ' + action[2] + ' in a ' + action[3] + ' room to ' + action[4] + ' room.'
    if 'place_glass' in action[0]:
      sentence = 'a robot places a ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'find_detergent' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'grasp_detergent' in action[0]:
      sentence = 'a robot grasps a bottle of ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'move_detergent' in action[0]:
      sentence = 'a robot moves a bottle of ' + action[2] + ' in a ' + action[3] + ' room to ' + action[4] + ' room.'
    if 'find_dishwasher' in action[0]:
      sentence = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'open_dishwasher' in action[0]:
      sentence = 'a robot opens a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'squeeze_detergent' in action[0]:
      sentence = 'a robot squeeze a bottle of ' + action[2] + ' in a ' + action[3] + ' in a ' + action[4] + ' room.'
    if 'place_detergent' in action[0]:
      sentence = 'a robot places a bottle of ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'close_dishwasher' in action[0]:
      sentence = 'a robot closes a ' + action[2] + ' in a ' + action[3] + ' room.'
    if 'turnon_dishwasher' in action[0]:
      sentence = 'a robot cleans a glass.'
    if sentence is None:
      print('!Error: not find corresponding action.')
      sys.exit(0)
    else:
      return sentence