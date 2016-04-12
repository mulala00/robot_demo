from robot.api.deco import keyword

__version__ = '1.0.1'


class MyStaticLib(object):
    """
    We should always create library with documentation
    """
    _num_of_instances = 0

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_CONTINUE_ON_FAILURE = True

    def __init__(self, name):
        print "%s is %s" % (name, self)
        MyStaticLib._num_of_instances += 1

    def static_api(self):
        """Library keyword also need with documentation """
        print "Static API from :%s, number of instances %d " % (self, MyStaticLib._num_of_instances)

    def suite_setup(self):
        pass

    def suite_teardown(self):
        pass

    def case_setup(self):
        pass

    def case_teardown(self):
        pass


class IHaveToUsingExplict(object):
    _num_of_instances = 0
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, name):
        print "%s is %s" % (name, self)
        IHaveToUsingExplict._num_of_instances += 1

    @keyword(tags=['tag1', 'tag2'])
    def static_api(self):
        print "Static API from :%s, number of instances %d " % (self, IHaveToUsingExplict._num_of_instances)

# It's a Little trick here, because "Library MyStaticLib" == "Library MyStaticLib.MyStaticLib"
# So using keyword 'function_keyword' will failure.'


def function_keyword(arg):
    print "I am a simple keyword:", arg


