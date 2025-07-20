---
name: Misty Breez
description: Bowless Lightning Wallet.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez je Lightning self-holding Wallet razvijen od strane Breez-a na osnovu njihovog Software Development Kit-a i **Liquid** mreže razvijene od strane BlockStream-a.


Dolazi sa potpuno novim pristupom radu bez Lightning čvora: potencijalni **GAME CHANGER** u Bitcoin međumrežnim transferima.


U ovom vodiču, opisaćemo kako ovaj portfolio funkcioniše i pružiti vam potpuni pregled.



## Kako funkcioniše Misty Breez?



Misty Breez je implementacija bez Lightning čvora kao pozadine. Razvijena je na osnovu Breez SDK i Liquid.



Liquid je paralelna Layer mreža za Bitcoin, koja nudi značajna poboljšanja u brzini i troškovima transakcija. Ovaj Layer omogućava Misty Breez da se oslobodi Lightning čvora i umesto toga koristi usluge treće strane Exchange kao što je **Boltz** kako bi osigurala interoperabilnost između Liquid Network i Lightning Network. Ne žuri, vratićemo se na ovo.



Za sada, hajde da započnemo našu avanturu sa Misty Breez Wallet.



## Početak sa Misty Breez



Mobilna aplikacija Misty Breez dostupna je na zvaničnim platformama za preuzimanje kao što su Google Play Store (na Androidu) i Apple Store (na iOS-u). Takođe možete biti preusmereni na pravu aplikaciju sa zvanične [Misty Breez] veb stranice(https://breez.technology/misty/).



⚠️ Pazite da ne pomešate Misty Breez sa Breez Wallet.



⚠️ **VAŽNO**: Za sigurnost vaših bitkoina, neophodno je preuzeti aplikaciju sa zvaničnih platformi kako biste osigurali njenu autentičnost.



![download-misty-breez](assets/fr/01.webp)



U ovom vodiču, počećemo sa Android uređajem. Ipak, svaki od koraka i specifičnih funkcija detaljno opisanih u ovom delu primenjuje se na iOS.



Nakon instalacije, Misty Breez vam daje opciju kreiranja novog Wallet ili vraćanja starog Lightning Wallet za koji imate reči za oporavak.


U ovom vodiču odlučujemo da kreiramo novi portfolio.



⚠️Misty Breez je trenutno u fazi razvoja, pa vam savetujemo da počnete sa razumnim količinama.



![create-wallet](assets/fr/02.webp)


### Sačuvaj svoje reči za oporavak :


Jedna od prvih stvari koju treba da uradite kada kreirate novi portfolio je da napravite rezervnu kopiju svojih 12 reči za oporavak.


Evo nekoliko saveta kako da napravite rezervnu kopiju vaše rezervne fraze.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Da biste napravili rezervnu kopiju svojih fraza, izaberite meni **Preferences > Security**, zatim opciju **Check your Backup Phrase**.



![backup](assets/fr/03.webp)


Radi dodatne sigurnosti, možete takođe **kreirati PIN kod** za autentifikaciju pristupa vašem Wallet.




Pronađite svoju lokalnu valutu u mnoštvu valuta koje prihvata Misty Breez. Podesite svoju valutu iz menija **Preferences > Fiat Currencies**, zatim izaberite valutu ili valute koje su vam potrebne.



![devises](assets/fr/04.webp)



### Pravljenje vaših prvih transakcija


Ako ste već upoznati sa Breez portfoliom, uopšte vas neće odbiti intuitivni Interface od Misty Breez.



Na meniju Interface **Balance**, kliknite na opciju **Receive** da kreirate fakture za primanje vaših bitkoina na vašem Wallet.



⚠️ Misty Breez će vas zamoliti da aktivirate obaveštenja za aplikaciju u podešavanjima vašeg telefona kako biste imali pravo na Lightning Address.



Sa Misty Breez, možete:




- Primajte bitkoine na Lightning Network od **100 satoshija** do **25,000,000 satoshija**.
- Primite bitkoine na glavnoj mreži Bitcoin od **25.000 satoshija**.



![transactions](assets/fr/05.webp)



Ovde počinje magija Misty Breez.


Za razliku od Breez Wallet, koji vam pruža Lightning čvor i traži da sami pokrijete troškove otvaranja i zatvaranja platnih kanala, Misty Breez ne traži od vas ništa. Kao što je ranije pomenuto, Misty Breez čak ne radi na osnovu Lightning čvora.



Hajde da pobliže pogledamo iza kulisa.



U stvarnosti, posedujete Liquid portfolio koji je povezan sa vašim Misty Breez portfoliom. Logično, bavićete se L-BTC (Liquid Bitcoin) po fiksnim stopama povezanim sa uslugama konverzije podmorskih satoshija trećih strana koje će vam omogućiti interoperabilnost sa Lightning Network.



Kada primite uplatu na vašem Misty Breez Wallet, vaš pošiljalac vam šalje satoshije koji će proći kroz konverzionu uslugu kao što je Boltz (trenutno koristi Misty Breez), kako bi konvertovao poslate satoshije u L-BTC koji će biti primljeni na vašem Misty Breez Wallet (povezan Liquid Wallet).


Evo pojednostavljeni dijagram procesa iza kulisa.



![lnswap-in](assets/fr/06.webp)



Kliknite na Interface u meniju **Balance**, kliknite na opciju **Send** da platite Lightning Invoice.


Ubacite Lightning Invoice, Lightning Address vašeg primaoca ili jednostavno skenirajte QR kod na Invoice da izvršite uplatu.



![send-bitcoins](assets/fr/07.webp)



Iza kulisa, omogućavate Liquid Wallet povezane sa vašim Misty Breez Wallet da konvertuju ekvivalent L-BTC u satoshije putem Boltz-a, zatim prenose te satoshije na Lightning Wallet vašeg primaoca (prisutan na Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Ova funkcija infrastrukture Misty Breez omogućava korisnicima da obavljaju transakcije čak i kada je Misty Breez van mreže.



Za iskusnije, tu je i meni **Preferences > Developers** koji vam daje malo više detalja o:




- Verzija Breez Softverskog Razvojnog Kompleta.
- Javni ključ vašeg Misty Breez Wallet.
- Zajmoprimac, jedinstveni identifikator izveden iz primarnog javnog ključa.
- Stanje vašeg portfolija.
- Saveti Liquid, za slanje malih količina L-BTC.
- Bitcoin Savet, za slanje malih količina Bitcoin.



Takođe možete izvršiti određene radnje, kao što su sinhronizacija sa Liquid Network, pravljenje rezervne kopije vaših ključeva, deljenje vašeg dnevnika aktivnosti i izbor ponovnog skeniranja Liquid Network.



![dev-mode](assets/fr/09.webp)


Čestitamo! Sada imate dobro razumevanje portfolija Misty Breez i njegovog doprinosa međumrežnim transakcijama Bitcoin. Ako ste našli ovaj vodič korisnim, molimo vas da nam date Green palac. Bili bismo oduševljeni da čujemo vaše mišljenje.



Da biste išli dalje, takođe preporučujem da otkrijete naš vodič za Aqua Wallet, koji radi na sličan način kao Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125