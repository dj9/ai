(ns brain.db.entity
  (:use korma.core
        [korma.db :only (defdb)])
  (:require [brain.db.schema :as schema]))

(defdb db schema/db-spec)

(defentity app_entity)
(defentity app_entitydescriptor)
(defentity app_entitydescriptorrelation)

(defn get-entity [name]
  (first (select app_entity (where {:name name})))
  )

(defn entity-exists? [name]
  (if (nil? (get-entity name))
    false true
    )
  )

(defn save-entity [name description]
  (let [db-entity (get-entity name)]
    (if (nil? db-entity)
      (insert app_entity (values {:name name :description description}))
      db-entity)))

(defn get-entity-descriptor [name]
  (first (select app_entitydescriptor (where {:name name})))
  )

(defn save-entity-descriptor [name description]
  (let [db-entity-descriptor (get-entity-descriptor name)]
    (if (nil? db-entity-descriptor)
      (insert app_entitydescriptor (values {:name name :description description}))
      db-entity-descriptor)))

(defn save-entity-descriptor-relation [entity relation descriptor best]
  
  )