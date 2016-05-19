from bs4 import BeautifulSoup
import requests
import sys
import os
import time
import re

#print time.ctime()

s =1
while s==1: 
       #print "scraping"
       page = requests.get('https://sabq.org/%D8%B1%D9%8A%D8%A7%D8%B6%D8%A9')
       pageSize = sys.getsizeof(page)
       data = page.text
       titles = []#holds titles foor news
       news =[]#holds news contents
       images =[] #holds images for the news
       soup = BeautifulSoup(data,'html.parser')
       #get images for news 
       img_res = soup.find_all('a', class_="mmlkaImgBody")
       for w in img_res:
           #add images to images list for later use
           images.append(str(w.img))

	# gets front page data in the middle
       res = str(soup.find_all('h4'))
       HPID = sys.getsizeof(res)
       soup = BeautifulSoup(res,'html.parser')
       res = soup.find_all('a')
       TSALL= 0
       TSOUD = 0
       #print "-------> Visting links"
# here we have all the links to the latest news
       for d in res:
    	#we store titles in thitles list
    	   titles.append(d.text)
       #Here we have link to the post page, so we get it
           page = requests.get(d.get('href'))
	   TSALL+= sys.getsizeof(page)  
           soup =  BeautifulSoup(page.text,"html.parser")
           news_content = soup.find(id="dev-content")
           TSOUD+= sys.getsizeof(news_content)
           old = ""
           for p in news_content:
               old+=str(p)
           news.append(old)


#now we have all news titles/contents -----> we are ready to write everything to our html page

 # open the file
       #print "-------> updating site " 
       f = open('sport.html','w')

       page_header = '''<!DOCTYPE html>
       <html dir="rtl">
       <head>
          <meta charset="UTF-8">
         <title>Mukhtasar Sabq</title>
         <link rel="stylesheet" type="text/css" href="style.css">
       </head>
         <body>
         <center>
	<div class='container'>
'''
# headerStart = "<h3 class='news_head'>"
# headerEnd = "</h3>"
#
# contentStart = "<div class ='content'"
# contentEnd = "</div>"
##--------------------------------------------------critical starts
       print >>f, page_header
# for deamon in range(len(titles)):

       for index in range(len(titles)):
               holder = titles[index].encode('utf-8')
	       holde  = holder.decode('unicode-escape')
	       holde = holde.encode('utf-8')
	       print >>f,"<div class='article_wrapper'>"
	       print >>f, "<h3 class='title' style='color:red;'>"
	       print >> f, holde
               print >> f, "</h3>"
               print >> f, images[index]
               print >> f, "<br>"
	       print >>f, "<div class='content' style='color:blue;'>"
       # holder = news[index].encode('utf-8')
	#holde = holder.decode('unicode-escape') 
	#holde = holde.encode('utf-8')
               print >> f, news[index]
	       print >> f, "</div></div>"



##------------------------------------------------------critical ends
       page_footer = '''
	  </div>
          </center>
          </body>
           </html>
           '''
       print >> f, page_footer
       f.close()
       #print "the original home page size"
       #print pageSize
       #print "useful data from this page "
      # print HPID
      # print "total size of all other pages compined"
      # print TSALL
      # print "total size of usefull data from all links"
      # print TSOUD
#       print "Finished, now it is time to sleep!"
       time.sleep(1800)



