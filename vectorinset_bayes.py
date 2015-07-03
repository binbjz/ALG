#!/usr/bin/env python
#filename: vectorinset_bayes.py
#

from numpy import *


def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]

    classVec = [0,1,0,1,0,1]

    return postingList,classVec


def createVocabList(dataSet):
    vocabSet = set([])

    for document in dataSet:
        vocabSet = vocabSet | set(document)

    return list(vocabSet)
     

def setOfWords2Vec(vocabList, inputSet):
    retVocabList = [0] * len(vocabList)

    for word in inputSet:
        if word in vocabList:
            retVocabList[vocabList.index(word)] = 1
        else:
            print 'word ', word, 'not in dict'

    return retVocabList


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)

    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1

    return returnVec


def trainNB0(trainMatrix,trainCatergory):
    numTrainDoc = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCatergory)/float(numTrainDoc)

    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0

    for i in range(numTrainDoc):
        if trainCatergory[i] == 1:
            p1Num +=trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num +=trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)

    return p0Vect,p1Vect,pAbusive
     

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)

    if p1 > p0:
        return 1
    else: 
        return 0
         

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]

    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))

    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)

    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
     

def main():
    testingNB()
     

if __name__ == '__main__':
    main()
