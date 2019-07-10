from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse


def main(request):
    with open('fileWithNames.txt', 'r') as file:
        friednsNames = file.readlines()

    content = {
        'friednsNames': friednsNames,
    }

    return render(request, 'authapp/index.html', content)


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('main'))
