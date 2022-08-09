#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date: 08.08.2022
@author: neural.net_

Title: Principal Component Analysis for s-curve dataset.
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

# Define the number of data points.
n_points = 3000

# Get the data and color map.
S_curve, S_colors = datasets.make_s_curve(n_points, random_state=0)

# Plot the original S-curve data.
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(S_curve[:,0], S_curve[:,1], S_curve[:,2],
            c = S_colors, cmap = plt.cm.Spectral)
ax.view_init(4,-72)
ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$y$', fontsize=20)
ax.set_zlabel('$z$', fontsize=20)
plt.title('S-curve dataset')

# Fit PCA object.
# Parameter num_dim defines the number of dimensions the original data should be reduced to.
num_dim = 2
pca = PCA(n_components=num_dim)                 # initialize PCA object
S_curve_pca = pca.fit_transform(S_curve)        # apply PCA

# Visualize the result.
fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot(111)
ax.scatter(S_curve_pca[:,0], S_curve_pca[:,1], c = S_colors, cmap = plt.cm.Spectral)
ax.set_xlabel('$u_0$', fontsize=20)
ax.set_ylabel('$u_1$', fontsize=20)
plt.title('PCA result')

# Print basis.
print('----------------- Orthogonal basis')
print('u_0 =', pca.components_[0])
print('u_1 =', pca.components_[1])