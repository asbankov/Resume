from django.http import HttpResponse
from django.views import View
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
import pdfkit
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form' : UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {'form' : form}
        return render(request, self.template_name, context)


class ResumeView(LoginRequiredMixin, View):
    template_name = 'editform.html'

    def get(self, request):
        #ResumeModel.objects.filter(user=request.user).delete()
        saved = ResumeModel.objects.all().filter(user=request.user)
        if len(saved) == 0:
            context = {'form' : ResumeForm(), 'isSaved' : 0}
            return render(request, self.template_name, context)
        else:
            saved = saved[0]
            form = ResumeForm(instance=saved)
            context = {'form' : form, 'isSaved' : 0}
            return render(request, self.template_name, context)


    def post(self, request):
        form = ResumeForm(request.POST)
        isSaved = 0
        if form.is_valid():
            ResumeModel.objects.filter(user=request.user).delete()
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            isSaved = 1
        else:
            isSaved = 2
        context = {'form' : form, 'isSaved' : isSaved}
        return render(request, self.template_name, context)


class ResultView(LoginRequiredMixin, View):
    template_name = 'result.html'

    def get(self, request):
        saved = ResumeModel.objects.all().filter(user=request.user)
        if len(saved) == 0:
            return redirect('editform')
        else:
            saved = saved[0]
            context = {'resume' : saved}
            return render(request, self.template_name, context)

@login_required()
def download(request):
    saved = ResumeModel.objects.all().filter(user=request.user)[0]
    context = {'resume' : saved, 'username' : request.user.username}
    html = render_to_string('resume.html', context)
    config = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, configuration=config, options={'encoding':'UTF-8', 'enable-local-file-access': True})
    #with open('./result.pdf', 'r') as f:
    #    file_data = f.read()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="result.pdf"'
    return response