<<<<<<< HEAD
from util import bd
import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def menu():
  return render_template('home.html')

=======
from util import bd
import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def menu():
  return render_template('home.html')

>>>>>>> 37d2cc99831ee1c718b63e252890e21e7f4df067
app.run(debug=True)