
#!/usr/bin/python  
# -*- coding:utf8 -*-  
  
import os  
# import commands
tomcat_name="/home/tomcat-7.0.73-"
dir='/home/test'
service_name=[["server_name1","server_name2"],
            ["server_name3"]]
service_id=[["ip1","ip2"],
            ["ip3"]]

def printScp():
    i=0
    for names in service_name:
        for name in names:
            for ip in service_id[i]:
                command=r'scp -i ~/.ssh/keyName -o "StrictHostKeyChecking no"  -r -P10088 %s%s test@%s:%s'%(tomcat_name,name,ip,dir)
                print(command)  #python3和2的输出语句写法不一样 2为 prin str
                # os.system(command)
        i=i+1

def printPath( path):  
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''  
    # 所有文件夹，第一个字段是次目录的级别  
    dirList = []  
    # 所有文件  
    # fileList = []  
    # 返回一个列表，其中包含在目录条目的名称(google翻译)  
    files = os.listdir(path)  
    # 先添加目录级别  
    # dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            # 排除隐藏文件夹。因为隐藏文件夹过多  
            if(f[0] == '.'):  
                pass  
            elif "tomcat-7.0.73-" in f:
                dirList.append(f)  
    for dl in dirList:  
        
       print ('%s/%s/logs/*'%(dir,dl))
       os.system('rm -rf %s/%s/logs/*'%(dir,dl))
        
       ml='scp -P10088 %s.tar.gz test@192.168.33.33:/home/test'%dl
       os.system(ml)
       print(ml)

# print dirList
if __name__ == '__main__':
    printScp()  