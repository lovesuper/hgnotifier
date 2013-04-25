# -*- coding: utf-8 -*-
import re
import time
import pynotify
from hgapi import Repo

pynotify.init("app")

pattern = re.compile(r'changeset:\s+(?P<changeset>[\d\w:]+)\ntag:\s+'
                     '(?P<tag>.+)\nuser:\s+(?P<user>[\w\d]+\s[\w\d]+)\s'
                     '(?P<email><[\w\d@.]+>)\ndate:\s+(?P<date>[\w\d :+]+)'
                     '\s.*\sdescription:\s(?P<description>.*)')
png = '/home/lovesuper/Documents/1.png'

repos = []
pathes = [
    '/home/lovesuper/merc/test2/testing',
]
for path in pathes:
    repos.append(Repo(path))


def show(pull):
    result = pattern.search(pull)
    user = result.group('user')
    email = result.group('email')
    desc = result.group('description')
    project = repo.path.split('/')[-1]
    header = u"Ебать копать новый пул в {0}!".format(project)
    message = u"от {0} ({1}) С комментом: {2}".format(
        user, email.strip('<>'), desc)
    note = pynotify.Notification(header, message, png)
    note.show()

if __name__ == "__main__":
    while True:
        for repo in repos:
            try:
                pull = repo.hg_command('in')
            except Exception:
                pass
            else:
                show(pull)
            time.sleep(30)
