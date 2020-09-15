from flask import Flask, render_template, redirect, request
app = Flask(__name__)

dect = {'rare': {'primo': 'kek', 'lol': 'jaja', 'no': 'ZAZAZAZZAZZA'}}
dect_keys = dect['rare'].keys()
brawlers = ['lol', 'no', 'PRImo']
rare = dect['rare']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('LOLLOOLL')
        return render_template('test.html')
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
