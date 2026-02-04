---
term: BIP0075
definition: Extension of BIP70 adding signing of payment requests and encryption of responses. Never widely adopted.
---

Extension that enhances the BIP70 payment protocol by introducing two major innovations. 
First, it allows the sender of a payment request to voluntarily sign this request and provide a certificate that enables the recipient to verify the sender's identity. 
Second, it encrypts the returned payment request to prevent any interception and ensure that only the participants can view the payment details. 
These improvements strengthen transaction security and privacy while also introducing features to enhance the user experience.
However, because BIP75 builds upon BIP70, it was never widely adopted.