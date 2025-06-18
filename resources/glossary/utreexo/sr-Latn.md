---
term: UTREEXO
---

Protokol koji je dizajnirao Tadge Dryja za kompaktiranje Bitcoin čvorova' UTXO seta koristeći akumulator zasnovan na Merkle drveću. Za razliku od klasičnog UTXO seta koji zahteva značajan prostor za skladištenje, Utreexo drastično smanjuje potrebnu memoriju tako što skladišti samo Merkle Tree korene. Ovo omogućava čvoru da verifikuje postojanje UTXO-a korišćenih u ulazima transakcija, bez potrebe da čuva kompletan set UTXO-a. Korišćenjem Utreexo-a, svaki čvor zadržava samo kriptografski otisak nazvan Merkle Root. Kada se izvrši transakcija, korisnik pruža dokaze Ownership UTXO-a i odgovarajuće Merkle putanje. Tako čvor može verifikovati transakcije bez skladištenja celog UTXO seta. Uzmimo primer sa dijagramom da bismo razumeli ovaj mehanizam:


![](../../dictionnaire/assets/15.webp)


U ovom primeru, namerno sam smanjio UTXO skup na 4 UTXO-a kako bih olakšao razumevanje. U stvarnosti, važno je zamisliti da postoji skoro 140 miliona UTXO-a na Bitcoin u trenutku pisanja ovih redova. U ovom dijagramu, Utreexo čvor bi trebao da drži samo Merkle Root u RAM-u. Ako primi transakciju koja troši UTXO br. 3 (u crnom), dokaz bi se sastojao od sledećeg Elements:


- UTXO 3;
- Hash 4;
- Hash 1-2.


Sa ovim informacijama koje je poslao pošiljalac transakcije, Utreexo čvor vrši sledeće provere:


- Izračunava otisak UTXO 3, što mu daje Hash 3;
- Konkatenira Hash 3 sa Hash 4;
- Izračunava njihov otisak, što mu daje Hash 3-4;
- Konkatenira Hash 3-4 sa Hash 1-2;
- Izračunava njihov otisak, što mu daje Merkle Root.


Ako je Merkle Root koji dobije kroz svoj proces isti kao Merkle Root koji je uskladištio u svom RAM-u, onda je uveren da je UTXO br. 3 zaista deo UTXO seta.

Ovaj metod smanjuje zahteve za RAM-om za operatere Full node. Međutim, Utreexo ima ograničenja, uključujući povećanje veličine bloka zbog dodatnih dokaza i potencijalnu zavisnost Utreexo čvorova od Bridge čvorova za dobijanje nedostajućih dokaza. Bridge čvorovi su tradicionalni puni čvorovi koji obezbeđuju potrebne dokaze Utreexo čvorovima, omogućavajući tako potpunu verifikaciju. Ovaj pristup nudi kompromis između efikasnosti i decentralizacije, čineći validaciju transakcija dostupnijom korisnicima sa ograničenim resursima.