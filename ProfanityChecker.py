import urllib.request as ur

def read_text():
    #quotes=open("C:\\Users\\Nehal\\Desktop\\profanity.txt")
    #contents_of_file=quotes.read()
    #print(contents_of_file)
    #quotes.close()
    check_profanity("---Write word or sentence----")

def check_profanity(text_to_check):
    output1=ur.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    print(output1.read())

read_text()
