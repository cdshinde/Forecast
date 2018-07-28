# -*- coding: utf-8 -*-
"""
Run this using the following command so that the output will be be saved to CSV file

scrapy crawl yearlyweather  --set FEED_URI=output.csv --set FEED_FORMAT=csv

"""

import scrapy
from weatherforcast.items import DailyWeatherItem
import logging

logger = logging.getLogger('customlogger')

class YearlyweatherSpider(scrapy.Spider):
    name = 'yearlyweather'
    allowed_domains = ['accuweather.com']
    start_urls = ['https://www.accuweather.com/en/in/pune/204848/month/204848?monyr=1/01/2017']

    def parse(self, response):
        """
        This parse will be called for the Jan month and Feb Month only
        :param response:
        :return:
        """

        item = DailyWeatherItem()

        year = response.xpath('//*[@id="panel-main"]/div[2]/div/div/div[1]/div/div[2]/ul/li[2]/a/span/text()').extract_first()

        # TODO - Cannot extract this duplicate code into a separate function, so kept it as it, for now...
        #self.process(response, item, year)

        for day in response.xpath('//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr[1]'):  # Sun
            item['day'] = day.xpath('//td[1]/div/h3/text()').extract()
            item['max'] = day.xpath('//td[1]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[1]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[2]/div/h3/text()').extract()          # Mon
            item['max'] = day.xpath('//td[2]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[2]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[3]/div/h3/text()').extract()          # Tue
            item['max'] = day.xpath('//td[3]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[3]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[4]/div/h3/text()').extract()          # Wed
            item['max'] = day.xpath('//td[4]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[4]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[5]/div/h3/text()').extract()          # Thu
            item['max'] = day.xpath('//td[5]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[5]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[6]/div/h3/text()').extract()          # Fri
            item['max'] = day.xpath('//td[6]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[6]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[7]/div/h3/text()').extract()          # Sat
            item['max'] = day.xpath('//td[7]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[7]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item

        next_page = response.xpath('//*[@id="panel-main"]/div[2]/div/div/div[2]/a/@href').extract_first()
        # print('111111111 next page is ', next_page)

        next_year = response.xpath('//*[@id="panel-main"]/div[2]/div/div/div[2]/a/text()').extract_first()

        if next_page is not None:
            request = scrapy.Request(next_page, callback=self.parse_Next)
            request.meta['year'] = next_year
            yield request


    def parse_Next(self, response):
        """
        This parse_Next will be called from March month onwards as the Next URL is different.
        :param response:
        :return:
        """

        year = response.meta['year']

        item = DailyWeatherItem()

        ## TODO -
        #self.process(response, item, year)

        for day in response.xpath('//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr[1]'):  # Sun
            item['day'] = day.xpath('//td[1]/div/h3/text()').extract()
            item['max'] = day.xpath('//td[1]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[1]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[2]/div/h3/text()').extract()          # Mon
            item['max'] = day.xpath('//td[2]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[2]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[3]/div/h3/text()').extract()          # Tue
            item['max'] = day.xpath('//td[3]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[3]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[4]/div/h3/text()').extract()          # Wed
            item['max'] = day.xpath('//td[4]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[4]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[5]/div/h3/text()').extract()          # Thu
            item['max'] = day.xpath('//td[5]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[5]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[6]/div/h3/text()').extract()          # Fri
            item['max'] = day.xpath('//td[6]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[6]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item
            item['day'] = day.xpath('//td[7]/div/h3/text()').extract()          # Sat
            item['max'] = day.xpath('//td[7]/div/div/div[2]/div/span[1]/text()').extract()
            item['min'] = day.xpath('//td[7]/div/div/div[2]/div/span[2]/text()').extract()
            item['year'] = year
            yield item

        next_page = response.xpath(
            '//*[@id="panel-main"]/div[2]/div/div/div[2]/a[2]/@href').extract_first()
        # print('222222222 next page is ', next_page)

        next_year = response.xpath('//*[@id="panel-main"]/div[2]/div/div/div[2]/a[2]/text()').extract_first()

        if next_page is not None:
            request = scrapy.Request(next_page, callback=self.parse_Next)
            request.meta['year'] = next_year
            yield request

