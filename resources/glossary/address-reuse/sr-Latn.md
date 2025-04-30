---
term: Address PONOVNA UPOTREBA
---

Ponovna upotreba Address odnosi se na praksu korišćenja istog prijemnog Address za blokiranje više UTXO-a, ponekad unutar nekoliko različitih transakcija. Bitkoini se obično zaključavaju korišćenjem kriptografskog para ključeva koji odgovara jedinstvenom Address. Pošto je Blockchain javan, lako je videti koje adrese su povezane sa koliko bitkoina. U slučaju ponovne upotrebe istog Address za više plaćanja, razumno je pretpostaviti da svi povezani UTXO-i pripadaju istoj entitetu. Stoga, ponovna upotreba Address predstavlja problem za privatnost korisnika. Omogućava determinističke veze između više transakcija i UTXO-a, kao i perpetuiranje praćenja sredstava On-Chain. Satoshi Nakamoto je već pomenuo ovaj problem u svom Belom Papiru:


> "*Kao dodatni firewall, novi par ključeva mogao bi se koristiti za svaku transakciju kako bi se sprečilo njihovo povezivanje sa zajedničkim vlasnikom.*" - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Konsultovano na https://Bitcoin.org/Bitcoin.pdf.

Da bi se očuvala privatnost na minimumu, snažno se preporučuje da se svaki prijemni Address koristi samo jednom. Za svaku novu uplatu, prikladno je generate novi Address. Za promenu izlaza, takođe bi trebalo koristiti svež Address. Srećom, zahvaljujući determinističkim i hijerarhijskim novčanicima, postalo je veoma lako koristiti mnoštvo adresa. Svi parovi ključeva povezani sa Wallet mogu se lako regenerisati iz seed. Ovo je takođe razlog zašto Wallet softver uvek generiše novu, drugačiju Address kada kliknete na dugme „Primi“.


> ► *Na engleskom se to zove "Address Reuse".*