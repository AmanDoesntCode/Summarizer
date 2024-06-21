from flask import Flask, render_template, request
from text_summarization import summarizer 

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/proceed', methods = ['GET','POST'])
def proceed():
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		summary, doc, len_doc, len_sum = summarizer(rawtext)
	return render_template('summary.html', summary = summary, doc=doc, len_doc = len_doc, len_sum = len_sum)

if __name__ == "__main__" :
	app.run(debug = True) 