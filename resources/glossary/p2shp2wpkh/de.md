---
term: P2SH-P2WPKH

---
P2SH-P2WPKH steht für *Pay to Script Hash - Pay to Witness Public Key Hash*. Es handelt sich um ein Standard-Skriptmodell, das zur Festlegung von Ausgabebedingungen auf einem UTXO verwendet wird, auch bekannt als "Nested SegWit".

P2SH-P2WPKH wurde mit der Einführung von SegWit im August 2017 eingeführt. Dieses Skript ist ein P2WPKH, das in ein P2SH verpackt ist. Es sperrt Bitcoins basierend auf dem Hash eines öffentlichen Schlüssels. Der Unterschied zum klassischen P2WPKH besteht darin, dass das Skript in das `redeemScript` eines klassischen P2SH eingewickelt ist.

Dieses Skript wurde bei der Einführung von SegWit erstellt, um seine Einführung zu erleichtern. Es ermöglicht die Nutzung dieses neuen Standards, auch mit Diensten oder Wallets, die noch nicht nativ mit SegWit kompatibel sind. Es handelt sich um eine Art Übergangsskript zum neuen Standard. Heutzutage ist es daher nicht mehr sehr relevant, diese Art von verpackten SegWit-Skripten zu verwenden, da die meisten Wallets natives SegWit implementiert haben. P2SH-P2WPKH-Adressen werden in `Base58Check`-Kodierung geschrieben und beginnen immer mit `3`, wie jede P2SH-Adresse.

> ► *`P2SH-P2WPKH` wird manchmal auch `P2WPKH-nested-in-P2SH` genannt