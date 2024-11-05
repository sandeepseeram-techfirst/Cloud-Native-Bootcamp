#### Building Multi-Agent Systems with LangGraph, EDA, and Generative AI on Google Cloud

##### Key Architectural Elements and Technologies:

###### Google Cloud Platform (GCP): Central to the entire system:

###### Vertex AI: Accesses Google's Gemini LLMs.
###### Cloud Run: Serverless platform for deploying containerized agents and functions.
###### Cloud SQL: PostgreSQL database for curriculum data.
###### Pub/Sub & Eventarc: Foundation of the event-driven architecture, enabling asynchronous communication between components.
###### Cloud Storage: Stores audio recaps and assignment files.
###### Secret Manager: Securely manages database credentials.
###### Artifact Registry: Stores Docker images for the agents.
###### Compute Engine: To deploy self-hosted LLM instead of relying on vendor solutions