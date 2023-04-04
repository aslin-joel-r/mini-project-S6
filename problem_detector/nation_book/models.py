from django.db import models

class ProblemStatement(models.Model):
    problem_name = models.CharField(max_length=200)
    problem_desc = models.CharField(max_length=500)
    problem_img=models.ImageField(upload_to='problem_img')
    problem_id=models.IntegerField(default=0)

    
    def __str__(self):
        return self.problem_name

class ProblemComments(models.Model):
    body=models.TextField(default='')
    time=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(ProblemStatement,on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.body
    
class SmallProblems(models.Model):
    body=models.TextField(default='')
    time=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(ProblemStatement,on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.body


