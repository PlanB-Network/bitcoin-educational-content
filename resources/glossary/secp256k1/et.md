---
term: SECP256K1

---
Nimi, mis on antud konkreetsele elliptilisele kõverale, mida kasutatakse Bitcoini protokollis ECDSA (*Elliptic Curve Digital Signature Algorithm*) ja Schnorr digitaalallkirja algoritmide rakendamiseks. Bitcoini leiutaja Satoshi Nakamoto valis kõveraks `secp256k1`. Sellel on mõned huvitavad omadused, eelkõige jõudluse eelised.

Bitcoinis tähendab "secp256k1" kasutamine seda, et iga privaatne võti (juhuslik 256-bitine number) vastab vastavale avalikule võtmele, milleks liidetakse ja kahekordistatakse privaatse võtme punkt "secp256k1" kõvera generaatori punktiga. Seda operatsiooni on lihtne teostada ühes suunas, kuid praktiliselt võimatu ümber pöörata, mis on Bitcoini digitaalallkirjade turvalisuse aluseks.

`secp256k1` kõver on määratud elliptilise kõvera võrrandiga $y^2 = x^3 + 7$, mis tähendab, et selle koefitsiendid $a$ on võrdsed $0$ ja $b$ on võrdsed $7$ elliptilise kõvera üldisel kujul $y^2 = x^3 + ax + b$. `secp256k1` on defineeritud lõpliku välja kohal, mille järjestus on väga suur algarv, täpsemalt $p = 2^{256} - 2^{32} - 977$. Kõveral on ka rühmakorraldus, mis on erinevate punktide arv kõveral, etteantud generaatorpunkt (ehk punkt $G$), mida kasutatakse krüptograafilistes operatsioonides võtmepaaride genereerimiseks, ja kofaktor, mis on võrdne $1$.

> ► *"SEC" tähendab "Tõhusa krüptograafia standardid". "P256" näitab, et kõver on defineeritud väljal $\mathbb{Z}_p$, kus $p$ on 256-bitine algarv. "K" viitab selle leiutaja Neal Koblitzi nimele. Lõpuks näitab "1", et tegemist on selle kõvera esimese versiooniga.*