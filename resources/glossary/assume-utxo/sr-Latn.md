---
term: PRETPOSTAVI UTXO
---

Parametar konfiguracije u vodećem Bitcoin Core klijentu koji omogućava čvoru koji je upravo inicijalizovan (ali još nije prošao kroz IBD) da odloži verifikaciju transakcija i UTXO seta do datog snimka. Koncept se oslanja na korišćenje UTXO seta (lista svih postojećih UTXO-a u datom trenutku) koju obezbeđuje Core i koja se smatra tačnom, što omogućava čvoru da se vrlo brzo sinhronizuje sa lancem sa najviše akumuliranog rada. Pošto čvor preskače dugotrajan IBD korak, postaje operativan za svog korisnika vrlo brzo. Pretpostavimo da UTXO deli sinhronizaciju (IBD) na dva dela:


- Prvo, čvor izvodi Header First Sync (verifikaciju samo zaglavlja) i smatra da je UTXO skup koji je obezbedio Core validan;
- Zatim, kada postane operativan, čvor će u pozadini verifikovati kompletnu istoriju blokova, ažurirajući novi UTXO set koji je sam verifikovao. Ako se ovaj novi UTXO set ne poklapa sa onim koji je obezbedio Core, proizvešće poruku o grešci.


Stoga, pretpostavimo da UTXO ubrzava pripremu novog Bitcoin čvora odlaganjem procesa verifikacije transakcija i UTXO seta kroz ažurirani snimak obezbeđen u Core.