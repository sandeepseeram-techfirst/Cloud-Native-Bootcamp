# Vertex AI Agent Builder – Creating a Data Store for Search

## Overview
Vertex AI Agent Builder simplifies creating search and recommendation engines using structured and unstructured data. This guide focuses on building **generic search experiences**.

---

## Types of Data Stores

### 1. Website Indexing
- Publicly accessible websites can be indexed using Google Search's existing indexed data.

### 2. Structured Data
- Examples: BigQuery, JSON (NDJSON / JSON Lines), product catalogs, provider directories.
- Structured data follows a schema.

### 3. Unstructured Data
- Examples: HTML, PDFs, plain text, slides.
- Does **not** follow a schema.

### 4. Third-party Data Sources (Preview)
- Supported connectors (in allowlist): **Confluence, Jira, Salesforce**
- Sync entities like issues (Jira), content/spaces (Confluence).
- Structured by nature and grouped under connector instances.

---

## Steps to Create a Basic Search Engine

### Step 1: Select Data Type
- Options: Website, Unstructured, Structured (1st or 3rd party).
- Data must be from:
  - BigQuery
  - Cloud Storage
  - Public website
  - Supported 3rd party connectors

### Step 2: Prepare the Data

#### For Cloud Storage:
- **Structured:** NDJSON or JSON Lines
- **Unstructured:** Optional metadata (stored in Cloud Storage or BigQuery)

#### PDF Handling (Preview Features):
- Enable **OCR** for scanned or image-based PDFs.
- For text-based PDFs, OCR is optional.
- Use `native_text = true` and `enhanced_document_elements = table` for better table parsing.
- Parsed documents can be uploaded as JSON with text, tables, and lists.

#### For BigQuery:
- Data is already structured; no extra transformation needed.

#### For Public Websites:
- Google Search indexing is used, and results are immediately available.

#### For 3rd Party Connectors:
- Requires authentication and sync schedule setup.

---

### Step 3: Schema Configuration for Structured Data

#### Options:
1. **Auto-detect schema** (Recommended for initial use, but lower quality results)
2. **Edit auto-detected schema** (Re-indexing required)
3. **Provide custom JSON schema** (Manual but fastest and most accurate)

#### Important Schema Fields:
- **Key Property Mapping:** Title, Description, URI, Category
- **Primitive Types:** boolean, object, array, number, string, integer

#### Field Options:
- **Indexable:** Supports filtering, boosting, sorting
- **Searchable:** Reverse index support
- **Retrievable:** Field included in search response
- **Dynamic Facetable:** Organize results into section headers
- **Completable:** Supports query suggestions

---

## Final Steps

### Import and Link Data
- Import as documents into the data store.
- Create an engine (Search or Chat) and link data stores.
- **Blended Search:** An engine can use multiple data stores for querying diverse data types.

---
