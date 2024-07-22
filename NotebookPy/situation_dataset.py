
#@title Situation dataset {display-mode: "form"}
def situation_simulator(task_id, debug, debug_situation_index):
  if task_id == 1:
    situations = {
        0: 'there is a power outage.',
        1: 'the vacuum is not working.',
        2: 'the vacuum is missing.',
        3: 'the vacuum cannot be turned on.',
        4: 'the vacuum plug is damaged.',
        5: 'the outlet is not available.',
        6: 'the vacuum is not plugged.',
        7: 'the vacuum canister is full.',
        8: 'the vacuum power cord is too short.',
        9: 'the robot cannot reach the vacuum.',
        10: 'the vacuum switch is not working.',
        11: 'the vacuum power cord is broken.',
        12: 'the vacuum is battery powered and does not need plug in.',
        13: 'the robot slips and falls.',
        14: 'the robot drops the vacuum.',
        15: 'the outlet is broken.'
    }

    situations_opp = {
        0: 'power available.',
        1: 'vacuum work.',
        2: 'vacuum found.',
        3: 'vacuum turned on.',
        4: 'vacuum plug good to use.',
        5: 'outlet found.',
        6: 'vacuum plugged.',
        7: 'vacuum canister empty.',
        8: 'vacuum power cord long enough.',
        9: 'robot reaching the vacuum.',
        10: 'vacuum switch working.',
        11: 'vacuum power cord good to use.',
        12: 'mains-powered.',
        13: 'robot standing.',
        14: 'robot picking up vacuum.',
        15: 'outlet good.'
    }

    situations_object = {
        0: 'power',
        1: 'vacuum',
        2: 'vacuum',
        3: 'vacuum',
        4: 'vacuum plug',
        5: 'outlet',
        6: 'vacuum',
        7: 'vacuum canister',
        8: 'vacuum power cord',
        9: 'robot',
        10: 'vacuum switch',
        11: 'vacuum power cord',
        12: 'vacuum plug',
        13: 'robot',
        14: 'robot',
        15: 'outlet'
    }

    situations_prob = {
        0: 28 / 91.,
        1: 12 / 91.,
        2: 10 / 91.,
        3: 10 / 91.,
        4: 8 / 91.,
        5: 6 / 91.,
        6: 3 / 91.,
        7: 3 / 91.,
        8: 2 / 91.,
        9: 2 / 91.,
        10: 2 / 91.,
        11: 1 / 91.,
        12: 1 / 91.,
        13: 1 / 91.,
        14: 1 / 91.,
        15: 1 / 91.,
    }

    situations_action = {
        0: ['turnon_vacuum', 'clean_table'],
        1: ['turnon_vacuum', 'clean_table'],
        2: ['grasp_vacuum'],
        3: ['grasp_vacuum'],
        4: ['plug_vacuum'],
        5: ['plug_vacuum'],
        6: ['plug_vacuum'],
        7: ['grasp_vacuum', 'clean_table'],
        8: ['plug_vacuum'],
        9: ['clean_table'],
        10: ['turnon_vacuum'],
        11: ['plug_vacuum'],
        12: ['plug_vacuum'],
        13: ['find_table'],
        14: ['grasp_vacuum'],
        15: ['plug_vacuum']
    }

    actions_prob = {
        0: [9 / 28., 19 / 28.],
        1: [11 / 12., 1 / 12.],
        2: [10 / 10.],
        3: [10 / 10.],
        4: [8 / 8.],
        5: [6 / 6.],
        6: [3 / 3.],
        7: [2 / 3., 1 / 3.],
        8: [2 / 2.],
        9: [2 / 2.],
        10: [2 / 2.],
        11: [1 / 1.],
        12: [1 / 1.],
        13: [1 / 1.],
        14: [1 / 1.],
        15: [1 / 1.],
    }
    # randomly select a situation
    situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

    # test
    if debug:
      situation_index = debug_situation_index

    situation = situations[situation_index]
    situation_opp = situations_opp[situation_index]
    situation_object = situations_object[situation_index]
    situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
    situation_predicate = generate_predicate(situation)
    return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 2:
    situations = {
      0: 'there is no soap.',
      1: 'the glass is missing.',
      2: 'the faucet is broken.',
      3: 'there is no water.',
      4: 'the glass falls and breaks.',
      5: 'the glass is too dusty to be cleaned.',
      6: 'there is no faucet.',
      7: 'the water pipe is broken.',
      8: 'the dining room is locked or blocked.',
      9: 'the water is super hot.',
      10: 'the soap bottle is empty.',
      11: 'the faucet is leaking.',
      12: 'the glasses are already clean.',
      13: 'the water does not come out due to blockage.',
      14: 'the water supply is not available.',
      15: 'the sink is filled up with soapy water.',
      16: 'the vessels are stained.',
      17: 'the glass slips from hand and shatters in the sink.',
      18: 'the dish is already in the sink.'
    }

    situations_opp = {
      0: 'soap present.',
      1: 'glass present.',
      2: 'faucet working.',
      3: 'water present.',
      4: 'glass intact.',
      5: 'cleanable glass.',
      6: 'faucet present.',
      7: 'water pipe not broken.',
      8: 'dining room accessible.',
      9: 'water not too hot.',
      10: 'soap bottle not empty.',
      11: 'faucet not leaking.',
      12: 'glasses need cleaning.',
      13: 'water flows without blockage.',
      14: 'water supply available.',
      15: 'sink empty.',
      16: 'vessels not stained.',
      17: 'glass does not shatter.',
      18: 'glass not in sink.'
    }

    situations_object = {
      0: 'soap',
      1: 'glass',
      2: 'faucet',
      3: 'water',
      4: 'glass',
      5: 'glass',
      6: 'faucet',
      7: 'water',
      8: 'dining room',
      9: 'water',
      10: 'soap',
      11: 'faucet',
      12: 'glass',
      13: 'water',
      14: 'water',
      15: 'sink',
      16: 'vessels',
      17: 'glass',
      18: 'glass'
    }

    situations_prob = {
      0: 32 / 96.,
      1: 6 / 96.,
      2: 5 / 96.,
      3: 14 / 96.,
      4: 8 / 96.,
      5: 1 / 96.,
      6: 1 / 96.,
      7: 2 / 96.,
      8: 2 / 96.,
      9: 1 / 96.,
      10: 14 / 96.,
      11: 1 / 96.,
      12: 2 / 96.,
      13: 1 / 96.,
      14: 1 / 96.,
      15: 1 / 96.,
      16: 1 / 96.,
      17: 2 / 96.,
      18: 1 / 96.
    }

    situations_action = {
      0: ['find_soap'],
      1: ['find_glass'],
      2: ['turnon_faucet'],
      3: ['turnon_faucet','find_soap','wash_glass'],
      4: ['find_glass','wash_glass'],
      5: ['wash_glass'],
      6: ['find_faucet'],
      7: ['walk', 'wash_glass'],
      8: ['turnon_faucet'],
      9: ['walk'],
      10: ['find_soap', 'grasp_soap'],
      11: ['turnon_faucet'],
      12: ['wash_glass'],
      13: ['find_soap'],
      14: ['find_soap'],
      15: ['wash_glass'],
      16: ['grasp_soap'],
      17: ['find_glass','wash_glass'],
      18: ['walk']
    }

    actions_prob = {
      0: [32 / 32.],
      1: [6 / 6.],
      2: [5 / 5.],
      3: [10 / 14., 2 / 14., 2 / 14.],
      4: [3 / 8., 5 / 8.],
      5: [1 / 1.],
      6: [1 / 1.],
      7: [1 / 2., 1 / 2.],
      8: [2 / 2.],
      9: [1 / 1.],
      10: [13 / 14., 1 / 14.],
      11: [1 / 1.],
      12: [2 / 2.],
      13: [1 / 1.],
      14: [1 / 1.],
      15: [1 / 1.],
      16: [1 / 1.],
      17: [1 / 2., 1 / 2.],
      18: [1 / 1.],
    }

    # randomly select a situation
    situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

    # test
    if debug:
      situation_index = debug_situation_index

    situation = situations[situation_index]
    situation_opp = situations_opp[situation_index]
    situation_object = situations_object[situation_index]
    situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
    situation_predicate = generate_predicate(situation)
    return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 3:
    situations = {
      0: 'there is no food.',
      1: 'food is missing.',
      2: 'refrigerator full, no space for more food.',
      3: 'refrigerator not working.',
      4: 'food already on table.',
      5: 'food cannot be refrigerated.',
      6: 'refrigerator temperature too high.',
      7: 'food unsuitable for refrigeration.',
      8: 'refrigerator cannot be closed properly.',
      9: 'there is no refrigerator.',
      10: 'refrigerator cannot be opened.',
      11: 'refrigerator broken.',
      12: 'food dropped out of the refrigerator.',
      13: 'paper bag holding food rips.',
      14: 'refrigerator power supply stopped.',
      15: 'refrigerator not working.',
      16: 'bag holding food breaks and spills on the floor.',
      17: 'food falls down.'
      }

    situations_opp = {
      0: 'food present.',
      1: 'food present.',
      2: 'refrigerator has space.',
      3: 'refrigerator working.',
      4: 'food not on table.',
      5: 'food can be refrigerated.',
      6: 'refrigerator temp normal.',
      7: 'food suitable for refrigeration.',
      8: 'refrigerator can be closed.',
      9: 'there is refrigerator.',
      10: 'refrigerator can be opened.',
      11: 'refrigerator working.',
      12: 'food not dropped from refrigerator.',
      13: 'bag holding food does not rip.',
      14: 'refrigerator power supply working.',
      15: 'refrigerator working.',
      16: 'bag holding food does not break.',
      17: 'food does not fall down.'
      }

    situations_object = {
      0: 'food',
      1: 'food',
      2: 'refrigerator',
      3: 'refrigerator',
      4: 'food',
      5: 'food',
      6: 'refrigerator',
      7: 'food',
      8: 'refrigerator',
      9: 'refrigerator',
      10: 'refrigerator',
      11: 'refrigerator',
      12: 'food',
      13: 'bag holding food',
      14: 'refrigerator',
      15: 'refrigerator',
      16: 'bag holding food',
      17: 'food'
    }

    situations_prob = {
      0: 10 / 95.,
      1: 10 / 95.,
      2: 28 / 95.,
      3: 1 / 95.,
      4: 2 / 95.,
      5: 1 / 95.,
      6: 1 / 95.,
      7: 1 / 95.,
      8: 1 / 95.,
      9: 2 / 95.,
      10: 8 / 95.,
      11: 5 / 95.,
      12: 1 / 95.,
      13: 1 / 95.,
      14: 1 / 95.,
      15: 1 / 95.,
      16: 4 / 95.,
      17: 17 / 95.
    }

    situations_action = {
      0: ['find_food', 'grasp_food', 'place_food'],
      1: ['find_food', 'grasp_food', 'place_food'],
      2: ['find_food', 'open_refrigerator', 'place_food'],
      3: ['place_food'],
      4: ['find_food','place_food'],
      5: ['walk'],
      6: ['walk'],
      7: ['walk'],
      8: ['close_refrigerator'],
      9: ['walk','find_refrigerator'],
      10: ['walk', 'grasp_food', 'find_refrigerator', 'open_refrigerator', 'place_food'],
      11: ['grasp_food', 'find_refrigerator', 'open_refrigerator', 'place_food'],
      12: ['walk'],
      13: ['grasp_food'],
      14: ['walk'],
      15: ['walk'],
      16: ['find_food', 'grasp_food'],
      17: ['find_food', 'grasp_food', 'find_refrigerator', 'open_refrigerator', 'place_food']
    }

    actions_prob = {
      0: [5 / 10., 2 / 10., 3 / 10.],
      1: [4 / 10., 4 / 10., 2 / 10.],
      2: [1 / 28., 3 / 28., 24 / 28.],
      3: [1 / 1.],
      4: [1 / 2., 1 / 2.],
      5: [1 / 1.],
      6: [1 / 1.],
      7: [1 / 1.],
      8: [1 / 1.],
      9: [1 / 2., 1 / 2.],
      10: [1 / 8., 1 / 8., 2 / 8., 2 / 8., 2 / 8.],
      11: [1 / 5., 1 / 5., 1 / 5., 2 / 5.],
      12: [1 / 1.],
      13: [1 / 1.],
      14: [1 / 1.],
      15: [1 / 1.],
      16: [1 / 4., 3 / 4.],
      17: [1 / 17., 9 / 17., 2 / 17., 1 / 17., 4 / 17.]
    }

    # randomly select a situation
    situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

    # test
    if debug:
      situation_index = debug_situation_index

    situation = situations[situation_index]
    situation_opp = situations_opp[situation_index]
    situation_object = situations_object[situation_index]
    situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
    situation_predicate = generate_predicate(situation)

    return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 4:
    situations = {
      0: 'the cup is broken.',
      1: 'the faucet has no water.',
      2: 'the cup is dirty.',
      3: 'the cup is missing.',
      4: 'the water is dirty.',
      5: 'the water is hot.',
      6: 'the faucet is broken.',
      7: 'the faucet cannot be turned on.',
      8: 'the sink is not found.',
      9: 'the faucet is dripping.',
      10: 'the faucet is not found.',
      11: 'the cup is in the box.',
      12: 'the water spills on the ground.',
      13: 'the cup is not full.',
      14: 'the water is drunk by others.',
      15: 'the cup full of water falls down.'
    }

    situations_opp = {
      0: 'a cup not broken.',
      1: 'a faucet have water.',
      2: 'a cup clean.',
      3: 'a cup found.',
      4: 'water clean.',
      5: 'water cold.',
      6: 'a faucet not broken.',
      7: 'a faucet easy to be turned on.',
      8: 'a sink found.',
      9: 'a faucet not dripping.',
      10: 'a faucet found.',
      11: 'a cup took out from the box.',
      12: 'a ground dry.',
      13: 'a cup full.',
      14: 'water not drunk by others.',
      15: 'a cup full of water not falling down.'
    }

    situations_object = {
      0: 'cup',
      1: 'faucet',
      2: 'cup',
      3: 'cup',
      4: 'water',
      5: 'water',
      6: 'faucet',
      7: 'faucet',
      8: 'sink',
      9: 'faucet',
      10: 'faucet',
      11: 'cup',
      12: 'water',
      13: 'cup',
      14: 'water',
      15: 'cup'
    }

    situations_prob = {
      0: 23 / 95.,
      1: 23 / 95.,
      2: 14 / 95.,
      3: 10 / 95.,
      4: 7 / 95.,
      5: 3 / 95.,
      6: 3 / 95.,
      7: 2 / 95.,
      8: 2 / 95.,
      9: 1 / 95.,
      10: 1 / 95.,
      11: 1 / 95.,
      12: 1 / 95.,
      13: 2 / 95.,
      14: 1 / 95.,
      15: 1 / 95.
    }

    situations_action = {
      0: ['find_cup', 'grasp_cup', 'fill_cup'],
      1: ['turnon_faucet', 'fill_cup'],
      2: ['find_cup', 'grasp_cup'],
      3: ['find_cup', 'grasp_cup'],
      4: ['turnon_faucet', 'fill_cup', 'place_cup'],
      5: ['find_cup', 'fill_cup'],
      6: ['turnon_faucet'],
      7: ['turnon_faucet'],
      8: ['find_faucet'],
      9: ['place_cup'],
      10: ['find_faucet'],
      11: ['find_cup'],
      12: ['fill_cup'],
      13: ['fill_cup', 'place_cup'],
      14: ['place_cup'],
      15: ['place_cup']
    }

    actions_prob = {
      0: [1 / 23., 16 / 23., 6 / 23.],
      1: [15 / 23., 8 / 23.],
      2: [13 / 14., 1 / 14.],
      3: [9 / 10., 1 / 10.],
      4: [2 / 7., 3 / 7., 2 / 7.],
      5: [2 / 3., 1 / 3.],
      6: [3 / 3.],
      7: [2 / 2.],
      8: [1 / 1.],
      9: [1 / 1.],
      10: [1 / 1.],
      11: [1 / 1.],
      12: [1 / 1.],
      13: [1 / 2., 1 / 2.],
      14: [1 / 1.],
      15: [1 / 1.]
    }

    # randomly select a situation
    situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

    # test
    if debug:
      situation_index = debug_situation_index

    situation = situations[situation_index]
    situation_opp = situations_opp[situation_index]
    situation_object = situations_object[situation_index]
    situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
    situation_predicate = generate_predicate(situation)

    return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 5:
      situations = {
          0: 'there is no detergent.',
          1: 'there is no water.',
          2: 'the dish cloth is dirty.',
          3: 'there is no clean dish cloth.',
          4: 'the sink is full.',
          5: 'the detergent is missing.',
          6: 'the faucet is not working.',
          7: 'there are no clean dish cloth.',
          8: 'the sink is blocked.',
          9: 'the dish cloth is torn.',
          10: 'the food is crusted onto the sink and cannot just be wiped off.',
          11: 'the floor is slippery because of the water.',
          12: 'the detergent has dropped to the floor.',
          13: 'the pipes are frozen so there is no running water.',
          14: 'the liquid bottle is empty.',
          15: 'the sink is too dirty.',
          16: 'the dish cloth is missing.'
      }

      situations_opp = {
          0: 'dish washing detergent present.',
          1: 'water present.',
          2: 'dish cloth clean.',
          3: 'clean dish cloth present.',
          4: 'sink not full.',
          5: 'detergent is not missing.',
          6: 'faucet working.',
          7: 'clean dish cloth present.',
          8: 'sink not blocked.',
          9: 'dish cloth not torn.',
          10: 'sink clean.',
          11: 'the floor is dry.',
          12: 'detergent did not drop to the floor.',
          13: 'pipes not frozen.',
          14: 'aliquid bottle not empty.',
          15: 'sink is not too dirty.',
          16: 'dish cloth is not missing.'
      }

      situations_object = {
          0: 'detergent',
          1: 'water',
          2: 'cloth',
          3: 'cloth',
          4: 'sink',
          5: 'detergent',
          6: 'faucet',
          7: 'cloth',
          8: 'sink',
          9: 'cloth',
          10: 'sink',
          11: 'floor',
          12: 'detergent',
          13: 'pipes',
          14: 'liquid bottle',
          15: 'sink',
          16: 'cloth'
      }
      situations_prob = {
          0: 22 / 85.,
          1: 5 / 85.,
          2: 11 / 85.,
          3: 10 / 85.,
          4: 1 / 85.,
          5: 9 / 85.,
          6: 5 / 85.,
          7: 1 / 85.,
          8: 1 / 85.,
          9: 2 / 85.,
          10: 1 / 85.,
          11: 1 / 85.,
          12: 4 / 85.,
          13: 1 / 85.,
          14: 7 / 85.,
          15: 2 / 85.,
          16: 2 / 85.
      }

      situations_action = {
          0: ['walk', 'find_detergent', 'grasp_detergent', 'find_sink', 'squeeze_detergent', 'wipe_sink'],
          1: ['turnon_faucet'],
          2: ['walk', 'find_cloth', 'wipe_sink'],
          3: ['walk', 'find_cloth', 'grasp_cloth'],
          4: ['wipe_sink'],
          5: ['grasp_cloth', 'find_detergent', 'grasp_detergent', 'squeeze_detergent', 'wipe_sink','place_cloth'],
          6: ['turnon_faucet', 'turnoff_faucet'],
          7: ['walk'],
          8: ['walk'],
          9: ['find_cloth', 'wipe_sink'],
          10: ['wipe_sink', ],
          11: ['find_sink'],
          12: ['grasp_detergent', ' find_sink', 'squeeze_detergent'],
          13: ['turnon_faucet'],
          14: ['grasp_detergent', ' find_sink', 'squeeze_detergent'],
          15: ['find_faucet', 'wipe_sink'],
          16: ['find_cloth']
      }

      actions_prob = {
          0: [1 / 22., 10 / 22., 3 / 22., 1 / 22., 6 / 22., 1 / 22.],
          1: [5 / 5.],
          2: [3 / 11., 7 / 11., 1 / 11.],
          3: [5 / 10., 3 / 10., 2 / 10.],
          4: [1 / 1.],
          5: [1 / 9., 4 / 9., 1 / 9., 1 / 9., 1 / 9., 1 / 9.],
          6: [4 / 5., 1 / 5.],
          7: [1 / 1.],
          8: [1 / 1.],
          9: [1 / 2., 1 / 2.],
          10: [1 / 1.],
          11: [1 / 1.],
          12: [2 / 4., 1 / 4., 1 / 4.],
          13: [1 / 1.],
          14: [1 / 7., 1 / 7., 5 / 7.],
          15: [1 / 2., 1 / 2.],
          16: [2 / 2.]
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 6:
      situations = {
          0: 'the plate is broken.',
          1: 'the plate is not found.',
          2: 'the plate is dirty.',
          3: 'the fork is dirty.',
          4: 'the fork is not found.',
          5: 'the table is dirty.',
          6: 'the table is not found.',
          7: 'the cupboard cannot open.',
          8: 'the plate falls on the ground.',
          9: 'the table does not have enough space.',
          10: 'the fork falls on the ground.',
          11: 'the cupboard has some mites.',
          12: 'the cupboard is broken.',
          13: 'the fork is already on the table.',
          14: 'the fork is broken.',
          15: 'the table is broken.',
          16: 'the robot is stopped due to obstacles.'
      }

      situations_opp = {
          0: 'a plate not broken.',
          1: 'a plate found.',
          2: 'a plate clean.',
          3: 'a fork clean.',
          4: 'a fork found.',
          5: 'a table clean.',
          6: 'a table found.',
          7: 'a cupboard open.',
          8: 'a plate grasped.',
          9: 'a table big enough.',
          10: 'a fork grasped.',
          11: 'mites in a cupboard killed.',
          12: 'a cupboard not broken.',
          13: 'a fork not on the table.',
          14: 'a fork broken.',
          15: 'a table broken.',
          16: 'there are no obstacles for the robot.'
      }

      situations_object = {
          0: 'plate',
          1: 'plate',
          2: 'plate',
          3: 'fork',
          4: 'fork',
          5: 'table',
          6: 'table',
          7: 'cupboard',
          8: 'plate',
          9: 'table',
          10: 'fork',
          11: 'cupboard',
          12: 'cupboard',
          13: 'fork',
          14: 'fork',
          15: 'table',
          16: 'obstacle'
      }

      situations_prob = {
          0: 21 / 92.,
          1: 13 / 92.,
          2: 12 / 92.,
          3: 8 / 92.,
          4: 7 / 92.,
          5: 6 / 92.,
          6: 4 / 92.,
          7: 4 / 92.,
          8: 4 / 92.,
          9: 4 / 92.,
          10: 3 / 92.,
          11: 1 / 92.,
          12: 1 / 92.,
          13: 1 / 92.,
          14: 1 / 92.,
          15: 1 / 92.,
          16: 1 / 92.
      }

      situations_action = {
          0: ['open_cupboard', 'find_plate'],
          1: ['find_cupboard', 'find_plate'],
          2: ['find_plate', 'grasp_plate', 'place_plate'],
          3: ['find_fork', 'grasp_fork', 'place_fork'],
          4: ['find_fork', 'grasp_fork'],
          5: ['find_table', 'place_plate'],
          6: ['find_table'],
          7: ['open_cupboard'],
          8: ['grasp_plate', 'place_plate'],
          9: ['place_plate', 'place_fork'],
          10: ['grasp_fork', 'place_fork'],
          11: ['open_cupboard'],
          12: ['open_cupboard'],
          13: ['find_fork'],
          14: ['find_fork'],
          15: ['find_table'],
          16: ['walk']
      }

      actions_prob = {
          0: [3 / 21., 18 / 21.],
          1: [2 / 13., 11 / 13.],
          2: [4 / 12., 4 / 12., 4 / 12.],
          3: [5 / 8., 2 / 8., 1 / 8.],
          4: [6 / 7., 1 / 7.],
          5: [2 / 6., 4 / 6.],
          6: [4 / 4.],
          7: [4 / 4.],
          8: [2 / 4., 2 / 4.],
          9: [2 / 4., 2 / 4.],
          10: [2 / 3., 1 / 3.],
          11: [1 / 1.],
          12: [1 / 1.],
          13: [1 / 1.],
          14: [1 / 1.],
          15: [1 / 1.],
          16: [1 / 1.]
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 7:
      situations = {
          0: 'the microwave is broken.',
          1: 'the burger cannot be put into the microwave.',
          2: 'the burger has fallen to the floor.',
          3: 'the burger is already in the microwave.',
          4: 'the burger is overcooked.',
          5: 'the burger is rotten.',
          6: 'the burger is spoiled.',
          7: 'the burger is still cold.',
          8: 'the refrigerator cannot be opened.',
          9: 'the refrigerator is not closed.',
          10: 'the microwave cannot be closed.',
          11: 'the microwave cannot be turned on.',
          12: 'the microwave is dirty.',
          13: 'the microwave is missing.',
          14: 'the microwave is not large enough to fit the entire burger at once.',
          15: 'the microwave is not plugged in.',
          16: 'the refrigerator is broken.',
          17: 'there is a power outage.',
          18: 'there is no dish to put burger in microwave.',
          19: 'there is no burger.'
       }

      situations_opp = {
          0: 'good microwave.',
          1: 'burger put into the microwave.',
          2: 'burger is not fallen',
          3: 'burger is not yet in microwave.',
          4: 'burger is not overcooked.',
          5: 'burger is fresh.',
          6: 'burger is not spoiled.',
          7: 'burger is warm or hot.',
          8: 'refrigerator can be opened.',
          9: 'refrigerator is closed properly.',
          10: 'microwave can be closed.',
          11: 'microwave can be turned on.',
          12: 'microwave is clean.',
          13: 'microwave is not missing.',
          14: 'microwave is large enough.',
          15: 'microwave is plugged in.',
          16: 'refrigerator is working properly.',
          17: 'no power cut.',
          18: 'there is a dish available.',
          19: 'there is burger available.',
          16: 'dishcloth is not missing.'
      }

      situations_object = {
          0: 'microwave',
          1: 'microwave',
          2: 'burger',
          3: 'microwave',
          4: 'burger',
          5: 'burger',
          6: 'burger',
          7: 'burger',
          8: 'refrigerator',
          9: 'refrigerator',
          10: 'microwave',
          11: 'microwave',
          12: 'microwave',
          13: 'microwave',
          14: 'microwave',
          15: 'microwave',
          16: 'refrigerator',
          17: 'power',
          18: 'dish',
          19: 'burger'
      }

      situations_prob = {
          0: 31 / 83.,
          1: 1 / 83.,
          2: 6 / 83.,
          3: 1 / 83.,
          4: 2 / 83.,
          5: 1 / 83.,
          6: 6 / 83.,
          7: 2 / 83.,
          8: 1 / 83.,
          9: 2 / 83.,
          10: 1 / 83.,
          11: 4 / 83.,
          12: 3 / 83.,
          13: 1 / 83.,
          14: 1 / 83.,
          15: 5 / 83.,
          16: 1 / 83.,
          17: 3 / 83.,
          18: 1 / 83.,
          19: 10 / 83.
      }


      situations_action = {
          0: ['walk', 'open_microwave',  'place_burger', 'close_microwave', 'turnon_microwave', 'turnoff_microwave'],
          1: ['walk'],
          2: ['grasp_burger', 'close_refrigerator', ' place_burger', ' turnon_microwave'],
          3: ['place_burger'],
          4: ['turnon_microwave'],
          5: ['grasp_burger'],
          6: ['turnon_microwave'],
          7: ['turnoff_microwave'],
          8: ['open_refrigerator'],
          9: ['close_refrigerator'],
          10: ['turnon_microwave'],
          11: ['turnon_microwave'],
          12: ['open_microwave', 'place_burger', 'turnoff_microwave'],
          13: ['find_burger'],
          14: ['place_burger'],
          15: ['turnon_microwave'],
          16: ['close_refrigerator'],
          17: ['walk', 'turnon_microwave'],
          18: ['turnon_microwave'],
          19: ['find_burger','grasp_burger']
      }

      actions_prob = {
          0: [1 / 31., 8 / 31., 4 / 31., 3 / 31., 13 / 31., 2 / 31.],
          1: [1 / 1.],
          2: [3 / 6., 1 / 6., 1 / 6., 1 / 6.],
          3: [1 / 1.],
          4: [2 / 2.],
          5: [1 / 1.],
          6: [6 / 6.],
          7: [2 / 2.],
          8: [1 / 1.],
          9: [2 / 2.],
          10: [1 / 1.],
          11: [4 / 4.],
          12: [1 / 3., 1 / 3., 1 / 3.],
          13: [1 / 1.],
          14: [1 / 1.],
          15: [5 / 5.],
          16: [1 / 1.],
          17: [1 / 3., 2 / 3],
          18: [1 / 1.],
          19: [7 / 10., 3 / 10]
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 8:
      situations = {
          0: 'the maker has no power.',
          1: 'ants have gotten into the maker and it cannot be used.',
          2: 'the bean spill onto the floor.',
          3: 'the bean are bad.',
          4: 'the coffee is too hot to drink.',
          5: 'the cup falls on the floor.',
          6: 'the cup is broken.',
          7: 'the cup is dirty.',
          8: 'the coffee has spilled.',
          9: 'the maker cannot be turned on.',
          10: 'the maker has been sealed shut.',
          11: 'the maker is missing.',
          12: 'the maker is not working.',
          13: 'the maker switch is stuck.',
          14: 'the lid of the maker is jammed.',
          15: 'there are no bean.',
          16: 'there are no cups.',
          17: 'there is no coffee filter.',
          18: 'there is a power outage.',
          19: 'there are not enough bean.',
          20: 'the coffee is overflowing.',
          21: 'the bean are not ground.',
          22: 'there is no water in the maker.',
          23: 'the bean have spilled out onto the table.',
          24: 'there is too much water in the maker and it overflows.'
         }

      situations_opp = {
          0: 'maker has power.',
          1: 'vacuum is working.',
          2: 'bean do not spill.',
          3: 'good bean.',
          4: 'coffee is at a comfortable temperature.',
          5: 'cup does not fall.',
          6: 'cup is not broken.',
          7: 'clean cup.',
          8: 'the spilled coffee clean.',
          9: 'maker can be turned on.',
          10: 'maker is not sealed shut.',
          11: 'maker is not missing.',
          12: 'maker is working.',
          13: 'maker switch is not stuck.',
          14: 'lid of maker is not jammed.',
          15: 'bean are available.',
          16: 'cups are available.',
          17: 'coffee filter is available.',
          18: 'no power outage.',
          19: 'enough bean.',
          20: 'coffee is not overflowing.',
          21: 'bean are ground properly.',
          22: 'water in maker.',
          23: 'bean have not spilled out.',
          24: 'not too much water in maker.'
         }

      situations_object = {
          0: 'maker',
          1: 'vacuum',
          2: 'bean',
          3: 'bean',
          4: 'coffee',
          5: 'cup',
          6: 'cup',
          7: 'cup',
          8: 'coffee',
          9: 'maker',
          10: 'maker',
          11: 'maker',
          12: 'maker',
          13: 'maker switch',
          14: 'maker',
          15: 'bean',
          16: 'cups',
          17: 'coffee filter',
          18: 'power',
          19: 'bean',
          20: 'coffee',
          21: 'bean',
          22: 'water',
          23: 'bean',
          24: 'water'
      }


      situations_prob = {
          0: 1 / 86.,
          1: 1 / 86.,
          2: 2 / 86.,
          3: 5 / 86.,
          4: 1 / 86.,
          5: 2 / 86.,
          6: 2 / 86.,
          7: 5 / 86.,
          8: 2 / 86.,
          9: 1 / 86.,
          10: 1 / 86.,
          11: 4 / 86.,
          12: 8 / 86.,
          13: 1 / 86.,
          14: 1 / 86.,
          15: 24 / 86.,
          16: 6 / 86.,
          17: 2 / 86.,
          18: 3 / 86.,
          19: 5 / 86.,
          20: 1 / 86.,
          21: 4 / 86.,
          22: 2 / 86.,
          23: 1 / 86.,
          24: 1 / 86.
      }


      situations_action = {
          0: ['place_cup'],
          1: ['place_bean'],
          2: ['place_bean'],
          3: ['find_bean', 'grasp_bean',],
          4: ['turnon_maker'],
          5: ['place_cup', 'grasp_bean'],
          6: ['find_cup', 'grasp_bean'],
          7: ['find_cup'],
          8: ['turnon_maker'],
          9: ['turnon_maker'],
          10: ['open_maker'],
          11: ['walk', 'open_maker', 'find_cup', 'turnon_maker'],
          12: ['open_maker', 'turnon_maker'],
          13: ['turnon_maker'],
          14: ['open_maker'],
          15: ['find_bean', 'grasp_bean', 'open_maker','place_bean', 'turnon_maker'],
          16: ['find_cup', 'grasp_bean'],
          17: ['place_bean',  'turnon_maker'],
          18: ['place_bean',  'turnon_maker'],
          19: ['find_bean','grasp_bean','place_bean'],
          20: ['turnon_maker'],
          21: ['grasp_bean', 'place_bean'],
          22: ['turnon_maker'],
          23: ['place_bean'],
          24: ['turnon_maker']
      }

      actions_prob = {
          0: [1 / 1.],
          1: [1 / 1.],
          2: [2 / 2.],
          3: [2 / 5., 3 / 5.],
          4: [1 / 1.],
          5: [1 / 2., 1 / 2],
          6: [2 / 3., 1 / 3.],
          7: [5 / 5.],
          8: [2 / 2.],
          9: [1 / 1.],
          10: [1 / 1.],
          11: [1 / 4., 1 / 4., 1 / 4., 1 / 4.],
          12: [1 / 8., 7 / 8.],
          13: [1 / 1.],
          14: [1 / 1.],
          15: [15 / 24., 3 / 24., 1 / 24., 4 / 24., 1 / 24.],
          16: [4 / 6., 2 / 6.],
          17: [1 / 2., 1 / 2],
          18: [1 / 3., 2 / 3],
          19: [2 / 5., 2 / 5., 1 / 5.],
          20: [1 / 1.],
          21: [2 / 4., 2 / 4.],
          22: [2 / 2.],
          23: [1 / 1.],
          24: [1 / 1.],
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 9:
      situations = {
          0: 'the sink is full.',
          1: 'the plate is broken.',
          2: 'the plate is already clean.',
          3: 'the dirty plate is missing on table.',
          4: 'the plate is dropped.',
          5: 'the plate is missing.',
          6: 'the table is missing.',
          7: 'the sink is too dirty.',
          8: 'there is no water in sink.',
          9: 'the table is dirty.',
          10: 'the table is broken.',
          11: 'the sink cannot be found.',
          12: 'the plate is grabbed by dog.',
          13: 'the door of dinning room is locked.',
          14: 'the dirty plate has already been placed in the sink.',
          15: 'people are not finishing food.'
      }

      situations_opp = {
          0: 'a sink empty.',
          1: 'a plate unbroken.',
          2: 'a plat dirty',
          3: 'a plate found',
          4: 'a plate not dropped.',
          5: 'a plate found.',
          6: 'a table found.',
          7: 'a sink clean.',
          8: 'water in the sink.',
          9: 'a table clean.',
          10: 'a table good.',
          11: 'a sink found.',
          12: 'a plate on the table.',
          13: 'a door open.',
          14: 'a plate on the table.',
          15: 'people finishing food.'
      }

      situations_object = {
          0: 'sink',
          1: 'plate',
          2: 'plate',
          3: 'plate',
          4: 'plate',
          5: 'plate',
          6: 'table',
          7: 'sink',
          8: 'water',
          9: 'table',
          10: 'table',
          11: 'sink',
          12: 'plate',
          13: 'door',
          14: 'plate',
          15: 'people'
      }

      situations_prob = {
          0: 24 / 91.,
          1: 17 / 91.,
          2: 11 / 91.,
          3: 11 / 91.,
          4: 9 / 91.,
          5: 6 / 91.,
          6: 2 / 91.,
          7: 2 / 91.,
          8: 1 / 91.,
          9: 1 / 91.,
          10: 1 / 91.,
          11: 1 / 91.,
          12: 1 / 91.,
          13: 1 / 91.,
          14: 2 / 91.,
          15: 1 / 91.
      }

      situations_action = {
          0: ['find_sink', 'place_plate'],
          1: ['grasp_plate'],
          2: ['grasp_plate', 'place_plate'],
          3: ['grasp_plate', 'place_plate'],
          4: ['grasp_plate', 'find_sink', 'place_plate'],
          5: ['grasp_plate', 'find_sink'],
          6: ['find_table'],
          7: ['find_sink'],
          8: ['find_sink'],
          9: ['find_table'],
          10: ['find_table'],
          11: ['find_sink'],
          12: ['grasp_plate'],
          13: ['walk'],
          14: ['grasp_plate'],
          15: ['walk']
      }

      actions_prob = {
          0: [23 / 24., 1 / 24.],
          1: [17 / 17.],
          2: [8 / 11., 3 / 11.],
          3: [8 / 11., 3 / 11.],
          4: [6 / 9., 1 / 9., 2 / 9.],
          5: [5 / 6., 1 / 6.],
          6: [2 / 2.],
          7: [2 / 2.],
          8: [1 / 1.],
          9: [1 / 1.],
          10: [1 / 1.],
          11: [1 / 1.],
          12: [1 / 1.],
          13: [1 / 1.],
          14: [1 / 1.],
          15: [1 / 1.]
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 10:
      situations = {
          0: 'the coke is not available.',
          1: 'the glass is broken.',
          2: 'the coke is missing.',
          3: 'the glass is dirty.',
          4: 'the glass falls down.',
          5: 'the coke spills.',
          6: 'the glass is missing.',
          7: 'the coke is flat.',
          8: 'the coke cannot be opened.',
          9: 'the coke is empty.',
          10: 'the coke is dropped.',
          11: 'the robot cannot recognize the bottle, and take beer out.',
          12: 'the coke is sticky and leaking.',
          13: 'the coke is not chill.',
          14: 'the coke is too frozen.'
      }

      situations_opp = {
          0: 'coke available.',
          1: 'a glass good.',
          2: 'coke found.',
          3: 'a glass clean',
          4: 'a glass picked up.',
          5: 'a ground clean.',
          6: 'a glass found.',
          7: 'coke full of carbon dioxide.',
          8: 'coke easy to be opened.',
          9: 'coke full of liquid.',
          10: 'coke grasped.',
          11: 'a robot successfully recognizing and grasping the coke.',
          12: 'coke clean.',
          13: 'coke chilled.',
          14: 'coke not too frozen.'
      }

      situations_object = {
          0: 'coke',
          1: 'glass',
          2: 'coke',
          3: 'glass',
          4: 'glass',
          5: 'coke',
          6: 'glass',
          7: 'coke',
          8: 'coke',
          9: 'coke',
          10: 'coke',
          11: 'robot',
          12: 'coke',
          13: 'coke',
          14: 'coke'
      }

      situations_prob = {
          0: 18 / 90.,
          1: 11 / 90.,
          2: 11 / 90.,
          3: 9 / 90.,
          4: 8 / 90.,
          5: 8 / 90.,
          6: 7 / 90.,
          7: 5 / 90.,
          8: 4 / 90.,
          9: 3 / 90.,
          10: 2 / 90.,
          11: 1 / 90.,
          12: 1 / 90.,
          13: 1 / 90.,
          14: 1 / 90.
      }

      situations_action = {
          0: ['find_coke', 'grasp_coke'],
          1: ['find_glass', 'move_glass'],
          2: ['find_coke'],
          3: ['find_glass'],
          4: ['pour_coke', 'place_glass'],
          5: ['pour_coke'],
          6: ['find_glass'],
          7: ['pour_coke'],
          8: ['pour_coke'],
          9: ['find_coke'],
          10: ['pour_coke'],
          11: ['find_coke'],
          12: ['find_coke'],
          13: ['grasp_coke'],
          14: ['grasp_coke']
      }

      actions_prob = {
          0: [14 / 18., 4 / 18.],
          1: [8 / 11., 3 / 11.],
          2: [11 / 11.],
          3: [9 / 9.],
          4: [2 / 8., 6 / 8.],
          5: [8 / 8.],
          6: [7 / 7.],
          7: [5 / 5.],
          8: [4 / 4.],
          9: [3 / 3.],
          10: [2 / 2.],
          11: [1 / 1.],
          12: [1 / 1.],
          13: [1 / 1.],
          14: [1 / 1.]
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 11:
      situations = {
          0: 'the chair is broken.',
          1: 'the burger is missing.',
          2: 'the fork is missing.',
          3: 'the plate is dirty.',
          4: 'the plate is missing.',
          5: 'the chair is occupied.',
          6: 'the fork is dirty.',
          7: 'the burger spills.',
          8: 'the burger is overcooked.',
          9: 'the chair is missing.',
          10: 'the chair is dirty.',
          11: 'the plate is placed already.',
          12: 'the table is dirty.',
          13: 'the plate is not available.',
          14: 'the plate is broken.',
          15: 'the fork is broken.',
          16: 'the burger smells bad.',
          17: 'the burger is not enough for a person.',
          18: 'the burger is expired.',
          19: 'the burger is dirty.',
          20: 'the chair slipped.',
          21: 'the chair is wet.'
      }

      situations_opp = {
          0: 'a chair unbroken.',
          1: 'a burger found.',
          2: 'a fork found.',
          3: 'a plate clean.',
          4: 'a plate found.',
          5: 'a chair available.',
          6: 'a fork clean.',
          7: 'a ground clean',
          8: 'a burger well-cooked.',
          9: 'a chair found.',
          10: 'a chair clean.',
          11: 'a plate not placed on the table.',
          12: 'a table clean.',
          13: 'a plate available.',
          14: 'a plate unbroken.',
          15: 'a fork unbroken.',
          16: 'a burger good.',
          17: 'a burger enough for a person.',
          18: 'a burger in good condition.',
          19: 'a burger clean.',
          20: 'a chair not slipped.',
          21: 'a chair dry.'
      }

      situations_object = {
          0: 'chair',
          1: 'burger',
          2: 'fork',
          3: 'plate',
          4: 'plate',
          5: 'chair',
          6: 'fork',
          7: 'burger',
          8: 'burger',
          9: 'chair',
          10: 'chair',
          11: 'plate',
          12: 'table',
          13: 'plate',
          14: 'plate',
          15: 'fork',
          16: 'burger',
          17: 'burger',
          18: 'burger',
          19: 'burger',
          20: 'chair',
          21: 'chair'
      }

      situations_prob = {
          0: 23 / 83.,
          1: 15 / 83.,
          2: 10 / 83.,
          3: 5 / 83.,
          4: 4 / 83.,
          5: 4 / 83.,
          6: 3 / 83.,
          7: 2 / 83.,
          8: 2 / 83.,
          9: 2 / 83.,
          10: 2 / 83.,
          11: 1 / 83.,
          12: 1 / 83.,
          13: 1 / 83.,
          14: 1 / 83.,
          15: 1 / 83.,
          16: 1 / 83.,
          17: 1 / 83.,
          18: 1 / 83.,
          19: 1 / 83.,
          20: 1 / 83.,
          21: 1 / 83.
      }

      situations_action = {
          0: ['find_chair', 'pull_chair'],
          1: ['find_burger'],
          2: ['find_fork'],
          3: ['find_plate'],
          4: ['find_plate'],
          5: ['find_chair'],
          6: ['find_fork'],
          7: ['place_plate'],
          8: ['find_burger'],
          9: ['find_chair'],
          10: ['find_chair'],
          11: ['place_plate'],
          12: ['find_table'],
          13: ['find_plate'],
          14: ['find_plate'],
          15: ['find_burger'],
          16: ['find_burger'],
          17: ['find_burger'],
          18: ['find_burger'],
          19: ['find_burger'],
          20: ['find_chair'],
          21: ['find_chair']
      }

      actions_prob = {
          0: [12 / 23., 11 / 23.],
          1: [15 / 15.],
          2: [10 / 10.],
          3: [5 / 5.],
          4: [4 / 4.],
          5: [4 / 4.],
          6: [3 / 3.],
          7: [2 / 2.],
          8: [2 / 2.],
          9: [2 / 2.],
          10: [2 / 2.],
          11: [1 / 1.],
          12: [1 / 1.],
          13: [1 / 1.],
          14: [1 / 1.],
          15: [1 / 1.],
          16: [1 / 1.],
          17: [1 / 1.],
          18: [1 / 1.],
          19: [1 / 1.],
          20: [1 / 1.],
          21: [1 / 1.]
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

  if task_id == 12:
      situations = {
          0: 'there is no electricity.',
          1: 'there is no dishwasher.',
          2: 'the glass are too dirty.',
          3: 'the dishwasher is full.',
          4: 'the dishwasher does not work.',
          5: 'there is no detergent.',
          6: 'the glass is already clean.',
          7: 'the detergent is spoiled.',
          8: 'the dishwasher door is jammed.',
          9: 'the glass is broken.',
          10: 'the floor is slippy because of water spills.',
          11: 'the glass is missing.',
          12: 'the dishwasher door cannot be closed.',
          13: 'the glass falls on the floor.',
       }

      situations_opp = {
          0: 'electricity power.',
          1: 'dishwasher is available.',
          2: 'the glass are clean.',
          3: 'the dishwasher is empty.',
          4: 'the dishwasher is functional.',
          5: 'detergent is available.',
          6: 'the glass is dirty.',
          7: 'fresh detergent is available.',
          8: 'the dishwasher door is working properly.',
          9: 'the glass is intact.',
          10: 'the floor is dry.',
          11: 'the glass is present.',
          12: 'the dishwasher door can be closed properly.',
          13: 'the glass is stable and not falling.',
      }

      situations_object = {
          0: 'electricity',
          1: 'dishwasher',
          2: 'glass',
          3: 'dishwasher',
          4: 'dishwasher',
          5: 'detergent',
          6: 'glass',
          7: 'detergent',
          8: 'dishwasher',
          9: 'glass',
          10: 'floor',
          11: 'glass',
          12: 'dishwasher',
          13: 'glass'
      }

      situations_prob = {
          0: 3 / 88.,
          1: 3 / 88.,
          2: 1 / 88.,
          3: 3 / 88.,
          4: 17 / 88.,
          5: 42 / 88.,
          6: 2 / 88.,
          7: 1 / 88.,
          8: 6 / 88.,
          9: 2 / 88.,
          10: 1 / 88.,
          11: 3 / 88.,
          12: 3 / 88.,
          13: 1 / 88.
      }

      situations_action = {
          0: ['turnon_dishwasher'],
          1: ['find_dishwasher'],
          2: ['find_detergent'],
          3: ['find_dishwasher','grasp_glass','place_glass'],
          4: ['place_glass', 'grasp_glass', 'turnon_dishwasher'],
          5: ['find_dishwasher','place_glass','find_detergent','grasp_glass','squeeze_detergent','close_dishwasher','turnon_dishwasher'],
          6: ['grasp_glass'],
          7: ['find_detergent'],
          8: ['open_dishwasher.','close_dishwasher'],
          9: ['grasp_glass'],
          10: ['walk'],
          11: ['grasp_glass'],
          12: ['close_dishwasher'],
          13: ['grasp_glass']
      }

      actions_prob = {
          0: [3 / 3.],
          1: [3 / 3.],
          2: [1 / 1.],
          3: [1 / 3., 1 / 3., 1 / 3.],
          4: [2 / 17., 1 / 17., 14 / 17.],
          5: [1 / 42., 1 / 42., 26 / 42., 5 / 42., 6 / 42., 1 / 42., 2 / 42.],
          6: [2 / 2.],
          7: [1 / 1.],
          8: [2 / 6., 4 / 6.],
          9: [2 / 2.],
          10: [1 / 1.],
          11: [2 / 2.],
          12: [3 / 3.],
          13: [1 / 1.]
      }

      # randomly select a situation
      situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

      # test
      if debug:
        situation_index = debug_situation_index

      situation = situations[situation_index]
      situation_opp = situations_opp[situation_index]
      situation_object = situations_object[situation_index]
      situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
      situation_predicate = generate_predicate(situation)

      return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action