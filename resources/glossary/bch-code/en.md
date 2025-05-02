---
term: BCH CODE
---

A class of error correction codes used to detect and correct errors in a data sequence. In other words, BCH error correction codes are used to find and correct random errors in transmitted information, to ensure that it arrives intact at its destination. The acronym "BCH" stands for the initials of the names of the inventors of these codes: Bose, Ray-Chaudhuri, and Hocquenghem.

This tool is used in many areas of computing, including SSDs, DVDs and QR codes. For example, thanks to these error-correcting codes, even if a QR code is partially covered, it is still possible to retrieve the information it encodes.

As part of Bitcoin, BCH codes are used for the checksum in Bech32 and Bech32m (post-SegWit) address formats. They represent a better compromise between checksum size and error detection capability than the simple hash functions previously used on Legacy addresses. In the context of Bitcoin, BCH codes are used only for error detection, not for error correction. Thus, Bitcoin portfolio software will identify and report to the user any errors in a receiving address, but will not change the incorrect address automatically. This choice is motivated by the fact that integrating error correction inevitably affects the algorithm's error detection capabilities.