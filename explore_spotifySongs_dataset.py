#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script explores the '114000 Spotify Songs' dataset:
    https://www.kaggle.com/datasets/priyamchoksi/spotify-dataset-114k-songs
    
Analysis of the dataset shows that the number of unique track_genres
(ie the number of classes to be predicted) is 114.  There are exactly
1000 samples for each of the 114 genres, so the dataset is nicely balanced.
'''

#%%

import pandas as pd
import os


#%%

data_dir = os.path.join('~', 'BigData-Misc', 'SpotifySongs')
filename = 'kaggle_114000_Spotify_Songs.csv'
filepath = os.path.join(data_dir, filename)
filepath = os.path.expanduser(filepath)

# load the training log summary stats into a dataframe
df = pd.read_csv(filepath)

print(f'dataframe shape: {df.shape}')
print()
print('column names:')
print(df.columns)

#%%

# ignore the first column which appears to be an unnamed index column
cols = [idx for idx in range(1,len(df.columns))]

# reload just the columns we want
df = pd.read_csv(filepath, usecols=cols)

print(f'dataframe shape: {df.shape}')
print()
print('column names:')
print(df.columns)


#%%

df.head()


#%%

print('Examine an individual data sample:')
print()

print(df.iloc[0])

#%%

feature_columns = ['popularity', 
                   'duration_ms', 
                   'explicit', 
                   'danceability',
                   'energy', 
                   'key', 
                   'loudness', 
                   'mode', 
                   'speechiness',
                   'acousticness', 
                   'instrumentalness', 
                   'liveness',
                   'valence', 
                   'tempo', 
                   'time_signature']

label_column = ['track_genre']

## Questions about certain columns:
## 1) 'explicit' looks boolean
## 2) 'key' looks categorical; how many values?
## 3) 'mode' looks categorical; how many values?
## 4) 'time_signature' looks categorical; how many values?


#%%

# 'popularity' is an integer between 0 and 100 representing a percentage;
# consider representing as real numbers
print()
print('popularity')
print(df['popularity'].describe())

# 'duration_ms' is an integer number of milliseconds in range of 6 to 7 figures;
# consider representing these as real numbers measuring seconds, to reduce 
# their magnitude
print()
print('duration_ms')
print(df['duration_ms'].describe())

# 'explicit' is a boolean;
# consider converting this feature to a binary feature
print()
print('explicit')
print(df['explicit'].describe())

# 'key' is categorical, with integers 0 to 11 used as 12 category labels;
# consider converting this feature to 12 binary features
print()
print('key')
print(df['key'].describe())
print(f"unique: {df['key'].unique()}")

# 'mode' is binary: 0 or 1
print()
print('mode')
print(df['mode'].describe())
print(f"unique: {df['mode'].unique()}")

# 'time_signature' is categorical, with integers 0,1,3,4,5 used as 5 category labels;
# consider converting this feature to 5 binary features
print()
print('time_signature')
print(df['time_signature'].describe())
print(f"unique: {df['time_signature'].unique()}")


#%%

print()
print('track_genre')
print(df['track_genre'].describe())
print(f"unique: {df['track_genre'].unique()}")


#%% count the data samples per track_genre

track_genres_unique = df['track_genre'].unique().tolist()

samples_per_genre = []
print('genre | n_samples')
print()
for genre in track_genres_unique:
    mask = df['track_genre'] == genre 
    n_samples = sum(mask)
    print(f'{genre} | {n_samples}')
    samples_per_genre.append(n_samples)

print()
print(f'sum of samples_per_genre: {sum(samples_per_genre)}')




