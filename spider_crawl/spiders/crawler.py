# -*- coding: utf-8 -*-
import scrapy
from ..items import SpiderCrawlItem
import requests as rq
from ..spiders import Reset34Model as ResNet34
from tensorflow.keras.models import load_model
# import matplotlib.image as mpimg
from tensorflow.keras.optimizers import SGD
import cv2
import numpy as np

learning_rate = 5e-3
decay = 5e-4
momentum = 0.9

num_samples = 5
n_test = 250

print("Loading model...")
# model = load_model('Model/resnet34.h5')
model_filepath = "Model/ResNet34.bestweights.hdf5"
model = ResNet34.ResNet34Model(learning_rate, momentum, decay)
model.load_weights(model_filepath)
sgd = SGD(lr=learning_rate, decay=decay, momentum=momentum, nesterov=True)
model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['mse', 'mae', 'mape', ResNet34.average_l1])
print("Model loaded successfully")
print(model.summary())


class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    # allowed_domains = ['https://www.amazon.in/b/ref=gbpp_itr_m13_649e_Savemore?node=17516498031&ie=UTF8']
    page_number = 2
    start_urls = [
        # 'https://www.imdb.com/list/ls049573604/',
        'https://www.imdb.com/list/ls069457382/'
    ]

    def parse(self, response):
        items = SpiderCrawlItem()
        name = response.css('.lister-item-header a::text').extract()
        movie = response.css('.text-muted a').css('::text').extract()
        image_links = response.css('img::attr(src)').extract()

        row_data = zip(name, movie, image_links)
        # author, price, image_links
        for data in row_data:
            items['name'] = data[0]
            items['movie'] = data[1]
            # items['price'] = price
            items['image_link'] = data[2]
            img_data = rq.get(data[2]).content
            items['image'] = img_data
            with open('img.jpg', 'wb+') as f:
                f.write(img_data)
            img = cv2.imread('img.jpg')
            img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
            img = np.expand_dims(img, axis=0)
            big_o = model.predict(img)[0]
            items['O'] = str(big_o[0])
            items['C'] = str(big_o[1])
            items['E'] = str(big_o[2])
            items['A'] = str(big_o[3])
            items['N'] = str(big_o[4])
            yield items

        # next_page = 'https://www.amazon.com/Books-Last-30-days/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=' + str(
        #     CrawlerSpider.page_number) + '&qid=1587721318&ref=sr_pg_2'
        # # if next_page is not None:
        # if CrawlerSpider.page_number < 5:
        #     CrawlerSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)
