# -*- coding: utf-8 -*-
import ConfigParser
import sys
import pynotify
import time
import tempfile
from hgapi import Repo
from parser import create_chunks, convert_chunks
from show import display_changesets
from daemon import Daemon

config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))
repos = config.get('main', 'repos').split()
repos = map(Repo, repos)
timing = config.get('main', 'check_time')
interval = float(timing[:-1])
mark = 1 if timing[-1] == 's' else 60


class MyDaemon(Daemon):

    def run(self):
        # for repo in repos:
        #     hgin = repo.hg_command('in')
        #     with open('/home/lovesuper/Documents/AAAAAAAA.txt', 'a') as f:
        #         f.write('str')
        #     hgin = open('/home/lovesuper/testhg.txt').read()

        #     chunks = create_chunks(hgin)
        #     count = len(chunks)
        #     changesets = convert_chunks(chunks)

        # выводить название репы ищо
        #     display_changesets(changesets, count)
        # time.sleep(interval * mark)
        #     self.run()
        while True:
            if pynotify.init('1'):
                pynotify.Notification('message', 'hello').show()


if __name__ == "__main__":
    pidFile = tempfile.gettempdir() + '/daemonHgPushNotify.pid'
    mydaemon = MyDaemon(pidFile)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            mydaemon.start()
        elif 'stop' == sys.argv[1]:
            mydaemon.stop()
        elif 'restart' == sys.argv[1]:
            mydaemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
