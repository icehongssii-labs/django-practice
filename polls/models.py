from django.db import models

# Create your models here.

class Questions(models.Model):
    pass 
    # 질문
    question_text = models.CharField(max_length=200)
    # 질문 생성 시각
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text    
    
    
class Choices(models.Model):
    pass
    # pk 
    # 초이스내용
    choice_text = models.CharField(max_length=200)
    # 질문 id 
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    # 투표수
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    