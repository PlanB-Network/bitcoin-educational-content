---
term: P2SH-P2WSH

---
P2SH-P2WSH steht für *Pay to Script Hash - Pay to Witness Script Hash*. Es handelt sich um ein Standard-Skriptmodell, das zur Festlegung von Ausgabenbedingungen auf einem UTXO verwendet wird, auch bekannt als "Nested SegWit".

P2SH-P2WSH wurde mit der Einführung von SegWit im August 2017 eingeführt. Dieses Skript beschreibt ein P2WSH, das in ein P2SH verpackt ist. Es sperrt Bitcoins basierend auf dem Hash eines Skripts. Der Unterschied zu einem klassischen P2WSH besteht darin, dass das Skript in das `redeemScript` eines klassischen P2SH verpackt ist.

Dieses Skript wurde bei der Einführung von SegWit erstellt, um seine Einführung zu erleichtern. Es ermöglicht die Nutzung dieses neuen Standards, auch mit Diensten oder Wallets, die noch nicht nativ mit SegWit kompatibel sind. Heutzutage ist es daher nicht mehr sehr relevant, diese Art von SegWit-Skripten zu verwenden, da die meisten Wallets natives SegWit implementiert haben. P2SH-P2WSH-Adressen werden in `Base58Check`-Kodierung geschrieben und beginnen immer mit `3`, wie jede P2SH-Adresse.