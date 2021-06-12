import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'

    def parse(self, response):
        for title in response.css('.olt .title'):
            yield {'title': title.css('a::text').getall(),
                   'link': title.css('a::attr(href)').getall()}

    def start_requests(self):
        for i in range(0, 125, 25):
            url = 'https://www.douban.com/group/498004/discussion?start={page}'.format(page=i)
            yield scrapy.Request(url=url, callback=self.parse)