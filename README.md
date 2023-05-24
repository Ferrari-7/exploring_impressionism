# Exploring impressionist art with VGG16

In this assignment I'm going to use the pretrained classifier VGG16 to explore similarities between impressionist artists. To do this, I will use a dataset containing nearly 5000 artworks from ten different impressionist artist. The dataset can been downloaded from Kaggle from this [link](https://www.kaggle.com/datasets/delayedkarma/impressionist-classifier-data).
The VGG16 model can be used to extract features from images. These image embeddings can then be compared using scikit-learn in order to find the nearest neighbours of a given image. The image embedding is a vector representation consisting of a large array of numbers. 

The code in this repository does the following: 
1. loops through every painting in the dataset
2. extracts features from each image using VGG16
3. finds most similar painting for each paining using scikit-learn (except for the paintings by same artist)
4. makes a visualization for each artist showing the artists sorted by amount of most similar paintings

## User instructions

1. Download the dataset from Kaggle via this [link](https://www.kaggle.com/datasets/delayedkarma/impressionist-classifier-data). The dataset will be downloaded as a zip-file called "archive" which will be dissolved into two folders called "training" and "validation" once unzipped. In order for the code to work, please save the zip-file into a folder called "paintings". 
2. In order for the os path system to work, please have the **paintings** folder open on the same level as this repository. 
3. Unzip the archive by navigating to the **paintings** folder in the terminal and type:

`unzip flowers.zip`

4. Install necessary packages by navigating to the *exploring_impressionism* repository and run the setup script like so:

`bash setup.sh`

5. run code by using the run.sh file like so:

`bash run.sh`

## Discussion of results

In my first version of the script, I included instances where the nearest painting was by the same artist. In the end, this meant that in all instances the artist with the most amount of most similar paintings was the artist himself (i.e. the nearest artist to Cézanne was Cézanne). And this was by a very large margin. Although it was encouraging to see that the VGG16 model seemed to be able to recognize the artists’ styles, I eventually chose to skip over nearest paintings by the same artist in order to focus on similarity to other artists. I did this by sorting out nearest indices where the index corresponded with the index number of the given artist.

Below are the results from runnings the code:

| | |
| --- | --- |
| ![](/out/Cezanne.png) | ![](/out/Degas.png) |
| ![](/out/Gauguin.png) | ![](/out/Hassam.png) |
| ![](/out/Matisse.png) | ![](/out/Monet.png) |
| ![](/out/Pissarro.png) | ![](/out/Renoir.png) |
| ![](/out/Sargent.png) |![](/out/VanGogh.png) |

While researching the different artists and their relation to each other, it appears to me that some of these relations seem to be represented in the data. That being said, one should be careful not to actively try to confirm the results while overlooking when the results does not match up to one's expectations. Therefore, I have also looked into connections between artist who, according to the VGG16, have less similar paintings

For example the visualization for Gauguin shows that the two nearest artist are Pissarro and Cézanne. This corresponds with the fact that Gauguin was friends with Pissarro and has been called his unofficial pupil. Furthermore, Pissarro introduced Gauguin to Cézanne. Both have been said to have influenced him heavily.[^1] Henri Matisse has also been inspired by both Cézanne, Gauguin and Renoir, which corresponds with the top results being Gauguin and Cézanne.[^2]

Another example is Renoir and Degas who both have each other as the artist with most similar paintings. This may be due to the fact that they were both urban impressionist (as opposed to landscape impressionist), who depicted mainly life in the city and the people living in it.[^3]

[^1] Kang, Cindy. "Paul Gauguin (1848–1903)," The Metropolitan Museum of Art, March, 2011. https://www.metmuseum.org/toah/hd/gaug/hd_gaug.htm.

[^2] “Henri Matisse,” The National Gallery, accessed May 24, 2023, https://www.nationalgallery.org.uk/artists/henri-matisse.

[^3] Bylsma, Megan, “ II. Chapter 9 – Pierre Auguste Renoir & Edgar Degas,” Open Education Alberta, accessed May 24, 2023, https://openeducationalberta.ca/19thcenturyart/chapter/chapter-9-renoir-and-degas/. 




