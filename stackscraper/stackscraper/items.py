from scrapy.item import Item, Field


class StackscraperItem(Item):
    title = Field()
    url = Field()
