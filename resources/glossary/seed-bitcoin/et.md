---
term: SEED (BITCOIN)

---
Bitcoini kontekstis on seemne 512-bitine väärtus, mida kasutatakse kõigi HD (Hierarchical Deterministic) rahakotiga seotud era- ja avalike võtmete tuletamiseks. Tehniliselt on seemne väärtus erinev taastamislausest (või mnemoonikast). Fraas, mis koosneb tavaliselt 12 või 24 sõnast, genereeritakse pseudosituatsiooniliselt entroopiaallikast ja täiendatakse kontrollsummaga. See fraas hõlbustab inimese varundamist, andes tekstilise kujutise väärtusest rahakoti põhjaosas.

Tegeliku seemne saamiseks töödeldakse taastamislauset, millele võib lisada valikulise parooli, läbi PBKDF2 algoritmi (*Password-Based Key Derivation Function 2*). Selle arvutuse tulemuseks on 512-bitine seemne. Seda seemet kasutatakse selleks, et genereerida deterministlikult põhivõti ja seejärel kogu HD rahakoti võtmekomplekt vastavalt BIP32-le.

![](../../dictionnaire/assets/31.webp)

> ► *Kaasaegses keeles viitab enamik bitcoin'i kasutajaid "seemnest" rääkides mnemoonilisele fraasile, mitte aga tuletamise vahepealsele seisundile, mis asub mnemoonilise fraasi ja peavõti vahel.*