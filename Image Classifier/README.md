# Image Classifier
The objective of this project is to get a glance at the power of neral networks. In this project the library tensorflow was used to build a neural network. Kearas layers was used to build multiple layers of the neural network.
## Preprocessing
1. This project is an example of supervised learning. A data set already bulit into the library tensorflow was taken.
2. The datasete was divided into training data set and testing data set.

## Building Neural Network
1. Kearas sequential layer was used to build a neural network.
2. Four layers of sequential layers were used namely:
    * Flatten
    * Dense - 128 activation = 'relu'
    * Dense - 128 actiavation = 'relu'
    * Dense - 10 activation = 'softmax'
3. Optimizer = 'adam'
   loss = 'sparse_categorical_crossentropy'


The number 128 represents the number of functions through which each pixel of the image is fed. The computer figures out the parameters of each function and returns one of 10 values.
### Various actiavtion used:
1. ReLu - Rectified Linear Unit
   If the value is grater than zero it returns the value else it returns zero.
2. Softmax
   Of all the 10 values in the last layer it sets the maximum value to '1' and the rest to '0'. As a result of which we do not need to find 
   the maximum value instead find '1'.
