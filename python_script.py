import paramiko
from paramiko.client import SSHClient
from paramiko.ssh_exception import AuthenticationException


class RemoteConnect:
    def __init__(self):
        self.host = "192.168.10.132"
        self.client = None
        self.scp = None
        self.__connect()

    def __connect(self):
        try:
            client = SSHClient()
            client.load_system_host_keys()
            client.connect(self.host)
            self.client.set_missing_host_key_policy(AutoAddPolicy())
            self.client.connect(hostname=self.host,
                                username=vagrant,
                                key_filename=id_rsa)
            self.scp = SCPClient(self.client.get_transport())
            client.close()
        except AuthenticationException as error:
            print('Authentication Failed: Please check your network/ssh key')
        # client.close()

    # def disconnect(self):
    #   self.client.close()
    #   self.scp.close()

    def execute_command(self):
        if self.client is None:
            self.client == self.__connect()
        stdin, stdout, stderr = self.client.exec_command('ls')
        status = stdout.channel.recv_exit_status()
        if status is 0:
            return stdout.read()
        else:
            return None

        # stdin, stdout, stderr = client.exec_command('ls -l')


if __name__ == "__main__":
    k = RemoteConnect()
    # k.connect()
    k.execute_command()
    # print(result)
