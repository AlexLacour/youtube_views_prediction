from flask import Flask, request, render_template
import requests


app = Flask(__name__)


@app.route('/')
def main_html():
    return render_template('front.html')


@app.route('/front', methods=['GET', 'POST'])
def main():
    if(request.method == 'POST'):
        url_to_scrap = {'url': request.form['url_value']}
        result = requests.post(
            url='http://scraper:5000/scrap', data=url_to_scrap).text

        final_output = 'View prediction = ' + result

        return final_output


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5002)
