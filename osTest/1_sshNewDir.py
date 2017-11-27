#!/usr/bin/python  
# -*- coding:utf8 -*-  
import paramiko   


private_key_filename=r'D:\文档\keyName'

service_id=["192.33.10.999"]
def remote_scp(host_ip,remote_path,local_path):
     
    client = paramiko.SSHClient() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
    private_key = paramiko.RSAKey.from_private_key_file (private_key_filename)
    client.connect(host_ip, 10088, username='test', pkey=private_key, timeout=4)
    t = client.get_transport()  
    sftp=paramiko.SFTPClient.from_transport(t)  
    d = sftp.put(local_path,remote_path)   
    # print(1) 
    t.close()  


def doCommand(i,command):
    # D:\pys\ostest\build.sh\build.sh
    client = paramiko.SSHClient() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
    client.connect(i, 10088, username='test', key_filename=private_key_filename, timeout=4)   
    stdin, stdout, stderr = client.exec_command(command)   
    # for std in stdout.readlines():   
    #     print (std)   
    client.close()   


def batchCommand(command):
    for i in service_id :           
        doCommand(i,command)

        # stdin, stdout, stderr = client.exec_command('mkdir -p /home/test/service')   
        # stdin, stdout, stderr = client.exec_command('mkdir -p /home/test/scripts')   
        # stdin, stdout, stderr = client.exec_command('chmod -R 777 /home/test/scripts')   
          
# mkdir()
def batchSftp():
    for i in service_id :
        remote_scp(i,'/home/test/scripts/build.sh',r'D:\pys\ostest\build.sh\build.sh')
        # remote_scp(i,'/home/test/scripts/chmodBuild.sh',r'D:\pys\ostest\build.sh\chmodBuild.sh')

if __name__ == '__main__':
    fileNmae='/home/test/scripts/build.sh'
    # strs=r"sed –e 's/.$//' %s > %s"%(fileNmae,fileNmae)
    strs="vi +':w ++ff=unix' +':q' %s"%fileNmae #windows 2 linux
    batchSftp()  
    # batchCommand('chmod -R 777 /home/test/scripts')
    batchCommand(strs)
    # batchCommand("yum install -y unzip zip")
    # print(strs)
    # batchCommand('rm  -rf  /home/test/*.sh')