from flask import jsonify
from Utilities import GenericProcessingTools
from TextUtilities import TextSummarizer,TextProcessor
import ImageToVid
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
    data = ""
    if isHeading:
        url = 'https://en.wikipedia.org/wiki/'+text
        data =  GenericProcessingTools.getTextFromHeadingBySearch(url)
        ImageToVid.generateVideoFromText(text,8)
    return ts.getSummaryFromText(data)

def get_summary_video(text):
    text = json.dumps(text, separators=(',', ':'))
    print(text)
    images = ImageToVid.getImagesFromSentences(text,5)
    if len(images)==0:
        return "no images"
    return ImageToVid.generateVideoFromText(images)