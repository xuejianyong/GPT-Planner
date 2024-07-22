(define (problem FR_4_5)
 (:domain first-response)
 (:objects  l1 l2 l3 l4  - location
	    f1 - fire_unit
	    v1 v2 v3 v4 v5 - victim
	    m1 m2 m3 - medical_unit
)
 (:init 
	;;strategic locations
     (hospital l4)
     (hospital l1)
     (water-at l3)
	;;disaster info
     (fire l4)
     (victim-at v1 l1)
     (victim-status v1 dying)
     (fire l4)
     (victim-at v2 l4)
     (victim-status v2 dying)
     (fire l3)
     (victim-at v3 l4)
     (victim-status v3 hurt)
     (fire l3)
     (victim-at v4 l3)
     (victim-status v4 hurt)
     (fire l2)
     (victim-at v5 l3)
     (victim-status v5 dying)
	;;map info
	(adjacent l1 l1)
	(adjacent l2 l2)
	(adjacent l3 l3)
	(adjacent l4 l4)
   (adjacent l1 l1)
   (adjacent l1 l1)
   (adjacent l2 l1)
   (adjacent l1 l2)
   (adjacent l2 l2)
   (adjacent l2 l2)
   (adjacent l2 l3)
   (adjacent l3 l2)
   (adjacent l3 l1)
   (adjacent l1 l3)
	(fire-unit-at f1 l3)
	(medical-unit-at m1 l4)
	(medical-unit-at m2 l4)
	(medical-unit-at m3 l1)
	)
 (:goal (and  (nfire l4) (nfire l4) (nfire l3) (nfire l3) (nfire l2)  (victim-status v1 healthy) (victim-status v2 healthy) (victim-status v3 healthy) (victim-status v4 healthy) (victim-status v5 healthy)))
 )
