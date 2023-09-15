# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from db.models import Update


class SqlitePipeline:
    def __init__(self):
        self.url = "sqlite:///./bot.db"
        self.engine = create_engine(url=self.url, echo=False)
        self.session = Session(bind=self.engine)

    def process_get_item(self, data: Update):
        query = select(Update).filter_by(
            link=data.link,
            episode=data.episode,
            translate=data.translate
        )
        result = self.session.execute(query).first()
        return result

    def process_item(self, item, spider):
        data = Update(
            name_ru=item['name_ru'],
            hash_link=item['hash_link'],
            link=item['link'],
            image=item['image'],
            episode=item['episode'],
            translate=item['translate']
        )
        if self.process_get_item(data) is None:
            self.session.add(data)
        return item

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
