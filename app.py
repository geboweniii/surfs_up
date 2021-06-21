
#*************************************************
#THIS is random code found on the internet
# It DOES work
#*************************************************
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return 'Web App with Python Flask! OK!'
# app.run(host='0.0.0.0', port=5000)

#*************************************************
#THIS code is from section 9.4.3.
# It does NOT work
#*************************************************
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello world'

#Run these commands in Anaconda Python Prompt from same source folder
# export FLASK_APP=app.py
# set FLASK_APP=app.py
# flask run


#*************************************************
#THIS is all the code from section 9.5
# It does NOT work
#*************************************************





#*************************************************
#*************************************************
#9.5.1 - Set Up the Database and Flask
#*************************************************
#*************************************************
# Dependencies and Setup
import datetime as dt
import numpy as np
import pandas as pd


# # Python SQL Toolkit and Object Relational Mapper
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
# from sqlalchemy.pool import StaticPool
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# # Import Flask
from flask import Flask, jsonify

# #################################################
# # Database Setup
# #################################################
# # Reference: https://stackoverflow.com/questions/33055039/using-sqlalchemy-scoped-session-in-theading-thread
# engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={"check_same_thread": False}, poolclass=StaticPool, echo=True)
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect Existing Database Into a New Model
Base = automap_base()
# Reflect the Tables
Base.prepare(engine, reflect=True)

# Save References to Each Table
Measurement = Base.classes.measurement
Station = Base.classes.station

# # Create Session (Link) From Python to the DB
session = Session(engine)

# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__)




#*************************************************
#*************************************************
#9.5.2 - Create the Welcome Route
#*************************************************
#*************************************************


# #################################################
# # Flask Routes
# #################################################
# Defining the root, welcome, to be the home page
# All of your routes should go after the app = Flask(__name__) line of code
# Otherwise, your code may not run properly.
# The forward slash is commonly known as the highest level of hierarchy in any computer system
# Whenever you make a route in Flask, you put the code you want in that specific route below @app.route()
@app.route('/')


# Our root, or welcome route, is set up
# Next step is to add the routing information for each of the other routes
# Creating a function welcome() with a return statement
# Adding the precipitation, stations, tobs,  temp routes that we'll need for this module into our return statement
# When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br>
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end <br>
    ''')


# Next route we'll build is for the precipitation analysis
# This route will occur separately from the welcome route
# Every time we create a new route, our code should be aligned to the left in order to avoid errors
@app.route("/api/v1.0/precipitation")




















# # Home Route
# @app.route("/")
# def welcome():
#         return """<html>
# <h1>Hawaii Climate App (Flask API)</h1>
# <img src="https://i.ytimg.com/vi/3ZiMvhIO-d4/maxresdefault.jpg" alt="Hawaii Weather"/>
# <p>Precipitation Analysis:</p>
# <ul>
#   <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
# </ul>
# <p>Station Analysis:</p>
# <ul>
#   <li><a href="/api/v1.0/stations">/api/v1.0/stations</a></li>
# </ul>
# <p>Temperature Analysis:</p>
# <ul>
#   <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
# </ul>
# <p>Start Day Analysis:</p>
# <ul>
#   <li><a href="/api/v1.0/2017-03-14">/api/v1.0/2017-03-14</a></li>
# </ul>
# <p>Start & End Day Analysis:</p>
# <ul>
#   <li><a href="/api/v1.0/2017-03-14/2017-03-28">/api/v1.0/2017-03-14/2017-03-28</a></li>
# </ul>
# </html>
# """

# # Precipitation Route
# @app.route("/api/v1.0/precipitation")
# def precipitation():
#         # Convert the Query Results to a Dictionary Using `date` as the Key and `prcp` as the Value
#         # Calculate the Date 1 Year Ago from the Last Data Point in the Database
#         one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
#         # Design a Query to Retrieve the Last 12 Months of Precipitation Data Selecting Only the `date` and `prcp` Values
#         prcp_data = session.query(Measurement.date, Measurement.prcp).\
#                 filter(Measurement.date >= one_year_ago).\
#                 order_by(Measurement.date).all()
#         # Convert List of Tuples Into a Dictionary
#         prcp_data_list = dict(prcp_data)
#         # Return JSON Representation of Dictionary
#         return jsonify(prcp_data_list)

# # Station Route
# @app.route("/api/v1.0/stations")
# def stations():
#         # Return a JSON List of Stations From the Dataset
#         stations_all = session.query(Station.station, Station.name).all()
#         # Convert List of Tuples Into Normal List
#         station_list = list(stations_all)
#         # Return JSON List of Stations from the Dataset
#         return jsonify(station_list)

# # TOBs Route
# @app.route("/api/v1.0/tobs")
# def tobs():
#         # Query for the Dates and Temperature Observations from a Year from the Last Data Point
#         one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
#         # Design a Query to Retrieve the Last 12 Months of Precipitation Data Selecting Only the `date` and `prcp` Values
#         tobs_data = session.query(Measurement.date, Measurement.tobs).\
#                 filter(Measurement.date >= one_year_ago).\
#                 order_by(Measurement.date).all()
#         # Convert List of Tuples Into Normal List
#         tobs_data_list = list(tobs_data)
#         # Return JSON List of Temperature Observations (tobs) for the Previous Year
#         return jsonify(tobs_data_list)

# # Start Day Route
# @app.route("/api/v1.0/<start>")
# def start_day(start):
#         start_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
#                 filter(Measurement.date >= start).\
#                 group_by(Measurement.date).all()
#         # Convert List of Tuples Into Normal List
#         start_day_list = list(start_day)
#         # Return JSON List of Min Temp, Avg Temp and Max Temp for a Given Start Range
#         return jsonify(start_day_list)

# # Start-End Day Route
# @app.route("/api/v1.0/<start>/<end>")
# def start_end_day(start, end):
#         start_end_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
#                 filter(Measurement.date >= start).\
#                 filter(Measurement.date <= end).\
#                 group_by(Measurement.date).all()
#         # Convert List of Tuples Into Normal List
#         start_end_day_list = list(start_end_day)
#         # Return JSON List of Min Temp, Avg Temp and Max Temp for a Given Start-End Range
#         return jsonify(start_end_day_list)

# # Define Main Behavior
# if __name__ == '__main__':
#     app.run(debug=True)