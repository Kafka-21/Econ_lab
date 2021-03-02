# finding the nearest neighbors
from sklearn import neighbors, datasets
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors = 2, algorithm = 'ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
print(indices)
print(distances)

# because the quert set matches the training set, the nearest neighbor of each point is the point itself, at a distance of zero
print(nbrs.kneighbors_graph(X).toarray())

from sklearn.neighbors import KDTree
kdt = KDTree(X, leaf_size = 30, metric = 'euclidean')
print(kdt.query(X, k=2, return_distance = False))

# classifcation using kNN

n_neighbors = 15

# import some data to play with
iris = datasets.load_iris()

# we only take the first two features. We could avoid this ugly slicing by using a two-dim dataset
X = iris.data[:, :2]
y = iris.target

h = .02 # step size in the mesh

# create color maps
cmap_light = ListedColormap(['orange', 'cyan', 'cornflowerblue'])
cmap_bold = ListedColormap(['darkorange', 'c', 'darkblue'])

for weights in ['distance']:
    # we create an instance of neighbors classifier and fit the data
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights = weights)
    clf.fit(X, y)

    # Plot the decision Boundary. For that, we will assign a color to each point in the mesh [x_min, x_max]x[y_min, y_max]
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx , yy = np.meshgrid(np.arange(x_min, x_max, h),
                          np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color Plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))

plt.show()
