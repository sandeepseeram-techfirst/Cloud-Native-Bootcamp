### MLflow

MLflow is an open-source platform designed to manage the machine learning (ML) lifecycle. It provides tools to streamline and standardize the process of developing, deploying, and maintaining machine learning models.


MLflow consists of four main components:

###### MLflow Tracking: A system for logging and querying experiments, including code, data, configuration, and results.
###### MLflow Projects: A packaging format for reproducible runs, allowing you to define and share ML code in a standardized way.
###### MLflow Models: A model packaging format that supports multiple frameworks, enabling easy deployment to various environments.
###### MLflow Registry: A centralized repository to manage the lifecycle of ML models, including versioning, staging, and deployment.

1. MLflow is a Python package. 
2. The Tracking Server is composed of a web application and REST API that allows you to view and manage your experiments.

3. cmd: mlflow server --host 0.0.0.0 --port 5000 

Note: MLflow runs locally by default, meaning it will store experiments and run in the local filesystem. However, we have the option to set up a remote Tracking Server to store the tracking data in a centralized location, which can be beneficial when working in a team or across multiple machines.