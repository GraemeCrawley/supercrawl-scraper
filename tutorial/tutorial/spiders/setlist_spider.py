import scrapy


class SetlistSpider(scrapy.Spider):
    name = "setlist"
    start_urls = [
        'http://supercrawl.ca/music',
    ]

    def parse(self, response):
        for column in response.css('div.col-3'):
            for letter in column.css('letter-group'):
                yield {
                    'text': letter.css('div.letter-group__letter::h2').extract_first()
                }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
