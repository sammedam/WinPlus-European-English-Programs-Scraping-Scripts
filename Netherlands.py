from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
driver = webdriver.Chrome("chromedriver")
name=[]
z=[]
ps=[]
Level=[]
TD=[]
Fee=[]
Country=[]
City=[]
u=[]
p=[]
xs=[]


#open up connection + grab the page
    
driver.get("https://www.studyinholland.co.uk/full_course_directory.html")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('p', attrs={'class':'fc-course'}):
    b=a.find('a')
    course=b.get_text()
    if len(course.strip())>4:
        print("course="+course)       
        url="https://www.studyinholland.co.uk/"+b.get('href')
        #driver.get(url)
        #actualContent=driver.page_source
        try:
            uClient = uReq(url)
            page_html = uClient.read()
            uClient.close()
        except:pass
       
        #actualsoup=BeautifulSoup(actualContent)
        actualsoup=BeautifulSoup(page_html, "html.parser")
        try:           
            summary=actualsoup.find('div', attrs={'class':'row course-summary-t'}) 
            uni=actualsoup.find('div', attrs={'class':'row course-summary-b'}).find('div', attrs={'class':'col-md-8'}).find('a').get_text()
            if uni is not None:
                u.append(uni)
                p.append(course)
            if(summary is not None):
                label=summary.find('span', attrs={'class':'course-label'})
                if(label is not None):
                    label=label.get_text()
                    subject=summary.find('strong').get_text()
                    xs.append(subject)
            for x in actualsoup.findAll('div', attrs={'class':'col-md-4'}):  
                
                s= x.find('span',attrs={'class':'course-label'})         
                if s is not None:
                    if(x.find('span',attrs={'class':'course-label'})) is not None:
                        title=x.find('span',attrs={'class':'course-label'}).get_text()
                    if(title=="Level"):
                        if(x.find('strong')) is not None:
                            a=x.find('strong').get_text()
                        elif (x.find('a')) is not None:
                            a=x.find('a').get_text()
                        Level.append(a)
                
                    if(title=="Type of Degree"):
                        if(x.find('strong')) is not None:
                            b=x.find('strong').get_text()
                        elif (x.find('a')) is not None:
                            b=x.find('a').get_text()
                        TD.append(b)
                
                    if(title=="EU Fees"):
                        if(x.find('strong')) is not None:
                            c=x.find('strong').get_text()
                        elif (x.find('a')) is not None:
                            c=x.find('a').get_text()
                        Fee.append(c)
                
                    if(title=="Country"):
                        if(x.find('strong')) is not None:
                            d=x.find('strong').get_text()
                        elif (x.find('a')) is not None:
                            d=x.find('a').get_text()
                        Country.append(d)
                    
                    if(title=="City"):
                        if(x.find('strong')) is not None:
                            e=x.find('strong').get_text()
                        elif (x.find('a')) is not None:
                            e=x.find('a').get_text()
                        City.append(e)
        except:continue
               
df = pd.DataFrame({'Program':p,'University':u,'Subject':xs,'Level':Level,'Type of Degree':TD,'EU Fees':Fee,'Country':Country,'City':City}) 
df.to_csv('Netherlands.csv', index=False, encoding='utf-8')