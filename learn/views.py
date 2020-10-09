from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    #pass data/strint/list in web page
    disctonary={'name':'chandan', 'place':'mars'}
    return render(request, 'index.html', disctonary)

def rmpun(request):
    # get text from index page for text analyzing
    # this is use in get type data post method
    # index_text = request.GET.get('text', 'default')
    #for data send using post method
    index_text = request.POST.get('text', 'default')
    # check checkbox value
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    newline_remover = request.POST.get('newlineremover', 'off')
    extraspace_remover = request.POST.get('spaceextraremover', 'off')
    char_count = request.POST.get('charcount', 'off')

    # remove puncuatation code
    if remove_punc == "on":
        puncuation = '''!()_~`{}[]:;'"/\|,<>.?@#$%^&*'''
        analyzed = ""
        for char in index_text:
            if char not in puncuation:
                analyzed = analyzed + char
        params = {'purpose':'Removed Puncutation', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # change in upper case code
    if(full_caps == "on"):
        analyzed = ""
        for char in index_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert Into UPPER CASE', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # remove new line from input text
    if(newline_remover == "on"):
        analyzed = ""
        for char in index_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    # space remove from input text
    if (extraspace_remover == "on"):
        analyzed = ""
        for inde, char in enumerate(index_text):
            if not(index_text[inde] == " " and index_text[inde+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    # charactour count from input text
    if (char_count == "on"):
        analyzed = 0
        for i in index_text:
            analyzed = analyzed+1
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if (remove_punc != "on" and newline_remover != "on" and char_count != "on" and extraspace_remover != "on" and full_caps != "on"):
        return HttpResponse("Error")



    return render(request, 'analyze.html', params)

def capfirst(request):
    return HttpResponse("cap first")

def newlinerm(request):
    return HttpResponse("char count")

def spacerm(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("char count")