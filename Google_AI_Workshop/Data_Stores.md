#### Data Stores

Data stores allow you to easily connect your generative AI applications to many sources of data.

There are many Google-provided data stores that allow your apps to query data from BigQuery, Cloud Storage, Cloud SQL databases, Google Drive, Gmail, Google Calendar, and more. There are also third-party connectors, allowing your apps to query data from other popular file storage, ticketing, customer-relationship management, chat, and project management platforms.

All of these data stores provide semantic retrieval.

“Semantic” means “based on the meaning”.

#### What is RAG? 

Technique of chunking data, searching for the relevant chunks at query time, and then building a generative response based on those chunks is called Retrieval-Augmented Generation ( or “RAG”).

Data Stores automate the process of connecting to your data, splitting it into smaller sections called chunks, then generating numeric representations of your data called embeddings. Those embeddings are then typically indexed so that when a user asks a question or looks for a small piece of information, the relevant “chunk” can be retrieved quickly.

