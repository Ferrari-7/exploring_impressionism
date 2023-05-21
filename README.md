# Exploring impressionist art with VGG16

In this assignment I'm going to use the pretrained classifier VGG16 to explore similarities between impressionist artists. To do this, I will use a dataset containing nearly 5000 pieces of art from ten different impressionist artist. The dataset can been downloaded from Kaggle from this [link](https://www.kaggle.com/datasets/delayedkarma/impressionist-classifier-data).
The VGG16 model can be used to extract features from images. Theese feautures can then be compared using scikit-learn in order to find the nearest neighbours of a given image. 

The code in this repository does the following: 
1. loops through every painting in the dataset
2. extracts features from each image using VGG16
3. finds most similar painting for each paining using scikit-learn
4. makes a visualization for each artist showing the artists sorted by amount of most similar paintings

## User instructions

## Discussion
