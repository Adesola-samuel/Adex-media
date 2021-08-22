from django.shortcuts import render, redirect
from .models import WorkCategory, FeaturedWork, Message
import datetime


def index(request):
    context = {}
    return render(request, 'index.html', context)


def about(request):
    birth_date = datetime.date(1991, 9, 25)
    present_date = datetime.date.today()
    age = present_date.year - birth_date.year - (
    (present_date.month, present_date.day) < (birth_date.month, birth_date.day))
    context = {'age': age}
    return render(request, 'about.html', context)


def resume(request):
    context = {}
    return render(request, 'resume.html', context)


def services(request):
    context = {}
    return render(request, 'services.html', context)


def portfolio(request):
    categories = WorkCategory.objects.all()
    works = FeaturedWork.objects.all()
    context = {'categories': categories, 'works': works}
    return render(request, 'portfolio.html', context)


def portfolio_details(request, pk):
    work = FeaturedWork.objects.get(pk=pk)
    context = {'work': work}
    return render(request, 'portfolio-details.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def message(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    s = Message(name=name, email=email, subject=subject, message=message)
    s.save()