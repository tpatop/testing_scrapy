import os
import time
from multiprocessing import Pool


# Запуск возможен лишь с каталога scrapy - проекта


def _crawl(spider_name):
    if spider_name:
        os.system(f'scrapy crawl {spider_name}')


def run_crawler():
    spider_names = ['project']
    # многопроцессорный вызов пауков для ускорения обработки (паралелльно)
    pool = Pool(processes=len(spider_names))
    pool.map(_crawl, spider_names)


if __name__ == '__main__':
    while True:
        run_crawler()
        time.sleep(10)  # время ожидания между вызовами
