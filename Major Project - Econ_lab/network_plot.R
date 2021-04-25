library(igraph)

data_employment <- da36151.0010
data_employment <- na.omit(data_employment)

correlationmatrix = cor(unique(data_employment$WS4))
distancematrix <- cor2dist(correlationmatrix)

DM1 <- as.matrix(distancematrix)
## Zero out connection where there is low (absolute) correlation 
## Keeps connection for cor ~ -1 
## You may wish to choose a different threshold 
## DM1[abs(correlationmatrix) < 0.33] = 0

G1 <- graph.adjacency(DM1, mode = "undirected", weighted = TRUE, diag = TRUE)

vcount(G1)
ecount(G1)

clusterlouvain <- cluster_louvain(G1)
plot(G1, vertex.color = rainbow(3, alpha = 0.6)[clusterlouvain$membership])
