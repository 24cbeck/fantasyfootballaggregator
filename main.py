from flask import Flask, render_template
import scraper

'''
Cody Beck
sunhacks 2020
10/09/20 - 10/10/20
main.py - Uses the Flask framework to create a webapp that displays fantasy football predictions

'''

app = Flask(__name__)

scraper.getStarted()
list = [scraper.StartEm, scraper.SitEm, scraper.Enigma]


@app.route('/')
def main():
    return render_template('index.html', list=list)


if __name__ == '__main__':
    app.run(debug=True)
