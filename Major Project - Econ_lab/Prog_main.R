# Loading the required packages and datasets

library("tidyverse")
library("dplyr")
library("ggplot2")

data_individual <- da36151.0001 # individual data

# selection of relevant columns from dataset
data_individual <- data_individual[,c("STATEID","DISTID","PSUID", "HHID", "HHSPLITID",
                                      "PERSONID", "IDPSU", "IDHH", "DISTRICT", "IDPERSON",
                                      "WT", "FWT", "RO3", "RO4","RO5", "RO6", "RO7", "ED6", "EDUC7", 
                                      "URBAN2011", "ID11", "ID13", "GROUPS",
                                      "ASSETS", "INCOME", "WS4")]


data_individual$num_RO4 <- fct_collapse(data_individual$RO4,
                                        "1" = c("(01) Head 1"),
                                        "2" = c("(02) Wife/Husband 2"),
                                        "3" = c("(03) Son/Daughter 3"),
                                        "4" = c("(04) Child-in-Law 4"),
                                        "5" = c("(05) Grandchild 5"),
                                        "6" = c("(06) Father/Mother 6"),
                                        "7" = c("(07) Brother/Sister 7"),
                                        "8" = c("(08) Parent-in-Law 8"),
                                        "9" = c("(09) Nephew/Niece 9"),
                                        "10" = c("(10) Sib-in-Law 10"),
                                        "11" = c("(11) Other rel 11"),
                                        "12" = c("(12) Servant/Others 12"),
                                       
                                        )





# network plots code

library(igraph)
library(RColorBrewer)
library(xtable)
library(FactoMineR)
library(factoextra)

####################################################################################
# Subset mydata to include occupations that are sufficiently represented
####################################################################################

mydata <- data_individual

# total occupations with HH 
occupations <- names(table(mydata$WS4)) 

##Considering only those occupations which are present in atleast 10 households in the sample

# list of household
HH <- as.character(unique(mydata$IDHH))
incidence <- matrix(0, nrow = length(HH), ncol = length(occupations))
rownames(incidence) <- HH
colnames(incidence) <- as.character(occupations)

#frame the unweighted incidence matrix 
for(i in 1:nrow(mydata)) {
   if(!is.na(mydata$WS4[i])) {
      incidence[as.character(mydata$IDHH[i]), as.character(mydata$WS4[i])] <- 1
   }
}

# List of occupations with sufficient sample(atleast 10 unweighted households)
Occ_suff_rep <- 0 # occupation sufficiently represented
count <- 0
for(i in 1:length(occupations)){
   if(sum(incidence[,occupations[i]]) >= 10){
      Occ_suff_rep[count] <- occupations[i]
      count <- count + 1
   }
}

# subset of mydata to include only those individuals with occupations in occupation sufficiently represented

mydata_1 <- mydata[which(mydata$WS4 %in% Occ_suff_rep),]
save(mydata_1, file = "/Users/quasar/downloads/mydata_1.Rda")

####################################################################################
# Creating One mode Adjacency matrix from 2 mode weighted incidence matrix
####################################################################################

HH <- as.character(unique(mydata_1$IDHH))
Bimodal <- matrix(0, nrow = length(HH), ncol = length(names(table(mydata_1$WS4))))
rownames(Bimodal) <- HH 
colnames(Bimodal) <- as.character(names(table(mydata_1$WS4)))

for(i in 1:nrow(mydata_1)){
   if(!is.na(mydata_1$WS4[i])){
      Bimodal[as.character(mydata_1$IDHH[i]), as.character(mydata_1$WS4[i])] <- mydata_1$WT[i] # weighted
   }
}

# Total weighted households
TWHH <- sum(mydata_1[which(mydata_1$num_RO4 == 1),"WT"]) 

n <- length(colnames(Bimodal))
OneModeAdj <- matrix(0, nrow =n, ncol = n)
rownames(OneModeAdj) <- colnames(Bimodal)
colnames(OneModeAdj) <- colnames(Bimodal)

