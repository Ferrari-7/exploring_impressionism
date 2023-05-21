
'''
This code does the following:
1. loops through every painting in the dataset
2. extracts features from each image using VGG16
3. finds most similar painting for each paining using scikit-learn
4. makes a visualization for each artist showing the artists sorted by amount of most similar paintings

'''

# Importing packages
# base tools
import os, sys
sys.path.append(os.path.join(".."))
# data analysis
import pandas as pd
import numpy as np
from numpy.linalg import norm
# tensorflow
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import (load_img, 
                                                  img_to_array)
from tensorflow.keras.applications.vgg16 import (VGG16, 
                                                 preprocess_input)
# sklearn
from sklearn.neighbors import NearestNeighbors
# for visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Defining helper function used to extract feautures from images.
# the following function was provided by course instructor
def extract_features(img_path, model):
    # Define input image shape
    input_shape = (224, 224, 3)
    # load image from file path
    img = load_img(img_path, target_size=(input_shape[0], 
                                          input_shape[1]))
    # convert to array
    img_array = img_to_array(img)
    
    # expand to fit dimensions
    expanded_img_array = np.expand_dims(img_array, axis=0)
    
    # preprocess image
    preprocessed_img = preprocess_input(expanded_img_array)
    
    # use the predict function to create feature representation
    features = model.predict(preprocessed_img)
    
    # flatten
    flattened_features = features.flatten()

    # normalise features
    normalized_features = flattened_features / norm(features)

    return normalized_features

# Loading the pre-trained classifer VGG16
def load_model():
    model = VGG16(weights='imagenet', 
                include_top=False,
                pooling='avg',
                input_shape=(224, 224, 3)) # defining image size
    
    return model

def load_data():
    # Making a Pandas data frame with filenames and accompanying artist label
    # using os to make a list of artist by listing directories in training folder
    artists = os.listdir(os.path.join("..", "paintings", "training", "training"))
    data = []
    for artist in artists: # looping through each artist folder
        root_dir = os.path.join("..", "paintings", "training", "training", artist)
        paintings = os.listdir(root_dir)
        for painting in paintings: # looping through each paing in artist folder
            filename = root_dir + "/" + painting # defining filename
            new_data = {"artist": artist, "filename": filename}
            data.append(new_data)

    # combining with data in validation folder
    artists = os.listdir(os.path.join("..", "paintings", "validation", "validation"))
    for artist in artists:
        root_dir = os.path.join("..", "paintings", "validation", "validation", artist)
        paintings = os.listdir(root_dir)
        for painting in paintings:
            filename = root_dir + "/" + painting
            new_data = {"artist": artist, "filename": filename}
            data.append(new_data)
    
    # making a data frame from list of dicts using pandas
    df = pd.DataFrame.from_records(data)

    return df

def peform_feature_extraction(df, model):
    # making filenames column back into a list
    filenames = df['filename'].tolist()

    feature_list = []
    for i in range(len(filenames)): # Looping through each number in index
        # using helper function from before to extract feautures
        feature_list.append(extract_features(filenames[i], model))
    
    # using K-Nearest Neighbours to find similar images
    neighbors = NearestNeighbors(n_neighbors=10, 
                             algorithm='brute',
                             metric='cosine').fit(feature_list)

    data_nearest = []
    for i in range(len(feature_list)): # Looping through each number in index
        # calculate nearest neighbours for i in index
        distances, indices = neighbors.kneighbors([feature_list[i]])
        # selecting nearest distance and index
        nearest_distance = distances[0][1]
        nearest_index = indices[0][1]
        # using nearest index to locate nearest artist in data frame along with filename
        nearest_artist = df.loc[nearest_index, "artist"]
        nearest_filename = df.loc[nearest_index, "filename"]
        nearest_dict = {"nearest_artist": nearest_artist, "nearest_filename": nearest_filename, "distance": nearest_distance}
        data_nearest.append(nearest_dict)
    
    # combining new data with previous data frame
    df2 = pd.DataFrame.from_records(data_nearest)
    df = pd.concat([df, df2], axis=1)
    df.to_csv(os.path.join("out", "impressionist.csv"))

    return df

def visualize(df):
    # defining custom palette 
    palette =  {"Pissarro" : "#E9DAAC", 
                "Hassam" : "#B5D870", 
                "Monet" : "#97A7DA", 
                "Degas" : "#EC8B36", 
                "Matisse" : "#C263CD", 
                "Sargent" : "#934829", 
                "Cezanne" : "#A3DDBE",
                "Gauguin" : "#C5182D",
                "Renoir" : "#BC9400",
                "VanGogh" : "#F3D83C"}

    artist_list = df["artist"].unique()
    for artist in artist_list:
        # selecting only rows with current artist in loop
        d = df[df["artist"]==artist]
        
        # counting the amount the nearest artist apears. 
        # this is done to make better visualizations where the artists are shown in descending order from most occuring to least
        count = d[["artist", "nearest_artist"]].groupby(["nearest_artist"]).count().reset_index() # counting
        count = count.sort_values(by="artist",ascending=False) # sort by descending
        order = count['nearest_artist'].tolist() # making into list for seaborn formatting

        plt.clf() # clearing plt for each loop
        # making countplot for each artist. Shows the nearest artists in order. 
        countplt = sns.countplot(x=d["nearest_artist"], order=order, palette=palette)
        # rotating labels so that they don't overlap
        plt.xticks(rotation=45, 
                horizontalalignment='right',
                fontweight='light',
                fontsize='small')
        countplt.set_title(artist) # making the current artist in loop the title
        
        # saving visualization
        vis_path = os.path.join("out", artist + ".png")
        plt.savefig(vis_path)

def main():
    model = load_model()
    df = load_data()
    df = peform_feature_extraction(df, model)
    visualize(df)

if __name__=="__main__":
    main()
