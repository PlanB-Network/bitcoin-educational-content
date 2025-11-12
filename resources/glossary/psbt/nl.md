---
term: PSBT
---

Acroniem voor "Partially Signed Bitcoin Transaction". Het is een specificatie die werd geïntroduceerd met BIP174 om de manier te standaardiseren waarop onvoltooide transacties worden opgebouwd in software gerelateerd aan Bitcoin, zoals Wallet software. Een PSBT kapselt een transactie in waarvan de invoer niet volledig ondertekend mag zijn. Het bevat alle benodigde informatie voor een deelnemer om de transactie te ondertekenen zonder dat er aanvullende gegevens nodig zijn. Een PSBT kan dus 3 verschillende vormen aannemen:


- Een volledig geconstrueerde transactie, maar nog niet ondertekend;
- Een gedeeltelijk ondertekende transactie, waarbij sommige inputs ondertekend zijn en andere nog niet;
- Of een volledig ondertekende Bitcoin transactie, die geconverteerd kan worden om uitgezonden te worden op het netwerk.


Het PSBT formaat vergemakkelijkt de interoperabiliteit tussen verschillende Wallet software en signatuurapparaten (Hardware Wallet). Momenteel wordt versie 0 van de PSBT gebruikt, zoals gedefinieerd in BIP174, maar versie 2 wordt voorgesteld via BIP370.


> ► *Versie 1 van de PSBT bestaat niet. Omdat versie 0 de eerste versie was, werd de tweede versie informeel versie 2 genoemd. Ava Chow, de auteur van BIP370, besloot daarom nummer 2 aan deze nieuwe versie toe te kennen om verwarring te voorkomen.*