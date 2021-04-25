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




