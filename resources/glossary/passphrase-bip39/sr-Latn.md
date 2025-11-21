---
term: passphrase (BIP39)
---

Opcioni lozinka koja, kada se kombinuje sa frazom za oporavak, pruža dodatni Layer nivo sigurnosti za determinističke i hijerarhijske Bitcoin novčanike. HD novčanici se obično generišu iz fraze za oporavak koja se sastoji od 12 ili 24 reči. Ova fraza za oporavak je veoma važna, jer omogućava obnavljanje svih ključeva u Wallet u slučaju gubitka. Međutim, ona predstavlja jedinstvenu tačku neuspeha (SPOF). Ako je kompromitovana, bitkoini su u opasnosti. Tu dolazi passphrase. To je opcioni lozinka, koju bira korisnik, koja se dodaje frazi za oporavak kako bi se poboljšala sigurnost Wallet. Ne treba je mešati sa PIN kodom ili običnom lozinkom, passphrase igra ulogu u derivaciji kriptografskih ključeva.


Funkcioniše u tandemu sa frazom za oporavak, modifikujući seed iz kojeg se generišu ključevi. Dakle, čak i ako neko dobije vašu frazu za oporavak, bez passphrase ne može pristupiti vašim sredstvima. Korišćenje passphrase u suštini stvara novi Wallet sa različitim ključevima. Modifikovanje (čak i minimalno) passphrase će generate drugačiji Wallet.


passphrase je proizvoljan i može biti bilo koja kombinacija karaktera koju korisnik odabere. Korišćenje passphrase nudi nekoliko prednosti. Prvo, smanjuje rizike povezane sa kompromitovanjem fraze za oporavak zahtevajući drugi faktor za pristup sredstvima. Zatim, može se strateški koristiti za kreiranje lažnih novčanika koji sadrže male količine bitkoina, u slučaju fizičke prinude da se ukradu vaša sredstva. Na kraju, njegova upotreba je zanimljiva kada se želi kontrolisati nasumičnost generisanja HD Wallet seed. passphrase mora biti dovoljno složen da izdrži napade grube sile i mora biti pouzdano sačuvan. Gubitak passphrase može dovesti do nemogućnosti pristupa sredstvima, baš kao i gubitak fraze za oporavak.


> ► *passphrase se ponekad naziva i: "dvofaktorska seed fraza," "lozinka," "seed ekstenzija," "ekstenziona reč," ili čak "13. ili 25. reč." Vredi napomenuti da postoje dve vrste lozinki na Bitcoin. Najpoznatija je ona opisana gore, koja zavisi od BIP-39, i omogućava obezbeđivanje čitavog HD Wallet. Međutim, BIP-38 je takođe specificirao način za obezbeđivanje jedinstvenog privatnog ključa sa passphrase. Ovaj drugi tip passphrase se danas gotovo više ne koristi.*