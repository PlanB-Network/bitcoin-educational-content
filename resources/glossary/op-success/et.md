---
term: OP_SUCCESS
---

`OP_SUCCESS` tähistab opcode'ide seeriat, mis olid minevikus keelatud ja on nüüd reserveeritud tulevikuks kasutamiseks Tapscriptis. Nende lõppeesmärk on hõlbustada skriptikeele uuendusi ja laiendusi, võimaldades uute funktsionaalsuste tutvustamist pehmete tarkvarauuenduste kaudu. Kui skriptis kohatakse ühte neist opcode'idest, näitab see selle skripti osa automaatset õnnestumist, olenemata kohal olevatest andmetest või tingimustest. See tähendab, et skript jätkab täitmist ilma veata, sõltumata eelnevatest toimingutest.

Seega, kui uus opcode lisatakse `OP_SUCCESS` peale, tähendab see tingimata rangema reegli lisamist kui eelmine. Uuendatud noodid saavad seejärel kontrollida selle reegli järgimist ja uuendamata noodid ei keeldu seotud tehingutest ja blokkidest, mis neid sisaldavad, kuna `OP_SUCCESS` valideerib selle skripti osa. Seetõttu ei toimu kõva tarkvarauuendust.

Võrdluses, `OP_NOP` (*No Operation*) toimib samuti skriptis kohatäitjatena, kuid neil ei ole skripti täitmisel mingit mõju. Kui skriptis kohatakse `OP_NOP`, jätkub skript lihtsalt ilma virna olekut või skripti kulgu muutmata. Peamine erinevus on seega nende mõjus täitmisele: `OP_SUCCESS` tagab eduka läbimise sellest skripti osast, samas kui `OP_NOP` on neutraalne ja ei mõjuta ei virna ega skripti kulgu. Neid opcode'e tähistatakse `OP_SUCCESSN`, kus `N` on number, mida kasutatakse `OP_SUCCESS` eristamiseks.