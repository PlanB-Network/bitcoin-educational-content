---
term: ADDRV2
---

Navrhovaný vývoj s BIP155 zprávy `addr` v síti Bitcoin. Zpráva `addr` byla používána k šíření adres uzlů, které přijímají příchozí spojení, ale byla omezena na 128bitové adresy. Tato velikost byla adekvátní pro IPv6, IPv4 a Tor V2 adresy, ale nedostačující pro jiné protokoly. Aktualizovaná verze `addrv2` je navržena tak, aby podporovala delší adresy, včetně 256bitových Tor v3 skrytých služeb, stejně jako další síťové protokoly, jako je I2P nebo budoucí protokoly.