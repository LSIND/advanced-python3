#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Video:
    def __init__(self, link, title, description, channel_name, channel_url, date_published):
        self.link = link
        self.title = title
        self.description = description
        self.channel_name = channel_name
        self.channel_url = channel_url
        self.date_published = date_published

    def __str__(self):        
        return f'{self.title} ({self.link}). {self.description}.\nChannel: {self.channel_name} ({self.channel_url}).\nDate published: {self.date_published}'