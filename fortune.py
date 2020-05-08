from flask import Flask, render_template, request, jsonify, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SelectField, DateField
from wtforms.validators import DataRequired
from randomdemo import *
from flask_restful import Resource, Api

# App config.
DEBUG = True
app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
@app.route("/")
def index():
    return render_template('index.html')

class Fortune(Resource):
    def get(self, date):
        dateNo=cutd(date)
        monthNo=cutm(date)
        x=checkm(monthNo)
        xNo=int(x)
        colornum=random.randint(0,8)
        year= date.split('-')[0]
        resultdate =  findDay(date)+"ที่ "+checkd(dateNo)+" "+getm(xNo)+" พ.ศ. "+str(int(year)+543)
        return {'bdate': resultdate, 
        'love': fortuneLove(),
        'work': fortuneLove(),
        'money': fortuneMoney(),
        'color': fortuneColor()
        }

api.add_resource(Fortune, '/fortune/<string:date>')
if __name__ == "__main__":
    app.run()