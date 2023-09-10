import scrapy
from parser.items import AnimeUpdate
from scrapy.spiders import CrawlSpider


class ProjectSpider(CrawlSpider):
    name = "project"

    def start_requests(self):
        urls = ['https://yummyani.me/catalog/anime-updates/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = AnimeUpdate()
        updates = response.xpath('//li[@class="one-video-update materiable"]')
        for upd in updates:
            link = upd.xpath('./a/@href').get()
            image = upd.xpath('./a/img/@src').get()
            name_ru = upd.xpath('.//span[@class="update-title"]/text()').get()
            update_text = ''.join(upd.xpath('.//span[@class="update-info"]//text()').getall())
            date_time = upd.xpath('./a//local-time/@data-time').get()

            item['link'] = link
            item['image'] = image
            item['name_ru'] = name_ru
            item['update_text'] = update_text
            item['date_time'] = date_time

            yield item
