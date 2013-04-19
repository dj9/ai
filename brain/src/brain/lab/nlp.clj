(ns brain.lab.nlp
  (:use clojure.pprint) 
  (:use opennlp.nlp)
  (:use opennlp.treebank) 
  (:use opennlp.tools.filters)
  )

(def get-sentences (make-sentence-detector "resources/models/en-sent.bin"))
(def tokenize (make-tokenizer "resources/models/en-token.bin"))
;(def detokenize (make-detokenizer "resources/models/english-detokenizer.xml"))
(def pos-tag (make-pos-tagger "resources/models/en-pos-maxent.bin"))
(def name-find (make-name-finder "resources/models/en-ner-person.bin"))
(def chunker (make-treebank-chunker "resources/models/en-chunker.bin"))

(defn meaning [sentence]
  (pprint (chunker (pos-tag (tokenize sentence))))
  )

(defn divide [sentence]
  (pprint (pos-tag (tokenize sentence)))
  )

(defn get-nouns [sentence]
  (pprint (nouns (pos-tag (tokenize sentence))))
  )


(def tom-cruise "Tom Cruise is an American film actor and producer.")