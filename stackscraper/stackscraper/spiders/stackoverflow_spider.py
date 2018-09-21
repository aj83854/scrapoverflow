from scrapy import Spider
from scrapy.selector import Selector


class StackoverflowSpider(Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
