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
