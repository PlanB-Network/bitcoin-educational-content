---
term: Addr

definition: En gammel Bitcoin-nettverksmelding som tillot å kommunisere IP-adresser til noder som aksepterer tilkoblinger. Erstattet av addrv2 (BIP155) for å støtte lengre adresseformater.
---
Nettverksmelding som tidligere ble brukt på Bitcoin for å kommunisere adressene til noder som godtar innkommende tilkoblinger. Dette gamle formatet, begrenset til 128 bits per adresse, var bare egnet for IPv6-, IPv4- og Tor-adresser i versjon 2. Med ankomsten av nye protokoller som Tor V3 og behovet for bedre skalerbarhet for fremtidige nettverksprotokoller, ble `addr`-formatet erstattet av `addrv2`, som ble introdusert i BIP155.