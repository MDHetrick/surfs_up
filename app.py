#9.5.1 - Set up DB & Flask
import datetime as dt
# import numpy as np
# import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up DB - access and query DB file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect DB into our classes
Base = automap_base()

# reflect tables
Base.prepare(engine, reflect=True)

#save references
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link
session = Session(engine)


######Set up flask

import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

#9.5.2 Create Welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')