from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            Rotate by:
            <input type="text" name="rot" value="0"/>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_value = request.form['rot']
    text_area = request.form['text']

    encrypted = rotate_string(text_area, int(rot_value))
    
    return form.format(encrypted)

@app.route("/")
def index():
    return form.format("")

app.run()