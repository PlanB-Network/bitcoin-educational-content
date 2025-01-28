---
term: ADDRV2

---
Foreslått utvikling med BIP155 av `addr`-meldingen i Bitcoin-nettverket. Addr-meldingen ble brukt til å kringkaste nodeadresser som aksepterer innkommende tilkoblinger, men den var begrenset til 128-bits adresser. Denne størrelsen var tilstrekkelig for IPv6-, IPv4- og Tor V2-adresser, men utilstrekkelig for andre protokoller. Den oppdaterte versjonen `addrv2` er utformet for å støtte lengre adresser, inkludert 256-biters skjulte Tor v3-tjenester, samt andre nettverksprotokoller som I2P eller fremtidige protokoller.