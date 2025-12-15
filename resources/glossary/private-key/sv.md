---
term: PRIVAT NYCKEL
---

En privat nyckel är ett grundläggande element i asymmetrisk kryptografi. Det är ett tal (256 bitar i samband med Bitcoin) som representerar en kryptografisk hemlighet. Denna nyckel används för att digitalt signera transaktioner och bevisa Ownership för en Bitcoin-offentlig nyckel (och i förlängningen en mottagande Address) genom att uppfylla en `scriptPubKey`. Privata nycklar gör det därför möjligt att spendera bitcoins genom att låsa upp de UTXO:er som är associerade med motsvarande offentliga nyckel. Privata nycklar måste hållas strikt konfidentiella, eftersom ett avslöjande av dem skulle kunna göra det möjligt för illvilliga tredje parter att ta kontroll över de tillhörande medlen.


I Bitcoin-systemet är den privata nyckeln kopplad till en publik nyckel genom en digital signaturalgoritm som använder elliptiska kurvor (ECDSA eller Schnorr). Den publika nyckeln härleds från den privata nyckeln, men det omvända är praktiskt taget omöjligt att uppnå på grund av de beräkningssvårigheter som är förknippade med att lösa det underliggande matematiska problemet (det diskreta logaritmproblemet). Den publika nyckeln används i allmänhet för att generate en Bitcoin Address, som används för att låsa bitcoins med hjälp av ett skript. Inom kryptografi är privata nycklar ofta slumpmässiga eller pseudoslumpmässiga tal. I det specifika sammanhanget med Bitcoin deterministiska och hierarkiska plånböcker härleds privata nycklar deterministiskt från seed. Privata nycklar förväxlas ofta med seed eller med återställningsfrasen (Mnemonic). Dessa Elements är dock distinkta.


> ► *På engelska kallas en privat nyckel för "private key". Denna term förkortas ibland som "privkey" eller "PV".*