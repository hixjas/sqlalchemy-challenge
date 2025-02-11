# Import the dependencies.

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, Float, Date
from datetime import datetime, timedelta

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///SurfsUp/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# Homepage route
@app.route('/', methods=['GET'])
def homepage():
    """List all available routes."""
    return (
        "Welcome to the Hawaii Climate Analysis API<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation - Precipitation data for the last 12 months.<br/>"
        "/api/v1.0/stations - List of all stations.<br/>"
        "/api/v1.0/tobs - Temperature observations for the most active station over the last 12 months.<br/>"
        "/api/v1.0/&lt;start&gt; - Min, avg, and max temperatures from a start date.<br/>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt; - Min, avg, and max temperatures for a date range."
    )

# Precipitation route
@app.route('/api/v1.0/precipitation', methods=['GET'])
def precipitation():
    """Return the last 12 months of precipitation data."""
    # Find the most recent date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d')

    # Calculate the date one year before the most recent date
    one_year_ago = most_recent_date - timedelta(days=365)

    # Query the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Convert results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

# Stations route
@app.route('/api/v1.0/stations', methods=['GET'])
def stations():
    """Return a list of all stations."""
    # Query all stations
    results = session.query(Station).all()

    # Convert results to a list of dictionaries
    stations_list = [{"id": station.id, "station": station.station, "name": station.name} for station in results]

    return jsonify(stations_list)


# Temperature observations route
@app.route('/api/v1.0/tobs', methods=['GET'])
def tobs():
    """Return temperature observations for the most active station over the last 12 months."""
    # Find the most active station (station with the most observations)
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    # Find the most recent date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d')

    # Calculate the date one year before the most recent date
    one_year_ago = most_recent_date - timedelta(days=365)

    # Query temperature observations for the most active station over the last 12 months
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= one_year_ago).all()

    # Convert results to a list of dictionaries
    tobs_data = [{"date": date, "temperature": tobs} for date, tobs in results]

    return jsonify(tobs_data)

# Start date route
@app.route('/api/v1.0/<start>', methods=['GET'])
def temp_start(start):
    """Return min, avg, and max temperatures from a start date."""
    # Query min, avg, and max temperatures for dates greater than or equal to the start date
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).all()

    # Convert results to a dictionary
    temp_data = {
        "start_date": start,
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(temp_data)

# Start and end date route
@app.route('/api/v1.0/<start>/<end>', methods=['GET'])
def temp_start_end(start, end):
    """Return min, avg, and max temperatures for a date range."""
    # Query min, avg, and max temperatures for the date range
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Convert results to a dictionary
    temp_data = {
        "start_date": start,
        "end_date": end,
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(temp_data)





# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
