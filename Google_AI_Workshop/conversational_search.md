# Conversational Search on Unstructured Data in Vertex AI Search

## Overview
Vertex AI Search supports **multi-turn, conversational-style search** on unstructured data search engines, providing a natural, context-aware search experience.

---

## Key Features

### 1. Natural Language Query Processing
- Users can submit questions in conversational language.
- The engine identifies the **intent** behind the query and returns relevant results.


### 2. Context Awareness
- Maintains memory of previous interactions.
- Provides **context-aware responses** to follow-up questions.

### 3. Multi-turn Conversations
- Supports **follow-up questions** without restating context.
- Enables **dialog-like interactions** with coherent, continuous responses.

#### Example:
- **User**: “When is the best time of year to vacation in Mexico?”
- **Follow-up**: “What is the exchange rate?”
  - The system understands context and gives a relevant response.

---

## Implementation Steps

### 1. Create a Conversation Store
- Stores conversations **per user**.
- A user can have **multiple conversations**.

### 2. Generate a Conversation ID
- Use this ID in subsequent requests to maintain context.
- Supports session continuity across requests.

### 3. Use a User Pseudo ID
- Identifies users on a single device (e.g., via HTTP cookie).

### 4. Use the `converse` Endpoint
- Supply:
  - `conversation_id`: to maintain the context.
  - `query` parameter: the user's input string.

---

## Conversation Management

- **List Conversations**:
  - Filter by user or conversation state.
  - States: `in progress` or `completed`.

- **View a Conversation**:
  - Inspect full conversation history.

- **Update State**:
  - Change a conversation’s status (e.g., mark as completed).

- **Delete Conversations**:
  - Remove conversations from the data store if needed.

---