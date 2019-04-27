import cv2
import os
from Utilities import DownloadGoogleImages
from PIL import Image
from TextUtilities import TextProcessor

def generateVideoFromText(images):
    video_name = 'video.avi'
    ext = '.jpg'
    fps = 1
    shape = 960, 720    

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    video = cv2.VideoWriter(video_name, fourcc, fps, shape)
    
    for image in images:
        image = cv2.imread(image)
        resized=cv2.resize(image,shape) 
        video.write(resized)

    cv2.destroyAllWindows()
    video.release()

def getImagesFromSentences(text,size):
    sentences = TextProcessor.getSentences(text)
    #text = TextProcessor.getProcessedTextualData(sentences)
    print(sentences)
    images = []
    for sentence in sentences:
        print(sentence+"\n")
        if len(sentence.split())<15:
            print("inside")
            x = DownloadGoogleImages.downloadimages(text, size)
            imageList = x[text]
            print(imageList)
            for imageLink in imageList:
                images.append(imageLink)
    return images
