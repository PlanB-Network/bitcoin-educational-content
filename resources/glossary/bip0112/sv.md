---
term: BIP0112
definition: Introduktion av opkoden OP_CHECKSEQUENCEVERIFY (CSV) som gör det möjligt att skapa relativa tidslås i skript.
---

Introducerar opkoden `OP_CHECKSEQUENCEVERIFY` (CSV) i Bitcoin Script-språket. Denna operation gör det möjligt att skapa transaktioner vars giltighet träder i kraft först efter en viss fördröjning i förhållande till en tidigare transaktion, definierad antingen i antal block eller i tidslängd. i `OP_CHECKSEQUENCEVERIFY` jämförs värdet högst upp i stacken med värdet i fältet `nSequence` i indata. Om det är större och alla andra villkor är uppfyllda är skriptet giltigt. Således begränsar `OP_CHECKSEQUENCEVERIFY` de möjliga värdena för fältet `nSequence` i den indata som används, och detta fält `nSequence` begränsar i sin tur när den transaktion som innehåller denna indata kan inkluderas i ett block. BIP112 introducerades via en Soft Fork den 4 juli 2016, tillsammans med BIP68 och BIP113, som för första gången aktiverades med BIP9-metoden.