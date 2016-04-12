"""
The simplest approach is having a module with methods which map directly to keyword names.
Keywords also take the same arguments as the methods implementing them. Keywords:
    report failures with exceptions,
    log by writing to standard output
    and can return values using the return statement.
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