# dot on indicators and then dot on one of the rows (both rows have same weights at first)
Idot <- function(x, y){
   I_x <- ifelse(as.vector(x) > 0,1,0)
   I_y <- ifelse(as.vector(y) > 0,1,0)
   return(sum((I_x*I_y)*x))
} 

for(i in 1:n){
   cat(i,'\n',sep = ',')
   for(j in 1:n){
      OneModeAdj[i,j] <- Idot(t(Bimodal)[i,],t(Bimodal)[j,])
   }
}

save(OneModeAdj,file = 'OneModeAdj')

transformUtoV <- function(U,h){
   V <- U
   for(i in 1:nrow(V)){
      for(j in 1:nrow(V)){
         E <- (U[i,i]*U[j,j])/h
         V[i,j] <- (U[i,j] - E)/E
      }
   }
   return(V)
}

Adj <- transformUtoV(OneModeAdj,TWHH)
Adj <- ifelse(Adj == -1,0,Adj+1)
save(Adj,file = "Adj.Rda")
Adj_Final <- ifelse(Adj > 0.7481,Adj,0) # Connections Above the third quartile
g <- graph_from_adjacency_matrix(Adj_Final,mode = "undirected",weighted = TRUE)
g <- simplify(g,remove.multiple = F,remove.loops = T)

delete.isolates <- function(graph) {
   isolates <- which(degree(graph) == 0)
   delete.vertices(graph, isolates)
}

# g <- delete.isolates(g)
clp <- cluster_louvain(g)
plot(clp,g)

####################################################################################
##### Plotting Neatly and with multiple node attributes separately            ######
####################################################################################

V(g)$community <- clp$membership
pal <- brewer.pal(length(table(clp$membership)), "Set3")
V(g)$color <- pal[V(g)$community]

# For better display maintain separation between communities
weight.community <- function(x,membership,weight.within,weight.between){
   #For node one community is
   c1 <- as.numeric( membership(clp)[ which( names(membership(clp)) == x[1]  ) ] )
   #For node two community is
   c2 <- as.numeric( membership(clp)[ which( names(membership(clp)) == x[2]  ) ] )
   if(c1 == c2){
      weight=weight.within
   }else{
      weight=weight.between
   }
   return(weight)
}

# Change color scheme based on membership
pal <- brewer.pal(length(table(clp$membership)), "Set3")
V(g)$color <- pal[V(g)$community]
# E(g)$width <- E(g)$weight/6
# E(g)$width <- E(g)$weight/10
E(g)$weight=apply(get.edgelist(g),1,weight.community,membership(clp),20,1)
l <- layout.fruchterman.reingold(g)
set.seed(100)
pdf("plot_network.pdf")
# cairo_ps("plot_network.eps")
# edge.width = E(g)$width #include inside plot if you want to see weights
plot(g,vertex.color=pal[V(g)$community],vertex.frame.color = "white",layout = l,canvas.width = 1000,canvas.height = 1000,vertex.label = V(g)$name,vertex.label.color="gray40",vertex.label.font=1,vertex.label.cex=0.5,vertex.size = 5,edge.width = 0.05,mark.groups = communities(clp))
legend(x=-1.5, y=0, c(names(table(clp$membership))), pch=21,
       col="#777777", pt.bg=pal, pt.cex=2, cex=.8, bty="n", ncol=1)
dev.off()


# Get distance matrix
g1 <- graph_from_adjacency_matrix(Adj,mode = c("undirected"),weighted = TRUE)
E(g1)$DIST <- 1/(E(g1)$weight)
DistMatrix <- distances(g1,v = V(g1),to = V(g1),weights = E(g1)$DIST)
# Computing maximum distance excluding Inf
temp <- as.vector(DistMatrix)
temp <- temp[which(!is.infinite(temp))]
a <- max(temp)
DistMatrix <- ifelse(is.infinite(DistMatrix),a,DistMatrix)
save(DistMatrix,file = 'DistMatrix_NoThreshold.Rda')

rescale <- function(x,min,max){ #Rescale between 0 to 100 
   return( 100*(x-min)/(max-min) )
}
DistRescaled <- rescale(DistMatrix,min(DistMatrix),max(DistMatrix))
save(DistRescaled,file = 'DistRescaled_NoThreshold.Rda')










