#### Concept of Embeddings

Embeddings represent content as a list of numbers called a vector.

For example, if you assign two-dimensional representations to a few words (“carrot”, “potato”, and “horse”), you may notice that “carrot” and “potato” are much closer to each other in this embedding space than they are to “horse”.


The embeddings in this case are the X and Y coordinates that represent each word’s position in this “embedding space”. A shorter distance between embeddings indicates greater similarity between the words represented.

In practice, embeddings have more than two dimensions. Google embeddings are typically 768 dimensions. You will hear them described interchangeably as embeddings, embedding vectors, or vectors. A very useful feature of embeddings is that multiple embeddings can be combined to represent a group of words, sentences, or even paragraphs.

#### Chunking 
Chunking is a very important part of this processing as well, because the meaning of a sentence is often related to the previous sentence or the section heading or page title. Then you vectorize it.


An embedding model processes the chunks of data and encodes the semantic meaning into embedding vectors. Those vectors are stored for subsequent lookup and indexed to make it faster to conduct similarity searches on queries. At runtime, when a user enters a query, you probably should perform a spell check and possibly create a few versions of their query.


#### AI Applications 
AI Applications data stores are responsible for the end-to-end search and discovery process of managing Extract-Transform-Load (ETL) of documents, Optical character recognition (OCR) where needed, chunking, embedding, indexing, storing, input cleaning, schema adjustments, information retrieval, and semantic and token-based search. And AI Applications apps are responsible for serving an app experience that receives user inputs, queries and retrieves relevant chunks from one or more data stores, passes those chunks to a model for a relevant response, and then presents the response and relevant documents to the user.

