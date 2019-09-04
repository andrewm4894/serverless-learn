import json
from my_utils.os_utils import subprocess_execute
from my_dev.dev import hello_world
import pandas as pd


def run(event=dict(), context=dict()):
    ''' Function to be called by serverless lambda
    '''
    # make a dummy df to ensure pandas available to the lambda function
    df = pd.DataFrame(data=['this is a dataframe'],columns=['message'])
    print(df.head())
    # call something from my_dev package
    hello_world()
    # print out results of ls
    print(subprocess_execute('ls -la'))
    # run shell command to print out results of pip freeze
    print(subprocess_execute('pip freeze'))

