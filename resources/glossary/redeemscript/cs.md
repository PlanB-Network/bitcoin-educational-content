---
term: REDEEMSCRIPT
---

Skript, který definuje konkrétní podmínky, které vstupy musí splnit, aby mohly odemknout prostředky spojené s výstupem P2SH. U UTXO P2SH obsahuje `scriptPubKey` hash `redeemScriptu`. Když transakce chce tento UTXO využít jako vstup, musí poskytnout čistý `redeemScript`, který odpovídá hashi obsaženému v `scriptPubKey`. `RedeemScript` je tedy uveden v `scriptSig` vstupu spolu s dalšími prvky nezbytnými pro splnění podmínek skriptu, jako jsou podpisy nebo veřejné klíče. Tato zapouzdřená struktura zajišťuje, že detaily podmínek výdaje zůstanou skryté až do skutečného vynaložení bitcoinů. Je to významně používáno pro Legacy P2SH multisignature peněženky.