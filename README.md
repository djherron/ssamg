# Spotify Songs and Music Genres

This repo describes a tabular classification dataset and a companion, custom OWL ontology class hierarchy.

# The Spotify Songs dataset

dataset name: 114000 Spotify Songs
* a tabular dataset whose features describe characteristics of songs on Spotify
* the objective is to classify the songs according to their **music genre**
* features: 19
  - 4 of these are string names, so are of no use
  - 2 of the remaining 15 features are categorical, one with 12 levels and one with 5 levels; if we imagine converting these two categorical features to binary features (12 and 5, respectively), we would have 13 + 12 + 5 = 30 features
* classes: 114  (114 unique music genres)
  - we don't have to use them all; we can choose a subset of genres that help to form an interesting music genre class hierarchy
  - the Kaggle page for the dataset says the dataset has 125 genre classes, but this is inaccurate. Analysis of the dataset shows that the data samples refer to 114 unique genres
* balance: each of the 114 music genres has exactly 1000 data samples

available at:
* https://www.kaggle.com/datasets/priyamchoksi/spotify-dataset-114k-songs
* If you don't already have an account on Kaggle, you may need to register in order to access and download the dataset (not sure).

`explore_spotifySongs_dataset.py`
* a script for getting familiar with the dataset
* performs some rudimentary exploratory data analysis
* feel free to use it as a starting point for evaluating the dataset
* download the dataset; place it somewhere on your local drive; adjust the directory locations in the script; run the script section-by-section and inspect the results written to your IDE's console

`The 114 track genres.txt`
* a listing of the 114 unique track genres (classes) in the dataset

why this dataset feels like a good candidate:
* for me, the dataset has several attractive features that suit our needs
* 114 classes (music genres) is a lot, but that's ok: we don't need to use them all; we can select a subset of music genres that a) gives us a moderate number of (base) classes and b) facilitates the quick design of a custom class hierarchy of suitable size, variety and complexity
* music genre classification is a domain that's flexible and familiar; our prospects for designing a custom music genre class hierarchy that fits the dataset and our experimental needs (for reasonable variety and complexity in the generalisation implied by the hierarchy) are good
* each music genre has exactly 1000 data samples; so no matter which subset of music genres we select, we'll still have a perfectly balanced dataset in the end; so we've got full freedom to choose a subset of music genres that facilitate the design of a class hierarchy with characteristics we like and want
* if we select something on the order of, say, N=20 music genres (base classes), we'll have a dataset of 20,000 samples; that leaves plenty of scope for further splitting the data into reasonably-sized (and balanced) training, validation and test sets
* a dataset of 20,000 to 30,000 samples, say, should mean training will still be fast and easy on laptops; no need to mess with GPUs and cloud platforms and long training turn-around times
* the flat, friendly features of this tabular dataset mean that much of the code and experiments already in place should be little impacted by migrating from the Zoo dataset 

datawrangling
* the exploratory data analysis suggests some data wrangling of the input features may be appropriate
* feature 'key' (the key of the song, presumably) is categorical, with 12 levels indicated by integers 0 to 11; consider converting this one categorical feature into binary features 
* feature 'time_signature' is categorical, with 5 levels indicated by integers; consider converting this one categorical feature into binary features
* if we select a subset of the 114 music genres, the number of levels of these two categorical features present in our subset may be lower than 11 and 5, respectively; so we won't know how many binary features we need until we've settled on the precise set of music genres we want as our base classes

# The MusicGenres OWL class hierarchy

`MusicGenres.ttl`
* an initial attempt at a custom OWL class hierarchy of music genres
* we can try it as-is, or use it as a starting point for further development
* current total number of classes (music genres) in the hierarchy: 43
* many of the classes (music genres) in the hierarchy map directly to track_genres in the SpotifySongs dataset; but, as is reflected in the class hierarchy visualisation (by class names surrounded with borders), we are currently proposing that only 17 of the genres be included in our subset of the SpotifySongs dataset
* the corresponding subset of the SpotifySongs dataset would have 17 * 1000 = 17,000 data samples
* the class hierarchy adjacency matrix would be 43 x 43

`MusicGenres_class_hierarchy.png`
* a visualisation of the MusicGenres OWL class hierarchy
![MusicGenres](MusicGenres_class_hierarchy.png "MusicGenres OWL class hierarchy")
* class names surrounded with borders indicate the genres from the SpotifySongs dataset that we propose be included in our subset of the dataset

Influences that helped shape the design of the MusicGenres OWL class hierarchy
* https://musicmap.info/
  - a genealogy of popular music genres
* https://en.wikipedia.org/wiki/List_of_music_genres_and_styles
  - a list (hierarchy) of music genres and styles
* hierarchy depth considerations: from amongst the 114 music genres in the dataset, we had a preference for those base classes that we can place deep within a class hierarchy --- i.e. so that they have multiple parent classes
* hierarchy width considerations: from amongst the 114 music genres in the dataset, we selected base classes that give a wide variety of different subsumption paths in the hierarchy; that is, we want different base classes to have differences in their sets of parent classes
* hierarchy variety considerations: in a class hierarchy, it's valid for any given class to have more than one direct parent class; so we selected base classes from the SpotifySongs dataset partly based on the opportunities they created for defining instances of multiple parentage in the class hierarchy
* personal bias


