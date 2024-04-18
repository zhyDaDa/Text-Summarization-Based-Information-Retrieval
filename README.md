# 部署项目

- [部署项目](#部署项目)
  - [windows环境](#windows环境)
    - [第一次拉取后的初始化操作](#第一次拉取后的初始化操作)
      - [安装node\_module](#安装node_module)
      - [python依赖](#python依赖)
      - [测试bert-base-chinese](#测试bert-base-chinese)
    - [启动系统](#启动系统)
  - [linux服务器环境](#linux服务器环境)
    - [vscode远程连接](#vscode远程连接)
    - [令人舒适的小妙招](#令人舒适的小妙招)
    - [删除并更新mySQL](#删除并更新mysql)
  - [uwsgi](#uwsgi)
    - [指令大全](#指令大全)
  - [nodeBB](#nodebb)
  - [MongoDB](#mongodb)
    - [指令](#指令)
    - [trouble-shoot](#trouble-shoot)
    - [mongosh内配置](#mongosh内配置)

>>>>>>> htmlchange

## windows环境

### 第一次拉取后的初始化操作

  1. 先node_module安装
  2. 安装python依赖
  3. 测试bert-base-chinese模型是否正常工作

#### 安装node_module

从文件夹根目录下执行cmd, 输入下面的命令

```bash
npm install
```

#### python依赖

在根目录下执行cmd, 输入下面的命令

```bash
pip install -r requirements.txt
```

#### 测试bert-base-chinese

在`test/bert计算相似度.py`中可以测试模型是否能正常使用  
模型会从`huggingface`中下载并保存到`cache`中, 所以第一次很慢是正常的(大约300M)  
如果希望一直从本地加载模型, 可以将以下代码:

```python
### 加载预训练的BERT模型和tokenizer
model = BertModel.from_pretrained('bert-base-chinese')
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
### 保存
### model.save_pretrained("./bert-base-chinese")
### tokenizer.save_pretrained("./bert-base-chinese")
### model = BertModel.from_pretrained('./bert-base-chinese')
### tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
```

调整为:

```python
### 加载预训练的BERT模型和tokenizer
model = BertModel.from_pretrained('bert-base-chinese')
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
### 保存
model.save_pretrained("./bert-base-chinese")
tokenizer.save_pretrained("./bert-base-chinese")
### model = BertModel.from_pretrained('./bert-base-chinese')
### tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
```

运行一次代码, 这样下载好的模型会被保存在`bert-base-chinese`中  
之后, 再修改代码为:

```python
### 加载预训练的BERT模型和tokenizer
### model = BertModel.from_pretrained('bert-base-chinese')
### tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
### 保存
### model.save_pretrained("./bert-base-chinese")
### tokenizer.save_pretrained("./bert-base-chinese")
model = BertModel.from_pretrained('./bert-base-chinese')
tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
```

就可以直接从本地加载模型了
> 在业务代码中统一从网络加载模型, 免去不必要的麻烦

### 启动系统

  1. 连接到数据库(建议使用`Navicat`, 打开数据库即可)
  2. 运行`py manage.py runserver`启动Django服务器
  3. 等待终端出现提示: `Starting development server at http://127.0.0.1:8000/`后, 打开浏览器, 访问该网址即可

> 注意, 使用虚拟环境后, 虽然安装了*Django*, 但是直接运行上述指令很可能调用的是全局的*py*  
> 如果你的全局*py*没有安装*Django*或者安装了不同版本的*Django*, 就会出现形如:"ImportError: Couldn't import Django. Are you sure ..."的报错  
> 解决方法: 直接填写虚拟环境中的python地址来运行, 例如: `"D:\python\python.exe" manage.py runserver`  
> > 笔者贴心的为你准备了一个`runserver.bat`, 双击即可运行!
> (假定你的虚拟环境名称是`venv`)

## linux服务器环境

### vscode远程连接

1. 打开vscode, 安装`Remote - SSH`插件
2. 点击左下角的`><`图标, 选择`Remote-SSH: Connect to Host...`
3. 输入服务器地址(例如: `root@服务器公网地址`), 点击`Enter`
4. 第一次会确认是否信任该主机, 输入`yes`确认
5. 连接成功后输入密码
6. 建立连接后, 可以在vscode中直接操作服务器了

### 令人舒适的小妙招

1. 不用再输入密码  
  将自己电脑上的公钥(.pub)复制到服务器的`~/.ssh/authorized_keys`中, 以后就不用输入密码了

2. 检查更新  
  第一时间检查mySQL, python 之类的版本信息, 及时更新可以大幅避免之后重装的麻烦

3. 舒心的linux命令行输出  
  在`.bashrc`的最后加入`export PS1="\033[47m\w\033[0m~\033[41m$\033[0m "`  
  能让输出变得美观

### 删除并更新mySQL

删除:  

```bash
sudo systemctl stop mysql
sudo apt remove mysql-server-8.0
sudo apt autoremove
sudo rm -rf /var/lib/mysql
sudo rm -rf /etc/mysql/
sudo find / -name "*mysql*" 2>/dev/null
```

安装:

```bash
sudo apt-get clean
sudo apt-get purge 'mysql*'
sudo apt-get update
sudo apt-get install -f
sudo apt-get install mysql-server-8.0
sudo apt-get dist-upgrade
```

重设密码(**本人亲测有效**):
> 我的版本是: `mysql  Ver 8.0.36-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))`

先获取当前生成的随机账号和密码

```bash
sudo cat /etc/mysql/debian.cnf
```

> 注意这个是mysql的基准, 这里的socket是正确的  
> 如果出现报错`ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)`  
> 那么把`/etc/my.cnf`这里的错误的socket改成正确的socket

使用随机账号和密码登录

```bash
mysql -u root -p
```

输入密码后, 使用以下命令修改密码

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '00000000';
FLUSH PRIVILEGES;
```

## uwsgi

### 指令大全

|       作用       |              指令              |
| :--------------: | :----------------------------: |
| 启动指定配置文件 |    `uwsgi --ini uwsgi.ini`     |
|     查看进程     |     `ps aux\|grep uwsgi`     |
|     结束进程     |         `kill -9 PID`          |
|  重启uwsgi服务   |   `uwsgi --reload uwsgi.pid`   |
|      杀端口      |    `sudo fuser -k 8002/tcp`    |
| 重启nginx服务端  | `sudo systemctl restart nginx` |

## nodeBB

配置参考 [官方文档](https://docs.nodebb.org/installing/os/ubuntu/)

## MongoDB

### 指令

|     作用     |              指令              |
| :----------: | :----------------------------: |
|     启动     | `sudo systemctl start mongod`  |
| 查看运行状态 | `sudo systemctl status mongod` |

### trouble-shoot

> Process: 23613 ExecStart=/usr/bin/mongod --config /etc/mongod.conf (code=exited, status=14)这句话搜到了解决方法

```bash
sudo chown -R mongodb:mongodb /var/lib/mongodb
sudo chown mongodb:mongodb /tmp/mongodb-27017.sock    
sudo service mongod restart
```

### mongosh内配置

```bash
use admin
db.createUser( { user: "admin", pwd: "00000000", roles: [ { role: "root", db: "admin" } ] } )
use nodebb
db.createUser( { user: "nodebb", pwd: "00000000", roles: [ { role: "readWrite", db: "nodebb" }, { role: "clusterMonitor", db: "admin" } ] } )
quit()
```
