import re

response = "输出：年龄：26岁；性别：女；身体部位：左边臀部，症状：抽筋；疾病：无"

regex = r"年龄：(.+?)；性别：(.+?)；身体部位：(.+?)，症状：(.+?)；疾病：(.+)"
response = re.findall(regex, response)
info_names = ['年龄', '性别', '身体部位', '症状', '疾病']
ret = {}
for i in range(len(info_names)):
    ret[info_names[i]] = response[0][i]
    
# merge
mergeString = ""
for (k, v) in ret.items():
    mergeString += k + "：" + v + "；"
mergeString = mergeString[:-1]
print(mergeString)