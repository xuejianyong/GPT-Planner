(define
	(domain dining_setup_table)
	(:requirements :strips :typing)
	(:types robot cupboard table plate fork location food utensil beverage furniture other appliance obstacle)
	(:predicates (robot_at ?r - robot ?l - location) (hand_empty ?r - robot) (cupboard_at ?c - cupboard ?l - location) (cupboard_is_found ?c - cupboard) (cupboard_is_open ?c - cupboard) (cupboard_is_closed ?c - cupboard) (table_at ?t - table ?l - location) (table_is_found ?t - table) (plate_at ?p - plate ?l - location) (plate_is_found ?p - plate) (plate_is_tookout ?p - plate) (plate_is_placed ?p - plate ?t - table) (fork_at ?f - fork ?l - location) (fork_is_found ?f - fork) (fork_is_tookout ?f - fork) (fork_is_placed ?f - fork ?t - table) (appliance_at ?a - appliance ?l) (robot_cannot_move ?o - obstacle))

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location ?o - obstacle)
		:precondition (and (robot_at ?r ?l1) (hand_empty ?r) (not (robot_cannot_move ?o)))
		:effect (and (robot_at ?r ?l2) (hand_empty ?r) (not (robot_at ?r ?l1)))
	)

	(:action find_cupboard
		:parameters (?r - robot ?c - cupboard ?l - location)
		:precondition (and (cupboard_at ?c ?l) (robot_at ?r ?l))
		:effect (and (cupboard_is_found ?c) (cupboard_at ?c ?l) (robot_at ?r ?l))
	)

	(:action open_cupboard
		:parameters (?r - robot ?c - cupboard ?l - location)
		:precondition (and (cupboard_is_closed ?c) (cupboard_at ?c ?l) (cupboard_is_found ?c) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (cupboard_is_open ?c) (not (cupboard_is_closed ?c)) (cupboard_at ?c ?l) (cupboard_is_found ?c) (robot_at ?r ?l) (hand_empty ?r))
	)

	(:action close_cupboard
		:parameters (?r - robot ?c - cupboard ?l - location)
		:precondition (and (cupboard_is_open ?c) (cupboard_at ?c ?l) (cupboard_is_found ?c) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (cupboard_is_closed ?c) (not (cupboard_is_open ?c)) (cupboard_at ?c ?l) (cupboard_is_found ?c) (robot_at ?r ?l) (hand_empty ?r))
	)

	(:action find_table
		:parameters (?r - robot ?t - table ?l - location)
		:precondition (and (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (table_is_found ?t) (table_at ?t ?l) (robot_at ?r ?l))
	)

	(:action find_plate
		:parameters (?r - robot ?p - plate ?c - cupboard ?l - location)
		:precondition (and (plate_at ?p ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l))
		:effect (and (plate_is_found ?p) (plate_at ?p ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l))
	)

	(:action takeout_plate
		:parameters (?r - robot ?p - plate ?c - cupboard ?l - location)
		:precondition (and (plate_is_found ?p) (plate_at ?p ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (plate_is_tookout ?p) (not (hand_empty ?r)) (plate_is_found ?p) (plate_at ?p ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l))
	)

	(:action move_plate
		:parameters (?r - robot ?p - plate ?l1 - location ?l2 - location)
		:precondition (and (plate_is_tookout ?p) (not (hand_empty ?r)) (plate_is_found ?p) (plate_at ?p ?l1) (robot_at ?r ?l1))
		:effect (and (plate_is_tookout ?p) (not (hand_empty ?r)) (plate_at ?p ?l2) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action place_plate
		:parameters (?r - robot ?p - plate ?t - table ?l - location)
		:precondition (and (table_is_found ?t) (plate_is_tookout ?p) (not (hand_empty ?r)) (plate_at ?p ?l) (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (plate_is_placed ?p ?t) (hand_empty ?r) (robot_at ?r ?l))
	)

	(:action find_fork
		:parameters (?r - robot ?f - fork ?c - cupboard ?l - location ?p - plate)
		:precondition (and (fork_at ?f ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l))
		:effect (and (fork_is_found ?f) (fork_at ?f ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l))
	)

	(:action takeout_fork
		:parameters (?r - robot ?f - fork ?c - cupboard ?l - location)
		:precondition (and (fork_is_found ?f) (fork_at ?f ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (fork_is_tookout ?f) (not (hand_empty ?r)) (fork_is_found ?f) (fork_at ?f ?l) (cupboard_is_open ?c) (cupboard_at ?c ?l) (robot_at ?r ?l))
	)

	(:action move_fork
		:parameters (?r - robot ?f - fork ?l1 - location ?l2 - location)
		:precondition (and (fork_is_tookout ?f) (not (hand_empty ?r)) (fork_is_found ?f) (fork_at ?f ?l1) (robot_at ?r ?l1))
		:effect (and (fork_is_tookout ?f) (not (hand_empty ?r)) (fork_at ?f ?l2) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action place_fork
		:parameters (?r - robot ?f - fork ?t - table ?l - location)
		:precondition (and (table_is_found ?t) (fork_is_tookout ?f) (not (hand_empty ?r)) (fork_at ?f ?l) (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (fork_is_placed ?f ?t) (hand_empty ?r) (robot_at ?r ?l))
	)

	(:action operate
		:parameters (?r - robot ?a - appliance ?l1 - location ?l2 - location)
		:precondition (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
		:effect (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
	)
)