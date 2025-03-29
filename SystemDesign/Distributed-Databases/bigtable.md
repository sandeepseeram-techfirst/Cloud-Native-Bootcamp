# Bigtable

Bigtable is a distributed database — specifically a wide-column NoSQL distributed database developed by Google.

The keys have some elaborate structure to them that helps construct a table-like abstraction on top of it.

The data can be multi-versioned, which helps speed up concurrent reads and writes without locking for some use cases.

A few table columns are physically kept together to benefit from the locality.

Bigtable is a column-family database that introduced many innovations like SSTables. This system shows us how a key-value store can be a high-performance database. Bigtable does not provide strong data consistency across table rows (the guarantees are only at the key level). Additionally, the data model of Bigtable is not relational, which implies that users of Bigtable have a learning curve.