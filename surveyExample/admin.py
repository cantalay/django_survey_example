from django.contrib import admin

# Register your models here.
from surveyExample.models import Survey, Surveyquestion,Surviver,answer,Option

admin.site.register(Survey)
admin.site.register(Surveyquestion)
admin.site.register(Surviver)
admin.site.register(answer)
admin.site.register(Option)