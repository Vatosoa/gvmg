import scrapy
from gvmg.items import ArticleItem


class GvmgspiderSpider(scrapy.Spider):
    name = "gvmgspider"
    allowed_domains = ["mg.globalvoices.org"]
    start_urls = ["http://mg.globalvoices.org/"]

    def parse(self, response):
        articles = response.css('article.gv-promo-card')

        for article in articles:
            relative_url = article.css('.gv-promo-card-text h3 a ::attr(href)').get() 
            yield response.follow(relative_url, callback=self.parse_article_page)
            
        next_page = response.css('div.navigation div.previous a ::attr(href)').get()

        if next_page is not None:
            next_page_url = next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_article_page(self, response):
        article_item = ArticleItem()
        
        article_item['url'] = response.url,
        article_item['date'] = response.css('div.post-header-meta span.post-date a ::attr(title)').get(),
        article_item['place'] = response.css('div.taxonomy-list-container span.active-term a::text').get(),
        article_item['author'] = response.css('.author .contributor-name a.user-link::text').get(),
        article_item['translator'] = response.css('.translator .contributor-name a.user-link::text').get() ,
        article_item['title'] = response.css('h2.screen-title a::text').get(),
        article_item['text_content'] = response.xpath('//div[@class="entry-container"]/div[@class="entry"]/p[not(ancestor::article or ancestor::blockquote)]/descendant-or-self::*/text()').getall()
        
        yield article_item
