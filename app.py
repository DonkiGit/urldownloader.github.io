import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    response = requests.get(url)
    filename = url.split("/")[-1]

    with open(filename, 'wb') as file:
        file.write(response.content)

    return f"<a href='{filename}' download>Click here to download {filename}</a>"

if __name__ == '__main__':
    app.run()
