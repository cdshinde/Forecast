# Forecast

This is a sample Python project that is used to showcase the the lifecyle of Data Processing right from scraping data from a website to formating that data and then analyzing that data.

Tools and technology used for the showcase were:
1. Python IDE
2. Python 3.x
3. Scrapy for crawling
4. Jupyter Notebook for Analysis of data

There are 2 folders that are there in this repositiory:
1. weatherforcast - This folder has the scrapy code. Inside this folder there is a spider folder which has the yearlyweather.py. You can run this file using scrapy command like this
          "scrapy crawl yearlyweather  --set FEED_URI=output.csv --set FEED_FORMAT=csv " 

2. analysis - This folder has the Weather_Forecast.ipynb file which is the Jupyter Notebook, you can open it with it. The data that is used for the analysis is the Max and Min temperature data for year of 2017.

Happy Analyzing!
