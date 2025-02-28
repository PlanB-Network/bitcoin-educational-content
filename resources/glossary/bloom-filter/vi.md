---
term: BLOOM FILTER

---
A probabilistic data structure used to test if an element is part of a set. Bloom Filters allow for quick membership checks without testing the entire dataset. They are particularly useful in contexts where space and speed are critical, but a low and controlled error rate is acceptable. Indeed, Bloom Filters do not produce false negatives, but they do generate a certain amount of false positives. When an element is added to the filter, multiple hash functions generate positions in a bit array. To check for membership, the same hash functions are used. If all the corresponding bits are set, the element is probably in the set, but with a risk of false positives. Bloom Filters are widely used in the fields of databases and networks. It is notably known that Google uses them for its compressed database management system *BigTable*. In the Bitcoin protocol, they are used particularly for SPV wallets according to BIP37.

> ► *When specifically talking about the use of Bloom Filters in the context of Bitcoin transactions, the term "Transaction Bloom Filtering" is sometimes encountered.*