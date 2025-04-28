# web/app.py

from flask import Flask, render_template, redirect, url_for, request, session
from web.forms import LoginForm
from core.auth import verify_password, verify_2fa
from core.access_control import can_access
from core.document_store import save_document, load_document
import os

app = Flask(__name__)
app.config.from_object('config.settings')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if verify_password(form.username.data, form.password.data) and verify_2fa(form.token.data):
            session['user'] = form.username.data
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/index')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    folders = os.listdir('data/vault')
    return render_template('index.html', folders=folders)

@app.route('/folder/<folder>')
def folder(folder):
    if 'user' not in session:
        return redirect(url_for('login'))
    if not can_access(session['user'], 'read'):
        return "Unauthorized", 403
    files = os.listdir(f'data/vault/{folder}')
    return render_template('folder.html', folder=folder, files=files)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
