[ Data Source ] → [ Preprocessing ] → [ Model Inference API ] → [ Results/Action ]
                                 ↑
              [ Model Registry ]←[ Monitoring & Retraining ]




[Data Ingestion] → [Preprocessing] → [Model Inference (ML/DL)] → [API/UX Layer]
                                              ↑
                       [MLOps: Training | Monitoring | Versioning]



[Data Source] → [Connector] → [Document Processor + Indexer] → [Search Index]
                                                        ↓
                                        [LLM (for Query + Summarization)]
                                                        ↓
                                          [Frontend API/UI or Agent]
