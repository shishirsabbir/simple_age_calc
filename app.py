from flask import Flask, request, render_template, Response, send_from_directory
from datetime import datetime

app = Flask(__name__)

# magic


def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


@app.route('/')
def index():
    return render_template('index.html')


# adding favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'static/age.png', mimetype='image/png')


@app.route('/calculate_age', methods=['GET', 'POST'])
def get_age():
    birthdate = request.form.get('birthdate')
    if not birthdate:
        return Response({"error": "Birthdate is required. Formate: YYYY-MM-DD"})

    try:
        age = calculate_age(birthdate)
        return render_template('index.html', age=age, birthdate=birthdate)

    except ValueError:
        return Response({'error': 'Invalid data formate. Please use YYYY-MM-DD '})


if __name__ == '__main__':
    app.run()
