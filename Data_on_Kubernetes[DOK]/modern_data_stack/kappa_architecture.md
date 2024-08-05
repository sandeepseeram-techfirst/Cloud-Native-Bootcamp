# Kappa Architecture 

The Kappa architecture emerged more recently as an alternative approach from primarily the same creators of the Lambda architecture. The main difference in the Kappa architecture is that it aims to simplify the Lambda model by eliminating the separate batch and speed layers.


## Stream processing layer: 
Responsible for ingesting and processing all data as streams. This layer handles both historical data (via replay of logs/files) as well as new incoming data.

## Serving layer: 
Responsible for responding to queries by accessing views produced by the stream processing layer.