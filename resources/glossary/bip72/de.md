---
term: BIP72
---

Ergänzt BIP70 und BIP71, indem die Erweiterung des Bitcoin-URI (BIP21) mit einem zusätzlichen Parameter `r` definiert wird. Dieser Parameter ermöglicht es, einen Link zu einer sicheren Zahlungsanforderung einzuschließen, die mit dem SSL-Zertifikat des Händlers signiert ist. Wenn ein Kunde auf diesen erweiterten URI klickt, kontaktiert sein Wallet den Server des Händlers, um Zahlungsdetails anzufordern. Diese Details werden automatisch in der Transaktionsschnittstelle des Wallets ausgefüllt, und der Kunde kann darüber informiert werden, dass er den Domaininhaber bezahlt, der dem Signaturzertifikat entspricht (zum Beispiel "pandul.fr"). Da diese Verbesserung zusammen mit BIP70 gebündelt ist, wurde sie nie weit verbreitet.