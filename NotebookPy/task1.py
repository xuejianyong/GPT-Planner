#@title Define actions, domain and problem for task 1 {display-mode: "form"}

if task_name == 'clean a table using a vacuum cleaner':
  names = locals()
  # define variables
  loca, loca1, loca2, = variables("loca loca1 loca2 ", types=["location"])
  robo,  = variables("robo ", types=["robot"])
  vacu, = variables("vacu ", types=["appliance"])
  tabl, = variables("tabl ", types=["furniture"])
  outl, = variables("outl ", types=["appliance"])
  appl, = variables("appl ", types=["appliance"])
  othe, = variables("othe ", types=["other"])

  # define constants
  kitchen, dining = constants("kitchen dining", types=["location"])
  robot_1, = constants("robot_1 ", types=["robot"])
  table_1, table_2, = constants("table_1 table_2 ", types=["furniture"])
  vacuum_1, vacuum_2, = constants("vacuum_1 vacuum_2 ", types=["appliance"])
  outlet_1, outlet_2, = constants("outlet_1 outlet_2 ", types=["appliance"])
  other_1, = constants("other_1 ", types=["other"])

  # define predicates
  robot_at = Predicate("robot_at", robo, loca)
  arm_is_free = Predicate("arm_is_free", robo)
  table_at = Predicate("table_at", tabl, loca)
  table_is_found = Predicate("table_is_found", tabl)
  table_is_clean = Predicate("table_is_clean", tabl)
  vacuum_at = Predicate("vacuum_at", vacu, loca)
  vacuum_is_grasped = Predicate("vacuum_is_grasped", vacu)
  vacuum_is_unplugged = Predicate("vacuum_is_unplugged", vacu)
  vacuum_is_plugged = Predicate("vacuum_is_plugged", vacu)
  vacuum_is_off = Predicate("vacuum_is_off", vacu)
  vacuum_is_on = Predicate("vacuum_is_on", vacu)
  outlet_at = Predicate("outlet_at", outl, loca)
  appliance_at = Predicate("appliance_at", appl, loca)

  # define actions
  walk = Action(
    name = "walk",
    parameters=[robo, loca1, loca2],
    precondition=robot_at(robo, loca1) & arm_is_free(robo),
    effect=~robot_at(robo, loca1) & arm_is_free(robo) & robot_at(robo, loca2)
  )

  plug_vacuum = Action(
    name = "plug_vacuum",
    parameters=[robo, vacu, outl, loca],
    precondition=robot_at(robo, loca) & vacuum_at(vacu, loca) & vacuum_is_unplugged(vacu) & outlet_at(outl, loca) & arm_is_free(robo),
    effect=vacuum_is_plugged(vacu) & ~vacuum_is_unplugged(vacu)
  )

  grasp_vacuum = Action(
    name = "grasp_vacuum",
    parameters=[robo, vacu, loca],
    precondition=robot_at(robo, loca) & vacuum_at(vacu, loca) & arm_is_free(robo),
    effect=~arm_is_free(robo) & vacuum_is_grasped(vacu)
  )

  find_table = Action(
    name = "find_table",
    parameters=[robo, tabl, loca],
    precondition=table_at(tabl, loca) & robot_at(robo, loca),
    effect=table_is_found(tabl)
  )

  turnon_vacuum = Action(
    name = "turnon_vacuum",
    parameters=[vacu],
    precondition=vacuum_is_plugged(vacu) & vacuum_is_off(vacu) & vacuum_is_grasped(vacu),
    effect=vacuum_is_on(vacu) & ~vacuum_is_off(vacu)
  )

  clean_table = Action(
    name = "clean_table",
    parameters=[robo, vacu, tabl, loca],
    precondition= table_is_found(tabl) & robot_at(robo, loca) & table_at(tabl, loca) & vacuum_is_on(vacu) & vacuum_is_grasped(vacu),
    effect=table_is_clean(tabl)
  )

  turnoff_vacuum = Action(
    name = "turnoff_vacuum",
    parameters=[vacu],
    precondition=~vacuum_is_off(vacu) & vacuum_is_grasped(vacu),
    effect=vacuum_is_off(vacu)
  )

  putdown_vacuum = Action(
    name = "putdown_vacuum",
    parameters=[robo, vacu, loca],
    precondition=vacuum_is_off(vacu) & vacuum_is_grasped(vacu) & robot_at(robo, loca) & vacuum_at(vacu, loca),
    effect=~vacuum_is_grasped(vacu) & arm_is_free(robo)
  )

  unplug_vacuum = Action(
    name = "unplug_vacuum",
    parameters=[robo, vacu, outl, loca],
    precondition=robot_at(robo, loca) & vacuum_at(vacu, loca) & vacuum_is_plugged(vacu) & vacuum_is_off(vacu) & outlet_at(outl, loca) & arm_is_free(robo),
    effect=vacuum_is_unplugged(vacu)
  )

  operate = Action(
    name = "operate",
    parameters=[robo, appl, loca],
    precondition=robot_at(robo, loca) & appliance_at(appl, loca),
    effect=robot_at(robo, loca) & appliance_at(appl, loca)
  )

  # define domain
  requirements = [Requirements.STRIPS, Requirements.TYPING]
  domain_1 = Domain("dining",
      requirements=requirements,
      types=["location", "robot", "food", "utensil", "beverage", "furniture", "appliance", "other"],
      predicates=[robot_at, arm_is_free,
                  table_at, table_is_found, table_is_clean,
                  vacuum_at, vacuum_is_grasped, vacuum_is_plugged, vacuum_is_unplugged, vacuum_is_off, vacuum_is_on,
                  outlet_at,
                  appliance_at
                  ],
      actions=[walk,
              find_table, clean_table,
              grasp_vacuum, plug_vacuum, turnon_vacuum, turnoff_vacuum, unplug_vacuum, putdown_vacuum,
              operate
              ])

  # define problem
  setting = np.random.choice(list(range(0, 2)), p=np.array([ratio_1object, 1.0 - ratio_1object]))

  if setting == 0: # only one vacuum
    dy_init_1 = [robot_at(robot_1, kitchen), arm_is_free(robot_1),
              vacuum_at(vacuum_1, dining), vacuum_is_unplugged(vacuum_1), vacuum_is_off(vacuum_1),
              table_at(table_1, dining),
              outlet_at(outlet_1, dining)]

    dy_init_1_content = [['robot_at', 'robot_1', 'kitchen'], ['arm_is_free', 'robot_1'],
                      ['vacuum_at', 'vacuum_1', 'dining'], ['vacuum_is_unplugged', 'vacuum_1'], ['vacuum_is_off', 'vacuum_1'],
                      ['table_at', 'table_1', 'dining'],
                      ['outlet_at', 'outlet_1', 'dining']]

    problem_1 = Problem(
          "clean_table",
          domain=domain_1,
          requirements=requirements,
          objects=[kitchen, dining, basement, robot_1, table_1, vacuum_1, outlet_1],
          init=dy_init_1,
          goal=table_is_clean(table_1) & vacuum_is_off(vacuum_1) & vacuum_is_unplugged(vacuum_1) & arm_is_free(robot_1)
      )
  else: # two vacuums and two outlets
    dy_init_1 = [robot_at(robot_1, kitchen), arm_is_free(robot_1),
              vacuum_at(vacuum_1, dining), vacuum_is_unplugged(vacuum_1), vacuum_is_off(vacuum_1),
              vacuum_at(vacuum_2, dining), vacuum_is_unplugged(vacuum_2), vacuum_is_off(vacuum_2),
              table_at(table_1, dining),
              outlet_at(outlet_1, dining), outlet_at(outlet_2, dining)]

    dy_init_1_content = [['robot_at', 'robot_1', 'kitchen'], ['arm_is_free', 'robot_1'],
                         ['vacuum_at', 'vacuum_1', 'dining'], ['vacuum_is_unplugged', 'vacuum_1'], ['vacuum_is_off', 'vacuum_1'],
                         ['vacuum_at', 'vacuum_2', 'dining'], ['vacuum_is_unplugged', 'vacuum_2'], ['vacuum_is_off', 'vacuum_2'],
                         ['table_at', 'table_1', 'dining'],
                         ['outlet_at', 'outlet_1', 'dining'], ['outlet_at', 'outlet_2', 'dining']]

    problem_1 = Problem(
          "clean_table",
          domain=domain_1,
          requirements=requirements,
          objects=[kitchen, dining, basement, robot_1, table_1, vacuum_1, vacuum_2, outlet_1, outlet_2],
          init=dy_init_1,
          goal=table_is_clean(table_1) & vacuum_is_off(vacuum_1) & vacuum_is_unplugged(vacuum_1) & vacuum_is_off(vacuum_2) & vacuum_is_unplugged(vacuum_2) & arm_is_free(robot_1)
      )

  print('!Note: we are defining actions, domain and problem for task 1:\'{}\', and the setting is \'{}\''.format(task_name, setting))