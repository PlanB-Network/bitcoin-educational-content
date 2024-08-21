---
term: SPV NODE (LIGHT NODE)
---

SPV (*Simple Payment Verification*) node, mida mõnikord nimetatakse ka "light node'iks", on Bitcoin node'i kerge klient, mis võimaldab kasutajatel tehinguid valideerida ilma, et peaks terve plokiahela salvestama. SPV node salvestab ainult ploki päised ja saab teavet konkreetsete tehingute kohta, küsides seda vajadusel täisnodidelt. Seda verifitseerimise põhimõtet võimaldab Bitcoin plokkides tehingute struktuur, mis on organiseeritud krüptograafilisse akumulaatorisse (Merkle Tree).

See lähenemine on kasulik piiratud ressurssidega seadmetele, nagu mobiiltelefonid. Siiski sõltuvad SPV nodid täisnodide poolt pakutava teabe kättesaadavusest, mis tähendab lisatasandit usalduses ja seega vähem turvalisust võrreldes täisnodidega. SPV nodid ei saa tehinguid autonoomselt valideerida, kuid nad saavad kontrollida, kas tehing on plokis, konsulteerides Merkle tõestustega.