---
term: OP_SUCCESS

---
`OP_SUCCESS` kujutab endast rida opkoode, mis olid minevikus välja lülitatud ja on nüüd reserveeritud edaspidiseks kasutamiseks Tapscriptis. Nende lõppeesmärk on hõlbustada skripti keele uuendusi ja laiendusi, võimaldades uute funktsioonide kasutuselevõttu soft forks'ide kaudu. Kui üks neist opkoodidest esineb skriptis, näitab see skripti selle osa automaatset õnnestumist, sõltumata olemasolevatest andmetest või tingimustest. See tähendab, et skript jätkab oma täitmist ilma tõrgeteta, sõltumata eelnevatest operatsioonidest.

Seega, kui `OP_SUCCESS'ile lisatakse uus op-kood, tähendab see tingimata rangema reegli lisamist kui eelmine. Uuendatud sõlmed saavad seejärel kontrollida selle reegli täitmist ja uuendamata sõlmed ei lükka sellega seotud tehinguid ja neid sisaldavaid plokke tagasi, sest `OP_SUCCESS` valideerib selle osa skriptist. Seetõttu ei ole kõva hargnemist.

Võrdluseks, `OP_NOP` (*No Operation*) on samuti paigutussalvestid skriptis, kuid neil ei ole mingit mõju skripti täitmisele. Kui tekib `OP_NOP`, jätkub skript lihtsalt, muutmata virna olekut või skripti kulgu. Seega on peamine erinevus nende mõju täitmisele: `OP_SUCCESS` tagab skripti selle osa eduka läbimise, samas kui `OP_NOP` on neutraalne ja ei mõjuta virna ega skripti kulgu. Neid opkoode tähistatakse `OP_SUCCESSN`, kus `N` on number, mida kasutatakse `OP_SUCCESS` eristamiseks.