from django.contrib import admin
from .models import ProblemStatement,SmallProblems,ProblemComments
# Register your models here.

admin.site.register(ProblemStatement)
admin.site.register(SmallProblems)
admin.site.register(ProblemComments)