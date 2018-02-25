import csv
#find all post id which contains Ubuntu as tag
with open("question_tags.csv",newline='') as all_tags:
    tags = csv.reader(all_tags, delimiter=',')
    id_set =set()
    for row in tags:
        if 'ubuntu' in row[1] or 'Ubuntu' in row[1]:
            id_set.add(row[0])

#from Post ID find other words tagged together with Ubuntu
with open("question_tags.csv", newline='') as all_tags:
    tags = csv.reader(all_tags, delimiter=',')
    tag_dict ={}
    for row in tags:
        if row[0] in id_set:
            if not tag_dict.get(row[0]):
                tag_dict[row[0]] = [row[1]]
            else:
                tag_dict[row[0]].append(row[1])



#get all tags and put in a list/set
tags_set = set()
for k, v in tag_dict.items():
    for x in v:
        tags_set.add(x)

print(tags_set)

with open('tags.txt' , 'w') as tags:
    for item in tags_set:
        tags.write("{}\n".format(item))






