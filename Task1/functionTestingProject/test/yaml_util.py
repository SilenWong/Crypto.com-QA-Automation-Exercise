import os
import yaml

#function to read testcase from yaml file
def read_yaml(yaml_name):
    with open(os.getcwd() + '/'+yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value