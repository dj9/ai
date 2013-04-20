(ns brain.lab.freebase
  (:require [clojure.data.json :as json]
            [clj-http.client :as client]))

(def api-key "AIzaSyAI-wwDvhhPd4zyrGlFKmKwoymUYQ0Hr0Q")
(def search-url "https://www.googleapis.com/freebase/v1/search")

(defn get-info [query]
  (json/read-str (:body (client/get search-url {:query-params {:query query :key api-key}})))
  )