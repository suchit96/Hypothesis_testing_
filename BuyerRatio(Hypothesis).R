# Hypothesis testing

# Load dataset

library(readxl)

Buyer<-read.csv(choose.files())
attach(Buyer)

t.test(Buyer$East)
?t.test
t.test(Buyer$West)

t.test(Buyer$North)

t.test(Buyer$South)

var.test(East,West)

shapiro.test(Buyer$Observed.Values) 


