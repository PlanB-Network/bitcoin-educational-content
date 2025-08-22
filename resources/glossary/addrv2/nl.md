---
term: ADDRV2
---

Voorgestelde evolutie met BIP155 van het `addr` bericht op het Bitcoin netwerk. Het `addr` bericht werd gebruikt om knooppuntadressen uit te zenden die inkomende verbindingen accepteerden, maar het was beperkt tot 128-bit adressen. Deze grootte was voldoende voor IPv6, IPv4 en Tor V2 adressen, maar onvoldoende voor andere protocollen. De bijgewerkte versie `addrv2` is ontworpen om langere adressen te ondersteunen, inclusief 256-bits Tor v3 verborgen diensten, evenals andere netwerkprotocollen zoals I2P of toekomstige protocollen.