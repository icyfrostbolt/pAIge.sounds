from flask import Flask, render_template, request, redirect
import spotifyStuff

app = Flask(__name__, static_folder="assets", template_folder="templates")

playlist_link = ""

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_post():
    text = request.form['book_title']
    print(text)

    spotifyStuff.createPlaylist(text)

    with open('link.txt', 'r') as file:
        playlist_link = " ".join(line.rstrip() for line in file)


    print("link final: " + playlist_link)
    return redirect(playlist_link, code=302)




if __name__ == '__main__':
	app.run()

