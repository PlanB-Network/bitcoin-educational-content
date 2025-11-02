---
name: BIP-39 passphrase SeedSigner
description: Kako da dodam passphrase u svoj SeedSigner portfolio?
---

![cover](assets/cover.webp)



passphrase BIP39 je opcionalna lozinka koja, u kombinaciji sa Mnemonic frazom, pruža dodatni Layer sigurnosti za determinističke i hijerarhijske Bitcoin novčanike. U ovom vodiču ćemo zajedno otkriti kako postaviti passphrase na vašem Bitcoin Wallet korišćenom sa SeedSigner-om.



![Image](assets/fr/01.webp)



## Preduslovi pre dodavanje passphrase



Pre nego što započnete ovaj tutorijal, ako niste upoznati sa konceptom passphrase, kako funkcioniše i njegovim implikacijama za vaš Bitcoin Wallet, toplo preporučujem da se posavetujete sa ovim drugim teorijskim člankom gde sve objašnjavam (ovo je veoma važno, jer korišćenje passphrase bez potpunog razumevanja kako funkcioniše može ugroziti vaše bitkoine) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Pre nego što započnete ovaj vodič, molimo vas da se uverite da ste već inicijalizovali vaš SeedSigner i generisali vašu Mnemonic frazu. Ako niste, a vaš SeedSigner je potpuno nov, pratite vodič na Plan ₿ Academy. Kada završite ovaj korak, možete se vratiti na ovaj vodič:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Kako da dodam passphrase na SeedSigner?



Dodavanje passphrase u vaš portfelj upravljan putem SeedSigner-a stvara potpuno novi portfelj, generišući potpuno drugačiji set ključeva. Shodno tome, ako već imate portfelj koji sadrži Satss, više nećete moći da mu pristupite sa passphrase, jer on generiše potpuno drugačiji portfelj.



Da biste primenili passphrase na vaš SeedSigner, uključite uređaj i skenirajte vaš SeedQR kao i obično. SeedSigner će zatim prikazati otisak prsta vašeg trenutnog Wallet, koji odgovara onom **bez passphrase**. Wallet sa passphrase će imati drugačiji otisak prsta.



Kliknite na dugme `BIP-39 passphrase`.



![Image](assets/fr/02.webp)



Zatim unesite passphrase po vašem izboru u predviđeno polje, koristeći tastaturu na ekranu. Obavezno napravite jednu ili više fizičkih rezervnih kopija (papir ili metal): gubitak ovog passphrase će rezultirati trajnim gubitkom pristupa vašim bitcoinima. **Za vraćanje Wallet, i Mnemonic i passphrase su neophodni** Ako se bilo koji izgubi, vaši bitcoini će biti nepovratno blokirani.



Kada završite unos, potvrdite pritiskom na dugme `KEY3` u donjem desnom uglu SeedSigner-a.



![Image](assets/fr/03.webp)



*U ovom primeru, koristio sam passphrase `pba`. Međutim, u vašem slučaju, pobrinite se da izaberete robustan passphrase. Da biste saznali kako definisati optimalan passphrase, molimo vas da pogledate ovaj drugi članak:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner zatim prikazuje novi otisak vašeg passphrase Wallet. Napravite nekoliko kopija ovog otiska: važno je kada koristite Wallet sa passphrase, jer vam omogućava da proverite, svaki put kada unesete passphrase, da niste napravili greške u kucanju i da pristupate pravom Wallet.



Na primer, ako u mom slučaju greškom zapišem passphrase `Pba` prilikom pokretanja SeedSigner-a umesto `pba`, ova jednostavna promena iz malih u velika slova će rezultirati kreiranjem potpuno drugačijeg portfolija od onog kojem želim da pristupim.



Ovaj otisak prsta ne predstavlja rizik za sigurnost ili poverljivost vašeg Wallet. Ne otkriva nikakve informacije, javne ili privatne, o vašim ključevima. Za razliku od Mnemonic i passphrase, možete sačuvati otisak prsta na digitalnom mediju. Preporučujem da zadržite kopiju na nekoliko mesta: na papiru, u menadžeru lozinki, itd.



Kada sačuvate otisak prsta, kliknite na `Gotovo`.



![Image](assets/fr/04.webp)



Zatim imate pristup svim funkcijama vašeg portfolija, baš kao na klasičnom SeedSigner-u.



![Image](assets/fr/05.webp)



Sada možete uvesti keystore u Sparrow wallet i koristiti svoj Wallet kao obično. Svaki put kada restartujete, moraćete i da skenirate svoj SeedQR i ponovo unesete svoj passphrase koristeći tastaturu, kao što smo ovde uradili.



Pre nego što zapravo koristite svoj Wallet sa passphrase, toplo preporučujem da izvršite potpuni test praznog oporavka. Ovo će vam omogućiti da potvrdite da su vaša Mnemonic fraza i passphrase bekapi validni. Da biste naučili kako da izvršite ovu proveru, pogledajte sledeći tutorijal:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895