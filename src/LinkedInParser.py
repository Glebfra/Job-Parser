import re

import bs4
import peewee

from src.models.Appliments import Appliements
from src.models.JobItem import JobItem


def parse_linkedIn_html(file: str) -> list[JobItem]:
    with open(file, 'r') as file:
        html_file = file.read()

    soup = bs4.BeautifulSoup(html_file, 'html.parser')
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


if __name__ == '__main__':
    response = parse_linkedIn_html('../data/LinkedIn/My Jobs _ LinkedIn.html')
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
