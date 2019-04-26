from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re


def getSentences(line):
    regex = re.compile("\((.*?)\)")
    line = re.sub( regex, ' ', line)
    regex = re.compile("\[(.*?)\]")
    line = re.sub( regex, ' ', line)
    line = re.sub(r'\s+', ' ', line) 
    return sent_tokenize(line)

def getWordEmbedding(fileName):
    word_embeddings = {}
    f = open( fileName, encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32') 
        word_embeddings[word] = coefs
    f.close()
    return word_embeddings

def removePunctuation(sentences):
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
    clean_sentences = [s.lower() for s in clean_sentences]
    return clean_sentences


def removeStopwords(sentenceList):
    stop_words = stopwords.words('english')
    newSentences = []
    for sentence in sentenceList:
        sentenceNew = " ".join([i for i in sentence.split() if i not in stop_words])
        newSentences.append(sentenceNew)
    return newSentences

    

    

    