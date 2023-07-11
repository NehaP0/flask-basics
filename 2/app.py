from flask import Flask, render_template, request

app = Flask(__name__)


entries = {}

@app.route('/')
def index():
    return "Welcome!"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        entries[key] = value
        return f"Entry created: {key} - {value}"
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', entries=entries)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in entries:
            entries[key] = value
            return f"Entry updated: {key} - {value}"
        else:
            return f"No entry found with key: {key}"
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in entries:
            del entries[key]
            return f"Entry deleted with key: {key}"
        else:
            return f"No entry found with key: {key}"
    return render_template('delete.html')

if __name__ == '__main__':
    app.run()
