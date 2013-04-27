# -*- coding: utf-8 -*-
from hgapi import Repo
from parser import create_chunks, convert_chunks
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))


def main():
    repos = config.get('main', 'repos').split()
    repos = map(Repo, repos)
    for repo in repos:
        hgin = repo.hg_command('in')
        chunks = create_chunks(hgin)
        count = len(chunks)
        changesets = convert_chunks(chunks)
        changeset = next(changesets)
        message = "Push from {0}".format(changeset.user.name)
        message += '\nand {0} else'.format(count - 1)

        print message


if __name__ == '__main__':
    main()
