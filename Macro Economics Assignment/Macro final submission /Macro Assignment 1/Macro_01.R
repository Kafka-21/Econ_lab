library(haven)
library(tidyverse)
library(readxl)

############################################################################

# Fig 1.1 - loading states data from excel file 
states_data <- read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet ="States_per_capita")

# plot states per capita gdp 
plot(density(states_data$`2018-19`), xlab = "gdp per capita",ylab = "Density of states",xlim = c(0, 225000), ylim = c(0, 2.2e-04), main ="Distribution of states per capita GDP")
lines(density(states_data$`2010-11`), col = "red")
lines(density(states_data$`2000-01`), col = "blue")
lines(density(states_data$`1990-91`), col = "orange")
lines(density(states_data$`1980-81`), col = "green")
lines(density(states_data$`1970-71`), col = "yellow")
lines(density(states_data$`1960-61`), col = "purple")

# Add legened
legend(150000, 2.2e-04, legend=c("2018-19", "2010-11", "2000-01", "1990-91", "1980-81", "1970-71", "1960-61"), col=c("black", "red", "blue", "orange", "green", "yellow", "purple"), lty= 1:1)

############################################################################

# Fig 1.2 -  plot states log per capita gdp 
plot(density(log10(states_data$`2018-19`)),xlab = "log gdp per capita",ylab = "Density of states", xlim = c(3.7, 5.5), ylim = c(0, 6), main ="Distribution of states log per capita GDP")
lines(density(log10(states_data$`2010-11`)), col = "red")
lines(density(log10(states_data$`2000-01`)), col = "blue")
lines(density(log10(states_data$`1990-91`)), col = "orange")
lines(density(log10(states_data$`1980-81`)), col = "green")
lines(density(log10(states_data$`1970-71`)), col = "yellow")
lines(density(log10(states_data$`1960-61`)), col = "purple")

# Add legened
legend(5, 6, legend=c("2018-19", "2010-11", "2000-01", "1990-91", "1980-81", "1970-71", "1960-61"), col=c("black", "red", "blue", "orange", "green", "yellow", "purple"), lty= 1:1)

############################################################################

# Fig 1.3 - Add Population weighted data 
Popu_weighted <- read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet ="Popu_weighted")

# plot states log per capita gdp 
plot(density(log10(states_data$`2010-11`)*Popu_weighted$`2010-11`), xlab = "log per capita gdp", ylab="Density of states", main ="Population weight Density plot states log GDP per capita")
lines(density(log10(states_data$`2000-01`)*Popu_weighted$`2000-01`), col = "red")
lines(density(log10(states_data$`1990-91`)*Popu_weighted$`1990-91`), col = "blue")
lines(density(log10(states_data$`1980-81`)*Popu_weighted$`1980-81`), col = "green")
lines(density(log10(states_data$`1970-71`)*Popu_weighted$`1970-71`), col = "purple")

# Add legend
legend(0.7, 3.2, legend=c("2010-11", "2000-01", "1990-91", "1980-81", "1970-71"), col=c("black", "red", "blue", "green", "purple"), lty= 1:1)

############################################################################

# Fig 1.4 - Add workers data 
workers_data <- read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet ="Worker_data")

# plot states log per capita gdp 
plot(density(log10(workers_data$`2010-11`)), xlim = c(4.2, 6), ylim = c(0, 3.2), xlab = "log gdp per worker", ylab = "Density of states", main ="Density plot states log GDP per worker")
lines(density(log10(workers_data$`2000-01`)), col = "red")
lines(density(log10(workers_data$`1990-91`)), col = "blue")
lines(density(log10(workers_data$`1980-81`)), col = "green")
lines(density(log10(workers_data$`1970-71`)), col = "purple")

# Add legened
legend(5.5, 3.2, legend=c("2010-11", "2000-01", "1990-91", "1980-81", "1970-71"), col=c("black", "red", "blue", "green", "purple"), lty= 1:1)

############################################################################

library(calibrate)
# Fig 1.5 Add Consumption data 
Consumption_data <- read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet ="Consumption_data")

# plot states log per capita gdp 
plot(log10(Consumption_data$`Per capita GDP`),log10(Consumption_data$`Per capita Consumption`),xlim = c(4, 5.5), xlab = 'Log GDP per capita', ylab = 'Log Consumption per capita', main = 'Log Consumption per capita vs Log gdp per capita')
abline(lm(log10(`Per capita Consumption`) ~ log10(`Per capita GDP`), data = Consumption_data), col = "blue")

# Add legend
textxy(log10(Consumption_data$`Per capita GDP`), log10(Consumption_data$`Per capita Consumption`), Consumption_data$`States 2011`, col = "red")

############################################################################
# Fig 1.6 Life Expectancy data
Life_expectancy <- read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet ="Life_exp")

