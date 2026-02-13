#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class JobVacancy:
    '''Вакансия с Habr Career'''    
    def __init__(self, title, company, rating, salary, skills, url):
        self.title = title
        self.company = company
        self.rating = rating
        self.salary = salary
        self.skills = skills
        self.url = url
    
    def __str__(self):
        return f'''
Вакансия: {self.title}
Организация: {self.company}
Рейтинг: {self.rating}
Зарплата: {self.salary}
Навыки: {self.skills[0]}
Ссылка: {self.url}
'''

class HabrJobParser:
    '''Парсер вакансий Python-разработчика'''
    
    def __init__(self):
        self.base_url = 'https://career.habr.com'
    
    def search(self, query='python', limit=10):
        '''Ищем вакансии по ключевому слову'''
        url = f'{self.base_url}/vacancies?q={query}'
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        vacancies = []
        for item in soup.find_all('div', class_='vacancy-card')[:limit]:
            title_tag = item.find('a', class_='vacancy-card__title-link')
            company_name = item.select('[class*="link-comp"]')
            for i in company_name:
                if company_name:
                    company_name = i.text
                break

            company_rat = item.find('span', class_='company-rating__value')            
            salary_tag = item.find('div', class_='basic-salary')
            skills_tags = item.find_all('div', class_='vacancy-card__skills')
            
            title = title_tag.text.strip() if title_tag else 'Без названия'
            company = company_name if company_name else 'Не указана'
            salary = salary_tag.text.strip() if salary_tag else 'Не указана'
            skills = [s.text.strip() for s in skills_tags]

            company_rat = company_rat.text.strip() if company_rat else 'Не указан'

            vacancies.append(JobVacancy(
                title=title,
                company=company,
                rating = company_rat,
                salary=salary,
                skills=skills,
                url=self.base_url + title_tag['href'] if title_tag else '#'
            ))
        return vacancies

if __name__ == '__main__':
    parser = HabrJobParser()
    jobs = parser.search('ms sql', limit=5)
    for job in jobs:
        print(job)
