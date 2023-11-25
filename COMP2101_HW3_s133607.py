"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
Lab:
Exe:
Purpose:
Input:
Output:
Algorithm:
Test:
"""
import re


def main():
    orgText = buildRefernce()
    corrections = detectNcorrect(orgText)
    display(corrections)

def buildRefernce():
    reference = set()
    file = open("original.txt", 'r')
    for line in file:
        listOfWords = re.sub(r"[^a-zA-Z']", ' ', line)
        reference.update(listOfWords.split(" "))
    return reference


def generatePermutations(word):
    lst = set()
    if len(word) == 1:
        return word
    else:
        for i, l in enumerate(word):
            remain = word[:i] + word[1 + i:]
            for per in generatePermutations(remain):
                lst.add(l + per)
    return lst


def proposeCorrections(word, text):
    lst = []
    for i in generatePermutations(word):
        if i in text:
            lst.append(i)
    return lst


def display(listt):
    for l in listt:
        print(l["word"]+" in line:",l["line"],",WordNo.:",l["wNo"],", possible corrections: ",end="")
        for w in range(len(l["corrections"])):
            if w < len(l["corrections"])-1:
                print(l["corrections"][w],end=",")
            else:
                print(l["corrections"][w])


def detectNcorrect(text):
    corrections = []
    file = open("misspelled", "r")
    linecount = 1
    for line in file:
        listOfWords = re.sub(r"[^a-zA-Z']", ' ', line).split(" ")
        wordcount = 1
        for word in listOfWords:
            if word not in text:
                corrections.append({"line": linecount,"wNo":wordcount, "word": word, "corrections": proposeCorrections(word, text)})
            wordcount +=1
        linecount += 1
    return corrections


main()
