import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import cv2

from sklearn import metrics
from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn import cross_validation as cv
from sklearn import svm
from sklearn import ensemble
from sklearn import linear_model

def main():
	train = pd.read_csv('../../data/raw/train.csv')
	print train.shape
	
	uniq = train['place_id'].nunique()
	print uniq

	col_headers = list(train.columns.values)
	print col_headers
	train[col_headers[1:-1]] = train[col_headers[1:-1]].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
	train['accuracy'] = 1 - train['accuracy']
	train_X_norm = train.values[:,:-1]
	print train_X_norm.shape

	K = uniq
	clusters = range(0,K)
	batch_size = 500
	n_init = 10

	train_X_norm = train_X_norm.astype(np.float32)
	print train_X_norm.dtype
	print train_X_norm.shape


	# define criteria and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	ret, label, center = cv2.kmeans(train_X_norm, K, criteria, n_init, cv2.KMEANS_RANDOM_CENTERS)

	print center.shape

if __name__ == '__main__':
	main()