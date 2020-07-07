from builtins import len, open
from locale import str
import requests
import json
import pandas as pd
import time

client_id = '6ff8da2ae4d057a6d048'  # you have to write your own id
client_secret = '3b6868e71ae5ef6d14a5d8114a3638e84bc22c7a'  # you have to write your own secret


def dict_creator(user_name, repo_name):
    df1 = pd.DataFrame(
        columns=['Name of repository', 'url', 'Frontend', 'Backend', 'Front/Backend', 'Angular', 'React',
                 'Vue', 'Ruby', 'TypeScript', 'JavaScript', 'Java', 'PHP', 'Python', 'MongoDB', 'MySql',
                 'PostgreSql'])

    dict1 = {'Name of repository': '', 'url': '', 'Frontend': '', 'Backend': '', 'Front/Backend': '', 'Angular': '',
             'React': '', 'Vue': '', 'Ruby': '', 'TypeScript': '', 'JavaScript': '', 'Java': '', 'PHP': '',
             'Python': '', 'MongoDB': '', 'MySql': '', 'PostgreSql': ''}
    try:
        link = 'https://raw.githubusercontent.com/' + user_name + '/' + repo_name + \
               '/master/package.json?client_id=' + client_id + '&client_secret=' + client_secret
        page = requests.get(link)

        if page.status_code != 404:
            dict1['Frontend'] = 'X'
            dict1['Name of repository'] = repo_name
            dict1['url'] = 'https://api.github.com/repos/' + user_name + '/' + repo_name
            dict1['PHP'] = 'X'
            series = pd.Series(dict1)
            series.to_frame()
            df1 = df1.append(series, ignore_index=True)
    except:
      print('error')




    return df1


data = pd.DataFrame(
    columns=['Name of repository', 'url', 'Frontend', 'Backend', 'Front/Backend', 'Angular', 'React',
             'Vue', 'Ruby', 'TypeScript', 'JavaScript', 'Java', 'PHP', 'Python', 'MongoDB', 'MySql',
             'PostgreSql'])

df = pd.DataFrame({'Name of repository': [], 'url': [], 'Frontend': [], 'Backend': [], 'Front/Backend': [],
                   'Angular': [], 'React': [], 'Vue': [], 'Ruby': [], 'TypeScript': [], 'JavaScript': [], 'Java': [],
                   'PHP': [], 'Python': [], 'MongoDB': [], 'MySql': [], 'PostgreSql': []})

with open('Json files/PHP projects/(2017-01-01--2020-06-30).json') as json_file:
    users = json.load(json_file)

count = 0
index = 0

for each_user in users:
        df = df.append(dict_creator(each_user['owner_name'], each_user['repo_name']))
        count += 1
        index += 1
        print('Projects of user ' + each_user['owner_name'] + ' are ready. Added project count: ' + str(count) + '. ' +
              str(len(users) - index) + ' users left.')


writer = pd.ExcelWriter('FormattedData(PHP).xlsx', engine='xlsxwriter')
df.to_excel(writer, 'Sheet1')
writer.save()

