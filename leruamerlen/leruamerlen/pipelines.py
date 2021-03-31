# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class LeruamerlenPipeline:
    def process_item(self, item, spider):
        item['price'] = int(item['price'])
        item['features'] = dict(zip(item['features_names'], item['features']))
        del item['features_names']
        print()
        return item
