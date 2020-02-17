import scrapy
import scrapy.exceptions.CloseSpider


class LinkSpider(scrapy.Spider):
    name = "link"

    start_urls = ["https://en.wikipedia.org/wiki/Chicago"]

    def parse(self, response):

        linkList = list(set(response.xpath('//div[@id="mw-content-text"]//a[contains(@href, "/wiki/")]/@href').getall()))

        yield {
            "links": linkList
        }
        
        for next_page in linkList:
            if "/wiki/iowa" == next_page:
                print("Hurray Hurray!")
                raise CloseSpider('Success')
            if next_page is None or next_page.count("/")>2: pass
            next_page = "https://en.wikipedia.org" + next_page#.encode("utf-16")
            print("AHHHHHHHHHHHHHHHHHHHhhhHHHhHHHHH: " + next_page)
            #next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)