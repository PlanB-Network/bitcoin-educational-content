---
term: CHECKSUM

---
A checksum is a calculated value from a set of data, used to verify the integrity and validity of that data during its transmission or storage. Checksum algorithms are designed to detect accidental errors or unintended alterations of data, such as transmission errors or file corruptions. Various types of checksum algorithms exist, such as parity checks, modular checksums, cryptographic hash functions, or BCH codes (*Bose, Ray-Chaudhuri, and Hocquenghem*).

In Bitcoin, checksums are used at the application level to ensure the integrity of receiving addresses. A checksum is calculated from the payload of a user's address, then added to this address to detect possible errors during its entry. A checksum is also present in recovery phrases (mnemonic).

> ► *The English translation of "somme de contrôle" is "checksum". It is generally accepted to directly use the term "checksum" in French.*