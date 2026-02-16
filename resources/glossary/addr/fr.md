---
term: Addr
definition: Ancien message réseau Bitcoin permettant de communiquer les adresses IP des nœuds acceptant des connexions. Remplacé par addrv2 (BIP155) pour supporter des formats d'adresses plus longs.
---

Message réseau anciennement utilisé sur Bitcoin pour communiquer les adresses des nœuds qui acceptent des connexions entrantes. Cet ancien format, se limitant à 128 bits par adresse, était seulement adapté aux adresses IPv6, IPv4 et aux adresses Tor de version 2. Face à l'arrivée de nouveaux protocoles comme Tor V3 et la nécessité de disposer d'une meilleure évolutivité pour de futurs protocoles réseau, le format `addr` a été supplanté par `addrv2`, introduit dans le BIP155.
