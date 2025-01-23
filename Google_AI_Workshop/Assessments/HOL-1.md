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