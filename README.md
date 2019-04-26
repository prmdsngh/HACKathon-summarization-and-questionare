# HACKathon-summarization-and-questionare
modules for summarization and questionare

API:

POST http://localhost:8001/summarize
request:
{
	"text" : "AI",
	"isHeading" : 1
}

POST http://localhost:8001/text/ocr
form-data file

GET http://localhost:8001/question
{
	"text":"",
	"isFormatted":0
}
