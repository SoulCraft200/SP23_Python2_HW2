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
    pass


def buildRefernce():
    text = set()
    file = open("original.txt", 'r')
    for line in file:
        listOfWords = re.sub(r"[^a-zA-Z']", ' ', line)
        text.update(listOfWords.split(" "))
    return text


def generatePermutations(word):
    lst = []
    if len(word) == 1:
        return word
    else:
        for i, l in enumerate(word):
            remain = word[:i] + word[1 + i:]
            for per in generatePermutations(remain):
                lst.append(l + per)
    return lst


def proposeCorrections(word,text):
    lst = []
    for i in generatePermutations(word):
        if word in text:
            lst.append(word)









main()