# plot states life expectancy
plot(log10(Life_expectancy$Per_capita_GDP), Life_expectancy$Life_expectancy,xlim = c(4, 5.5), xlab = 'Log GDP per capita', ylab = 'Life expectancy in years (2011)', main = 'Life expectancy vs Log gdp per capita')
abline(lm(Life_expectancy ~ log10(Per_capita_GDP), data = Life_expectancy), col = "blue")

# Add Legend
textxy(log10(Life_expectancy$Per_capita_GDP), Life_expectancy$Life_expectancy, Life_expectancy$`States 2011`, col = "red")

############################################################################

# Fig. 1.7 - Average growth rate plot worker per capita gdp 
avg_worker_growth <- read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet ="Worker_growth_rates")

#plot average growth rates 
plot(density(avg_worker_growth$`2010-11`), xlim = c(-0.1, 0.2), ylim = c(0, 25), xlab = "average growth rates", ylab = "Density of states", main = "growth rate of GDP per worker distribution")
lines(density(avg_worker_growth$`2000-01`), col = "red")
lines(density(avg_worker_growth$`1990-91`), col = "blue")

legend(0.1 , 25, legend=c("2010-11", "2000-01", "1990-91"), col=c("black", "red", "blue"), lty= 1:1)
############################################################################

# Fig 1.8 - evolution of income growth across states
income_gr_states <- read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet = "Evolution_states")
plot(log10(income_gr_states$`Andhra Pradesh`)~ income_gr_states$Years, col = "black", type = "l", ylim = c(3.7, 5.2), xlab = "Years", ylab =" Log per capita GDP", main = "Income evolution of states")
lines(log10(income_gr_states$Bihar)~ income_gr_states$Years, col = "red", type = "l")
lines(log10(income_gr_states$Gujarat)~ income_gr_states$Years, col = "blue", type = "l")
lines(log10(income_gr_states$Karnataka)~ income_gr_states$Years, col = "green", type = "l")
lines(log10(income_gr_states$Kerala)~ income_gr_states$Years, col = "orange", type = "l")
lines(log10(income_gr_states$`Madhya Pradesh`)~ income_gr_states$Years, col = "tan", type = "l")
lines(log10(income_gr_states$Maharashtra)~ income_gr_states$Years, col = "purple", type = "l")
lines(log10(income_gr_states$Orissa)~ income_gr_states$Years, col = "pink", type = "l")
lines(log10(income_gr_states$Rajasthan)~ income_gr_states$Years, col = "coral", type = "l")
lines(log10(income_gr_states$`Tamil Nadu`)~ income_gr_states$Years, col = "yellow", type = "l")
lines(log10(income_gr_states$`Uttar Pradesh`)~ income_gr_states$Years, col = "aquamarine", type = "l")
lines(log10(income_gr_states$`West Bengal`)~ income_gr_states$Years, col = "brown", type = "l")

###########################################################################

# Fig 1.9 Log GDP per worker in 2011 versus log GDP per worker in 1961, together with the 45◦ line.

income_wrt_AP = read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet = "Worker_data_AP")
plot(income_wrt_AP$`1970-71`, income_wrt_AP$`2010-11`, xlim = c(0.94, 1.04), xlab = "log GDP per worker relative to the AP in 1970-71", ylab = "log GDP per worker relative to the AP in 2010-11")
abline(0, 1, lty = 1, col = "red")

# add legend
textxy(income_wrt_AP$`1970-71`, income_wrt_AP$`2010-11`, income_wrt_AP$States, col = "red")

###########################################################################

# Fig 1.13 Annual growth rate of GDP per worker between 1970 and 2010 versus log GDP per worker in 1970 for all states

fig_13 = read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet = "Fig_13")
plot(log10(fig_13$`gdp per worker 1970`), fig_13$`1970-2011`, xlab ="log gdp per worker 1970", xlim = c(4.4, 4.8),ylab= "annual growth rate 1970-2010", main = "Annual growth rate of GDP per worker between 1970 and 2010 versus log GDP per worker in 1970 ")

abline(lm(`1970-2011` ~ log10(`gdp per worker 1970`), data = fig_13), col = "blue")

# add legend
textxy(log10(fig_13$`gdp per worker 1970`), fig_13$`1970-2011`, fig_13$States, col = "red")

###########################################################################

# fig 14
fig_14 = read_excel("/Users/quasar/downloads/Macro_data_assignment.xlsx", sheet = "Fig_14")
plot(log10(fig_14$`gdp per worker 1970`), fig_14$`1970-2011`, xlab ="log gdp per worker 1970", xlim = c(4.4, 4.8),ylab= "annual growth rate 1970-2010", main = "Annual growth rate of GDP per worker between 1970 and 2010 versus log GDP per worker in 1970 ")

abline(lm(`1970-2011` ~ log10(`gdp per worker 1970`), data = fig_14), col = "blue")

# add legend
textxy(log10(fig_14$`gdp per worker 1970`), fig_14$`1970-2011`, fig_14$States, col = "red")

###########################################################################

