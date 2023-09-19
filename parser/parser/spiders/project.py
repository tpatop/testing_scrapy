import scrapy
from parser.items import AnimeUpdate
from scrapy.spiders import CrawlSpider
from service.hash import hash_text


class ProjectSpider(CrawlSpider):
    name = "project"

    def start_requests(self):
        urls = ['https://yummyani.me/catalog/anime-updates/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = AnimeUpdate()
        updates = response.xpath('//li[@class="one-video-update materiable"]')

        if not updates:
            pass  # блок для обработки ошибки, связанной с изменением атрибутов

        for upd in updates:
            link = upd.xpath('./a/@href').get()
            image = upd.xpath('./a/img/@src').get()
            name_ru = upd.xpath('.//span[@class="update-title"]/text()').get()
            update_text = upd.xpath(
                './/span[@class="update-info"]//text()').getall()
            episode = update_text[2].split('-')[0].strip()
            translate = update_text[3].split(':')[-1].strip()
            # date_time = upd.xpath('./a//local-time/@data-time').get()

            item['link'] = link
            item['hash_id'] = hash_text(link + translate)
            item['image'] = image
            item['name_ru'] = name_ru
            item['episode'] = episode
            item['translate'] = translate

            yield item
