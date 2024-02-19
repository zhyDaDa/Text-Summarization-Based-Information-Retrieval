# 第一次拉取后的初始化操作
  1. 先node_module安装
  2. 安装python依赖
  3. 测试bert-base-chinese模型是否正常工作

## 安装node_module
从文件夹根目录下执行cmd, 输入下面的命令
```bash
npm install
```

## 测试bert-base-chinese
在`test/bert计算相似度.py`中可以测试模型是否能正常使用  
模型会从`huggingface`中下载并保存到`cache`中, 所以第一次很慢是正常的(大约300M)  
如果希望一直从本地加载模型, 可以将以下代码:
```python
# 加载预训练的BERT模型和tokenizer
model = BertModel.from_pretrained('bert-base-chinese')
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
# 保存
# model.save_pretrained("./bert-base-chinese")
# tokenizer.save_pretrained("./bert-base-chinese")
# model = BertModel.from_pretrained('./bert-base-chinese')
# tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
```
调整为:
```python
# 加载预训练的BERT模型和tokenizer
model = BertModel.from_pretrained('bert-base-chinese')
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
# 保存
model.save_pretrained("./bert-base-chinese")
tokenizer.save_pretrained("./bert-base-chinese")
# model = BertModel.from_pretrained('./bert-base-chinese')
# tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
```
运行一次代码, 这样下载好的模型会被保存在`bert-base-chinese`中  
之后, 再修改代码为:
```python
# 加载预训练的BERT模型和tokenizer
# model = BertModel.from_pretrained('bert-base-chinese')
# tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
# 保存
# model.save_pretrained("./bert-base-chinese")
# tokenizer.save_pretrained("./bert-base-chinese")
model = BertModel.from_pretrained('./bert-base-chinese')
tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
``` 
就可以直接从本地加载模型了
> 在业务代码中统一从网络加载模型, 免去不必要的麻烦