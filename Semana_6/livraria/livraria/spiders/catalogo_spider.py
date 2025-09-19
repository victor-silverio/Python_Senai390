#Spider para extrair dados de livros do site books.toscrape.com.
      
import scrapy

class CatalogoSpider(scrapy.Spider):
    name = 'catalogo'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # Itera sobre cada livro
        for book in response.css('article.product_pod'):
            yield {
                'titulo': book.css('h3 a::attr(title)').get(),
                'preco': book.css('.price_color::text').get(),
                'disponibilidade': book.css('p.availability').xpath('normalize-space()').get()
            }
        
        # Encontra o link e segue
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)