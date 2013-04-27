 # -*- coding: utf-8 -*-
import re
from collections import namedtuple


patterns = {
    "changeset": re.compile(r'^changeset:\s+([\d:\w]+)$', re.MULTILINE),
    "tag": re.compile(r'^tag:\s+([\d\w]+)$', re.MULTILINE),
    "user": re.compile(r'^user:\s+([\d@. <>\w]+)$', re.MULTILINE),
    "date": re.compile(r'^date:\s+([+:\d \w]+)$', re.MULTILINE),
    "files": re.compile(r'^files:\s+([^\n]+)$', re.MULTILINE),
    "description": re.compile(r'^description:\s+([\w\s.,!?#]+)', re.MULTILINE),
}
user_pattern = re.compile(r'(?P<name>[\w\d\s.]+)\s<(?P<email>[\w\d@.]+)>')

Changeset = namedtuple('Changeset', patterns.keys())
User = namedtuple('User', ['name', 'email', 'pic'])


def create_chunks(string):
    raw_chunks = string.split("\n\n")
    raw_chunks = map(lambda e: re.sub(r' +', ' ', e), raw_chunks)
    return filter(lambda e: len(e) > 1, raw_chunks)


def convert_chunks(raw_chunks):
    for chunk in raw_chunks:
        keys = {}
        for key, pattern in patterns.iteritems():
            match = pattern.findall(chunk)
            match = ''.join(match)
            if key == 'files':
                match = match.split()
            elif key == 'user':
                match = user_pattern.match(match)
                email = match.group('email')
                name = match.group('name')
                # FIXIT: Check for avatars
                pic = open('/home/lovesuper/Documents/pics/1.png', 'rb')
                match = User(name, email, pic)

            keys.update({key: match})

        yield Changeset(**keys)
