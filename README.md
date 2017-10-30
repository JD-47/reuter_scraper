# scrapy_web crawler
for UBUNTU
(Preferred scrapy over conventional Beautiful Soup given its better speed ).

project set up guide :

python : sudo apt-get install python
pip : sudo apt-get install python-pip
scrapy : pip install Scrapy
xlsxwriter : sudo pip install xlsxwriter


Environment setting :

Type the folllowing commands in the terminal :-
 
1. $ scrapy
   To check if it is properly installed.(you can see, there is a short list of scrapy commands)
2. Go to the directory , to which you want to add your project.
3. $ scrapy startproject scrapy_spider
4. $ cd scrapy_spider
5. $ scrapy genspider quotes_spider www.reuters.com
6. Go to , scrapy_spider/spiders folder.
7. Replace the existing quotes_spider.py  with our quotes_spider.py

Running the script : 

1. Open the terminal and go to the project directory.
2. Then go to the directory containing quotes_spider.py
3. $ scrapy crawl quotes_spider

Errors:

1. Internal server error if internet speed is not good.
2. When running all the modules togther. Url not found error is not handled.
3. write now, have one single file having functions corresponding to each step in quotes_spider.py .
4. trying to make code more formatted.

Comments :
In last 3 days ,tried python and scrapy for the very first time , Great Experience !
Our first web crawler :D (y)





