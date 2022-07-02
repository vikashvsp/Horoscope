from flask import Flask
from decouple import config
from flask_restx import Api

app=Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api=Api(app,version='1.0',title='Horoscope Api',
description='Get horoscope data using api',
license='Vsp',
contact='Vikash Kumar',
contact_email='vkvikashkumar987@gmail.com',
doc='/',
prefix='/api/v1')

from core import routes

