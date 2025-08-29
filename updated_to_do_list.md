# Updated Analyst To‑Do List – Business Analytics Portfolio

This list reflects the current status of the car‑wash market intelligence project as of **August 29, 2025**. It distinguishes between completed work and remaining tasks so you can prioritise your time ahead of the interview.

## ✅ Completed Analytics & Narrative Work

* **Real competitor dataset and cleaning:** Compiled location counts for major express tunnel chains (Mister Car Wash, Quick Quack, Mod Wash, etc.) from public sources and created a clean `competitor_dataset.csv`.
* **Exploratory analysis (EDA):** Generated bar and line charts illustrating competitor store counts and historical growth trends.
* **Geospatial mapping:** Simulated store coordinates to demonstrate how to visualise geographic coverage and identify expansion opportunities.
* **Time‑series forecasting:** Applied exponential smoothing to project Mod Wash’s store growth out to 2026–2027, saving results in `mod_wash_forecast.csv`.
* **Membership ROI analysis:** Modelled break‑even points for unlimited wash plans versus pay‑per‑wash pricing to quantify customer value.
* **Customer sentiment analysis:** Performed basic text mining on sample reviews to highlight common compliments and complaints and produced a sentiment chart.
* **Integrated analyses into report:** Added sections in `report.Rmd` covering data cleaning, EDA, forecasting, membership ROI, sentiment analysis and geospatial analysis.
* **Added case‑study narratives:** Wrote four business‑focused case studies (expansion trends, membership ROI, sentiment insights, and big‑box competition) to contextualise the analytics for decision‑makers.

## 🚧 Outstanding Analytics Enhancements

* **Interactive dashboard:** Build a Shiny or Plotly dashboard to allow recruiters to explore the dataset and forecasts interactively. This remains a stretch goal and is not required for the upcoming interview.

## 📦 Deployment & Repository Tasks

* **Enable GitHub Pages:** Turn on Pages in the repository settings (`Settings → Pages → Source = GitHub Actions`) so the site will deploy on pushes to `main`.
* **Commit and push updates:** Publish the updated report (`report.Rmd`), README and case‑study narratives to `main` to trigger the Pages workflow.
* **Verify the live site:** After deployment, test the site at `https://nemeangames.github.io/business-analytics-portfolio/` to ensure charts render correctly and navigation works.
* **Project‑specific README:** Add a `README.md` under `projects/carwash‑market‑intelligence/` summarising the case study, datasets and scripts so visitors can understand the scope and reproduce the analysis.
* **Repository hygiene:** Add a `.gitignore` to exclude unnecessary files, include an open‑source licence, and reorganise the folder structure (e.g. `data/`, `scripts/`, `projects/`) as recommended.

## 📈 Business Impact & Presentation

* **Business implications documented:** The report now ties each analysis to strategic decisions (e.g. expansion planning, pricing strategy, service improvements, competitive positioning).
* **Visual polish and narrative refinement:** Finalise the wording and formatting in the report and README to ensure clarity, professionalism and consistent styling. Consider using a corporate colour palette when customising plots.
* **Executive summary:** Craft a concise summary of top findings and actionable recommendations at the start of the README and the report for busy hiring managers.
* **Seek feedback:** Share the draft portfolio with peers or mentors for feedback and incorporate their suggestions before the final submission.

---

Once the remaining tasks are completed and pushed, the updated portfolio will auto‑deploy to GitHub Pages and provide a live demonstration of your analytic skills and business acumen for your interview.
