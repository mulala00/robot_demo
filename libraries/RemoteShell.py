from SSHLibrary import SSHLibrary
import time
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger

ROBOT_FW = BuiltIn()


class _Target:
    def __init__(self, host, username=None, password=None):
        # Default properties
        self.properties = {
            'init_login_prompt': 'login: ',
            'init_username': None,
            'login_prompt': 'Please give the username:',
            'login_timeout': '3 second',
            'password_prompt': 'Please give the password for user',
            'port': 22,
            'prompt': '\n# ',
            'prompt_is_regexp': True,
            'timeout': '2 minutes',
            'max_conn_attempts': 3,
            'ssh_log_file': None,
            'ssh_key_file': None,
        }

        self.host = host
        self.username = username
        self.password = password
        self.conn = SSHLibrary()
        self.conn_open = False


class RemoteShell(object):
    """Library for executing commands in CLA shell of FlexiPlatform.

    The library inherits all the keywords from DSPRemoteLib library
    for telnet connection handling.
    """
    CONNECTION_REFUSED = 111
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.target = None

    def connect_to_target(self, host, username, password):
        target = _Target(host, username, password)
        i = 0
        while not target.conn_open:
            try:
                target.conn.open_connection(target.host, "cla", target.properties['port'])
                target.conn_open = True
            except Exception, error:
                i += 1
                msg = 'Opening connection to %s  failed: ' % HOST + str(error)
                if error[0] == self.CONNECTION_REFUSED and i < target.properties['max_conn_attempts']:
                    logger.console("Trying to reconnect in 5 seconds")
                    time.sleep(5)
                else:
                    raise AssertionError(msg)

        if target.properties['ssh_log_file']:
            target.conn.enable_ssh_logging(target.properties['ssh_log_file'])

        target.conn.set_client_configuration(prompt=target.properties['prompt'])
        target.conn.set_client_configuration(timeout=target.properties['login_timeout'])

        if target.properties['ssh_key_file'] is None:
            target.conn.login(target.username, target.password)
        else:
            target.conn.login_with_public_key(target.username, target.properties['ssh_key_file'])

        target.conn.set_client_configuration(timeout=target.properties['timeout'])

        if target.properties['ssh_log_file']:
            target.conn.enable_ssh_logging(target.properties['ssh_log_file'])
        self.target = target

    def dsp_core_should_be_enable(self, shelf="1", slot="4", device="0", core="0"):
        """
        fshwModuleId=core-0,fshwModuleId=DSP2-0,fshwModuleId=dsp2farm-0,fshwPIUId=piu-4,fshwEquipmentHolderId=chassis-1,fshwEquipmentHolderId=cabinet-1,fsFragmentId=HW,fsClusterId=ClusterRoot:
        administrative(UNLOCKED)
        operational(ENABLED)
        availability()
        """
        target_core = "dsp-%s-%s-%s-%s" % (str(shelf), str(slot), str(device), str(core))
        output = self.my_execute_command('fsclish -c "show dsp has-state core %s"' % target_core)
        ROBOT_FW.should_contain(output, 'operational(ENABLED)', "DSP is not enable:\n%s" % output)

    def dsp_core_should_be_disable(self, shelf="1", slot="4", device="0", core="0"):
        """
        fshwModuleId=core-0,fshwModuleId=DSP2-0,fshwModuleId=dsp2farm-0,fshwPIUId=piu-4,fshwEquipmentHolderId=chassis-1,fshwEquipmentHolderId=cabinet-1,fsFragmentId=HW,fsClusterId=ClusterRoot:
        administrative(UNLOCKED)
        operational(ENABLED)
        availability()
        """
        target_core = "dsp-%s-%s-%s-%s" % (str(shelf), str(slot), str(device), str(core))
        output = self.my_execute_command('fsclish -c "show dsp has-state core %s"' % target_core)
        ROBOT_FW.should_contain(output, 'operational(DISABLED)', "DSP is not enable:\n%s" % output)

    def my_execute_command(self, cmd, return_stdout=True, return_stderr=False, return_rc=False):
        """
        Executes `cmd` on the remote machine and returns its outputs.
        :param cmd:
        :return: command output
        """
        return self.target.conn.execute_command(cmd, return_stdout, return_stderr, return_rc)

    def my_start_command(self, cmd):
        """
        Starts execution of the `command` on the remote machine and returns immediately.
        :param cmd:
        :return: None
        """
        self.target.conn.start_command(cmd)

    @keyword(tags=["mulala"])
    def hostname_should_be(self, name):
        output = self.my_execute_command("hostname")
        logger.debug(output)
        if output != name:
            raise AssertionError("Not CLA-0! You get %s" % output)

    def write_syslog(self, message):
        self.my_execute_command("looger %s" % message)

    def disconnect_to_target(self):
        self.target.conn.close_all_connections()

    def upload_file(self, source, destination='.', mode='0744', newline=''):
        self.target.conn.put_file(source, destination, mode, newline)

    def download_file(self, source, destination='.'):
        self.target.conn.get_file(source, destination)

    def collect_syslog(self, destination):
        tmp_syslog = "/tmp/syslog.txt"
        self.my_execute_command("tail -n 100 /srv/Log/log/syslog > %s" % tmp_syslog)
        self.download_file(tmp_syslog, destination)
        self.my_execute_command("rm %s -rf" % tmp_syslog)

    def echo_var(self, *vars):
        for each_var in vars:
            print type(each_var), each_var




