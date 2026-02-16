---
term: BIP0385
definition: addr() en raw() functies voor het beschrijven van outputscripts per adres of in hexadecimaal in descriptors.
---

Introduceert de Descriptor functies `addr(ADDR)` en `raw(HEX)`. De `addr(ADDR)` functie maakt het mogelijk een uitvoerscript te beschrijven met behulp van een ontvangende Address, terwijl de `raw(HEX)` functie het mogelijk maakt een uitvoerscript te specificeren met behulp van een ruwe hexadecimale representatie van dat script. BIP385 werd geïmplementeerd samen met alle andere Descriptor gerelateerde BIPs (behalve BIP386) in versie 0.17 van Bitcoin core.