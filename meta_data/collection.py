'''
    collect prompt, objects...
'''

import os
import json

import yaml


# access *.yaml
def get_yaml_content(yaml_file):
    with open(yaml_file, 'r') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    return content

def select_yaml_content(yaml_file, key):
    # key is a list
    content = get_yaml_content(yaml_file)
    # select the content
    new_content = {}
    for i, k in enumerate(key):
        new_content[k] = content[k]
        
    return content

def get_yaml_files(yaml_dir):
    yaml_files = []
    file_name_list = []
    for item in os.listdir(yaml_dir):
        if item.endswith('.yaml'):
            yaml_files.append(yaml_dir + item)
            file_name_list.append(item.split('.')[0])

    return yaml_files, file_name_list

def save_to_jsonl(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)
    print(f"Saved to {file_name}")

if __name__ == '__main__':
    yaml_dir = '../video_configs/'
    yaml_files, file_name_list = get_yaml_files(yaml_dir)
    print(yaml_files)
    print(file_name_list)

    select_content = ['prompt', 'phrases']
    # collect the prompt and phrases from one yaml file
    select_contents = {}
    for yaml_file in yaml_files:
        content = select_yaml_content(yaml_file, select_content)
        video_name = file_name_list[yaml_files.index(yaml_file)]
        select_contents['id'] = video_name
        select_contents['prompt'] = content['prompt']

        # process 'phrases'
        phrases = content['phrases'][0]
        select_contents['objects'] = phrases
        # save to jsonl
        
        print(select_contents)
        save_to_jsonl(f'prompt/{video_name}.jsonl', select_contents)