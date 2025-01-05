#### Overview
Vertex AI Search brings together the power of deep information retrieval, state-of-the-art natural language processing, and the latest in large language processing to understand user intent and return the most relevant results for the user.

##### Task 1. Enable the Discovery Engine API for AI Applications

##### Task 2. Create and preview a website search app

##### Task 3. Create and preview a structured data search app
Structured data can be used to make website content more visible to search engines. A structured data search app improves the discoverability of website content and provides users with a more relevant search experience.

##### Task 4. Create and Preview an unstructured data search app
Unstructured data is data that does not have a predefined format. This type of data can be difficult to search within using traditional search engines. An unstructured data search app can be used to make this data more accessible to gain insights that can be used to improve business operations.

Layout Parser for Vertex AI Search to identify content elements like text blocks, tables, lists, and structural elements such as titles and headings and use them to define the organization and hierarchy of a document. 

curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/290618728919/locations/global/collections/default_collection/engines/google-cloud-docs_1750494813158/servingConfigs/default_search:search" \
-d '{"query":"What are Google Support Plans","pageSize":10,"queryExpansionSpec":{"condition":"AUTO"},"spellCorrectionSpec":{"mode":"AUTO"},"languageCode":"en-US","userInfo":{"timeZone":"Asia/Calcutta"}}' 