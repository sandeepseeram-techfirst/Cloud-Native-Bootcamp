# Autocomplete Feature in Vertex AI Agent Builder

## Overview
Autocomplete enhances search experiences for both **structured** and **unstructured** search engines by suggesting query completions based on indexed data or user interactions.

---

## How Autocomplete Works

- **Suggestions** are based on:
  - Document content (for structured/unstructured engines)
  - Search history or user events (for website search engines via API)

- **Initialization Time**: 
  - Takes **1–2 days** after data import or traffic activity to start generating suggestions.

---

## Requirements

- Requires **real search traffic** for search history-based suggestions.
- **API requests** enable advanced features like tail suggestions and model selection.

---

## Autocomplete Models

| Model                    | Description                                                                 | Applicable To             |
|--------------------------|-----------------------------------------------------------------------------|----------------------------|
| `document`               | Suggestions from imported documents.                                       | Not for website search     |
| `completeable_fields`    | Uses text from structured data fields marked as `completeable`.             | Structured data engines    |
| `search_history`         | Based on historical search API activity.                                   | Requires traffic            |
| `user_event`             | Uses imported user search events for suggestions.                          | Structured or unstructured |

---

## Using Autocomplete via API

- Use the **`dataStores.completeQuery`** method.
- Optional parameters:
  - `includeTailSuggestions`: 
    - `true` → suggests completions of the last word in query.
    - Example: `"songs with he"` → suggestions like `"Hello World"`, `"Hello Kitty"`.
  - `autocompleteModel`: Specify the desired model (e.g., `document`, `completeable_fields`, `search_history`, `user_event`).

---
