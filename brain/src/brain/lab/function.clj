(ns brain.lab.function)



(defn entity-type [entity type]
  (if ( = (:type entity ) type)
    true false
    )
  )

(defn get-entity [] {:gender "male"})


(defn save-relation [entity-1 relation entity-2]
  (println "relation saved")
  
  )


(defn brother [entity1 entity2]
  (if (= "male" (entity-type entity1))
    (save-relation entity1 "brother" entity2)
    )
  (println entity1 "brother of" entity2)
  )

(defn relation [str-entity-1 function str-entity-2]
  (println (function (get-entity str-entity-1) (get-entity str-entity-2)))

  )

;(relation "Tom Cruise" is the brother of "Mathew Cruise")


(def sister "sister")
