from django.db import models

# Create your models here.
class studentModel(models.Model):
    stu_id = models.CharField(max_length=30,null=True)
    stu_name = models.CharField(max_length=20,null=True)
    department = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f'{self.stu_name}'
