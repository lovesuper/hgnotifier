# -*- coding: utf-8 -*-
import pynotify
pynotify.init("Some Application or Title")
picpath = '/home/lovesuper/Documents/1.png'
# note = pynotify.Notification('Message', 'ddddddd', picpath)
# note.show()


def callback_function(notification=None, action=None, data=None):
    print "It worked!"

n = pynotify.Notification("Title", "body", "dialog-warning")
n.set_urgency(pynotify.URGENCY_NORMAL)
n.set_timeout(pynotify.EXPIRES_NEVER)
n.add_action("clicked", "Button text", callback_function, None)
n.show()


# comparing with http://localhost:8000/
# searching for changes
# all local heads known remotely
# changeset:   1:7c950cad694a
# tag:         tip
# user:        anton kost <antononrails@gmail.com>
# date:        Thu Apr 25 20:46:09 2013 +0400
# files:       file.txt
# description:
# 22
#
