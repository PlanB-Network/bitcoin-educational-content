---
term: PROS. TRAJANJE RUNDE
---

Prosečno trajanje runde je pokazatelj koji se koristi za procenu vremena potrebnog da Mining pool pronađe blok, na osnovu težine mreže i Hashrate bazena. Izračunava se tako što se broj deonica potrebnih za pronalaženje bloka podeli sa Hashrate bazena. Na primer, ako Mining pool ima 200 rudara, i svaki generiše u proseku 4 deonice u sekundi, ukupna računarska snaga bazena je 800 deonica u sekundi:


```text
200 * 4 = 800
```


Pod pretpostavkom da je u proseku potrebno 1 milion akcija da bi se pronašao važeći blok, *Prosečno trajanje runde* bazena bi bilo 1.250 sekundi, ili oko 21 minut:


```text
1,000,000 / 800 = 1,250
```


U praktičnim terminima, to znači da bi Mining pool u proseku trebalo da pronađe blok na svakih 21 minut ili tako nešto. Ovaj indikator fluktuira sa promenama u Hashrate bazenu: povećanje Hashrate smanjuje *Prosečno Trajanje Runde*, dok smanjenje produžava. Takođe će fluktuirati sa svakom periodičnom prilagodbom ciljne težine Bitcoin (svakih 2016 blokova). Ova mera ne uzima u obzir blokove pronađene od strane drugih bazena i fokusira se isključivo na unutrašnje performanse bazena koji se proučava.