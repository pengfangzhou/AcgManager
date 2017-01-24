# -*- coding: utf-8 -*-

from fabric.api import cd,run,env

# env.hosts = ['root@123.57.138.29',]
# env.password = 'Asd868**123qwe'

env.hosts = ['zhoupengfang@127.0.0.1',]
env.password = 'zpf13156'

def dotask():
    print "dotask()"
    # lsfab()
    gitfresh()

#git更新
def gitfresh():
    print "gitfresh()"
    with cd("/Users/zhoupengfang/Documents/spaces/acgSpace/AcgServer/"):
        # run('git commit -am "c"')
        run('git pull')


#简单的本地操作
def lsfab():
    with cd('~'):
        run('ls')

#简单命令
def hello():
    # name,value
    print("Hello world")