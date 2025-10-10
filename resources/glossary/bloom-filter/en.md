---
term: BLOOM FILTER
---

A Bloom filter is a probabilistic data structure used to test whether an element is a member of a set. 
It enables very fast membership checks without scanning the entire dataset, making it particularly useful in contexts where memory efficiency and speed are critical, and where a small, controlled error rate is acceptable. 
Bloom filters guarantee no false negatives (if the filter says an element is not in the set, it definitely isn’t) but allow for a small probability of false positives (it may incorrectly indicate that an element is present).
When an element is added to the filter, multiple hash functions generate positions in a bit array. To check for membership, the same hash functions are used. If all the corresponding bits are set, the element is probably in the set, but with a risk of false positives. 
Bloom filters are widely used in databases and network systems. For example, *Google’s Bigtable* database management system makes use of them. In the Bitcoin protocol, Bloom filters are used for SPV wallets (Simplified Payment Verification) as specified in BIP37.

> ► *When specifically talking about the use of Bloom Filters in the context of Bitcoin transactions, the term "Transaction Bloom Filtering" is sometimes encountered.*