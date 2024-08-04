


## Stream processing layer: 
Responsible for ingesting and processing all data as streams. This layer handles both historical data (via replay of logs/files) as well as new incoming data.

## Serving layer: 
Responsible for responding to queries by accessing views produced by the stream processing layer.