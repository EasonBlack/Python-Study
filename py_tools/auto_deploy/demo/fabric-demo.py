# encoding: utf-8

from fabric.api import *

env.user = 'root'
env.hosts=['47.52.102.168'] 



def play():   
    print("Hello World")
    print(env.hosts[0])
    

def connect():
    run('pwd')
    with cd('/usr/share/nginx/html/campaign'):
        run("ls")

list = [
    "-r e:/alead/campaign/dist",
    "e:/alead/campaign/index.html"
]
dest = "root@" + env.hosts[0] + ":/usr/share/nginx/html/campaign"

def update():
    for o in list:
        local("pscp " + o + " " + dest)

def build():
    with lcd("e:\Blead\campaign"):
        local("npm run build")

