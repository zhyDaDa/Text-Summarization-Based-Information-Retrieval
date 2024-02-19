from paddlenlp import Taskflow

def extract_information(text):
    schema = ['年龄', '性别', '身体部位', '症状', '疾病']
    my_ie = Taskflow("information_extraction", schema=schema,)
    data = my_ie(text)
    result = ""
    for d in data:
        for k, v in d.items():
            result += k + "："
            for item in v:
                result += item['text'] + "，"
            result = result[:-1] + "；"  # 去掉最后一个逗号，加上分号
    result = result[:-1]  # 去掉最后一个分号
    return result

text = "四岁小男孩的头感到十分疼痛，之前患过脑震荡"
print(extract_information(text))
