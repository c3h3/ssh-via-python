import subprocess
import sys
import os
import time


USER = os.environ.get("USER", "")
HOST = os.environ.get("HOST", "")
LOCAL_SSH_PORT = os.environ.get("LOCAL_SSH_PORT", "22")
HOST_PORT_TO_LOCAL = os.environ.get("HOST_PORT_TO_LOCAL", "7777")
RSA_PRIVATE_KEY_PATH = os.environ.get("RSA_PRIVATE_KEY_PATH", "/home/c3h3/.ssh/id_rsa")

TUNNELING_CMD_TEMPLATE = "ssh -R {host_port_to_local}:localhost:{local_ssh_port} -N {host_user}@{host_ip}"

ssh_cmd = TUNNELING_CMD_TEMPLATE.format(host_port_to_local=HOST_PORT_TO_LOCAL,
                                        local_ssh_port=LOCAL_SSH_PORT,
                                        host_user=USER,
                                        host_ip=HOST)#,
                                        #rsa_private_key_path=RSA_PRIVATE_KEY_PATH)

print "ssh_cmd = ", ssh_cmd

# checking ssh tunneling
p1 = subprocess.Popen(["ps","aux"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "ssh"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
result = p2.stdout.readlines()


ssh_cmd_process = filter(lambda xx:len(xx.split(ssh_cmd))>1,result)

print "ssh_cmd_process = ", ssh_cmd_process

if len(ssh_cmd_process) == 0:
    print "create new ssh tunneling process ... "
    ssh = subprocess.Popen(ssh_cmd.split(),shell=False)
    print ssh.stdout
    print "here"
    #time.sleep(5.)

print "here"

