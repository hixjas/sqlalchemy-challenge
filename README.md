# sqlalchemy-challenge
Module 10
Hawaii Climate Analysis API
This project uses SQLAlchemy ORM queries, pandas and Matplotlib to analyze and explore climate data. A Flask API is used for analyzing climate data stored in a SQLite database. The API allows users to retrieve precipitation data, station information, temperature observations, and temperature statistics for specified date ranges.

Table of Contents
Features

Installation

Usage

API Endpoints

Contributing


Features
Retrieve the last 12 months of precipitation data.

Get a list of all weather stations.

Fetch temperature observations for the most active station over the last 12 months.

Calculate minimum, average, and maximum temperatures for a specified date range.

Installation
Prerequisites
Python 3.x

SQLite database (hawaii.sqlite)

Steps
Clone the repository:

bash
Copy
git clone https://github.com/your-username/climate-analysis-api.git
cd climate-analysis-api
Install the required Python packages:

bash
Copy
pip install -r requirements.txt
Ensure the SQLite database (hawaii.sqlite) is in the project directory.

Run the Flask application:

bash
Copy
python app.py
Access the API at http://127.0.0.1:5000.

Usage
Homepage
Visit the homepage to see a list of available routes:

Copy
http://127.0.0.1:5000/
Example Requests
Precipitation Data:

Copy
GET /api/v1.0/precipitation
List of Stations:

Copy
GET /api/v1.0/stations
Temperature Observations:

Copy
GET /api/v1.0/tobs
Temperature Statistics (Start Date):

Copy
GET /api/v1.0/2010-01-01
Temperature Statistics (Date Range):

Copy
GET /api/v1.0/2010-01-01/2010-01-31
API Endpoints
Homepage
URL: /

Method: GET

Description: Lists all available routes.

Precipitation Data
URL: /api/v1.0/precipitation

Method: GET

Description: Returns the last 12 months of precipitation data.

List of Stations
URL: /api/v1.0/stations

Method: GET

Description: Returns a list of all weather stations.

Temperature Observations
URL: /api/v1.0/tobs

Method: GET

Description: Returns temperature observations for the most active station over the last 12 months.

Temperature Statistics (Start Date)
URL: /api/v1.0/<start>

Method: GET

Description: Returns the minimum, average, and maximum temperatures for all dates greater than or equal to the start date.

Temperature Statistics (Date Range)
URL: /api/v1.0/<start>/<end>

Method: GET

Description: Returns the minimum, average, and maximum temperatures for the specified date range.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a pull request.

Notes:
Replace your-username with your actual GitHub username.

Update the database name (hawaii.sqlite) if your database has a different name.

Add a requirements.txt file listing the required Python packages (e.g., Flask, SQLAlchemy, pandas, etc.).