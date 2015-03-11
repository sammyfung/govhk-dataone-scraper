# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovhkDataoneItem(scrapy.Item):
  datasetUrl = scrapy.Field()
  datasetTitle = scrapy.Field()
  datasetType = scrapy.Field()
  lastUpdate = scrapy.Field()
  lastupdateDatetime = scrapy.Field()
  sourceUrl = scrapy.Field()
