import azure.functions as func
import logging
import pandas as pd
import os

import requests
import json

import pyodbc

from datetime import datetime, timedelta


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="irail_http_trigger_func")
def irail_http_trigger_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # --- iRail API Call ---

    station = "Sint-Niklaas"
    url = f"https://api.irail.be/liveboard/?station={station}&format=json&lang=en"

    response = requests.get(url)

    # Convert the response to JSON (Python dictionary)
    data = response.json()

    # Save the extracted data in a list
    result = []


    # --- Extract info ---

    time_consultat = data["timestamp"]
    departure_station = data["station"]

    for train in data["departures"]["departure"]:
        train_data = {

            "departure_station": departure_station,
            "arrival_station": train["station"],
            "delay": train["delay"],
            "platform": train["platform"],
            "canceled": train["canceled"],
            "timestamp": time_consultat
        }

        result.append(train_data)


    # Convert the dictionary list to a DataFrame

    df = pd.DataFrame(result)


    df['delay'] = df['delay'].astype(int) # convert the data to an integer
    df['canceled'] = df['canceled'].astype(int) # convert the data to an integer

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s') # convert the data to a date and time

    # Adjust to Belgian time (+1)
    df['timestamp'] = df['timestamp'] + timedelta(hours=1)


    # --- Connect to SQL and insert data ---

    conn_str = os.environ["SqlConnectionString"]

    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()


    # Enter the data into SQL

    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO station (departure_station, arrival_station, platform, delay, canceled, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """,

        row['departure_station'],
        row['arrival_station'],
        row['platform'],
        row['delay'],
        row['canceled'],
        row['timestamp']
        )


    conn.commit()   # Save the changes to the database
    cursor.close()  # close the cursor
    conn.close()    # Close the connection



    # Return the response as JSON
    return func.HttpResponse(
        body=json.dumps(result),
        status_code=200,
        mimetype="application/json"
    )




# codigo para ejecutar
#     & "C:\Program Files\Microsoft\Azure Functions Core Tools\func.exe" start
