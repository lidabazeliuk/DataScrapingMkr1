import scrapy
from bs4 import BeautifulSoup
from mkr1_lida.items import WashMachineItem

class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/bt/stiralnye-i-sushilnye-mashiny/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        
        washMachines = soup.find(class_ = 'list-body__content').find_all(class_ = 'list-item')
        
        for washMachine in washMachines:
            
            name = washMachine.find(class_ = 'list-item__title').find(string=True, recursive=False)
            
            url = washMachine.find(class_ = 'list-item__title').get('href')
            
            price = washMachine.find(class_ = 'price__value').find(string=True, recursive=False)
            
            img = f"https://hotline.ua{washMachine.find(name='img').get('src')}"
            
            
            yield WashMachineItem(
                name=name,
                price=price,
                url=url,
                image_urls=[img]
            )

