from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from paddlenlp import Taskflow
import torch
from transformers import BertTokenizer, BertModel
from django.http import JsonResponse
import json

print("import done...")

def calculate_cosine_similarity(text1, text2):
    # 加载预训练的BERT模型和tokenizer
    model = BertModel.from_pretrained('bert-base-chinese')
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
    # 保存
    # model.save_pretrained("./bert-base-chinese")
    # tokenizer.save_pretrained("./bert-base-chinese")
    # model = BertModel.from_pretrained('./bert-base-chinese')
    # tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
    # 对文本进行tokenize和编码
    encoded_text1 = tokenizer.encode(text1, add_special_tokens=False)
    encoded_text2 = tokenizer.encode(text2, add_special_tokens=False)
    # 将编码后的文本转换为PyTorch tensor，并添加一个维度表示batch_size
    input_ids1 = torch.tensor([encoded_text1])
    input_ids2 = torch.tensor([encoded_text2])
    # 使用BERT模型将文本转换为向量
    with torch.no_grad():
        outputs1 = model(input_ids1)
        outputs2 = model(input_ids2)
    # 取出向量中的CLS token表示整个句子的向量表示
    vector1 = outputs1[0][0][0]
    vector2 = outputs2[0][0][0]
    # 计算两个向量的余弦相似度
    cosine_similarity = torch.dot(vector1, vector2) / (torch.norm(vector1) * torch.norm(vector2))
    return cosine_similarity.item()

words=[
    ["爹","父"],
    ["爸爸","妈妈"],
    ["爸爸","父亲"],
    ["士","兵"],
    ["冷","热"],
    ["冷","凉"], 
]

for i in range(words.__len__()):
    print("%s 和 %s 的相似度是：%f" % (words[i][0], words[i][1], calculate_cosine_similarity(words[i][0], words[i][1])))
    
# print("%s 和 %s 的相似度是：%f" % (words[0][0], words[0][1], calculate_cosine_similarity(words[0][0], words[0][1])))