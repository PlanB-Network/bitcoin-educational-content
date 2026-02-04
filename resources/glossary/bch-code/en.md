---
term: BCH code
definition: Error-correcting codes used in Bech32 and Bech32m addresses to detect input errors.
---

A class of error-correcting codes used to detect and correct errors in a data sequence. In other words, BCH error-correcting codes allow random errors in transmitted data to be identified and corrected, ensuring that the information arrives intact at its destination. The acronym "BCH" comes from the initials of the inventors of these codes: Bose, Ray-Chaudhuri, and Hocquenghem.

This codes are used widely in computing, notably in SSDs, DVDs and QR codes. For example, thanks to these error-correcting codes, even if a QR code is partially obscured, it is still possible to retrieve the information encoded within it.

In Bitcoin, BCH codes are used for the checksum in Bech32 and Bech32m address formats (introduced post-SegWit). They represent an improved trade-off between checksum size and error detection capability compare to the simple hash functions previously used on Legacy addresses. However within the Bitcoin context, BCH codes are used exclusively for error detection, not for error correction. Bitcoin wallet software, therefore, identifies and alerts users to errors in receiving addresses, but does not automatically correct an incorrect address. This choice is deliberate, as integrating error correction capabilities would inevitably diminish the algorithm's ability to detect errors.