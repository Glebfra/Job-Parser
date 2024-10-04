import re

import bs4
import peewee

from src.models.Appliments import Appliements
from src.models.JobItem import JobItem


def parse_indeed_html(file: str) -> list[JobItem]:
    with open(file, 'r') as file:
        html_file = file.read()

    soup = bs4.BeautifulSoup(html_file, 'html.parser')
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


if __name__ == '__main__':
    response = parse_indeed_html('../data/Indeed/My jobs _ Indeed.html')
    getted, created = 0, 0
    for job in response:
        try:
            Appliements.get(name=job.name, url=job.url)
            getted += 1
        except peewee.DoesNotExist:
            appliement = Appliements(name=job.name, url=job.url)
            appliement.save()
            created += 1

    print(f'{getted=}, {created=}')
