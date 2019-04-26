from flask import jsonify
from Utilities import GenericProcessingTools
from TextUtilities import TextSummarizer,TextProcessor
import json

ts = TextSummarizer.TextSummarizer()
def convert_pdf_html(name, file):
    # Do some stuff
    # f = open(file, "r")
    # print(f.read())
    return jsonify({"api":"Convert PDF to HTML","message":"successful","text":name})

def getTextFromImage(name):
    return GenericProcessingTools.getTextFromImage(name)

def get_question_answer(text, isFormatted):
    if not isFormatted:
        sentences = TextProcessor.getSentences(text)
        text = ' '.join(sentences)
    return ts.getQuestionAnswerFromText(text)

def get_summary(text, isHeading):
    if isHeading:
        url = 'https://en.wikipedia.org/wiki/'+text
        text =  GenericProcessingTools.getTextFromHeadingBySearch(url)
    return ts.getSummaryFromText(text)