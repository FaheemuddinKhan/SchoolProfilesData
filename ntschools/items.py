# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NtschoolsItem(scrapy.Item):
    Name = scrapy.Field()
    PhysicalAddress = scrapy.Field()
    PostalAddress = scrapy.Field()
    Email = scrapy.Field()
    Phone = scrapy.Field()