# -*- coding: utf-8 -*-

"""
在robot framework 里， 如果我们使用多线程， 非主线程的打印，异常都无法被Robotframework 所有获取
如果我们需要获取非主线程的打印， 可以使用BackgroundLogger
"""

from threading import Thread
from robotbackgroundlogger import BackgroundLogger


logger = BackgroundLogger()
threads = {}


def log_on_thread(message, level='INFO', html=False, name=None):
    thread = Thread(name=name, target=logger.write, args=[message, level, html])
    thread.start()
    threads[thread.getName()] = thread


def log_on_threads(message, name_prefix, count):
    for i in range(int(count)):
        name = '%s %d' % (name_prefix, i+1)
        thread = Thread(name=name, target=logger.info,
                        args=['%s says <i>%s</i>.' % (name, message)],
                        kwargs={'html': True})
        thread.start()
        threads[thread.getName()] = thread


def finish_all():
    while threads:
        threads.popitem()[1].join()
    logger.log_background_messages()


def finish_one(name):
    threads.pop(name).join()
    logger.log_background_messages(name)
