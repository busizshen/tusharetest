
#!/usr/bin/python  
# -*- coding:utf8 -*-  
  
import paramiko

# import commands
 
service_id=["192.168.11.22"]

port=22
username='root'
password='test'
private_key_filename=r'D:\文档\keyName'


def remote_scp(host_ip,remote_path,local_path,private_key_filename):
     
    client = paramiko.SSHClient() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if(private_key_filename):#私钥登陆
        private_key = paramiko.RSAKey.from_private_key_file (private_key_filename)
        client.connect(host_ip, port, username='test', pkey=private_key, timeout=4)
    else:#密码登陆
        client.connect(host_ip, port, username='test', password='123456', timeout=4)
    # private_key = paramiko.RSAKey.from_private_key_file (private_key_filename)
    # client.connect(host_ip, 10088, username='test', pkey=private_key, timeout=4)
    t = client.get_transport()  
    sftp=paramiko.SFTPClient.from_transport(t)  
    d = sftp.put(local_path,remote_path)   
    # print(1) 
    t.close()  

# remote_scp("192.168.10.121",'/home/test/scripts\build.sh',r'D:\pys\ostest\build.sh\build.sh')
def doCommand(i,command):
    # D:\pys\ostest\build.sh\build.sh
    client = paramiko.SSHClient() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
    print(i)
    client.connect(i, port, username=username, password=str(password), timeout=4)   
    stdin, stdout, stderr = client.exec_command(command)   
    # print("stdin:%s"%stdin)
    for line in stdout.readlines():
        print("stdout:%s"%line)
    # print("stderr:%s"%stderr)
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

# strs=['systemctl enable docker']

strs='systemctl enable docker' #docker 开机启动
shutdown='shutdown -r now' #重启

dockerimages='docker images' #docker 开机启动

if __name__ == '__main__':
    # fileNmae='/home/test/scripts/build.sh'
    # strs=r"sed –e 's/.$//' %s > %s"%(fileNmae,fileNmae)
    # strs="vi +':w ++ff=unix' +':q' %s"%fileNmae #windows 2 linux
    # batchSftp()  
    # batchCommand('chmod -R 777 /home/test/scripts')
    # batchCommand("yum install -y unzip zip") 
    # print(strs)
    # batchCommand('rm  -rf  /home/test/*.sh')
    
    batchCommand(dockerimages)

    # batchCommand(shutdown)