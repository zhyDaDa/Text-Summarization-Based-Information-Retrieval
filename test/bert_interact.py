# import os
# import paddle
#
# # 指定模型文件所在的文件夹
# model_folder = "D:/Coding/Projects/Text Summarization-based Information Retrieval/GraduateSystem/app01/checkpoint/model_best/static"
#
# # 加载模型
# model_path = os.path.join(model_folder, "inference.pdmodel")
# params_path = os.path.join(model_folder, "inference.pdparams")
# ernie_model = paddle.load_model(model_path, params_path)
#
#
# # 使用模型进行预测
# def interact(prompt):
#     # 对输入文本进行分词
#     input_ids = ernie_model.tokenizer.encode(prompt)
#
#     # 使用模型进行预测
#     outputs = ernie_model(input_ids)
#
#     # 获取预测结果
#     response = ernie_model.tokenizer.decode(outputs[0], skip_special_tokens=True)
#
#     return response
#
#
# # 示例：在控制台与 ERNIE 模型进行交互
# while True:
#     user_input = input("您：")
#     if user_input.lower() == "退出":
#         break
#     response = interact(user_input)
#     print("ERNIE:", response)

# 学长原先的测试, 但是缺少tokenizer2加载时缺少两样东西

from paddlenlp.transformers import ErnieModel
from paddlenlp.transformers import ErnieTinyTokenizer

# ernie_tiny_dir = "./app01/checkpoint/model_best/static"
ernie_tiny_dir = "./app01/checkpoint/model_best"
ernie_tiny = ErnieModel.from_pretrained(ernie_tiny_dir)
target_dir = "./app01/checkpoint/model_best"
# target_dir = "./app01/checkpoint/model_best/static"
tokenizer2 = ErnieTinyTokenizer.from_pretrained(target_dir)


# 使用模型进行预测
def interact(prompt):
    # 对输入文本进行分词
    input_ids = tokenizer2.encode(prompt)

    # 使用模型进行预测
    outputs = ernie_tiny(input_ids)

    # 获取预测结果
    response = ernie_tiny.tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response


# 示例：在控制台与 ERNIE 模型进行交互
while True:
    user_input = input("您：")
    if user_input.lower() == "退出":
        break
    response = interact(user_input)
    print("ERNIE:", response)
