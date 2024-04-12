#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from Video import Video

def parse_data(link):
    if link:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        content = requests.get(link, headers = headers)
        if content.status_code == 200:
            print(f'Start reading {link}')
            try:
                content = content.text
                soup = BeautifulSoup(content, 'html.parser')                
                video = soup.find("div", class_ = "watch-main-col")
                
                title = video.find('meta', itemprop = "name")['content']
                descr = video.find('meta', itemprop = "description")['content']
                channel_name = video.find('link', itemprop = "name")['content']
                date_published = video.find('meta', itemprop = "uploadDate")['content']
                channel = soup.find("span", itemprop="author")
                channel_url = channel.find('link', itemprop = "url")['href']
                vf = Video(link, title, descr, channel_name, channel_url, date_published)

            except Exception as e:
                print('Error parsing data')
                print(f'Cannot parse data for {link}; {e}')
                return None
            else:
                return vf # dictionary
        else:
            print(content.status_code)
            print(f'Page {link} returns {content.status_code}')
            return None
    else:
        print('Invalid link')
        return None

if __name__ == '__main__':
    '''Urls from file'''
    with open('links.txt', encoding = 'utf-8') as infile:
        for link in infile:
            if link is None or link.isspace():
                continue
            link = link.strip()

            video_object = parse_data(link)
            if video_object:                
                print(video_object)
            else:
                print(f'Cannot parse data for {link}')
            print(10*'#', end='\n')