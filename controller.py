import manager
from flask import request,jsonify,render_template
from werkzeug import secure_filename
from forms import pdfFileForm
import sys
from FileUtilities import FileUtils

def routes(app):

    @app.route("/")
    def hello():
        return render_template("index.html")
    
    @app.route('/convertpdf/html', methods=['GET','POST'])
    def convertpdf():
        if(request.method == 'POST'):
            if(request.form['name'] == '' or request.files['file'] == ''):
                return jsonify({"Error" : "All Fields are required."})
            else:
                pdf_file = request.files['file']
                name = request.form['name']
                print("hello")
                pdf_file.save(secure_filename(pdf_file.filename))
                print("hello2")
                return manager.convert_pdf_html(name, pdf_file)

    @app.route('/question', methods=['POST'])
    def get_question_answer():
        data = request.get_json()
        isFormatted = data['isFormatted']
        text = data['text']
        try : 
            return jsonify({"code":"200","message":"successful","data":manager.get_question_answer(text, isFormatted)})
        except Exception as e:
            return jsonify({"code":"500","message":"error","data":str(e)})

    @app.route('/text/ocr', methods=['POST'])
    def getOcr():
        if(request.files['file'] == ''):
            return jsonify({"code":"400","message":"error","data":"error"})
        else:
            try:
                image_file = request.files['file'] 
                fileName = image_file.filename
                if FileUtils.verifyFile(fileName) :
                    image_file.save(secure_filename(fileName))
                    data = manager.getTextFromImage(fileName)
                    return jsonify({"code":"200","message":"successful","data":data})
                else:
                    return jsonify({"code":"400","message":"error","data":"error"})
            except Exception as e:
                return jsonify({"code":"500","message":"error","data":str(e)})

    @app.route('/summarize', methods = ['POST'])
    def getSummary():
        data = request.get_json()
        text = data['text']
        isHeading = data['isHeading']
        try:
            return jsonify({"code":"200","message":"successful","data":manager.get_summary(text, isHeading)})
        except Exception as e:
            return jsonify({"code":"500","message":"error","data":str(e)})

    @app.route('/summarize/video', methods = ['POST'])
    def getSummaryVideo():
        data = request.get_json()
        text = data['text']
        try:
            return jsonify({"code":"200","message":"successful","data":manager.get_summary_video(text)})
        except Exception as e:
            return jsonify({"code":"500","message":"error","data":str(e)})

    

    