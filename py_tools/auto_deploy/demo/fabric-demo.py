# encoding: utf-8

from fabric.api import *

env.user = 'root'
env.hosts=['xx.xx.xx.xx'] 
env.password = 'pw'


def play():   
    print "Hello World"
    with cd('/'):
        run("ls -l")
   