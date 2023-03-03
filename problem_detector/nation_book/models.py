from django.db import models

class ProblemStatement(models.Model):
    problem_name = models.CharField(max_length=200)
    problem_desc = models.CharField(max_length=500)
    problem_img=models.ImageField(upload_to='problem_img',blank=True)
    problem_id=models.IntegerField(default=0)
    
    def __str__(self):
        return self.problem_name