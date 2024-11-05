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


##### LLMs: The "brains" of the system:

1. Google's Gemini models: (Gemini 1.0 Pro, Gemini 2 Flash, Gemini 2 Flash Thinking, Gemini 1.5-pro) Used for lesson planning, content generation, dynamic HTML creation, quiz explanation and combining the assignments.
2. DeepSeek: Utilized for the specialized task of generating self-study assignments