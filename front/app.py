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

        if(url_to_scrap['url'][0:31] != 'https://www.youtube.com/watch?v'):
            result = "Erreur d'URL"
        else:
            try:
                result_views = requests.post(
                    url='http://scraper:5000/scrap', data=url_to_scrap).text
                result = 'Nombre de vues estimé : ' + result_views
            except Exception:
                result = "Echec du scraping"

        return render_template('front.html', result=result)
    return render_template('front.html')


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5002)
