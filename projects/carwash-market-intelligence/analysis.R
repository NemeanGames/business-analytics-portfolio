# analysis.R
# Basic analysis for Car Wash Market Intelligence project

# Load libraries
# Uncomment to install packages if necessary
# install.packages(c("dplyr", "ggplot2", "tidyr"))

library(dplyr)
library(ggplot2)
library(tidyr)

# Placeholder data: sample growth numbers for Quick Quack (QQ), Mister (MC), Zips
growth_data <- data.frame(
  year = c(2019, 2020, 2021, 2022, 2023),
  QuickQuack = c(100, 150, 180, 220, 275),
  Mister = c(350, 370, 400, 430, 476),
  Zips = c(200, 210, 230, 250, 295)
)

# Convert to long format for plotting
growth_data_long <- pivot_longer(growth_data, cols = -year, names_to = "Company", values_to = "Sites")

# Plot growth trends
ggplot(growth_data_long, aes(x = year, y = Sites, color = Company)) +
  geom_line() +
  geom_point() +
  ggtitle("Car Wash Sites Growth (Sample Data)") +
  xlab("Year") +
  ylab("Number of Sites")
