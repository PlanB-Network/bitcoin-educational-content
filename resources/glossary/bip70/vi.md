---
term: BIP70

---
Interactive payment protocol for Bitcoin. It enables the sending of payment requests and the secure and standardized receipt of payments. In this protocol, the client clicks on a Bitcoin URI (BIP21) extended with an additional parameter (described in BIP72). The payment request is signed with the merchant's SSL certificate. Upon receiving and validating this request, the payment details are automatically filled in the client's wallet transaction interface. This protocol provides payment confirmation and enhances security and user experience by clarifying the payment's beneficiary entity. This method proposed in BIP70 was never widely adopted by merchants.