from flask import Flask, render_template
import scraper


app = Flask(__name__)
print(1)
scraper.getStarted()
list = [scraper.StartEm, scraper.SitEm, scraper.Enigma]
@app.route('/')
def main():
    return render_template('index.html', list=list)


if __name__ == '__main__':
    app.run(debug=True)