---
term: OPIS IZLAZNOG SKRIPTA
---

Izlazni skript deskriptori, ili jednostavno deskriptori, su strukturirani izrazi koji u potpunosti opisuju izlazni skript (`scriptPubKey`) i pružaju sve potrebne informacije za praćenje transakcija prema ili od specifičnog skripta. Ovi deskriptori olakšavaju upravljanje ključevima u HD novčanicima kroz standardni opis strukture i tipova adresa koje se koriste.


Glavna prednost deskriptora leži u njihovoj sposobnosti da enkapsuliraju sve bitne informacije za obnavljanje Wallet u jednom nizu (pored fraze za oporavak). Čuvanjem deskriptora sa odgovarajućim Mnemonic frazama, moguće je obnoviti ne samo privatne ključeve već i preciznu strukturu Wallet i pridružene parametre skripte. Naime, obnavljanje Wallet zahteva ne samo poznavanje početnog seed već i specifične indekse za derivaciju parova ključeva potomaka, kao i `xpub` svakog faktora u slučaju Multisig Wallet. Ranije se pretpostavljalo da su ove informacije implicitno poznate svima. Međutim, sa diverzifikacijom skripti i pojavom složenijih konfiguracija, ove informacije bi mogle postati teške za ekstrapolaciju, čime se ovi podaci pretvaraju u privatne i Hard-za-bruteforce informacije. Korišćenje deskriptora uveliko pojednostavljuje proces: dovoljno je znati frazu(e) za oporavak i odgovarajući deskriptor da bi se sve obnovilo pouzdano i sigurno.


Opis se sastoji od nekoliko Elements:


- Skripte funkcije kao što su `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature), i `sortedmulti` (Multisignature sa sortiranim ključevima);
- Putanje derivacije, na primer, `[d34db33f/44h/0h/0h]` označavajući izvedenu putanju i specifičan otisak prsta glavnog ključa;
- Ključevi u različitim formatima kao što su heksadecimalni javni ključevi ili prošireni javni ključevi (`xpub`);
- Kontrolni zbir, prethodi mu Hash, za verifikaciju integriteta deskriptora.


Na primer, opis za P2WPKH Wallet mogao bi izgledati ovako:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

U ovom opisu, funkcija derivacije `wpkh` označava Pay-to-Witness-Public-Key-Hash tip skripte. Sledi putanja derivacije koja sadrži:


- `cdeab12f`: otisak prsta glavnog ključa;
- `84h`: što označava korišćenje BIP84 svrhe, namenjene za SegWit v0 adrese;
- `0h`: što ukazuje da je to BTC valuta na Mainnet;
- `0h`: što se odnosi na specifičan broj računa korišćen u Wallet.


Opis takođe uključuje prošireni javni ključ korišćen u ovom Wallet:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Dalje, notacija `/<0;1>/*` specificira da deskriptor može generate adrese iz eksterne (`0`) i interne (`1`) lanca, sa džoker znakom (`*`) koji omogućava sekvencijalnu derivaciju više adresa na konfigurisani način, slično upravljanju "gap limitom" na tradicionalnom Wallet softveru.


Konačno, `#jy0l7nr4` predstavlja kontrolni zbir za proveru integriteta deskriptora.