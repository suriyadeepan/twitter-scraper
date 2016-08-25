import scrapy
from bs4 import BeautifulSoup

import utils

class TwitterSpider(scrapy.Spider):
    name = 'tspider'
    allowed_domains = [ 'twitter.com' ]
    start_urls = utils.get_urls(filename='seeds.csv')

    def parse(self, response):
        # get soup from response
        soup = BeautifulSoup(response.body,'lxml')
        # get text from soup
        tweet_text = soup.find('div', {'class' : 'js-tweet-text-container'}).find('p').text
        # get tweet id from url
        tweet_id   = utils.url2id(response.url)
        # return data
        yield { 'tid'  : tweet_id, 'text' : tweet_text }
