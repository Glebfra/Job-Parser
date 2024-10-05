import bs4
import peewee
from dotenv.main import load_dotenv

from src.models.Appliments import Appliements
from src.parsers.IndeedParser import IndeedParser
from src.parsers.LinkedInParser import LinkedInParser

load_dotenv('../.env')


def parse_linked_in():
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

    print(f'LinkedIn: {getted=}, {created=}')


def parse_indeed():
    with open('../data/Indeed/My jobs _ Indeed.html', 'r') as file:
        html_file = file.read()

    soup = bs4.BeautifulSoup(html_file, 'html.parser')
    response = IndeedParser.parse_from_html(soup)

    getted, created = 0, 0
    for job in response:
        try:
            Appliements.get(name=job.name, url=job.url)
            getted += 1
        except peewee.DoesNotExist:
            appliement = Appliements(name=job.name, url=job.url)
            appliement.save()
            created += 1

    print(f'Indeed: {getted=}, {created=}')


if __name__ == '__main__':
    parse_linked_in()
    parse_indeed()
