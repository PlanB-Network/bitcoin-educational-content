---
term: BIP72

---
Ergänzt BIP70 und BIP71 durch die Definition der Erweiterung der Bitcoin-URI (BIP21) mit einem zusätzlichen Parameter "r". Dieser Parameter ermöglicht die Aufnahme eines Links zu einer sicheren Zahlungsanforderung, die mit dem SSL-Zertifikat des Händlers signiert ist. Wenn ein Kunde auf diese erweiterte URI klickt, kontaktiert seine Wallet den Server des Händlers, um die Zahlungsdetails anzufordern. Diese Angaben werden automatisch in die Transaktionsschnittstelle der Wallet eingegeben, und der Kunde kann darüber informiert werden, dass er an den Eigentümer der Domain zahlt, die dem signierten Zertifikat entspricht (z. B. "pandul.fr"). Da diese Erweiterung mit BIP70 gebündelt ist, hat sie sich nie durchgesetzt.