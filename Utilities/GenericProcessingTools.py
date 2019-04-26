from Utilities import pytesseract
from PIL import Image
import re
import urllib.request
import bs4 as bs

def getTextFromImage(name):
    ImageText = pytesseract.image_to_string(Image.open(name), lang = "eng" )
    regex = re.compile("\((.*?)\)")
    ImageText = re.sub( regex, ' ', ImageText)
    ImageText = re.sub(r'\s+', ' ', ImageText) 
    return ImageText; 

def getTextFromHeadingBySearch(url):
    article = urllib.request.urlopen(url).read()
    parsed_article = bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text = ""
    for p in paragraphs:  
        article_text += p.text
    return article_text


