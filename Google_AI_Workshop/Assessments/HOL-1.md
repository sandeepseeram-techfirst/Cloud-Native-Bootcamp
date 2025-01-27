# Configure AI Applications to Optimize Search Results 

cat > travel_requests_schema.json << EOF
[
  {
    "name": "user",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "travel_purpose",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "departure_city",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "destination_city",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "departure_date",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "return_date",
    "type": "STRING",
    "mode": "NULLABLE"
  }
]
EOF 

### Create the BigQuery dataset trip and table travel_requests, using the schema defined in the travel_requests_schema.json file

bq --location=US mk -d trip
bq mk -t trip.travel_requests travel_requests_schema.json