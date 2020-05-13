from flask import Flask, render_template, request, jsonify, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SelectField, DateField
from wtforms.validators import DataRequired
from randomdemo import *
from flask_restful import Resource, Api

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class Fortune(FlaskForm):
    date = DateField('date', validators=[DataRequired()])
    @app.route("/", methods=('GET', 'POST'))
    def index():
        
        title=['วันเกิดของคุณคือ','ความรัก','การงาน','การเงิน','สีนำโชค']
        form = Fortune()
        result = {}
        if request.method == 'POST':
            date = request.form['date']
            dateNo=cutd(date)
            monthNo=cutm(date)
            x=checkm(monthNo)
            xNo=int(x)
            colornum=random.randint(0,8)
            year= date.split('-')[0]
            resultdate =  findDay(date)+"ที่ "+checkd(dateNo)+" "+getm(xNo)+" พ.ศ. "+str(int(year)+543)
            result = {'bdate': resultdate, 
            'love': fortuneLove(),
            'work': fortuneWork(), 
            'money': fortuneMoney(),
        'color': fortuneColor()
        }

        return render_template('index.html', form = form, result = result)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5001)