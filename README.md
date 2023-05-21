# Exploring impressionist art with VGG16

In this assignment I'm going to use the pretrained classifier VGG16 to explore similarities between impressionist artists. To do this, I will use a dataset containing nearly 5000 pieces of art from ten different impressionist artist. The dataset can been downloaded from Kaggle from this [link](https://www.kaggle.com/datasets/delayedkarma/impressionist-classifier-data).
The VGG16 model can be used to extract features from images. Theese image embeddings can then be compared using scikit-learn in order to find the nearest neighbours of a given image. The image embedding is a vector representation consisting of a large array of numbers. 

The code in this repository does the following: 
1. loops through every painting in the dataset
2. extracts features from each image using VGG16
3. finds most similar painting for each paining using scikit-learn
4. makes a visualization for each artist showing the artists sorted by amount of most similar paintings

## User instructions

1. Download the dataset from Kaggle via this [link](https://www.kaggle.com/datasets/delayedkarma/impressionist-classifier-data). The dataset will be downloaded as a zip-file called "archive" which will be dissolved into two folders called "training" and "validation" once unzipped. In order for the code to work, please save the zip-file into a folder called "paintings". 
2. In order for the os path system to work, please have the **paintings** folder open on the same level as this repository. 
3. Unzip the archive by navigating to the **paintings** folder in the terminal and type:

`unzip flowers.zip`

4. Install necessary packages by running setup script like so:

`bash setup.sh`

5. run code by using the run.sh file like so:

`bash run.sh`

## Discussion of results

The visualizations show that in all instances the artist with most amount of similar paintings is the target artist. This means that the VGG16 can recognize the specific artist's style. 

