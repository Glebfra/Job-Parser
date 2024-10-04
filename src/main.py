import bs4
import peewee

from src.models.Appliments import Appliements
from src.parsers.LinkedInParser import LinkedInParser

with open('../data/LinkedIn/My Jobs _ LinkedIn.html', 'r') as file:
    html_file = file.read()

soup = bs4.BeautifulSoup(html_file, 'html.parser')
response = LinkedInParser.parse_from_html(soup)

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
