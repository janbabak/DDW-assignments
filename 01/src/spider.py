import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for title in response.css('a.oxy-post-title'):
            yield {'title': title.css('::text').extract_first()}

        next_page = response.css('div.oxy-easy-posts-pages a.next ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)