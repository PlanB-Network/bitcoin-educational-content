---
term: BIP0381

definition: Funções pk(), pkh() e sh() para descrever scripts Legacy nos descriptors.
---
Introduz funções para descritores, notadamente `pk(KEY)` (Pay-to-PubKey), `pkh(KEY)` (Pay-to-PubKey-Hash), e `sh(SCRIPT)` (Pay-to-Script-Hash). Estas funções padronizam a maneira de descrever tipos de scripts Legacy em descritores. BIP381 foi implementado junto com todos os outros BIPs relacionados a descritores (exceto BIP386) na versão 0.17 do Bitcoin Core.