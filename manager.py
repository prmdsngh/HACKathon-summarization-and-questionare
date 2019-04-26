from flask import jsonify
from Utilities import GenericProcessingTools
from TextUtilities import TextSummarizer
import json

def convert_pdf_html(name, file):
    # Do some stuff
    # f = open(file, "r")
    # print(f.read())
    return jsonify({"api":"Convert PDF to HTML","message":"successful","text":name})

def getTextFromImage(name):
    return GenericProcessingTools.getTextFromImage(name)

def get_question():
    return jsonify({"api":"Get Question","message":"successful","text":[{"answer":"speculation","question":"After all the __________ about whether we would have the fight, the last few weeks have seen much name-calling and animosity on both sides, as the rivalry intensifies ahead of the big day.","similar_words":["adverse opinion","guess","side"],"title":"mytopic"}]})

def get_summary(text, isHeading):
    ts = TextSummarizer.TextSummarizer()
    if isHeading:
        url = 'https://en.wikipedia.org/wiki/'+text
        text = GenericProcessingTools.getTextFromHeadingBySearch(url)
    summary = ts.getSummaryFromText(text)
    return summary