import re
from typing import List

import bs4

from src.models.JobItem import JobItem


class IndeedParser:
    def __init__(self, headers):
        self.headers = headers

    @staticmethod
    def parse_from_html(soup: bs4.BeautifulSoup) -> List[JobItem]:
        items = (
            soup.find('div', attrs={'role': 'tabpanel'})
            .find_next('div', class_='atw-Updates')
            .find_all('li')
        )
        job_items = []
        for item in items:
            job = (
                item.find_next('div', class_='atw-AppCard-mainContainer')
                .find_next('a', class_='atw-JobInfo-jobTitle')
            )
            name = ' '.join(re.findall(r'^.*description', job.get_text()))
            name = name.replace(' description', '')
            url = job['href']
            job_items.append(JobItem(name=name, url=url))
        return job_items
