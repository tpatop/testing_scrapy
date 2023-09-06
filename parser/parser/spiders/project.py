import scrapy


class ProjectSpider(scrapy.Spider):
    name = "project"
    allowed_domains = ["yummyani.me"]
    start_urls = ["https://yummyani.me"]

    def parse(self, response):
        pass
