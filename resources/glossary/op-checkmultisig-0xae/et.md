---
term: OP_CHECKMULTISIG (0XAE)

---
Kontrollib mitut allkirja mitme avaliku võtme vastu. See võtab sisendiks "N" avaliku võtme ja "M" allkirja, kus "M" võib olla väiksem või võrdne "N". `OP_CHECKMULTISIG` kontrollib, kas vähemalt `M` allkirja vastab `N` avalikust võtmest `M`-le. Pange tähele, et ajaloolise off-by-one vea tõttu eemaldab `OP_CHECKMULTISIG` virnast täiendava elemendi. Seda elementi nimetatakse "*dummy elemendiks*". Et vältida viga `scriptSig`is, lisatakse seega `OP_0`, mis on kasutu element, et rahuldada eemaldamist ja vältida viga. Alates BIP147-st (mis võeti kasutusele koos SegWitiga 2017. aastal) peab vea tõttu tarbetu element olema `OP_0`, et skript oleks kehtiv, sest see oli malleerimisvektor. See opkood eemaldati Tapscriptis.
