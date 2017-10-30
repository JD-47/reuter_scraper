# -*- coding: utf-8 -*-
import scrapy
import xlsxwriter

workbook = xlsxwriter.Workbook('step04.xlsx')
worksheet1 = workbook.add_worksheet()

workbook = xlsxwriter.Workbook('step05.xlsx')
worksheet2 = workbook.add_worksheet()
temp=[]
r=0
c=0
class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['reuters.com']
    #start_urls=['https://www.reuters.com/finance/stocks/company-officers/9437.T']

    start_urls=['https://www.reuters.com/sectors/industries/rankings?view=size&industryCode=8']
    # 3.start_urls=['https://www.reuters.com/sectors/industries/overview?industryCode=4']
    #start_urls = ['https://www.reuters.com/sectors/industries/rankings?view=size&industryCode=179']
    # 2. start_urls = ['https://www.reuters.com/sectors/energy?smbl=SPDR']
    BASE_URL='https://www.reuters.com'
    

    def parse(self, response):
	name = response.xpath("//td[@class='sectorTitle']//a/text()").extract()
        links = response.xpath("//td[@class='sectorTitle']//a/@href").extract()      
	dictionary = dict(zip(name, links))

#	dictionary = dict(itertools.izip(keys,values))  // more economical in term of memory (for python2 only).       

	workbook = xlsxwriter.Workbook('step01.xlsx')
  	worksheet = workbook.add_worksheet()

	bold = workbook.add_format({'bold': True}) 	
 	worksheet.write('A1', 'Sector', bold)
	worksheet.write('B1', 'URL', bold)

	row = 1
	col = 0

	for name , addr in dictionary.items():
	    worksheet.write(row, col,     name)
	    worksheet.write(row, col + 1, addr)
	    row += 1
	
	for link in links:
	    url = self.BASE_URL + link
	    yield scrapy.Request(url, callback=self.parse_item)
	    	
    def parse_item(self, response):
	link = response.xpath("//div[@class='sectionRelatedTopics']/ul/li[1]/a/@href").extract()
        temp.append(link)
	print "LINK IS " ,link
	str1 = ''.join(link)
	url=self.BASE_URL+str1
	print "URL formed is " , url
	yield scrapy.Request(url, callback=self.parse_attr)
	return 
	
	
    def parse_attr(self, response):
	name = response.xpath("//div[@class='sectionRelatedTopics relatedIndustries']/ul/li/a/text()").extract()
	link = response.xpath("//div[@class='sectionRelatedTopics relatedIndustries']/ul/li/a/@href").extract()	
    
	str1 = '\n'.join(link)
	url =self.BASE_URL+str1
	print "url is " , url

	yield scrapy.Request(url, callback=self.parse_ticker)

    def parse_ticker(self, response):
	# printing headings.
	name = response.xpath("//table[@class='dataTable']/tbody[@class='dataSmall']/tr[1]/th/a/text()").extract()
	n=len(name)
	for i in range(0,n):
		name[i]=name[i].strip()  # string is immutable in PYTHON.
	
	name[2:3] = [''.join(map(str,name[2:3]))]
	print "TITLES ARE" , name			
	
	workbook = xlsxwriter.Workbook('step03.xlsx')
  	worksheet = workbook.add_worksheet()

	bold = workbook.add_format({'bold': True}) 
	
 	for i,e in enumerate(name,start=0):
		worksheet.write(0,i,e,bold)

	#/html/body/div[4]/div[3]/div/div[2]/div[1]/div[7]/div/table/tbody/tr[3]/td[1]/a
	tickers = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[7]/div/table/tbody//tr/td[1]/a/text()").extract()
	
	n=len(tickers)
	for i in range(0,n):
		tickers[i]=tickers[i].strip()

	for i,e in enumerate(tickers,start=1):
		worksheet.write(i,0,e)
	
	print tickers

	name = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[7]/div/table/tbody//tr/td[2]/a/text()").extract()

	n=len(name)
	for i in range(0,n):
		name[i]=name[i].strip()

	for i,e in enumerate(name,start=1):
		worksheet.write(i,1,e)

	print name

	cost = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[7]/div/table/tbody//tr/td[3]/text()").extract()

	n=len(cost)
	for i in range(0,n):
		cost[i]=cost[i].strip()

	for i,e in enumerate(cost,start=1):
		worksheet.write(i,2,e)

	print cost

	value = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[7]/div/table/tbody//tr/td[4]/text()").extract()

	n=len(value)
	for i in range(0,n):
		value[i]=value[i].strip()

	for i,e in enumerate(value,start=1):
		worksheet.write(i,3,e)
	
	print value



	x = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[7]/div/table/tbody//tr/td[5]/text()").extract()

	n=len(x)
	for i in range(0,n):
		x[i]=x[i].strip()

	for i,e in enumerate(x,start=1):
		worksheet.write(i,4,e)
	
	print x






    def parse_people(self ,response):
	name = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/table/tbody//tr/td[1]/h2/a/text()").extract()
	
	n=len(name)
	for i in range(0,n):
		name[i]=name[i].strip()

	for i,e in enumerate(name,start=0):
		worksheet1.write(i,0,e)
		
	age = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/table/tbody//tr/td[2]/text()").extract()

	n=len(age)
	for i in range(0,n):
		age[i]=age[i].strip()

	for i,e in enumerate(age,start=0):
		worksheet1.write(i,1,e)

	year = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/table/tbody//tr/td[3]/text()").extract()

	n=len(year)
	for i in range(0,n):
		year[i]=year[i].strip()

	for i,e in enumerate(year,start=0):
		worksheet1.write(i,2,e)
	desig = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/table/tbody//tr/td[4]/text()").extract()

	n=len(desig)
	for i in range(0,n):
		desig[i]=desig[i].strip()

	for i,e in enumerate(desig,start=0):
		worksheet1.write(i,3,e)
	

	des=response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div[3]/div/div[2]/table/tbody//tr/td[2]/text()").extract()
	
	print "description is ",des
	n=len(des)
	for i in range(0,n):
		des[i]=des[i].strip()

	for i,e in enumerate(des,start=0):
		worksheet1.write(i,4,e)


