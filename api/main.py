import sys
sys.path.append('../')

from flask import Flask

app = Flask(__name__)

@app.route('/dashboard/data', methods=['GET'])
def get_dashboard_data():
    """
    Function to get dictionary of all formatted data for Dashboard page in frontend
    """
    return {
        'report1': [],
        'report2': []
    }

@app.route('/statistics/pa-counts-by-carecenter', methods=['GET'])
def get_pa_counts_by_cc():
    """
    Function to get formatted data for Statistics page in frontend
    """
    return [
        {id:0}, {id:1}
    ]

@app.route('/statistics/pa-counts-by-room-type', methods=['GET'])
def get_pa_counts_by_room_type():
    """
    Function to get formatted data for Statistics page in frontend
    """
    return [
        {id:0}, {id:1}
    ]

@app.route('/data/carecenters', methods=['GET'])
def get_carecenters():
    """
    Function to get formatted data for Data page in frontend
    """
    return [
        {id:0}, {id:1}
    ]

@app.route('/data/patient-admissions-by-country', methods=['GET'])
def get_patient_admissions_by_country():
    """
    Function to get formatted data for Data page in frontend
    """
    return [
        {id:0}, {id:1}
    ]

if __name__ == '__main__':
    app.run(debug=True)