---
term: Assume utxo
definition: Parametar Bitcoin Core-a koji omogućava brzu sinhronizaciju novog čvora upotrebom snimka UTXO skupa pretpostavljenog kao validan, pre provere istorije u pozadini.
---
Konfiguracioni parametar u većinskom klijentu Bitcoin Core koji omogućava čvoru koji je upravo inicijalizovan (ali još nije izvršio IBD) da odloži verifikaciju transakcija i UTXO seta pre određenog snimka stanja (snapshot). Koncept se zasniva na korišćenju UTXO seta (liste svih postojećih UTXO-a u datom trenutku) koji obezbeđuje Core i koji se smatra tačnim, što omogućava čvoru da se veoma brzo sinhronizuje sa lancem koji ima najviše akumuliranog rada. Pošto čvor preskače dugačku fazu IBD-a, on veoma brzo postaje funkcionalan za svog korisnika.

Assume UTXO deli sinhronizaciju (IBD) na dva dela: Prvo, čvor vrši Header First Sync (samo verifikaciju zaglavlja) i smatra važećim UTXO set koji mu dostavlja Core; Zatim, kada postane funkcionalan, čvor će u pozadini verifikovati kompletnu istoriju blokova, ažurirajući novi UTXO set koji je sam proverio. Ako se ovaj poslednji ne poklapa sa UTXO setom koji je dostavio Core, on će izdati poruku o grešci.

Assume UTXO stoga omogućava ubrzavanje pripreme novog Bitcoin čvora odlaganjem procesa verifikacije transakcija i UTXO seta zahvaljujući ažuriranom snimku stanja (snapshot) koji se dobija u Core-u.







