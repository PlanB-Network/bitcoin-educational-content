---
term: BIP0070
---

Interactive payment protocol for Bitcoin. 
It enables merchants to send payment requests and receive payments in a secure and standardized way. 
In this protocol, the customer clicks on a Bitcoin URI (BIP21) extended with an additional parameter (described in BIP72). The payment request is signed with the merchant's SSL certificate. Once the wallet receives and validates this request, the payment details are automatically populated in the customer's wallet interface. 
This protocol provides payment confirmation and improves both security and user experience by clearly identifying the payment recipient.
However, BIP70 was never widely adopted by merchants.