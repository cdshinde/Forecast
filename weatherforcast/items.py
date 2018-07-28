# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherforcastItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cityname = scrapy.Field()
    curr_temperature = scrapy.Field()
    todays_temperature = scrapy.Field()
    weather_cond = scrapy.Field()
    tomorrow_temperature = scrapy.Field()


class DailyWeatherItem(scrapy.Item):
    day = scrapy.Field()
    max = scrapy.Field()
    min = scrapy.Field()
    year = scrapy.Field()
