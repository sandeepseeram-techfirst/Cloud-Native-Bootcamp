import functions_framework
from google.cloud import bigquery

@functions_framework.http
def record_travel_request(request):
    """Writes travel requests to BigQuery.
    Args:
        request (flask.Request): A request object with JSON
          containing fields for user, travel_purpose, departure_city,
          destination_city, departure_date, and return_date.
    Returns:
        JSON response containing a 'message' field indicating the
          status of the request.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args
    print("JSON:" + str(request_json))
    print("args:" + str(request_args))

    bq_client = bigquery.Client()
    table_id = "qwiklabs-gcp-00-bcb13bb236e9.trip.travel_requests"

    row_to_insert = [
        {"user": request_json["user"],
        "travel_purpose": request_json["travel_purpose"],
        "departure_city": request_json.get("departure_city",""),
        "destination_city": request_json.get("destination_city",""),
        "departure_date": request_json.get("departure_date",""),
        "return_date": request_json.get("return_date",""), 
        },
    ] 

    errors = bq_client.insert_rows_json(table_id, row_to_insert)  # Make an API request.
    if errors == []:
        return {"message": "New row has been added."}
    else:
        return {"message": "Encountered errors while inserting rows: {}".format(errors)}