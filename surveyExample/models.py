
from django.conf import settings
from django.db import models
from django.utils import timezone



class Survey(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    survey_image = models.TextField(default="Null")

    def __str__(self):
        return self.title + " - " + str(self.pk)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Surveyquestion(models.Model):
    question = models.TextField()
    survey = models.ManyToManyField(Survey)
    question_image = models.TextField()

    def __str__(self):
        return self.question + " - " + str(self.pk)


class Option(models.Model):
    question = models.ForeignKey(Surveyquestion,on_delete=models.CASCADE)
    option_image = models.TextField(default="Null")
    option = models.TextField()

class Surviver(models.Model):
    Company = models.CharField(max_length=200, null= False)
    Position = models.CharField(max_length=200, null= False)
    def __int__(self):
        return Surviver.pk

class answer(models.Model):
    survey_id = models.ForeignKey(Survey,on_delete=models.CASCADE)
    surviver_id = models.ForeignKey(Surviver, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Surveyquestion,on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, null=False)



