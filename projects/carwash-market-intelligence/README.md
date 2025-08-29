# Carwash Market Intelligence & Growth Analytics

This project investigates the U.S. express carwash industry using publicly sourced data and demonstrates a range of analytics skills in R and Python. The case study replicates the type of market intelligence work an analyst might perform when evaluating competitors, designing membership pricing and identifying strategic threats.

## Data Sources

- **Competitor counts** – Number of locations for major express tunnel chains (e.g. Mister Car Wash, Quick Quack, Mod Wash, BlueWave Express, etc.) collected from ScrapeHero's location data.
- **Pricing information** – Average monthly membership price (~$25/month) from the International Carwash Association's 2024 Industry Pulse Report.
- **Synthetic data** – Growth trends (2020-2025) and geospatial coordinates are simulated to illustrate forecasting and mapping techniques.

## Contents

- **analysis.R** – R script for loading data, cleaning, generating plots and performing time‑series forecasting.
- **report.Rmd** – R Markdown report summarizing the analysis with narrative commentary, including:
  - **Growth & expansion** – Bar and line charts showing competitor store counts and projected growth to 2027.
  - **Membership ROI** – Breakeven analysis comparing unlimited plans to per‑wash pricing.
  - **Customer sentiment** – Simple text mining of sample reviews with sentiment distribution chart.
  - **Geospatial mapping** – Example scatter map of simulated store locations.
  - **Business case studies** – Four narrative sections translating analytics into strategic insights (expansion strategy, membership ROI, sentiment insights, and the threat from big‑box club car washes).
- **updated_to_do_list.md** – Tracker of completed and outstanding tasks for this portfolio (in root directory).

## Running the analysis

To reproduce the figures and tables in the report:

1. Install required R packages (ggplot2, forecast, dplyr, tidytext, etc.).
2. Run `analysis.R` to generate cleaned data, charts and forecast results.
3. Knit `report.Rmd` to HTML via RStudio or `rmarkdown::render()`. This will include the generated plots and narrative commentary.

## Notes

- All personal or proprietary data has been removed. Synthetic data is used where necessary for demonstration.
- The project is structured as part of a larger business analytics portfolio and can be extended with interactive dashboards (e.g. Shiny or Plotly) in the future.
