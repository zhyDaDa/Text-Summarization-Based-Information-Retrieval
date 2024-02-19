from django.db import models
class User(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_position = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'
        managed = True  # 将模型映射到现有表，不创建新表

class medical(models.Model):
    question_content = models.CharField(max_length=255)
    answer_content = models.CharField(max_length=50)
    question_extraction = models.CharField(max_length=50)
    user_id= models.CharField(max_length=50)
    class Meta:
        db_table = 'test'
        managed = True  # 将模型映射到现有表，不创建新表