---
term: TRANSACTIEGETUIGE
---

Verwijst naar een onderdeel van Bitcoin transacties dat werd verplaatst met SegWit Soft Fork naar Address het probleem van de vervormbaarheid van transacties. De getuige bevat de handtekeningen en publieke sleutels die nodig zijn om de bitcoins te ontsluiten die in een transactie zijn uitgegeven. In legacy transacties vertegenwoordigde de getuige de som van `scriptSig` van alle ingangen. In SegWit transacties vertegenwoordigt de getuige de som van `scriptWitness` voor elke invoer, en dit deel van de transactie wordt nu verplaatst naar een aparte Merkle Tree binnen het blok.


Vóór SegWit konden handtekeningen licht gewijzigd worden zonder ongeldig gemaakt te worden voordat een transactie bevestigd werd, waardoor de identificatiecode van de transactie veranderde. Dit maakte het moeilijk om verschillende protocollen te bouwen, omdat de identifier van een onbevestigde transactie kon veranderen. Door de getuigen te scheiden, maakt SegWit transacties niet-malleerbaar, omdat elke verandering in de handtekeningen niet langer de transactie-identifier (txid) beïnvloedt, maar alleen de getuige-identifier (WTXID). Naast het oplossen van het probleem van de vervalsbaarheid, maakt deze scheiding een verhoging van de capaciteit van elk blok mogelijk.


> ► *In het Engels wordt "témoin" vertaald als "getuige".*