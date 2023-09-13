import scrapy
from parser.items import AnimeUpdate
from scrapy.spiders import CrawlSpider
from service.hash import hash_text
# from db.models import Update
# from db import UpdateRepo, init


class ProjectSpider(CrawlSpider):
    name = "project"

    def start_requests(self):
        urls = ['https://yummyani.me/catalog/anime-updates/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # update = Update()
        item = AnimeUpdate()
        updates = response.xpath('//li[@class="one-video-update materiable"]')
        if not updates:
            pass  # блок для обработки ошибки, связанной с изменением атрибутов
        for upd in updates:
            link = upd.xpath('./a/@href').get()
            image = upd.xpath('./a/img/@src').get()
            name_ru = upd.xpath('.//span[@class="update-title"]/text()').get()
            update_text = ''.join(upd.xpath('.//span[@class="update-info"]//text()').getall())
            date_time = upd.xpath('./a//local-time/@data-time').get()

            # update.link = link
            # update.hash_link = hash_text(link)
            # update.image = image
            # update.name_ru = name_ru
            # update.update_text = update_text
            # update.date_time = date_time

            item['link'] = link
            item['hash_link'] = hash_text(link)
            item['image'] = image
            item['name_ru'] = name_ru
            item['update_text'] = update_text
            item['date_time'] = date_time

            yield item
