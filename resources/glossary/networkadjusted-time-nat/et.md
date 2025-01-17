---
term: (NAT)

---
Universaalaja hindamine, mis on kehtestatud võrgusõlmede kellade alusel. Iga sõlmpunkt arvutab oma NAT-i, võttes oma kohaliku kella (UTC) ja nende sõlmede kellaaja erinevuste mediaani, millega ta on ühendatud, ning lisades seejärel oma kohaliku kella nende erinevuste mediaanile, maksimaalselt 70 minutit. Võrguga korrigeeritud aeg on seega iga sõlme poolt lokaalselt arvutatud sõlme aegade mediaan. Seda võrdlusraamistikku kasutatakse seejärel plokkide ajatemplite kehtivuse kontrollimiseks. Selleks, et üks sõlm saaks ploki heaks kiita, peab selle ajatempel olema MTP (11 viimase kaevandatud ploki mediaan) ja NAT-i pluss 2 tundi:

```text
MTP < Valid Timestamp < (NAT + 2h)
```