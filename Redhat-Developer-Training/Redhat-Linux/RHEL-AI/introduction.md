# Redhat Linux AI

Red Hat Enterprise Linux (RHEL) AI addresses this challenge by providing a low-cost, security-focused, single-server environment to experiment with large language models. RHEL makes it easy for users with little to no data science expertise to start developing and enhancing large language models without any data privacy or security concerns. 

# How are LLMs created?

### LLM workflow stages 

![Workflow Stages](image.png)


### Data collection
Large language models get their name from the vast amount of data required to train a model. This data is collected from various sources such as websites, blogs, scientific publications, books, etc. The collected data will need to be cleaned up to ensure that it is appropriate for use in training the model.

### Pre-training
Pre-training refers to training a model to get a more generalized understanding of the data set and its underlying language. For example, given a word, the pre-trained model will be able to predict the next word in a sequence. This is a computationally intensive phase because the size of the data is very large and it requires a large number of accelerators to support the training.

### Fine-tuning
Fine-tuning takes the model toward the next step in understanding a specific task, such as translating a sentence from one language to another, classifying the sentiment in the given text, answering questions, etc. Alignment tuning, consisting of instruction tuning and reference tuning, can also be considered phases of fine-tuning. 

### Evaluation
Once a model is fine-tuned and ready for use, the next step is to continuously evaluate the model for accuracy and performance. If the model does not perform satisfactorily, then it is likely that the data may have changed (i.e., new data has come into the picture). At this stage, we need to retrain the model. 