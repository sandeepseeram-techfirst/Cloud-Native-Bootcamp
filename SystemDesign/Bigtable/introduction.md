# Bigtable

Bigtable is a sparse, distributed, persistent multi-dimensional sorted map. 

With the advent of **hyperscale services** such as:

- Worldwide search engines
- Online shopping platforms
- Messaging applications
- And other internet-scale applications

...the limitations of **traditional databases** (based on the **relational data model**) became increasingly apparent.

These limitations fall into two main categories:

1. **Scalability Challenges** – Difficulty in handling growing data volumes and user loads across distributed environments.
2. **Performance Challenges** – Inability to maintain low latency and high throughput at massive scale.


In traditional databases, we have two-dimensional layouts. Each cell is determined by a row ID and column name. On the other hand, Bigtable has the following four dimensions.

Row key: It uniquely determines the row.
Column family: This depicts a group of columns.
Column name: It uniquely determines the column.
Timestamp: The columns can have different versions of a value uniquely determined by timestamps.