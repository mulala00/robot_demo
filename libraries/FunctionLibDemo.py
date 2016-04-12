"""
Dynamic libraries are classes that implement a method to get the names of the keywords they implement,
and another method to execute a named keyword with given arguments.
The names of the keywords to implement, as well as how they are executed, can be determined dynamically at runtime,
but reporting the status, logging and returning values is done similarly as in the static API.
"""
from robot.api import logger


def function_keyword(*arg):
    print "I am a simple keyword:", arg


def log_in_python(*args, **kwargs):
    for _arg in args:
        logger.info("%s is a type of %s" % (str(_arg), type(_arg)))

    for _kwarg in kwargs:
        logger.info("%s:%s is a type of dictionary" % (str(_kwarg), kwargs[_kwarg]))
