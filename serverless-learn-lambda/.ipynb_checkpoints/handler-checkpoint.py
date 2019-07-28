import datetime
import logging
import json
from ftplib import FTP
from my_utils.os_utils import subprocess_execute


def run(event=dict(), context=dict()):
    ''' Function to be called by serverless lambda
    '''
    # print out results of ls
    print(subprocess_execute('ls'))
    # run shell command to print out results of pip freeze
    print(subprocess_execute('pip freeze'))

