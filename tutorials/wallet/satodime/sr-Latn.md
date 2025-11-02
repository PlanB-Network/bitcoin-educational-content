---
name: Satodime
description: Saznajte kako koristiti Satodime sa mobilnom aplikacijom
---
![cover](assets/cover.webp)



Ovaj vodič vas vodi kroz instalaciju, konfiguraciju i korišćenje Satodime mobilne aplikacije. Naučićete kako da preuzmete svoju karticu, kreirate sefove, dodate sredstva, otpečatite i povratite svoje privatne ključeve. Dodaci pružaju resurse, najbolje prakse i tehnička objašnjenja.



## Uvod



**Satodime**, razvijen od strane **[Satochip](https://satochip.io/fr/)**, je sigurna kartica za čuvanje Bitcoin na opipljiv i jednostavan način. Djeluje kao samostalni kustos Hardware Wallet, gde imate potpunu kontrolu nad svojim privatnim ključevima bez oslanjanja na treću stranu. Otvorenog koda i EAL6+ sertifikovan, podržava do tri nezavisna sefa.



### Pozadina proizvoda



Satodime, **carte au porteur, pripada onome ko je fizički poseduje**, bez potrebe za prethodnom registracijom ili identifikacijom. Zadovoljava potrebu za sigurnim, prenosivim Bitcoin skladištem, omogućavajući svakome ko drži karticu da je koristi ili prenese bitkoine skeniranjem putem mobilne aplikacije kako bi preuzeo vlasništvo ili otvorio sefove. Za razliku od papirnog računa, koristi sigurni čip za Seal privatne ključeve, koji se otkrivaju tek nakon otvaranja, čineći karticu sličnom gotovini gde je Ownership određen fizičkim posedovanjem. Idealna za poklanjanje bitkoina, olakšava siguran prenos bitkoina iz ruke u ruku, dok mobilna aplikacija koristi NFC za pristupačnu interakciju sa pametnim telefonima.





- Bezbednost**: Privatni ključevi generisani i uskladišteni u čipu otpornom na neovlašćeno menjanje; vidljiv status (zapečaćeno, nezapečaćeno, prazno).
- Funkcije**: Kupite bitkoine direktno putem aplikacije (Paybis partner); upravljajte Mainnet i Testnet.
- Otvoreni kod**: Kod pod AGPLv3 licencom, proverljiv na GitHub-u.



### Kontinuirana evolucija



Aplikacija se redovno razvija. Proverite Satochip vebsajt ili prodavnice za ažuriranja. Na primer, nove blokčejnove ili funkcionalnosti kupovine mogu biti dodate. Proverite [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) za tekuće razvojne aktivnosti.



## 1. Preduslovi



Pre nego što počnete sa **Satodime**, uverite se da imate sledeće stavke:





- Kompatibilan pametni telefon**: Android ili iOS uređaj sa omogućenim NFC-om.
- Satodime** kartica: Nova ili neinicijalizovana.
- Internet konekcija**: Za preuzimanje aplikacije.
- Osnovno znanje**: Razumevanje privatnih/javnih ključeva i rizika od gubitka (nepovratno).
- Siguran medijum**: Sigurno mesto za beleženje privatnih ključeva nakon otvaranja (papir, metal; nikada digitalno).



## 2. Instalacija





- Preuzmite aplikaciju** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Proverite programera (Satochip) kako biste izbegli prevaru.
 - Satodime je **open-source**. Izvorni kod : [Satochip's GitHub](https://github.com/Toporin/Satodime-Applet).





- Instalirajte i pokrenite aplikaciju**: Aktivirajte NFC na vašem telefonu ako je potrebno.



![image](assets/fr/01.webp)



## 3. Inicijalna konfiguracija



### 3.1 Pokreni aplikaciju i skeniraj



Otvorite aplikaciju i pratite čarobnjaka. Postavite Satodime karticu na NFC čitač vašeg telefona (obično na poleđini). Držite je pritisnutu tokom cele operacije kako biste osigurali stabilnu vezu.





- Ako NFC ne radi, proverite postavke telefona.
- Tost potvrđuje uspeh: "Uspešno čitanje".



![image](assets/fr/02.webp)



Kao opšte pravilo, **sve sledeće operacije će zahtevati potvrdu skeniranjem Satodime kartice**



### 3.2 Preuzimanje kartice (*Ownership*)



Za prvu upotrebu, postanite vlasnik kartice da biste je osigurali:





- Kliknite na "*Take Ownership*" u aplikaciji.
- Potvrdite operaciju: ovo generiše jedinstveni ključ vlasnika.
- Ponovo skeniraj mapu da primeniš izmene.
- Upozorenje**: Ovaj korak je nepovratan. Molimo vas da se obratite [*Ownership* članku](https://satochip.io/satodime-Ownership-explained/).



![image](assets/fr/03.webp)




## 4. Kreiraj sef



Satodime podržava do 3 sefa. Kreirajte jedan za čuvanje Bitcoin :





- Odaberite prazan sef (npr. Sef 01).
- Izaberite Blockchain (Bitcoin).
- Kliknite na "*Create & Seal*".
- Skenirajte karticu na generate i Seal privatni ključ (nepoznat dok se ne otpečati).
- Čestitamo**: Vaš sef je sada zapečaćen i spreman za primanje sredstava.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Dodaj sredstva



Kada se zapečati, napunite sef bitcoinima:





- Odaberite sef.
- Kliknite na "*Dodaj sredstva*".
- Kopiraj javni Address ili skeniraj QR kod.
- Pošalji sredstva sa drugog Wallet.
- Proveri saldo nakon potvrde na Blockchain.
- Opcija kupovine: Kliknite na "*Purchase*" za direktnu kupovinu putem Paybis-a (Visa, Mastercard, itd.). Primjenjive naknade.



![image](assets/fr/06.webp)



## 6. Otvorite sef



Da biste pristupili privatnom ključu i prebacili sredstva na drugo mesto, otvorite sef:





- Izaberite zapečaćeni sef.
- Kliknite na "Unseal".
- Potvrdite upozorenje: ova operacija je nepovratna.
- Skeniraj karticu da otključaš.
- Sef je postavljen na "*Otključano*"; privatni ključ se sada može pregledati/izvesti.
- Upozorenje**: Kada se jednom otvori, privatni ključ je dostupan. Ako neko preuzme vaš pametni telefon, može pristupiti ovom ključu i na taj način povratiti sredstva iz vašeg sefa (nepovratno).



![image](assets/fr/07.webp)



## 7. Oporavak privatnog ključa



Nakon otpečaćivanja, izvezite ključ za upotrebu u drugom Wallet :





- Uverite se da ste u bezbednom okruženju.
- Kliknite na "*Prikaži privatni ključ*".
- Izaberite format: Legacy, SegWit, WIF, itd.
- Kopiraj ključ ili skeniraj QR kod.
- Bezbednost**: Nikada ne delite svoj privatni ključ. Čuvajte ga van mreže.
- Uvezite ga u Wallet softverski program kompatibilan sa upravljanjem fondovima (npr. Sparrow wallet ili Electrum).



![image](assets/fr/08.webp)





## 8. Reset trunk



Resetovanje sefa nepovratno briše povezani privatni ključ. Drugim rečima, ako niste obezbedili kopiju svog privatnog ključa ili ga uvezli u drugi Wallet, resetovanje sefa će izazvati nepovratan gubitak sredstava u njemu.



![image](assets/fr/09.webp)



Resetovanje prtljažnika čini slot praznim i spremnim za novi prtljažnik.



## 9. Transfer Ownership



Da biste - na primer - ponudili bitkoine putem Satodime, morate:




- Uzmi Ownership sa kartice,
- Napravite Bitcoin sef,
- Prenesi Satss tamo,
- Prenosna kartica Ownership: sledeća osoba koja skenira karticu postaje njen vlasnik,
- Dajte Satodime karticu osobi po vašem izboru i pozovite je da preuzme aplikaciju, a zatim skenira karticu kako bi preuzela Ownership sa nje - i tako pristupila bitcoinima 'skladištenim' na njoj.



![image](assets/fr/10.webp)




## DODACI



### A1. Najbolje prakse



Da biste bezbedno koristili **Satodime** :





- Osigurajte karticu**: Tretirajte je kao gotovinu; gubitak = izgubljena sredstva ako niste vlasnik.
- Rezervna kopija ključa**: Nakon otvaranja, zabeležite privatne ključeve na sigurnom fizičkom mediju. Nikada digitalno.
- Proveri status**: Uvek skeniraj da potvrdiš karticu Ownership i status zapečaćen/nezapečaćen sefova.
- Poverljivost**: Koristite nove adrese; izbegavajte centralizovane menjačnice za transfere.
- Ažuriranja**: Ažurirajte aplikaciju putem prodavnica.
- Recovery**: If the card is lost but owned, the funds are on the Blockchain; use the private key if unsealed.



### A2. Dodatni resursi



Specifično za Satodime :




- [Satodime proizvod](https://satochip.io/fr/product/satodime/)
- [Mobile Guide](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Network](https://planb.network/) za tutorijale o samostalnom čuvanju, privatnim ključevima, itd.



**Sačuvaj svoju frazu za oporavak** :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Uputstvo za Satochip (prvi proizvod brenda) :**



https://planb.network/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Seedkeeper tutorijali:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. O Satochipu



**Zvanični linkovi** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Podrška: info@satochip.io



**Satochip** je belgijska kompanija koja razvija hardverska i softverska rešenja za upravljanje i skladištenje bitkoina i drugih kriptovaluta. Njihov vodeći proizvod, Satochip Hardware Wallet, je NFC kartica opremljena sa EAL6+ sertifikovanim secure element. U kombinaciji sa Seedkeeper-om, Mnemonic menadžerom fraza i tajni, i Satodime-om, karticom na donosioca, Satochip nudi sveobuhvatan asortiman prilagođen potrebama korisnika. Njihovi uređaji, pokretani softverom otvorenog koda, imaju za cilj da demokratizuju sigurnost na Bitcoin.