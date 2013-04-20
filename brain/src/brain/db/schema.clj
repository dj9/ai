(ns brain.db.schema
  (:require [clojure.java.jdbc :as sql]))

(def db-spec
  {:subprotocol "postgresql"
   :subname "//localhost/people"
   :user "retailer"
   :password "retailer"})