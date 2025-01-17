---
term: ADDRV2

---
Navrhovaná evoluce zprávy `addr` v síti Bitcoin pomocí protokolu BIP155. Zpráva `addr` se používala k vysílání adres uzlů, které přijímaly příchozí spojení, ale byla omezena na 128bitové adresy. Tato velikost byla dostatečná pro adresy IPv6, IPv4 a Tor V2, ale nedostatečná pro ostatní protokoly. Aktualizovaná verze `addrv2` je navržena tak, aby podporovala delší adresy, včetně 256bitových skrytých služeb Tor v3, a také další síťové protokoly, například I2P nebo budoucí protokoly.