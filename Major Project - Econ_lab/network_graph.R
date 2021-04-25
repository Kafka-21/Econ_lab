library(igraph)
library(mlbench) # for Ionoshphere data
library(psych) # for cor2dist
data(Ionosphere)

correlationmatrix = cor(Ionosphere[, which(sapply(Ionosphere, class) == 'numeric')])
distancematrix <- cor2dist(correlationmatrix)

DM1 <- as.matrix(distancematrix)
## Zero out connection where there is low (absolute) correlation 
## Keeps connection for cor ~ -1 
## You may wish to choose a different threshold 
DM1[abs(correlationmatrix) < 0.33] = 0

G1 <- graph.adjacency(DM1, mode = "undirected", weighted = TRUE, diag = TRUE)

vcount(G1)
ecount(G1)

clusterlouvain <- cluster_louvain(G1)
plot(G1, vertex.color = rainbow(3, alpha = 0.6)[clusterlouvain$membership])

DM2 <- as.matrix(distancematrix)
## Zero out connections where there is low correlation 
DM2[correlationmatrix < 0.33] = 0

G2 <- graph.adjacency(DM2, mode = "undirected", weighted = TRUE, diag = TRUE)
clusterlouvain <- cluster_louvain(G2)
plot(G2, vertex.color = rainbow(4, alpha = 0.6)[clusterlouvain$membership])
















