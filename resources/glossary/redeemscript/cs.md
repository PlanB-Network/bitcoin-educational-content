---
term: REDEEMSCRIPT

---
Skript, který definuje specifické podmínky, které musí vstupy splňovat, aby se uvolnily prostředky spojené s výstupem P2SH. V P2SH UTXO obsahuje `scriptPubKey` hash `redeemScript`. Když chce transakce utratit toto UTXO jako vstup, musí poskytnout čistý `redeemScript`, který odpovídá hash obsaženému ve `scriptPubKey`. `redeemScript` je tedy uveden v `scriptSig` vstupu spolu s dalšími prvky nezbytnými pro splnění podmínek skriptu, jako jsou podpisy nebo veřejné klíče. Tato zapouzdřená struktura zajišťuje, že podrobnosti podmínek utrácení zůstanou skryty, dokud nejsou bitcoiny skutečně utraceny. Používá se zejména pro starší P2SH peněženky s více podpisy.