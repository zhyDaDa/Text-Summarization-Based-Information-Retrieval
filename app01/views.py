print("\033[3;37;44mLoading imports...\033[0m", end="")
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from paddlenlp import Taskflow
import torch
from transformers import BertTokenizer, BertModel
from django.http import JsonResponse
import json
import re
from zhipuai import ZhipuAI

print("\033[1;33;40mDone!\033[0m\n")

# 实体加载
print("\033[3;33;44mLoading bert model...\033[0m", end="")
model = BertModel.from_pretrained("./bert-base-chinese")
tokenizer = BertTokenizer.from_pretrained("./bert-base-chinese")
print("\033[1;33;40mDone!\033[0m\n")


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "login.html")  # 返回HTML页面。
    elif request.method == "POST":  # 前端如果是post请求
        username = request.POST.get(
            "username"
        )  # 获取POST请求中的username值,字符串username要和前端form表单中的对应起来。
        password = request.POST.get(
            "password"
        )  # 获取POST请求中的password值，字符串password要和前端form表单中的对应起来。
        # request.POST.get返回的值是字符串，所以下面if中的判断是成立的。
        conn = connection.cursor()
        conn.execute(
            "SELECT * FROM user WHERE user_id = %s AND user_password = %s",
            [username, password],
        )
        row = conn.fetchone()
        conn.close()
        if row:
            return render(request, "index.html")
        else:  # 如果用户名或者密码错误，返回登录页面
            return render(request, "login.html")


def index(request):
    print("views.py | \033[0;36;47m index\033[0m >>> Get request: ", request)
    return render(request, "index.html")


@csrf_exempt
def upload(request):
    print("views.py | \033[0;36;47m upload\033[0m >>> Get request: ", request)
    if request.method == "GET":  # 前端如果是get请求
        print("nm")
        return render(request, "upload.html")  # 返回HTML页面。
    elif request.method == "POST":  # 前端如果是post请求
        id = request.POST.get("id")
        content = request.POST.get("content")
        result = request.POST.get("result")
        date = request.POST.get("date")
        history=request.POST.get("history")
        allergy=request.POST.get("allergy")
        examination=request.POST.get("examination")
        mediacal=request.POST.get("mediacal")
        notes=request.POST.get("notes")
        gender=request.POST.get("gender")
        # extract=extract_byGLM4(content)
        username = 1001
        print(id, date, content, result, extract)
        # request.POST.get返回的值是字符串，所以下面if中的判断是成立的。
        conn = connection.cursor()
        conn.execute(
            "INSERT INTO test3 (id,question_content,patient_history,patient_allergy,patient_examination,patient_medical,patient_gender,notes,answer_content,question_extraction,date,user_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                id,
                content,
                history,
                allergy,
                examination,
                mediacal,
                gender,
                notes,
                result,
                extract,
                date,
                username,
            ),
        )
        conn.close()
        return render(request, "upload.html")
        return render(request, "upload.html")
            


def select(request):
    print("views.py | \033[0;36;47m select\033[0m >>> Get request: ", request)
    # 搜索之后调用该函数
    # if request.method == "POST":
    if True:
        searchText = request.POST.get("select")
        print("\033[0;36;47mselect\033[0m >>> Fetch searchText: ", searchText)  
        # TODO: 后续要在这里接受前端的筛选条件并写出相应的SQL语句
        conn = connection.cursor()
        conn.execute("SELECT  id ,question_content ,answer_content, user_id  FROM  test  ORDER BY RAND(); ")
        select = conn.fetchall()
        conn.close()
        return render(request,"select.html",{'select': select})
        post_list = find_max_similarity_rows(searchText)
        # print(post_list)
        return render(
            request, "select.html", {"post_list": post_list, "searchText": searchText}
        )
    else:
        return render(request, "select.html")


@csrf_exempt
def extract(request):
    print("views.py | \033[0;36;47m extract\033[0m >>> Fetch sentence: ", request)
    if request.method == "POST":
        sentence = request.POST.get("sentence")  # 获取前端页面输入的句子
        extracted_entities = extract_byGLM4(sentence)
        # 构造包含实体类型和实体值的对象列表
        extracted_entities_list = []
        for k, v in extracted_entities.items():
            extracted_entities_list.append({"type": k, "value": v})

        # 将抽取结果传递给前端页面进行渲染
        return render(
            request,
            "extract.html",
            {"extracted_entities": extracted_entities_list, "sentence": sentence},
        )
    else:
        return render(request, "extract.html")


def scan(request):
    print("views.py | \033[0;36;47m scan\033[0m >>> Fetch sentence: ", request)
    conn = connection.cursor()
    conn.execute(
        "SELECT  id ,question_content ,answer_content  FROM  test1  ORDER BY RAND() LIMIT 10; "
    )
    scan = conn.fetchall()
    conn.close()
    return render(request, "scan.html", {"scan": scan})


def user(request):
    conn = connection.cursor()
    conn.execute("SELECT  id ,question_content ,answer_content  FROM  test1")
    scan = conn.fetchall()
    conn.execute(
        "SELECT  test1.id ,question_content ,answer_content  FROM  test1,collect where test1.id=collect.medical_id"
    )
    scan1 = conn.fetchall()
    conn.close()
    return render(request, "user.html", {"scan": scan, "scan1": scan1})


