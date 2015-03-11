# -*- coding: utf-8 -*-
# GovHK Data.One Datasets Scraper
# Sammy Fung <sammy@sammy.hk>
import scrapy
import re
from govhk_dataone.items import GovhkDataoneItem

class DataoneSpider(scrapy.Spider):
    name = "dataone"
    allowed_domains = ["gov.hk"]
    start_urls = (
        'http://www.gov.hk/en/theme/psi/datasets/',
    )

    def parse(self, response):
      #response.xpath("//span[contains(@class, 'dataName')]/a/text()").extract()
      for i in response.xpath("//span[contains(@class, 'dataName')]/a/@href").extract():
        yield scrapy.Request("http://www.gov.hk%s"%i, callback=self.parse_dataset)

    def parse_dataset(self, response):
      lastUpdate = response.xpath("//p[contains(@id, 'lastUpdate')]/text()")[0].extract()
      lastUpdate = re.sub('^.*date: ', '', lastUpdate)
      datasetTitle = response.xpath("//meta[contains(@name, 'description')]/@content").extract()[0]
      datasetDatetime = response.xpath("//meta[contains(@name, 'date')]/@content").extract()[0]
      for dataset in response.xpath("//tr[contains(@class, 'odd')]/td/a"):
        item = GovhkDataoneItem()
        item['datasetUrl'] = dataset.xpath("@href").extract()[0]
        item['datasetTitle'] = datasetTitle
        item['datasetType'] = dataset.xpath("@title").extract()[0]
        item['lastUpdate'] = lastUpdate
        item['lastupdateDatetime'] = datasetDatetime
        item['sourceUrl'] = response.url
        yield item
