from builtins import len, open
from locale import str
import requests
import json
import pandas as pd
import time
import glob, os

client_id = '6ff8da2ae4d057a6d048'  # you have to write your own id
client_secret = '3b6868e71ae5ef6d14a5d8114a3638e84bc22c7a'  # you have to write your own secret
count = 0
fail_count = 0
os.chdir("/File Structure/PHP files")
sentences = []


# def file_reader(file_name):
#     content = open(file_name + '.txt', 'r')
#     return content.read()

def sentence_formatter(line):
    line = line.replace("/", " ")
    line = line.replace(".", "")
    line = line.replace("_", "")
    line = line.replace("-", "")
    return line


def sentence_parser(text):
    sentence_list = []
    for each_sentence in text:
        # print(sentence_formatter(each_sentence))
        sentence_list.append(sentence_formatter(each_sentence))
    return sentence_list


df = pd.DataFrame(
    columns=['Name of repository', 'Url', 'Project type', 'Framework', 'Programming language', 'Database',
             'File structure'])

dict1 = {'Name of repository': '', 'Url': '', 'Project type': '', 'Framework': '', 'Programming language': '',
         'Database': '', 'File structure': ''}

excel_data_df = pd.read_excel('FormattedData(PHP).xlsx', sheet_name='Sheet1')
json_str = excel_data_df.to_json(orient="records")

projects = json.loads(json_str)

for each_project in projects:
    count += 1
    try:
        dict1['Name of repository'] = each_project['Name of repository']
        dict1['Url'] = each_project['url']
        if each_project['Frontend'] == 'X':
            dict1['Project type'] = 'Frontend'
        if each_project['Backend'] == 'X':
            dict1['Project type'] = 'Backend'
        if each_project['Angular'] == 'X':
            dict1['Framework'] = 'Angular'
            dict1['Programming language'] = 'Typescript'
        if each_project['React'] == 'X':
            dict1['Framework'] = 'React'
            dict1['Programming language'] = 'Javascript'

        file = open(each_project['Name of repository'] + '.txt', 'r')
        contents = file.readlines()
        # print(contents)
        sentence_parser(contents)
        sentences.append(sentence_parser(contents))

        dict1['File structure'] = sentences[0]
        sentences = []
        file.close()
        series = pd.Series(dict1)
        series.to_frame()
        df = df.append(series, ignore_index=True)
    except:
        fail_count += 1
        continue
    print(str(len(projects) - count) + ' projects left')

writer = pd.ExcelWriter('FormattedData(PHP)(2).xlsx', engine='xlsxwriter')
df.to_excel(writer, 'Sheet1')
writer.save()

print(str(fail_count))