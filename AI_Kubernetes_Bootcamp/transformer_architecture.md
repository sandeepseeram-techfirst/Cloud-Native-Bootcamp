# Transformer Architecture 

A transformer model uses an encoder-decoder architecture, where the encoder maps the input sequences/tokens through a self-attention mechanism. 

This mapped data is used by the decoder to generate the output sequence.

The mapping of input tokens retains not only their intrinsic values but also their context and weight in the original sequence.


### Input Embeddings

this is a key part of the transformer model, which converts input sequences/tokens into high-dimensional vector embeddings.
In real-world applications, output embeddings from a trained model may be stored in high-dimensional vector databases, such as Elasticsearch, Milvus, or PineCone. 

