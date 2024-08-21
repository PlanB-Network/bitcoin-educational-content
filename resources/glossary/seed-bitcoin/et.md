---
term: SEED (BITCOIN)
---

Bitcoin'i kontekstis on seeme 512-bitine väärtus, mida kasutatakse kõigi HD (Hierarhiliselt Deterministliku) rahakoti seotud privaat- ja avalike võtmete tuletamiseks. Tehniliselt on seeme erinev väärtus taastefraasist (või mnemoonikast). Fraas, mis tavaliselt koosneb 12 või 24 sõnast, genereeritakse pseudojuhuslikul viisil entroopia allikast ja täiendatakse kontrollsummaga. See fraas hõlbustab inimvarundust, pakkudes tekstilist esitust rahakoti aluseks olevast väärtusest.

Tegeliku seemne saamiseks töödeldakse taastefraasi, võimalik, et koos valikulise paroolifraasiga, läbi PBKDF2 algoritmi (*Password-Based Key Derivation Function 2*). Selle arvutuse tulemus on 512-bitine seeme. Just seda seemet kasutatakse deterministlikult peavõtme genereerimiseks ja seejärel kogu võtmekomplekti jaoks HD rahakotis, vastavalt BIP32-le.

![](../../dictionnaire/assets/31.png)

> ► *Siiski, üldkeeles viitavad enamik bitcoinereid mnemoonilisele fraasile, kui nad räägivad "seemnest," mitte vahepealsele tuletamisetapile, mis jääb mnemoonilise fraasi ja peavõtme vahele.*