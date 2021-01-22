import scrapy



class QuotesSpider(scrapy.Spider):
    name = "farfetch"
   # allowed_domains = ["http://www.farfetch.com/de/shopping/men/shoes-2/items.aspx"]
    def start_requests(self):
        urls = [] 
        for i in range(1, 236):
            url = "https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page=" + str(i)
            urls.append(url)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        self.log("success")
        # for loop for main url 
        for product_details in response.xpath("//li[@class='_a44404 _d85b45']/a[@class='_5ce6f6']"):
            # other part of the url for the brand
            product_Brand = product_details.xpath("div[@class='_bab25b _18fbc8']/h3/text()").get()
            # for Name
            product_Name = product_details.xpath("div[@class='_bab25b _18fbc8']/p[@itemprop='name']/text()").get()
            # for price
            product_Price = product_details.xpath("div[@class='_bab25b _18fbc8']/div/span[@data-test='price']/text()").get()
            
            # replace (.) with ()
            # product_Price = product_Price.replace(".","")
            # replace ( €) with ()
            # product_Price = product_Price.replace(" €","")
            # change in float 
            # product_Price = float(product_Price)

            # for product url
            product_url = product_details.xpath("@href").get()
            # join url with the base url
            product_url = response.urljoin(product_url)

            # for image url
            product_imageurl = product_details.xpath("meta[@itemprop='image']/@content").get()
     
            # put the value in dictionary with the help of yield
            yield {
                "Brand" : product_Brand,   
                "Name" : product_Name,
                "Price(in Euros €)" : product_Price,
                "Product_Url" : product_url,
                "Image_Url" : product_imageurl
            }
