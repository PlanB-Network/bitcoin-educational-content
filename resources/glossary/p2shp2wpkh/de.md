---
term: P2SH-P2WPKH
---

P2SH-P2WPKH steht für *Pay to Script Hash - Pay to Witness Public Key Hash*. Es handelt sich um ein standardisiertes Skriptmodell, das verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen, auch bekannt als "Nested SegWit".

P2SH-P2WPKH wurde mit der Implementierung von SegWit im August 2017 eingeführt. Dieses Skript ist ein P2WPKH, das innerhalb eines P2SH eingebettet ist. Es sperrt Bitcoins basierend auf dem Hash eines öffentlichen Schlüssels. Der Unterschied zum klassischen P2WPKH besteht darin, dass das Skript im `redeemScript` eines klassischen P2SH eingebettet ist.

Dieses Skript wurde bei der Einführung von SegWit erstellt, um dessen Adoption zu erleichtern. Es ermöglicht die Verwendung dieses neuen Standards, auch bei Diensten oder Wallets, die noch nicht nativ mit SegWit kompatibel sind. Es handelt sich um eine Art Übergangsskript zum neuen Standard. Heute ist es daher nicht mehr sehr relevant, diese Arten von eingebetteten SegWit-Skripten zu verwenden, da die meisten Wallets native SegWit implementiert haben. P2SH-P2WPKH-Adressen werden mit der `Base58Check`-Kodierung geschrieben und beginnen immer mit `3`, wie jede P2SH-Adresse.

> ► *`P2SH-P2WPKH` wird manchmal auch als `P2WPKH-nested-in-P2SH` bezeichnet.*