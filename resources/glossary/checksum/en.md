---
term: CHECKSUM
---

The checksum is a value calculated from a set of data, used to verify the integrity and validity of that data during transmission or storage. Checksum algorithms are designed to detect accidental errors or unintentional alterations to data, such as transmission errors or file corruption. Different types of checksum algorithms exist, such as parity checks, modular checksums, cryptographic hash functions, or BCH (*Bose, Ray-Chaudhuri and Hocquenghem*) codes.

On Bitcoin, checksums are used at the application level to ensure the integrity of receiving addresses. A checksum is calculated from the payload of a user's address, then added to that address to detect any errors in its input. A checksum is also present in recovery phrases (mnemonics).

> ► *It is generally accepted to use the English term "checksum" directly in French.*