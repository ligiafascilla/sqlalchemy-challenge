# Import the dependencies.
from flask import Flask, jsonify
from datetime import datetime, timedelta
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# Database Setup
engine = create_engine("sqlite:///your_database_file_path_here")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    """Homepage"""
    return (
        f"Welcome to the Climate App API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Precipitation data for the last 12 months"""

@app.route("/api/v1.0/stations")
def stations():
    """List of stations"""

@app.route("/api/v1.0/tobs")
def tobs():
    """Temperature observations for the previous year of the most active station"""

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    """Minimum, average, and maximum temperature for the specified date range"""

if __name__ == '__main__':
    app.run(debug=True)
