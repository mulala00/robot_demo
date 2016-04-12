"""Variables example from a py  file

    Variables define in this file can both using in Robot and Python Library

    In Robot:
        Library                vars_with_args   buck
"""


REMOTE_HOST = {
    'hzling09':    {'HOST':              'hzling09.china.nsn-net.net',
                    'USER':              'xiuzhou',
                    'PASSWORD':          "I Can't Tell You"},

    'BUCK':        {'HOST':              '10.68.10.88',
                    'USER':              'root',
                    'PASSWORD':          "root"}
}


def get_variables(server_name):
    """
    Do Not change This function Name.

    RobotFramework will call 'get_variables' automatically to get variables with arguments
    :param: server_name
    :return: The Address of the sever, User and passwords
    """

    return REMOTE_HOST[server_name]
