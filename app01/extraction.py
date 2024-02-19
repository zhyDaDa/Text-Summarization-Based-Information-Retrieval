# from paddlenlp import Taskflow

# def extract_information(text):
#     schema = ['年龄', '性别', '身体部位', '症状', '疾病']
#     my_ie = Taskflow("information_extraction", schema=schema, taskpath="./checkpoint/model_best")
#     data = my_ie(text)
#     result = ""
#     for d in data:
#         for k, v in d.items():
#             result += k + "："
#             for item in v:
#                 result += item['text'] + "，"
#             result = result[:-1] + "；"  # 去掉最后一个逗号，加上分号
#     result = result[:-1]  # 去掉最后一个分号
#     return result


import re
from zhipuai import ZhipuAI


def extract_information(text):
    client = ZhipuAI(api_key="c198388676d36d397ab90659cfcbe7de.VOh7XShjotaMj1C2")  # 填写您自己的APIKey
    # 设计prompt
    prompt = """
        你是一个信息抽取模型，你需要从句子中抽取出['年龄', '性别', '身体部位', '症状', '疾病']这些信息。
        特别注意! 如果没有明确信息, 请填写"_"。
        
        输入：四岁小孩的头感到十分疼痛，之前患过脑震荡
        输出: 年龄：四岁；性别：_；身体部位；头，症状：疼痛；疾病：脑震荡
        输入：50 岁患者抱怨左腿肿胀、红斑，伴有持续发热和剧烈疼痛。她之前曾被诊断为类风湿关节炎。
        输出：年龄：50岁；性别：女；身体部位：左腿，症状：疼痛、红斑、肿胀、发热；疾病：类风湿关节炎
        输入：儿子 4 岁检查出右脑室有脑积水
        输出：年龄：4岁；性别：男；身体部位：右脑室，症状：_；疾病：脑积水
        输入：
    """
    while True:
        # 调用模型
        message = [{"role": "user", "content": prompt+text}]
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=message,
        )
        response = response.choices[0].message.content
        
        regex = r"年龄：(.+?)；性别：(.+?)；身体部位：(.+?)，症状：(.+?)；疾病：(.+)"
        response = re.findall(regex, response)
        info_names = ['年龄', '性别', '身体部位', '症状', '疾病']
        if len(response) < 1:
            continue
        ret = {}
        for i in range(len(info_names)):
            if response[0][i].strip() == "_":
                continue
            ret[info_names[i]] = response[0][i].strip()
        break
    return ret
        
def mergeGLM4Output(outputObj):
    mergeString = ""
    for (k, v) in outputObj.items():
        mergeString += k + "：" + v + "；"
    return mergeString[:-1]

text = "一位 26 岁女生怀孕两月后左边臀部总抽筋。"
# print(extract_information(text))
print(mergeGLM4Output(extract_information(text)))