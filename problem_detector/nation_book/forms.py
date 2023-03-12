from django import forms
from . models import ProblemStatement,ProblemComments

class ProblemStatementForm(forms.ModelForm):
    class Meta:
        model=ProblemStatement
        fields=['problem_name','problem_desc','problem_img']

class ProblemCommentsForm(forms.ModelForm):
    class Meta:
        model=ProblemComments
        fields=['body']