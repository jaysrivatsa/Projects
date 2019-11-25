# Dataset
## Section 1

The dataset (Section_1) contains 500 summaries of news item from CMA’s homepage (500 observations) and class label (Class 1 about merger and Class 0 otherwise) associated with each summary. Task 1 is focussed on text pre-processing and feature extraction. 
The task is coded in Python using NLTK, Scikit-Learn, Pandas, Numpy and Matplotlib. Text pre-processing is done in three steps: first, removal of stop words, second, tokenisation and third, stemming. 

* Stop words are most commonly used words in any language, which means they carry no significant information
* Once the stop words are removed, the sentences in text is broken into individual words, a process known as tokenisation. 
* The tokenised words there might be few inflected word forms which needs to be converted to their base form, for instance, “investigated” and “investigating” are two inflections of the word “investigate”. This process of converting inflected words to base form or root form is called stemming

Section 1 output file contains three columns:
* Column 1-Summary with no stop words
* Column 2- Summary with no stop words and tokenisation
* Column 3-Summary with no stop words, tokenisation and stemmed 
* Column 4-Label from given dataset

## Section 2

The dataset (500 x 1294) contains frequency count of all the words present in each observation. To classify the features across two classes (1-mergers, 0-no mergers) I tried three classifiers-Logistic Regression, Naïve Bayes and SVM. 
As a preliminary step, data is split into train and testing sets. All the models were built on training dataset and validated on testing dataset. 

The following machine learning methods (demonstrated with Logistic regression) have been used in the process of building above machine learning models. 
* Hyper parameter tuning was achieved using GridSearchCV method in scikit-learn package. For instance hyper parameters for logistic regression are: penalty:{l1,l2} ,l1_ratio={0,1,0.05}
* The model then outputs best parameters and classification report is generated with those best parameters including the learning curves
* Used F1-Score (geometric mean of recall and precision) as a classification metric as it takes into account precision (positive predicted value) and recall  (true positive rate)
* Plotted ROC curves with AUC value, indicating how good is the classification above chance level (0.5)

I have repeated the above mentioned process for two different types of document word matrices: Stem frequency word count and TF-IDF.
The SVM model has performed better with TF-IDF features giving an F1-score of 0.96 for class-0 and 0.90 for class-1

## What could be done to improve the model performance
 Instead of using Stem frequency count, using TF-IDF improves the performance (which I demonstrated)
Techniques such as word embeddings and LSTM models mighjt improve model performance but we need more data to achieve that
