from flask import Flask, render_template, request

app = Flask(__name__, static_folder="assets", template_folder="templates")


@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_post():
    text = request.form['book_title']
    processed_text = text.upper()
    print(text)
    return processed_text

if __name__ == '__main__':
	app.run()

