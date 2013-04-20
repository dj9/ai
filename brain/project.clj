(defproject brain "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.5.1"]
                 [clojure-opennlp "0.2.0"]
                 [clojurewerkz/neocons "1.0.3"]
                 [http-kit "2.0.1"]
                 [org.clojure/data.json "0.2.2"]
                 [clj-http "0.7.2"]
                 [compojure "1.1.5"]
                 [korma "0.3.0-RC5"]
                 [org.postgresql/postgresql "9.2-1002-jdbc4"]
                 ]
  :main brain.core)
