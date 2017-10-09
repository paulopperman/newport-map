"""
A basic web app for mapping newport data project geospatial datasets
"""

import os
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)



# # grab all relevant files in the static directory - we want to inject them
# # into the main entry point's HEAD section
# css_files = [Path(os.path.join(parent.replace('static'+os.sep, '', 1), x))
#              for parent, _, files
#              in os.walk('static')
#              for x in files
#              if x.endswith(".css")]
#
# js_files = [Path(os.path.join(parent.replace('static'+os.sep, '', 1), x))
#             for parent, _, files
#             in os.walk('static')
#             for x in files
#             if x.endswith(".js")]

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
