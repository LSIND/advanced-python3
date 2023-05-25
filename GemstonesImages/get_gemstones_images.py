#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Get images of gemstones from minerals.net'''
import os, shutil
import requests
from bs4 import BeautifulSoup

def get_gemstones_names(page):
    '''get gemstones names and links to their pages
    Returns a dictionary {gemstone : link }'''
    names_paths = {}
    resp = requests.get(page)
    if resp.status_code == 200:
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        table_gems=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
       
        for data in table_gems:
            for link in data.find_all('a'):
                if(link.text!=''):
                    names_paths[link.text] = link.get('href')
    return names_paths

def download_images(key, value):
    '''gets dictionary fetched from main page ../GemStoneMain.aspx
    creates folders for every Gemstone class
    fetches images and saves them to corresponding folder in every page of every gemstone'''
    gem_link = gemslink+value
    print(f'---- {key} ---- {gem_link} ----') # print name and link
    
    resp = requests.get(gem_link)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        table_images=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
        if table_images:                         # create folder if THERE ARE IMAGES
            if not os.path.exists(key):          # create folder if not exists
                os.mkdir(key)                

            for data in table_images:
                for link in data.find_all('img'):
                    src = link.get('src').replace('-thb','').replace('-t', '')
                    if src:
                        img_link = f'{gemslink}{src}'                  
                        r = requests.get(img_link, stream=True)
                        if r.status_code == 200:      # OK
                            print(f'{img_link}: OK')
                            filename = img_link.split('/')[-1]
                            with open(os.path.join(key, filename), 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                        else:
                            print(f'{img_link}: FAILED')
        else:
            print(f'No images found for {key}')
    else:
        print('Page not found')

if __name__ == '__main__':
    gemslink = 'https://www.minerals.net/'
    mainpage = gemslink + 'GemStoneMain.aspx'        # main page to get all names and links

    gems_links = get_gemstones_names(mainpage)
    if gems_links:
        for key, value in gems_links.items():        # get images in every page
            download_images(key, value)