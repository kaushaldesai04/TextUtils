from django.http import HttpResponse
from django.shortcuts import render

# Index page
def index(request):
   
    return render(request,'index.html')

#analyzing the text
def analyze(request):
    # grab the text
    inputtext=request.POST.get('textarea','default')
    # grab the value of removepunc
    removepunc =request.POST.get('removepunc','off')
    # grab the value of fullcaps
    fullcaps =request.POST.get('fullcaps','off')
    # grab the value of newline remover
    newlineremover=request.POST.get('newlineremover','off')
    # GRAB THE VALUE OF EXTRASPACE REMOVER
    extraspaceremover = request.POST.get('extraspaceremove','off')

    charactercount = request.POST.get('charcounter','off')
    punchuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    purpose=""

    # for removing punctuations
    if removepunc == "on":

        analyzed = ""
        for i in inputtext:
            if i not in punchuations:
                analyzed+=i
        #passing parameters to the templates
        purpose= purpose + 'Removepunc , '
        inputtext=analyzed

    # for capitalizing all the letters from given text
    if fullcaps=="on":
        inputtext=inputtext.upper()
        purpose+='Capitalize the txt , '

    # for removing the newline
    if newlineremover=="on":
        analyzed_text=''
        for i in inputtext:
            if i != '\n' and i!="\r":
                analyzed_text+= i
            else:
                analyzed_text+=' '
        purpose += 'Remove new line , '
        inputtext = analyzed_text

    #remove extra space from lines
    if extraspaceremover =="on":
        i=0
        analyzed_text=''
        while i <= len(inputtext)-1:
            if inputtext[i]==" " and inputtext[i+1]==" ":
                analyzed_text+=" "
                i+=2
            else:
                analyzed_text+=inputtext[i]
                i+=1
        purpose +='remove Extra space , '
        inputtext = analyzed_text

    if charactercount =='on':
        print(type(inputtext))
        count = 0
        for i in inputtext:
            if i !=" ":
                count+=1
        purpose += 'count characters , '
        inputtext =inputtext + ', wordcount of given line is : '+ str(count)
    params = {'purpose':purpose,'analyzed_text':inputtext}
    return render(request,'analyze.html',params)


def contact(request):

        return render(request,'contact.html')
