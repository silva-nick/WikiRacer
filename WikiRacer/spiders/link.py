import scrapy
import queue
import sys


class LinkSpider(scrapy.Spider):
    name = "link"

    start = "/wiki/" + input("Primary directory: ")
    destination = "/wiki/" + input("Final directory: ")

    start_urls = [
        "https://en.wikipedia.org"+start]
    urls = queue.Queue()
    urls.put(start)
    visited = [start]

    def parse(self, response):
        linkList = list(set(response.xpath(
            '//div[@id="mw-content-text"]//a[contains(@href, "/wiki/")]/@href').getall()))

        for x in linkList:
            if not(x in self.visited):
                self.urls.put(x)

        # yield {
        #    "links": linkList
        # }

        next_page = self.get_next_page()

        if self.destination == next_page:
            print("Hurray Hurray!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Found the Page: " + next_page)
            raise scrapy.CloseSpider('Success')
        if next_page is None:
            raise scrapy.CloseSpider('YEet')
        while next_page.count("/") > 2:
            print("Bad Page: " + next_page)
            next_page = self.get_next_page()
        next_page = "https://en.wikipedia.org" + next_page  # .encode("utf-16")
        print("Next page: " + next_page)

        pageRequest = scrapy.Request(url=next_page, callback=self.parse)
        yield pageRequest

    def get_next_page(self):
        next_page = self.urls.get()
        while next_page in self.visited and not(self.urls.empty()):
            next_page = self.urls.get()
        self.visited.append(next_page)
        return next_page
