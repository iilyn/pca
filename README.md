# Principal Component Analysis (PCA)
This is a simple example of how to implement the PCA using scikit-learn.

The PCA is applied to a s-curved dataset. The dataset lies in the vector space spanned by the basis $x = [1, 0, 0]^T$, $y = [0, 1, 0]^T$ and $z = [0, 0, 1]^T$. The goal of the PCA is to transform the original 3-dimensional data into a 2-dimensional representation while losing as little information as possible.

The scikit-learn library provides a predefined PCA functionality. Therefore, implementation is quite simple.

By printing the basis of the 2D, as well as visualising data, one can see that the new vector space is almost the x- and z-axis. 

