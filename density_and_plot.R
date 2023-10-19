library(ggplot2)

plot(density(for_r_drop$bleu), main = "Distribution", xlab="BLEU score", xlim=c(0,1))

median(for_r_drop$bleu)

scores <- c(0.7261140381247376, 0.577793828381643, 0.46773651949751927, 0.5337197138587872, 0.5408556463821856, 0.7220347865797387)
x <- c(1, 2, 3, 4, 5, 6)
c_labels <- c("32bl28b", "32block12batch", "baseline", "gpt3small12b32b", "gpt3small15tokens", "gpt3smallwithdrop")

# Create a data frame
data <- data.frame(x, scores)

# Create a ggplot object
ggplot(data, aes(x = x, y = scores)) +
  geom_point() +  # Use points for the plot
  labs(x = "Configs", y = "BLEU Scores") +  # Set axis labels
  scale_x_continuous(breaks = x, labels = c_labels) +  # Customize x-axis labels
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


