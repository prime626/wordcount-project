from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] +=1
        else:
            wordDictionary[word] = 1

    sortedDictionary = sorted(wordDictionary.items(), key=itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordList), 'sortedDictionary':sortedDictionary})

def about(request):
    return render(request, 'about.html')
