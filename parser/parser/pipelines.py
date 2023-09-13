# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import sqlite3


# class SqlitePipelineR:
#     def __init__(self):
#         # Create/Connect to database
#         self.con = sqlite3.connect('bot.db')

#         # Create cursor, used to execute commands
#         self.cur = self.con.cursor()

#         # Create quotes table if none exists
#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS quotes(
#             text TEXT,
#             tags TEXT,
#             author TEXT
#         )
#         """)

#     def process_item(self, item, spider):
#         # Define insert statement
#         self.cur.execute("""
#             INSERT INTO quotes (text, tags, author) VALUES (?, ?, ?)
#         """,
#         (
#             item['image'],
#             str(item['name_ru']),
#             item['update_text']
#         ))

#         # Execute insert of data into database
#         self.con.commit()
#         return item


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Update


class SqlitePipeline:
    def __init__(self):
        self.url = "sqlite:///./bot.db"
        self.engine = create_engine(url=self.url, echo=False)
        self.session = Session(bind=self.engine)
        # self.update = Update()

    def process_item(self, item, spider):
        c = Update(
            name_ru = item['name_ru'],
            hash_link = item['hash_link'],
            link = item['link'],
            image = item['image'],
            update_text = item['update_text'],
            # date_time = item['date_time']
        )
        self.session.add(c)
        return item

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
