# Configuring Website Search Results in Vertex AI Search

## Overview
Vertex AI Search offers configurable settings for customizing website search results through widgets and APIs.

---

## General Search Engine Configuration Settings

These features can be enabled or disabled for website search engines:

- **Autocomplete**  
  Suggests letters and words based on prior queries and indexed data.

- **Feedback**  
  Allows users to provide feedback on search results.

- **Safe Search**  
  Filters explicit content, including sexual activity and graphic violence.

---

## Search Results Preview

- Google Cloud Console provides a **preview** of search results as they would appear on your website.
- Embedding the widget into your site replicates this output.

---

## Image Search with Advanced Site Search

- **Advanced Site Search** enables image searching on your website.
- Available **only via APIs and SDKs** at the time of this recording.

### Enabling Image Search: 

1. **Enable Advanced Site Search**
   - A long-running operation.
   - Indexing can take **minutes to hours**, depending on data size.

2. **Perform Image Search**
   - Use the `default_config.search` method within the `servingConfig` object.
   - Provide a **text string query** to retrieve relevant images. 

---
