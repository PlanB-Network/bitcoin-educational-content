---
term: P2SH-P2WSH
---

P2SH-P2WSH steht für *Pay to Script Hash - Pay to Witness Script Hash*. Es handelt sich um ein standardisiertes Skriptmodell, das verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen, auch bekannt als "Nested SegWit".

P2SH-P2WSH wurde mit der Implementierung von SegWit im August 2017 eingeführt. Dieses Skript beschreibt ein P2WSH, das in einem P2SH eingebettet ist. Es sperrt Bitcoins basierend auf dem Hash eines Skripts. Der Unterschied zu einem klassischen P2WSH besteht darin, dass das Skript im `redeemScript` eines klassischen P2SH eingebettet ist.

Dieses Skript wurde bei der Einführung von SegWit erstellt, um dessen Annahme zu erleichtern. Es ermöglicht die Verwendung dieses neuen Standards, auch bei Diensten oder Wallets, die noch nicht nativ mit SegWit kompatibel sind. Heute ist es daher nicht mehr sehr relevant, diese Arten von eingebetteten SegWit-Skripten zu verwenden, da die meisten Wallets natives SegWit implementiert haben. P2SH-P2WSH-Adressen werden mit der `Base58Check`-Kodierung geschrieben und beginnen immer mit `3`, wie jede P2SH-Adresse.