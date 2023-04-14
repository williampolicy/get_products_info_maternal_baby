import scrapy

class NemoSpider(scrapy.Spider):
    name = 'nemo_spider'
    start_urls = ['https://www.buybuybaby.com/store/s/toy?ta=typeahead']

    def parse(self, response):
        product_titles = response.css('div.prodTitle::text').getall()
        print(product_titles)

        for title in product_titles:
            title_text = title.strip()
            if "Nemo" in title_text:
                print(f"找到了含有Nemo字段的产品：{title_text}")
