from tkinter import *
from bs4 import BeautifulSoup
import requests
import random


"""
1º generate the text -> ok
2º tk infinite loop to enter "keys",
3º start by start typing, at the same time, start a clock to know how much time did the user use. 
4º check the enter key == text.
5º continue if all correct, if not, need to first delete
6ª finish when all typed and correct, show used time
"""

def createText(each_paragraph):
    countAss = 0
    textToType = ""

    for frase in each_paragraph:
        ass = frase.find_all("a")
        maxRange = len(ass) - 1

        if ass:
            if ass[countAss].string is None:
                ""
            elif frase == ass[countAss]:
                textToType = "{}{}".format(textToType, ass[countAss].string)
                # print(ass[countAss].string)
                if countAss != maxRange:
                    countAss += 1
        else:
            textToType = "{}{}".format(textToType, frase.string)

    return textToType

def generateText():
    # this website can be whatever...
    url = "https://www.dissentmagazine.org/online-articles"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    # print(doc.prettify())

    listOfLink = []
    articles = doc.find_all("article")
    count = 0
    listOfText = []

    for each_article in articles:
        listOfLink.append(each_article.a["href"])

    for each_link in listOfLink:
        page = requests.get(each_link)
        doc2 = BeautifulSoup(page.text, "html.parser")

        content = doc2.find_all("article")

        for each_paragraph in content:
            each_paragraph = each_paragraph.find_all("p")
            listOfText.append(createText(each_paragraph))

    listOfText = [each_frase.replace("None", "") for each_frase in listOfText]

    text = random.choice(listOfText)

    return text

def transform(event):
    # can do ASCII...
    transformed = event.keysym
    if event.keysym == "Caps_Lock" or event.keysym == "Shift_L" or event.keysym == "Shift_R" or event.keysym == "Tab" or event.keysym == "Control_L" or event.keysym == "Win_L" or event.keysym == "Alt_L" or event.keysym == "Return":
        transformed = ""
    elif event.keysym == "comma":
        transformed = ","
    elif event.keysym == "semicolon":
        transformed = ";"
    elif event.keysym == "colom":
        transformed = ":"
    elif event.keysym == "minus":
        transformed = "-"
    elif event.keysym == "plus":
        transformed = "+"
    elif event.keysym == "asterisk":
        transformed = "*"
    elif event.keysym == "space":
        transformed = " "
    elif event.keysym == "parenleft":
        transformed = "("
    elif event.keysym == "parenright":
        transformed = ")"
    elif event.keysym == "quotedbl":
        transformed = '"'
    elif event.keysym == "period":
        transformed = "."
    return transformed

def addKey(event):
    transformed = transform(event)
    list2String = ""
    if transformed == "BackSpace":
        typed.pop()
        list2String = list2String.join(typed)
    elif transformed == "":
        list2String = list2String.join(typed)
    else:
        typed.append(transformed)
        list2String = list2String.join(typed)
        if list2String == text:
            root.destroy()

    showText = "{}{}".format("\r", list2String)
    print(showText, end="")


# main:
# generate the text
text = generateText()
print(text)

# typing
typed = []
root = Tk()
root.bind("<Key>", addKey)
root.mainloop()

# congrats
print("")
print("Congratulations, you finished")