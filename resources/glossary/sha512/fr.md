---
term: SHA512
---

Sigle pour « *Secure Hash Algorithm 512 bits* ». C'est une fonction de hachage cryptographique produisant un condensat de 512 bits. Elle a été conçue par la *National Security Agency* (NSA) au début des années 2000. Pour Bitcoin, la fonction `SHA512` n'est pas utilisée directement dans le cadre du protocole, mais elle est utilisée dans le cadre des dérivations de clés enfants au niveau applicatif, selon le BIP32 et le BIP39. Dans ces processus, elle est utilisée plusieurs fois dans l'algorithme `HMAC`, ainsi que dans la fonction de dérivation de clés `PBKDF2`. La fonction `SHA512` fait partie de la famille des SHA 2, comme `SHA256`. Son fonctionnement est d'ailleurs très similaire à cette dernière.


