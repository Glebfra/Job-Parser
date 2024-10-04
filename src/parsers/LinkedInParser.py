import re
from typing import List

import bs4

from src.models.JobItem import JobItem


class LinkedInParser:
    def __init__(self, headers):
        self.headers = headers

    @staticmethod
    def parse_from_html(soup: bs4.BeautifulSoup) -> List[JobItem]:
        items = soup.find_all('li', class_='reusable-search__result-container')
        job_items = []
        for item in items:
            job = (
                item.find_next('div').find_next('div').find_next('div').find_next('div')
                .find_next('div').find_next('div').find_next('div').find_next('div')
            ).find_next('a')
            name = ' '.join(re.findall(r'\w+', job.get_text()))
            url = job['href']
            job_items.append(JobItem(name=name, url=url))
        return job_items
