import csv
import codecs

filepath = '/Users/rild/Downloads/android_game/FlixelRL-master/assets/data/'
filename = 'achievement.csv'

# ['id', 'name', 'type', 'param0', 'param1', 'param2', 'cond']
# row にはこんな感じのデータが入っていた

# type(row)
# >>> <class 'list'>

with open(filepath + filename, newline=''):
    reader = csv.reader(codecs.open(filepath + filename, 'rb', 'utf-8'))
    for row in reader:
        index, name, tag = row[0], row[1], row[2]
        print(index + name + tag)

