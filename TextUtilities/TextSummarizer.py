from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import numpy as np
from TextUtilities import TextProcessor
from nltk.corpus import stopwords
from TextUtilities import TextSummarizerUtils
from nltk.tokenize import sent_tokenize
import math
import os

trainedDataSet = r'../trainedData/glove.6B.100d.txt'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, trainedDataSet)

class TextSummarizer:
    def __init__(self):
        self.word_embeddings = TextProcessor.getWordEmbedding(filename)

    def getSummaryFromText(self, line):
        sentences = TextProcessor.getSentences(line)
        print(sentences)
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, trainedDataSet)
        cleanSentences = TextProcessor.removePunctuation(sentences)
        cleanSentences = TextProcessor.removeStopwords(cleanSentences)
        
        sentence_vectors = TextSummarizerUtils.createSentenceVector(cleanSentences, self.word_embeddings)
        sim_mat = TextSummarizerUtils.createSimilarityMatrix(cleanSentences, sentence_vectors)
        scores = TextSummarizerUtils.getScoreFromSimilarityMatrix(sim_mat)
        ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
        summary=""
        size = len(ranked_sentences)
        if(size>5):
            size = int(math.sqrt(size))
        for i in range(size):
            summary = summary + ranked_sentences[i][1] + " "
        return summary
    
    def getQuestionAnswerFromText(self, text):
        processedText = TextProcessor.getProcessedTextualData(text)
        sposs = {}
        for sentence in processedText.sentences :
            poss = {}
            sposs[sentence.string] = poss
            for tags in sentence.tags:
                tag = tags[1].encode('utf-8')
                if tag not in poss:
                    poss[tag] = []
                poss[tag].append(tags[0].encode('utf-8'))

        questionAnswerList = []
        for sentence in sposs.keys():
            poss = sposs[sentence]
            (word, newSentence, replaced) = TextProcessor.removeWordFromSentence(sentence, poss)
            val = {}
            if replaced is not None:
                val['question'] = replaced
                val['answer'] = word
            questionAnswerList.append(val)
        return questionAnswerList



    

    
