from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Surveyquestion,Survey,Survpiver,answer, Option
from django.core.files.storage import FileSystemStorage



def index(request):
    form = AuthenticationForm()
    post = Survey()
    if request.user.is_authenticated:
        return render(request, 'index.html',{'form': form})
    if request.POST.get('make_survey'):
        return  render(request, 'makeSurvey.html', {'form': form})
    else:
        return HttpResponse("<h1>Please Check your permission or Login</h1>")

def makeSurvey(request):
    post = Survey()
    posts = Survey.objects.all()

    if request.POST.get('survey_title'):
        print("Im in create survey")
        post.title = request.POST.get('survey_title')
        post.author = request.user
        try:
            survey_image = request.FILES['survey_image']
            fs = FileSystemStorage()
            s_image = fs.save(survey_image.name, survey_image)
            post.survey_image = fs.url(s_image)
        except:
            print("No Survey Image")

        post.save()
        return redirect('makeQuestion', pk=post.pk)
    return render(request, 'makeSurvey.html', {'post': posts})

def makeQuestion(request,pk):
    survey_question = Surveyquestion.objects.all()
    survey_object = Survey.objects.get(pk=pk)
    if request.POST.get('pk'):#if we add from db to our new survey to question
        dbQuestion = Surveyquestion.objects.get(pk=request.POST.get('pk'))
        print(dbQuestion)
        dbQuestion.survey.add(Survey.objects.get(pk=pk))

    if request.POST.get('survey_question'):
        try:
            question_image = request.FILES['question_image']
            fs = FileSystemStorage()
            q_image = fs.save(question_image.name, question_image)
            post = survey_object.surveyquestion_set.create\
                (question=request.POST.get('survey_question'), question_image=fs.url(q_image))
        except:
            post = survey_object.surveyquestion_set.create\
                (question=request.POST.get('survey_question'))
            print("No question Image")

        i = 1
        for i in range(11):
            optiontext = 'option' + str(i)
            if request.POST.get(optiontext)!= None:
                try:
                    option_image = request.FILES['option_image' + str(i)]
                    fs = FileSystemStorage()
                    o_image = fs.save(option_image.name, option_image)
                    post.option_set.create(option=request.POST.get('option' + str(i)), option_image=fs.url(o_image))
                except:
                    post.option_set.create(option=request.POST.get('option' + str(i)))
                    print("No Question Image")

    return render(request,'makeQuestion.html',{'survey_question': survey_question, 'survey_object': survey_object})

def allSurvey(request):
    survey_object = Survey.objects.all()
    if request.POST.get('survey_id'):
        print(request.POST.get('survey_id'))
        question_object = survey_object.get(pk=request.POST.get('survey_id'))

        return render(request, 'allSurvey.html', {'survey': survey_object, 'question': question_object.surveyquestion_set.all()})

    return render(request, 'allSurvey.html',{'survey': survey_object})