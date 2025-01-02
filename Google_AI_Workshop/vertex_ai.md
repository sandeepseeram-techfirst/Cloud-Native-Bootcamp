
# Vertex AI Search: App Types and Features

## App Types

### 1. Custom Search Apps
- Combine search from various sources: public sites, structured/unstructured documents, Google Workspace, etc.

### 2. Website Search Apps
- Help users search across a website's content.
- Can incorporate additional data sources.
- Enhancements possible via meta tags.

### 3. Media Search
- Search and display fully-styled results for content like:
  - Movies
  - Articles
  - Podcasts
  - Music

### 4. Retail Search Apps
- Use the **Retail Search API** for e-commerce-related search apps.

### 5. Healthcare Search Apps
- Search **FHIR (Fast Healthcare Interoperability Resources)** data.
- FHIR is a standard API for electronic health records (EHR).

## Enterprise Edition Features (App-Level, Additional Cost)

- **Extractive Answers**: Verbatim excerpts (e.g., paragraphs, tables) from documents.
- **Extractive Segments**: Larger verbatim text blocks from documents, possibly formatted.
- **Search Tuning**: Customizes search models for industry/company-specific queries.

> 🔒 Required for all website search apps (basic or advanced).  
> ⚠️ Cannot be disabled for apps using website data stores. Disabling removes dependent features.

## Advanced LLM Features (App-Level, Additional Cost)

- **Search Summarization**: Summarizes top results from a search query.
- **Search with Follow-ups**: Multi-turn conversation support; understands query context.
- **Search with Answers & Follow-ups**:
  - Natural language processing and answer generation.
  - Combines search and Q&A over multiple interactions.

> ❌ Not supported for media or healthcare data stores.  
> ⚠️ Required for advanced website indexing. Disabling removes dependent functionality.
