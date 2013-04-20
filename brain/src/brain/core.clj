(ns brain.core
  (:gen-class)
  (:use org.httpkit.server))

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))


(defn app [req]
  {:status  200
   :headers {"Content-Type" "text/html"}
   :body    "hello HTTP!"})



(defn -main
  [& args]
  (println "Welcome to brain"))