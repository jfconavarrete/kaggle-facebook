kaggle-facebook
==============================

Kaggle Facebook Competition

Project template created using cookiecutter.
https://drivendata.github.io/cookiecutter-data-science/

## Getting Started

1. Run src/data/download_dataset.py to download and extract the datasets.

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
	|
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── LICENSE

## Notes

### Essential questions

* Did you specify the type of data analytic question (e.g. exploration, association causality) before touching the data?
	* We are trying to order the places (i.e by their likelihood) based on the following measurements from the dataset: coordinates, accuracy (?), time (?) and place_id.
	
* Did you define the metric for success before beginning?
	* The metric is Mean Average Precision (What is this?)
	
* Did you understand the context for the question and the scientific or business application?
	* We are building a system that would rank a list of places given 'coords', 'accuracy' and 'time'. The purpose might be to enable for specific ads (i.e interesting places around the hotel) to be shown to the person (on FB?) depending on this list.
	
* Did you record the experimental design?
	* Given.
	
* Did you consider whether the question could be answered with the available data?
	* We need to further explore 'accuracy' and to check if we could identify different clusters of users - we don't know if the data was genereted by 1 person or many, so we need to check its structure.
	
### Checking the data
* Null values?
	* No!
	
* What do we know of the measurements?
	* First column is ID and is useless.
	
	* Second and Third are coords., they are in kilometers and are floating point. Min is (0,0) and max is (10,10);
	
	* Fourth column is accuracy. Range is (1, 1033) and seems to follow a power law distribution. We assume that this is the accuracy of the location given by the GPS. This claim is supported by the fact that the data comes from a mobile device,
	which is able to give location but this information is sometimes not accurate (i.e in buildings), so we would like to know
	what is the accuracy of the reading. In order to convert this into real accuracy, we need to normalize the column and assign it values of (1 - current_val).
	
	* The fifth column is time given as a timestamp. It looks like the UNIX timestamps so we assume that 0 means 01/01/1970 and
	everything else is the number of seconds since 0.
	
	* Last column is the class_id, given as an integer

### Modelling
* Based on our assumption that the 'accuracy' column indicates GPS uncertainty, we would like to first pin-point the possible real locations of all unique places. We are currently trying to apply K-Means for that purpose, however the dataset is huge - need to find a GPU-based implementation.

* Following, we might use the cluster centers directly to train a classifier or build some basis-functions centered at the centroids. The reasoning behind that is that we would like to be able to rate a place based on its distance to a given data point.
