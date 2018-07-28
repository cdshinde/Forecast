# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
import logging

logger = logging.getLogger('customlogger')

class WeatherforcastPipeline(object):
    def process_item(self, item, spider):
        return item


class YearlyweatherPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        """
         Note the value for every key is stored as a list since we loaded extract and not extract_first .
         Also striping off the leading '/' from the minimum temp using list comprehension technique.

        """
        # day = pd.DataFrame()
        print("length of the item is ------>>>>> ", len(item['max']))
        if len(item['max']) > 0:
            day_dict = {'day': item['day'],
                        'max': [x.rstrip('°') for x in item['max']],
                        'min': [x.strip('/°') for x in item['min']],
                        'year': item['year']
                        }
        else:
            day_dict = {'day': item['day'],
                        'max': ['NA', 'NA', 'NA', 'NA'],
                        'min': ['NA', 'NA', 'NA', 'NA'],
                        'year': item['year']
                        }

        # print(day_dict)
        return day_dict