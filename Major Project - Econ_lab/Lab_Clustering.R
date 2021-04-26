library(tidyverse) # data manipulation
library(cluster) # clustering algorithm
library(factoextra) # clustering algorithms & visualization 

# data preparation 
# any missing value in the data must be removed or estimated
# data must be standardized(i.e. scaled) to make variables comparable

df <- USArrests
df <- na.omit(df)

# clustering algorithm need not to depend to an arbitrary variable unit - standardized

df <- scale(df)
head(df)

# dissimilarity or distance matrix
# choice of distance - critical step in clustering
# defines how the similarity of two elements is calculated and it will 
# influence the shape of the clusters
# classical methods for distance measures are euclidean and manhattan distances

distance <- get_dist(df)
fviz_dist(distance, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))

# using Hartigan Wong algorithm for clustering 

k2 <- kmeans(df, centers = 2, nstart = 25)
str(k2)












