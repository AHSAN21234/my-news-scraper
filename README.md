#  Automated News Intelligence Scraper
[![Run My Scraper](https://github.com/AHSAN21234/my-news-scraper/actions/workflows/run_daily.yml/badge.svg)](https://github.com/AHSAN21234/my-news-scraper/actions)

A serverless Python application that automatically scrapes top tech headlines every 24 hours and logs them to a version-controlled file.

##  Tech Stack & Execution
* **Language:** Python 3.9
* **Libraries:** BeautifulSoup4, Requests
* **Automation:** GitHub Actions (YAML)
* **Hosting:** GitHub Infrastructure ($0 Server Cost)

##  How it Works
1. **Trigger:** A GitHub Action is triggered via a `cron` schedule every day at midnight.
2. **Execution:** The script runs in a virtual Linux environment (Ubuntu).
3. **Scraping:** Python extracts the top 5 headlines from Hacker News.
4. **Logging:** The data is appended to `results.txt` and automatically committed back to this repository.

##  Live Data Log
You can view the latest scraped headlines here: 
👉 [**View results.txt**](https://github.com/AHSAN21234/my-news-scraper/blob/main/results.txt)

---
*Created by AHSAN21234 for Portfolio Demonstration.*
