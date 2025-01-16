# Configuring Search Results from Unstructured Data in Vertex AI Search

## Overview
Unstructured search engines in Vertex AI Search offer multiple ways to display search result content:

- **Summarizations**
- **Snippets**
- **Extractive Answers**
- **Extractive Segments** *(API only)*

---


## 1. Summarizations

- A synthesized **paragraph** from top search results.
- **Default:** Summarizes top **5** results (customizable).
- **Search Types:**
  - List-only results
  - Summary + list
  - Summary with follow-up Q&A (conversational)

### Customization:
- Control number of results summarized.
- Customize tone, style, and verbosity using prompts.
  - Example:  
    `"You are an expert financial advisor working for FinAnalytics. Return professional concise answers to financial experts."`

### API-Only Features:
- Use `contentSearchSpec` to specify:
  - `summarySpec.topResultsCount` (up to 5)
  - `extractiveContentSpec.maxExtractiveAnswerCount` (0 or 1)
  - `includeCitations`: Adds inline citation numbers.
  - `ignoreAdversarialQuery`: Skips unsafe/policy-violating queries.
  - `ignoreNonSummarySeekingQuery`: Skips generic/non-specific queries.

### Model Selection:
- Default: `text-bison`
- Optional: `Gemini Pro` (Public Preview)

---

## 2. Snippets

- **Short quote or sentence** under document title.
- Default: 1 snippet per result.
- Preview of relevant verbatim content.

---

## 3. Extractive Answers

- **Longer** than snippets.
- Pulls relevant passages from documents.
- Displays more detailed content than a snippet.

---

## 4. Extractive Segments *(API Only)*

- Returns **detailed content blocks** with broader context.
- Not available via UI as of now.

---

## Additional Features

### General Options:
- **Autocomplete**: Suggests query completions.
- **Feedback**: Lets users send feedback on results.
- **Safe Search**: Filters explicit/unsafe content.

### Facets:
- Used to group and organize content into sections.
- Configure by:
  - Selecting a **document field**
  - Providing a **display name** (header) for that field

---

