# -*- coding: utf-8 -*-
from time import sleep
from pynotify import Notification, init

init("Some Application or Title")
plura = {'': [1], 'а': [2, 3, 4], 'ов': [5, 6, 7]}


def display_changesets(changesets, count):
    for changeset in changesets:
        modified = len(changeset.files)
        count -= 1
        count = count if count > 0 else u'ждем'
        suffix, = filter(lambda e: modified in plura[e], plura.iterkeys())
        count_suf = filter(lambda e: count in plura[e], plura.iterkeys())
        count_suf = count_suf.pop() if count_suf else ''

        message = (u'Изменения от {0} <{1}>\n{2}\n Изменения: {3} файл{4}\n'
                   u'Описание: {5}\nЕще {6} бабл{7}.').format(
                       changeset.user.name,
                       changeset.user.email,
                       changeset.date,
                       modified,
                       suffix,
                       changeset.description,
                       count,
                       count_suf
                   )
        note = Notification(changeset.user.name,
                            message,
                            changeset.user.pic)
        note.show()
        sleep(11)
