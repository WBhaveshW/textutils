# I have created this file - Bhavesh

from django.http import HttpResponse

# this package is for template rendering
from django.shortcuts import render
def indexs(request):
    return HttpResponse("hello")

def abouts(request):
    return HttpResponse("<h1>This is About Section</h1>")

def contacts(request):
    return HttpResponse("This is Contact Section<br><a href='/'>Back</a> ")

def readFile(request):
    # return HttpResponse("This is Read File Section")
    f = open('/Django/textutils/textutils/TextFile.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        f.close()
        # it will shows file as it is
        # else it will show file contents in one line
        return HttpResponse(contents, content_type='text/plain')
        return HttpResponse(contents)

def readFile2(request):
    # return HttpResponse("This is Read File Section")
    f = open('/Django/textutils/textutils/TextFile.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        f.close()
        # it will shows file as it is
        # else it will show file contents in one line
        # return HttpResponse(contents, content_type='text/plain')
        return HttpResponse(contents)

def personalNavigator(request):
    # return HttpResponse('''<H1>Home</H1><br><a href="http://learning.techfryday.com/coronarealtimecounts/">Corona Reatime Track</a>
    #             <br><a href="/">Back</a>''')
    return HttpResponse('''<input type=button value="Back" onClick="javascript:history.go(-2);"> ''')

def removePunch(request):
    # we can define default value in case error occurs
    # Get the text
    # print(request.GET.get('text', 'default'))
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # Analyze the text
    return HttpResponse('''<h1>This is removePunch Section</h1><br> <button onclick="goBack()">Go Back</button>
<script>
function goBack(){
window.history.back();
}
</script>''')


def capitalize(request):
    return HttpResponse('''<h1>This is capitalize Section</h1><br> <button onclick="goBack()">Go Back</button>
<script>
function goBack(){
window.history.back();
}
</script>''')

def newLineRemove(request):
    return HttpResponse("<h1>This is newLineRemove Section</h1>")


def spaceRemove(request):
    return HttpResponse("<h1>This is spaceRemove Section</h1>")


def charCounts(request):
    return HttpResponse("<h1>This is charCounts Section</h1>")


def templateLoad(request):
    params = {'name': 'bhavesh', 'place': 'uran'}
    return render(request, 'index.html', params)


def templateLoad2(request):
    return render(request, 'index2.html')


def textAnalyzerHome(request):
    return render(request, 'index3.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    print(djtext)
    print(removepunc)
    # analyzed = djtext
    analyzed = ""
    purpose = ""

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose += "Removed Punctuations"
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        # return HttpResponse("<h1>Remove Punctuations</h1>")
        print(djtext)
        djtext = analyzed
        # return render(request, 'analyzer.html', params)

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose += "| Change to uppercase"
        params = {'purpose': purpose, 'analyzed_text': analyzed}
            # return HttpResponse("<h1>Remove Punctuations</h1>")
        djtext = analyzed
        # return render(request, 'analyzer.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose += "| Remove New Lines"
        params = {'purpose': purpose, 'analyzed_text': analyzed}
            # return HttpResponse("<h1>Remove Punctuations</h1>")
        djtext = analyzed
        # return render(request, 'analyzer.html', params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        purpose += "| Remove New lines"
        params = {'purpose': purpose, 'analyzed_text': analyzed}
            # return HttpResponse("<h1>Remove Punctuations</h1>")
        djtext = analyzed
        # return render(request, 'analyzer.html', params)

    if charactercounter == "on":
            analyzed = len(djtext)
            purpose += "| Character Count"
            params = {'purpose': purpose, 'analyzed_text': analyzed}
            # return HttpResponse("<h1>Remove Punctuations</h1>")
            djtext = analyzed
    # else:
    #     return HttpResponse("Error")
    if(charactercounter != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != 'on' and removepunc != "on"):
        return HttpResponse("Please select any operation and try again!.")

    return render(request, 'analyzer.html', params)
