#Plots the probability density function of a given CSV of BLEU scores
#and also plots the scores for a few of our models.

library(ggplot2)

#Plot the probability density function of the BLEU scores (sampling distribution)
plot(density(for_r_drop$bleu), main = "Distribution", xlab="BLEU score", xlim=c(0,1))

#Take the median
median(for_r_drop$bleu)

#Set the vectors I want to plot
scores = c(0.7261140381247376, 0.577793828381643, 0.46773651949751927, 0.5337197138587872, 0.5408556463821856, 0.7220347865797387)
x = c(1, 2, 3, 4, 5, 6)
c_labels = c("32bl28b", "32block12batch", "baseline", "gpt3small12b32b", "gpt3small15tokens", "gpt3smallwithdrop")

data = data.frame(x, scores)

#Plot the scores for our models
ggplot(data, aes(x = x, y = scores)) +
  geom_point() + 
  labs(x = "Configs", y = "BLEU Scores") + 
  scale_x_continuous(breaks = x, labels = c_labels) + 
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


