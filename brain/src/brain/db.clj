(ns brain.db
  (:require [clojurewerkz.neocons.rest :as nr]
            [clojurewerkz.neocons.rest.nodes :as nn]))

(defn create-node [name type]
  (nr/connect! "http://localhost:7474/db/data/")
  (let [node (nn/create {:name name :type type})]
    (println node)))

(defn get-node [name]
  (nr/connect! "http://localhost:7474/db/data/")
  (nn/get name)
  )