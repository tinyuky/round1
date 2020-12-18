import os

import requests
from datetime import datetime
from database.models import Commits

base_url = 'https://api.github.com'
search_url = '/search/commits?q=repo:elastic/elasticsearch+committer-date:>2020-10-01&per_page=100&page='
languages_url = '/repos/elastic/elasticsearch/languages'
token = f"token {os.environ['PERSONAL_ACCESS_TOKEN']}"


def import_list_commits():
    print('Syncing data')
    Commits.objects().delete()
    x = 1
    while x > 0:
        data = call_search_commits_api(str(x))
        if 'items' in data:
            insert_commits_data(data['items'])
            x += 1
        else:
            break

    return True


def call_search_commits_api(page):
    url = base_url + search_url + page
    headers = {'Accept': 'application/vnd.github.cloak-preview', 'Authorization': token}
    r = requests.get(url, headers=headers)
    return r.json()


def insert_commits_data(data):
    for item in data:
        Commits(
            authored_date=datetime.strptime(item['commit']['author']['date'], '%Y-%m-%dT%H:%M:%S.%f%z'),
            committer_id=str(item['author']['id']),
            committer_name=item['author']['login'],
            committer_avatar_url=item['author']['avatar_url'],
            commit_html_url=item['html_url']
        ).save()

    return True


def call_languages_api():
    url = base_url + languages_url
    headers = {'Accept': 'application/vnd.github.cloak-preview', 'Authorization': token}
    return requests.get(url, headers=headers)
