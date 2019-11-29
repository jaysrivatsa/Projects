## Objctive
Develop a machine learning program to identify when an article might be fake news.

The metric used to tune this model is 'accuracy'.

accuracy = (correct predictions/(correct predictions + incorrect predictions))

## What is NLP?

Natural language processing is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human languages, in particular how to program computers to process and analyze large amounts of natural language data.

## Glossary

Lemmatization: It is the process of converting the a word into its root form.

Stemming: Abruptly chopping off words is called Stemming. For example: computational, computed etc are converted to comput.

Removing stop words: Stop words are words whose frequency is very high in number. Words like 'the', 'is', 'a' are known as stop words.

## Process in NLP

1. Prerocessing textual data
    * Stemming
    * Lemetization
    * Removing stop words
    * Tokeninzing
2. Creating a document term matrix.
3. Converting the document term matrix to tfidf vectorizer.
4. Building models for classification