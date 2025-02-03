---
term: MAST

---
Acronym for "Merkelised Alternative Script Tree." A technique that uses a Merkle tree to summarize an arbitrary number of spending conditions selected by the user in a receiving address, one of which must be met to spend the concerned bitcoins. The Merkle tree allows the user to choose which condition they wish to fulfill without revealing the details of the other conditions on the blockchain. This helps to reduce the fees associated with these scripts, create much more complex conditions, and, over time, improve user privacy (in addition to the use of Schnorr signatures). This concept was the subject of several proposals but was ultimately added to Bitcoin via the Taproot soft fork in 2021.

> ► *Initially, "MAST" stood for "Merklized Abstract Syntax Tree." The use within the Taproot framework no longer relates to an "Abstract Syntax Tree." However, users continued to use the term MAST. Anthony Towns thus proposed changing the original meaning while retaining this widely used acronym as: "Merklized Alternative Script Tree."*