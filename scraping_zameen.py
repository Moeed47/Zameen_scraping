#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:26:34 2022

@author: moeed
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_zameen(URL_Zameen):
    df=pd.DataFrame(columns=('Price','Location','Beds','Baths','Area','Descriptions'))
    i=1
    temp_url=URL_Zameen[0:-6]
    while (i>0):
        URL = temp_url+str(i)+".html"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        quotes=soup.findAll("article", class_="f0349ab4")
        if quotes==[]:
            break
        for q in quotes:
            #Price
            fav_quote1=q.findAll("div",class_="_7ac32433")
            #Price=fav_quote1[0].text.strip()
            #print (Price)
            #Location
            fav_quote2=q.findAll("div",class_="_162e6469")
            Location=fav_quote2[0].text.strip()
            #print (Location)
            Beds=''
            Baths=''
            Area=''
            Price=''
            
            span_tags=q.select('span[aria-label]')
            for tag in span_tags:
                if 'Beds' in str(tag):
                    Beds=tag.text.strip()
                    #print (tag.text.strip())
                if 'Price' in str(tag):
                    Price=tag.text.strip()
                    #print (tag.text.strip())
                if 'Baths' in str(tag):
                    Baths=tag.text.strip()
                   # print (tag.text.strip())
                if 'Area' in str(tag):
                    Area=tag.text.strip()
                    #print (tag.text.strip())
        
            fav_quote4=q.findAll("div",class_="ee550b27")
            Description=fav_quote4[0].text.strip()
            #print (Description)
            temp_df={'Price':Price,'Location':Location,'Beds':Beds,'Baths':Baths,'Area':Area,'Descriptions':Description}
            df=df.append(temp_df,ignore_index=True)
        print (URL)
        i=i+1
    zameen_scrap=df.to_json(orient='index')    
    df.to_csv('/home/moeed/Desktop/Hamza_DreamAI/imadi_zameen/Zaneen_scraping.csv')
    return zameen_scrap
    
string="https://www.zameen.com/Homes/Islamabad_DHA_Defence_Phase_2-339-1.html"
print (scrape_zameen(string))
