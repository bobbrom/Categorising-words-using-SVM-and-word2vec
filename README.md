# Categorising-words-using-SVM-and-word2vec

This project shows how a Support Vector Machine can be used to tell if a word is a noun, verb, adverb or adjective.

While this has little to no practical use it is a great demonstration of how word2vec works as it creates vectors out of words based on their place within a sentence then it makes sense that these categories such as these would be clustered together. These clusters can be then found using a simple linear Support Vector Machine.

### A brief summary of Word2Vec

Word2Vec is a model for creating such word embeddings. Here words are turned into vectors based on their semantics in many aspects; each aspect is given a vector which is changed via its meaning. This means that words which are similar in meaning have a smaller Euclidian distance than words which are less similar and also means that words can have maths performed on them based on their semantics.

This is done via two algorithms the first being the Continuous Bag Of Words (CBOW) named as the order of the words itself does not matter which takes the surrounding words and tries to predict the word itself using a shallow neural network. The second can be seen as the inverse of this and is called the Skip-Gram model (Mikolov et al., 2013). Here the neural network attempts to calculate the context words given a centre word. 

This project uses a pre-trained model that in comprised of the Google News dataset. 

<u>As this file is too big to add to the repository it can be downloaded here:</u>

https://figshare.com/articles/dataset/GoogleNews-vectors-negative300_bin/6007688/1

### A brief summary of Support Vector Machines 

A Support Vector Machine (SVM) is a method for supervised learning which provides a binary classification of data. This means that given a set of vectors and labels for each vector an SVM can be trained to see where distinctions can be made between the two sets. This is done by first finding the support vectors which are points which are closest to the opposing data. Then two hyperplanes are drawn between these support vectors with the maximum distance between them after the decision boundary is drawn directly in the middle of these two hyperplanes.



### Results

|           | TP   | FN   | TN   | FP   | Recall   | Precision | F1 Score    |
| --------- | ---- | ---- | ---- | ---- | -------- | --------- | ----------- |
| Noun      | 4044 | 209  | 2206 | 331  | 0.950858 | 0.924343  | 0.937413074 |
| Adjective | 816  | 428  | 5259 | 287  | 0.655949 | 0.739801  | 0.695355773 |
| Adverb    | 401  | 62   | 6298 | 29   | 0.866091 | 0.932558  | 0.898096305 |
| Verb      | 494  | 84   | 6168 | 44   | 0.854671 | 0.918216  | 0.885304659 |

Here we can see even with a linear classifier we can predict if a word is a Noun, Adverb or Verb with a degree of accuracy while Adjective was far less accurate it is still has a significant F1 score meaning it can still be predicted with relative accuracy.
