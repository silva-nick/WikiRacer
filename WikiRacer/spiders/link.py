import scrapy


class LinkSpider(scrapy.Spider):
    name = "link"

    start_urls = ["https://en.wikipedia.org/wiki/Romania"]

    def parse(self, response):
        
        for link in response.xpath("//table[@class='infobox']/tbody/tr"):
            if not link.xpath(".//table[@class='infobox']/tbody/tr/th/a") is None:
                yield {
                    'new_link': link.xpath(".//table[@class='infobox']/tbody/tr/th/a/@href").extract_first()
                }
            
        for link in response.xpath(""):
            yield {
                'new_link': link.xpath("")
            }
        