def extract_byGLM4(text):
    """
    通过GLM-4模型抽取信息

    :param text: 输入的文本
    :return: 抽取出的信息(字典形式)
    """
    client = ZhipuAI(
        api_key="e380b61b65e101c22d2f89e7ab8cde34.jlpqhJVQyYIkHtzH"
    )  # 填写您自己的APIKey
    # 设计prompt
    prompt = """
        你是一个信息抽取模型，你需要从句子中抽取出['年龄', '性别', '身体部位', '症状', '疾病']这些信息。
        特别注意! 如果没有明确信息, 请填写"_"。
        
        输入：四岁小孩的头感到十分疼痛，之前患过脑震荡
        输出: 年龄：4岁；性别：_；身体部位；头，症状：疼痛；疾病：脑震荡
        输入：伍拾柒岁患者抱怨左腿肿胀、红斑，伴有持续发热和剧烈疼痛。她之前曾被诊断为类风湿关节炎。
        输出：年龄：57岁；性别：女；身体部位：左腿，症状：疼痛、红斑、肿胀、发热；疾病：类风湿关节炎
        输入：儿子 ④岁检查出右脑室有脑积水
        输出：年龄：4岁；性别：男；身体部位：右脑室，症状：_；疾病：脑积水
        输入：
    """
    while True:
        # 调用模型
        message = [{"role": "user", "content": prompt + text}]
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=message,
        )
        response = response.choices[0].message.content

        regex = r"年龄：(.+?)；性别：(.+?)；身体部位：(.+?)，症状：(.+?)；疾病：(.+)"
        response = re.findall(regex, response)
        info_names = ["年龄", "性别", "身体部位", "症状", "疾病"]
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
    """合并GLM-4模型的输出为一个字符串"""
    mergeString = ""
    for k, v in outputObj.items():
        mergeString += k + "：" + v + "；"
    return mergeString[:-1]


def calculate_cosine_similarity(text1, text2):
    print(
        "views.py | \033[0;36;47m calculate_cosine_similarity\033[0m >>> Fetch text1: %s, text2: %s"
        % (text1, text2)
    )
    # 加载预训练的BERT模型和tokenizer
    global model, tokenizer
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
    cosine_similarity = torch.dot(vector1, vector2) / (
        torch.norm(vector1) * torch.norm(vector2)
    )
    return cosine_similarity.item()


def find_max_similarity_rows(text):
    print(
        "views.py | \033[0;36;47m find_max_similarity_rows\033[0m >>> Fetch text: ",
        text,
    )
    itemsCount = 4
    # 连接MySQL数据库
    print("\033[3;33;44mConnecting MySQL database...\033[0m", end="")
    mycursor = connection.cursor()
    print("\033[1;33;40mDone!\033[0m\n")
    # 由大模型抽取结果
    result = extract_byGLM4(text)
    # 查询 test 表中的所有数据
    mycursor.execute(
        "SELECT id, question_content, question_extraction,answer_content FROM test1"
    )
    # 定义变量来保存相似度最高的四个问题的数据
    max_similarity_rows = []
    max_similarity_values = [0.0] * itemsCount
    # 逐条计算相似度
    for row in mycursor:
        # 提取问题内容和问题提取字段的文本
        question_extraction = row[2]
        # 计算余弦相似度
        similarity = calculate_cosine_similarity(
            mergeGLM4Output(result), question_extraction
        )
        # 如果相似度比其中的一个元素更大，就更新这个元素和对应的行数据
        for i in range(itemsCount):
            if similarity > max_similarity_values[i]:
                max_similarity_rows.insert(i, row)
                max_similarity_values.insert(i, similarity)
                max_similarity_rows = max_similarity_rows[:4]
                max_similarity_values = max_similarity_values[:4]
                break
    # 关闭数据库连接
    mycursor.close()
    # 返回相似度最高的四个问题的数据
    return max_similarity_rows


def collect(request):
    if request.method == "POST":
        data = json.loads(request.body)
        record_id = data.get("recordId")

        # 在这里执行插入收藏数据的操作，将record_id插入collect表中的id
        mycursor = connection.cursor()

        # 查询 test 表中的所有数据
        mycursor.execute(
            "INSERT INTO collect (medical_id,user_id) VALUES (%s,1001)", [record_id]
        )
        mycursor.close()
        # 假设插入成功，返回收藏成功的响应
        return JsonResponse({"message": "收藏成功"})


def delete(request):
    if request.method == "POST":
        data = json.loads(request.body)
        record_id = data.get("recordId")

        # 在这里执行插入收藏数据的操作，将record_id插入collect表中的id
        mycursor = connection.cursor()

        # 查询 test 表中的所有数据
        mycursor.execute("delete from collect where medical_id=%s", [record_id])
        mycursor.close()
        # 假设插入成功，返回收藏成功的响应
        return JsonResponse({"message": "删除成功"})


def delete1(request):
    if request.method == "POST":
        data = json.loads(request.body)
        record_id = data.get("recordId")
        mycursor = connection.cursor()
        # 查询 test 表中的所有数据
        mycursor.execute("delete from test2 where id=%s", [record_id])
        mycursor.close()
        # 假设插入成功，返回收藏成功的响应
        return JsonResponse({"message": "删除成功"})


def faqpage(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "faqpage.html")  # 返回HTML页面。。


def lock(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "lock.html")  # 返回HTML页面。


def userEdit(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "userEdit.html")  # 返回HTML页面。


def calendar(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "calendar.html")  # 返回HTML页面。


def recoverpw(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "recoverpw.html")  # 返回HTML页面。


def pagesconfirmmail(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "pagesconfirmmail.html")


def chat(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "chat.html")  # 返回HTML页面。


def doctorlist(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "doctorlist.html")  # 返回HTML页面。


def forum(request):
    if request.method == "GET":  # 前端如果是get请求
        return render(request, "forum.html")  # 返回HTML页面。
