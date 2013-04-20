(ns brain.model.human)


;(save-relation "Tom Cruise" son of "Mathew Cruise" and "Marie Cruise")
;of supports reverse relations
(defn of [related-entity & others] 
  
  )

(defmacro save-relation [& grammer]
  
  )
(defn brother [entity1 entity2]
  (if (= "male" (entity-type entity1))
    (save-relation entity1 "brother" entity2)
    )
  (println entity1 "brother of" entity2)
  )

(defn father [child]
  
  )

(defn child [male-parent female-parent]
  
  )

(defn mother [child])

(defn son
  "Check if more than two parents. Also check if parents are of different sex. If same sex, mark as adopted"
  [parent]
  
  )

(defn daughter[parent])

(defn brother [sibling])
(defn sister [sibling])

(defn aunt [relative-child])
(defn uncle[relative-child])


(defn save-entity [entity-name]
  
  )


(defn person [entity-name]
  (save-entity entity-name )
  )
