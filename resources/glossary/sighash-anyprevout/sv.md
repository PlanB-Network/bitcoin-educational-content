---
term: SIGHASH_ANYPREVOUT
definition: SigHash-förslag som gör det möjligt att inte binda signaturen till en specifik UTXO.
---

Förslag till implementering av en ny SigHash Flag-modifierare i Bitcoin, introducerad med BIP118. `SIGHASH_ANYPREVOUT` ger större flexibilitet i transaktionshanteringen, särskilt för avancerade applikationer som betalningskanaler på Lightning Network och Eltoo-uppdateringen. Med `SIGHASH_ANYPREVOUT` kan signaturen inte knytas till någon specifik tidigare UTXO (*Any Previous Output*). Används i kombination med `SIGHASH_ALL`, skulle det göra det möjligt att signera alla utdata i en transaktion, men ingen av ingångarna. Detta skulle göra det möjligt att återanvända signaturen för olika transaktioner, så länge som vissa angivna villkor är uppfyllda.


> denna SigHash-modifierare SIGHASH_ANYPREVOUT härrör från idén om SIGHASH_NOINPUT som ursprungligen föreslogs av Joseph Poon 2016 för att förbättra hans koncept för Lightning Network