# Using Document AI for Parsing and Chunking Documents in RAG Solutions

## Overview
Vertex AI Agent Builder integrates with **Document AI** to enable advanced document parsing and processing, useful for building RAG (Retrieval-Augmented Generation) pipelines.

---

## Document Processing API

- Core tool for parsing and processing documents using Document AI.
- Leverages the **Layout Parser** to:
  - Extract content elements: text, tables, lists, figures.
  - Detect document structure and hierarchy.
  - Enable context-aware chunking.
  - Improve generative AI applications with structured data.

---

## Capabilities of Document AI

- Parses various elements: text, images, tables, and more.
- Uses **annotators** to enrich extracted content.

### Example:
- Parsed biography of Albert Einstein.
- Extracted entities: `Country = Germany`, `Research Area = Relativity`.
- Parsed table summarizing key life events.

- Organizes content using **layout detection** under document headings.
- Breaks down documents into **chunks**, each represented by a single embedding.

---

## Limitations

- Max file size: **20 MB**
- Daily limit: **100 documents per project**
- **Batch processing is not supported**
- Supported file types: **HTML**, **PDF**, **DOCX**

### Element Detection by File Type:
- **DOCX**: Highly structured – detects paragraphs, tables, titles, lists, headings, headers, footers.
- **PDF**: Less structured – detects paragraphs, tables, titles, headings.

---

## Steps to Parse and Chunk Documents

1. **Create a Layout Parser**
   - Processor type: `LAYOUT_PARSER_PROCESSOR`

2. **Enable the Parser**
   - Use the associated processor ID.

3. **Send Document for Parsing**
   - Input document for processing and chunking. 
   - Set:
     - **Chunk Size**: Number of tokens per chunk.
     - **Include Ancestor Headings** (`true/false`): Adds context by including up to 2 levels of parent headings.

---

## Request Options (Synchronous / Online Requests)

- **Single document processing** with immediate response.

### Key Request Parameters:
- `skipHumanReview`: Boolean (only for Human-in-the-Loop processors)
- `fieldMask`: Comma-separated list of fields (e.g., `text`, `entities`, `pages.pageNumber`)
- `individualPages`: List of pages to process.
- `fromStart` / `fromEnd`: Number of pages to process from start or end.

---
