from builtins import open
import glob, os

client_id = '6ff8da2ae4d057a6d048'  # you have to write your own id
client_secret = '3b6868e71ae5ef6d14a5d8114a3638e84bc22c7a'  # you have to write your own secret
id_secret = '?client_id=6ff8da2ae4d057a6d048&client_secret=3b6868e71ae5ef6d14a5d8114a3638e84bc22c7a'
os.chdir("/File Structure")
sentences = []
last = []
count = 0


def sentence_formatter(line):
    line = line.replace("/", " ")
    line = line.replace(".", "")
    line = line.replace("_", "")
    line = line.replace("-", "")
    return line


def sentence_parser(text):
    sentence_list = []
    for each_sentence in text:
        print(sentence_formatter(each_sentence))
        sentence_list.append(sentence_formatter(each_sentence))
    return sentence_list


for file in glob.glob("*.txt"):
    try:
        f = open(file, "r", encoding="utf-8")
        contents = f.readlines()
        sentences.append(sentence_parser(contents))
        count += 1
    except:
        continue
    if count == 1:
        break

for x in sentences:
    print(x)
