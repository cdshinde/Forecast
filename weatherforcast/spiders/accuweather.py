# -*- coding: utf-8 -*-

"""
This spider gets the weather for today with the current weather and the temperature.
Also there is a possibility to get the cold_flu, asthma and migraine details for the same city.
Which am not doing right now.

"""
import scrapy
from weatherforcast.items import WeatherforcastItem

class AccuweatherSpider(scrapy.Spider):
    name = 'accuweather'
    allowed_domains = ['accuweather.com']

    start_urls = [

                    'https://www.accuweather.com/en/in/pune/204848/weather-forecast/204848/',
                    # 'https://www.accuweather.com/en/in/pune/204848/cold-flu-weather/204848',
                    # 'https://www.accuweather.com/en/in/pune/204848/asthma-weather/204848',
                    # 'https://www.accuweather.com/en/in/pune/204848/migraine-weather/204848'
                  ]

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        item = WeatherforcastItem()

        item['cityname'] = response.css('li.selected a.tab span.current-city h1::text').extract_first()
        item['curr_temperature'] = response.css('li.selected a.tab span.local-temp::text').extract_first()
        item['weather_cond'] = response.xpath('//*[@id="feed-tabs"]/ul/li[2]/div/div[2]/span/text()').extract_first()
        item['tomorrow_temperature'] = response.xpath('//*[@id="feed-tabs"]/ul/li[4]/div/div[2]/div/span[1]/text()').extract_first()
        item['todays_temperature'] = response.xpath('//*[@id="feed-tabs"]/ul/li[2]/div/div[2]/div/span[1]/text()').extract_first()

        yield item