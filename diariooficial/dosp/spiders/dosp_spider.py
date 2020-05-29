# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from diariooficial.dosp.items import DospItem


class DospSpiderSpider(CrawlSpider):
    name = 'dosp'
    date_search = datetime.today() - timedelta(3)
    allowed_domains = ['jusbrasil.com.br']
    start_urls = [f'https://www.jusbrasil.com.br/diarios/DOSP/{date_search.year}/{date_search.strftime("%m")}/{date_search.strftime("%d")}']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths="//ul[@class='sections']//h3//a",
            )
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths="//div[@class='paginator']/a[contains(@href, '?p')]"
            )
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths="//ul[@class='diario-pages']//li[@class='page']//a"
            ),
            callback='parse_new'
        )
    )

    def parse_new(self, response):
        journal = response.css('.breadcrumb-item:nth-child(2) a ::text').get()
        book_name = response.css('.breadcrumb-item:nth-child(4) a ::text').get()
        page_number = response.css('.breadcrumb-item--active ::text').get().split(' ')[1]
        title = response.css('h1.document-title ::text').get()
        page_text = [p for p in response.xpath('//p//text()').getall()]

        items = DospItem()
        items['journal'] = journal
        items['book_name'] = book_name
        items['page_number'] = int(page_number)
        items['title'] = title
        items['page_text'] = page_text
        items['url'] = response.url
        items['date_journal'] = self.date_search
        items['date_scraped'] = datetime.now()
        yield items
