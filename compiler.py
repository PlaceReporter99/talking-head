import os
import speech_recognition as sr
import re
r=sr.Recognizer()
stack=[]
def soundtext(x):
    with sr.AudioFile(x) as snd:
        data=r.record(snd)
        return r.recognize_google(data)
def readmic(x):
    with sr.Microphone() as mic:
        data=r.record(mic,duration=x)
        return r.recognize_google(data)
def hex2chr(x):
    try:
        return ''.join([chr(int('0x'+y,16)) for y in [x[2*y]+x[2*y+1] for y in range(len(x)//2)]])
    except ValueError:
        raise ValueError("Invalid hex bytes.")
def textcom(text):
    if text[:4]=="push":
        if text[4:8]=="bite":
            stack.append(hex2chr(text[8:]))
        elif text[4:9]=="input":
            stack.append(input(text[9:]))
        else:
            stack.append(eval(text[4:]))
    elif text[:7]=="execute":
        if text[7:11]=="bite":
            exec(hex2chr(text[8:]))
        elif text[7:12]=="input":
            exec(input(text[9:]))
        else:
            exec(text[5:])
    elif text[:3]=="pop":
        if text[3:]:
            print(stack.pop(int(text[3:])))
        else:
            print(stack.pop())
    else:
        raise SyntaxError("Invalid Syntax.")
def compilele(code):
    y=code
    y=re.sub('after that','\n',y)
    y=re.sub('quote','"',y)
    y=re.sub('comma',',',y)
    y=re.sub('full stop','.',y)
    y=re.sub('exclamation mark','!',y)
    y=re.sub('question mark','?',y)
    y=re.sub(' ','',y)
    y=re.sub('space',' ',y)
    y=re.sub('equals','=',y)
    y=re.sub("zero","0",y)
    y=re.sub("one","1",y)
    y=re.sub("two","2",y)
    y=re.sub("three","3",y)
    y=re.sub("four","4",y)
    y=re.sub("five","5",y)
    y=re.sub("six","6",y)
    y=re.sub("seven","7",y)
    y=re.sub("eight","8",y)
    y=re.sub("nine","9",y)
    y=re.sub("bike","bite",y)
    for z in y.split('\n'):
        textcom(z)
if (x:=input("Type in the filepath of the WAV audio file, or \"r\" to record your voice to execute.\n\n"))=="r":
    y=int(input("How many seconds to record? "))
    print("Start speaking.")
    z=readmic(y)
    print("Stop speaking.")
    print("Interpreted code: "+z)
    compilele(z)
else:
    dirlist=x.split("\\")
    os.chdir("\\".join(dirlist[:-1]))
    print("Interpreted code: "+(abc:=soundtext(dirlist[-1])))
    compilele(abc)