import functions_framework
from google.cloud import bigquery

@functions_framework.http
def record_feedback(request):
    """Writes employee feedback to BigQuery.
    Args:
        request (flask.Request): A request object with JSON
          containing fields for feedback and a store_number.
    Returns:
        JSON response containing a 'message' field indicating the
          status of the request.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args
    print("JSON:" + str(request_json))
    print("args:" + str(request_args))

    bq_client = bigquery.Client()
    table_id = "qwiklabs-gcp-02-67a6143af4db.feedback.employee_feedback"

    row_to_insert = [
        {
        "feedback": request_json["feedback"],
        "store_number": request_json.get("store_number",0)
        },
    ]

    errors = bq_client.insert_rows_json(table_id, row_to_insert)  # Make an API request.
    if errors == []:
        return {"message": "New row has been added."}
    else:
        return {"message": "Encountered errors while inserting rows: {}".format(errors)}