from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/characters', methods=['POST'])
def get_characters():
    text_value = request.form['number']
    url = f'https://swapi.dev/api/people/{text_value}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return render_template('characters.html', character=data)
    else:
        return 'Error fetching data'


if __name__ == '__main__':
    app.run(debug=True)
