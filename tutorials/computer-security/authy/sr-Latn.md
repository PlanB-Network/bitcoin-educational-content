---
name: Authy 2FA
description: Kako koristiti 2FA aplikaciju?
---
![cover](assets/cover.webp)


Danas je dvofaktorska autentifikacija (2FA) postala neophodna za poboljšanje sigurnosti online naloga protiv neovlašćenog pristupa. Sa porastom sajber napada, oslanjanje isključivo na lozinku za zaštitu vaših naloga ponekad nije dovoljno. 2FA uvodi dodatni Layer nivo sigurnosti zahtevajući drugi oblik autentifikacije pored lozinke. Ova verifikacija može imati nekoliko oblika, kao što je kod poslat putem SMS-a, dinamički kod generisan od strane posebne aplikacije, ili korišćenje fizičkog sigurnosnog ključa. Korišćenje 2FA značajno smanjuje rizik od kompromitovanja vaših naloga, čak i u slučaju krađe vaše lozinke.


## 2FA putem aplikacija za autentifikaciju


Istražićemo druga rešenja kao što su fizički sigurnosni ključevi u drugim tutorijalima, ali u ovom predlažem da posebno diskutujemo o 2FA aplikacijama. Rad ovih aplikacija je prilično jednostavan: kada je 2FA aktiviran na nalogu, pri svakom prijavljivanju, od vas će se tražiti ne samo vaša uobičajena lozinka već i 6-cifreni kod. Ovaj kod generiše vaša 2FA aplikacija. Važna karakteristika ovog 6-cifrenog koda je da nije statičan; nova šifra se generiše od strane aplikacije svakih 30 sekundi.

![AUTHY 2FA](assets/notext/01.webp)

Obnavljanje koda svakih 30 sekundi čini veoma teškim za napadača da pristupi vašem nalogu. Ovaj sistem sprečava napadače da ponovo koriste ukraden ili presretnut kod, jer on brzo ističe. Dakle, čak i ako napadač uspe da dobije kod, moći će da ga iskoristi samo tokom veoma kratkog vremenskog perioda pre nego što bude potreban novi kod. Štaviše, činjenica da se kod menja tako često značajno smanjuje vreme dostupno hakeru koji pokušava da pogodi kod putem brute force metode.


2FA putem aplikacija za autentifikaciju predstavlja jednostavan i besplatan način da značajno poboljšate sigurnost vaših online naloga.


Postoji mnogo aplikacija za postavljanje 2FA, među kojima su Google Authenticator i Microsoft Authenticator najpoznatije. Međutim, u ovom vodiču želim da vas upoznam sa drugim, manje poznatim rešenjem pod nazivom Authy. Sve ove aplikacije rade koristeći isti TOTP (*Time based One Time Password*) protokol, što čini njihovu upotrebu prilično sličnom.

Authy nudi nekoliko prednosti u odnosu na druga rešenja velikih tehnoloških kompanija. Prvo i najvažnije, omogućava vam da sinhronizujete svoje 2FA tokene na više uređaja, što može biti korisno u slučaju gubitka ili promene telefona. Authy vam takođe omogućava da generate šifrovanu rezervnu kopiju i skladištite je online, osiguravajući da nikada ne izgubite pristup svojim tokenima, čak i ako izgubite svoj primarni uređaj. Iz korisničke Interface perspektive, lično smatram da Authy nudi prijatnije i intuitivnije iskustvo od svojih alternativa.


## Kako instalirati Authy?


Na svom pametnom telefonu idite u prodavnicu aplikacija (Google Play Store ili Apple Store) i potražite "*Twilio Authy Authenticator*".



- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

Prilikom prvog pokretanja aplikacije, potrebno je da kreirate nalog. Izaberite pozivni broj vaše zemlje, kao i vaš broj telefona, zatim kliknite na "*Submit*".

![AUTHY 2FA](assets/notext/03.webp)

Unesite svoj email Address za oporavak koda.

![AUTHY 2FA](assets/notext/04.webp)

E-pošta će vam biti poslana da verifikujete vaš Address. Unesite 6 primljenih cifara da potvrdite.

![AUTHY 2FA](assets/notext/05.webp)

Odaberite jedan od dva dostupna načina za verifikaciju vašeg broja telefona. Ako se odlučite za primanje SMS-a, unesite 6-cifreni kod primljen porukom da potvrdite vaš broj.

![AUTHY 2FA](assets/notext/06.webp)

Čestitamo, vaš Authy nalog je kreiran!

![AUTHY 2FA](assets/notext/07.webp)

## Kako konfigurisati Authy?


Da biste započeli, idite na postavke aplikacije klikom na tri male tačke koje se nalaze u gornjem desnom uglu ekrana.

![AUTHY 2FA](assets/notext/08.webp)

Zatim kliknite na "*Settings*".

![AUTHY 2FA](assets/notext/09.webp)

U kartici "*Moj nalog*", imate opciju da izmenite svoj nalog. Preporučujem dodavanje PIN koda aplikaciji odabirom opcije "*Zaštita aplikacije*". Ovo dodaje dodatni Layer nivo sigurnosti za pristup vašoj aplikaciji.

![AUTHY 2FA](assets/notext/10.webp)

Na kartici "*Accounts*", možete postaviti rezervnu kopiju za vaše tokene. Ova rezervna kopija omogućava oporavak vaših kodova u slučaju problema. Šifrovana je pomoću lozinke koju morate definisati. Važno je da ova lozinka bude jaka i čuvana na sigurnom mestu. Postavljanje ove rezervne kopije nije nužno obavezno ako imate druge metode oporavka, kao što je drugi uređaj sa istim Authy nalogom, na primer.

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


Ako želite da omogućite dodavanje drugih uređaja, savetujem vam da aktivirate opciju koja zahteva potvrdu sa trenutno autorizovanih uređaja na vašem Authy nalogu pre dodavanja novog uređaja.

![AUTHY 2FA](assets/notext/12.webp)

Da biste dodali novi uređaj, jednostavno ponovite proces instalacije prikazan u prethodnom delu koristeći iste akreditive. Zatim će vam biti zatraženo da potvrdite ovaj novi pristup sa vašeg glavnog uređaja.


## Kako postaviti 2FA na nalog?


Da biste postavili 2FA autentifikacioni kod putem aplikacije kao što je Authy na nalogu, nalog mora podržavati ovu funkciju. Danas većina online servisa nudi ovu 2FA opciju, ali to nije uvek slučaj. Uzmimo za primer Proton mail nalog koji sam predstavio u drugom vodiču:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

Ovu opciju 2FA obično ćete pronaći u postavkama vašeg naloga, često pod odeljkom "*Lozinka*" ili "*Bezbednost*".

![AUTHY 2FA](assets/notext/14.webp)

Kada aktivirate ovu opciju na svom Proton mail nalogu, prikazuje vam se QR kod. Zatim morate skenirati ovaj QR kod pomoću vaše Authy aplikacije.

![AUTHY 2FA](assets/notext/15.webp)

Na Authy, kliknite na dugme "*+*".

![AUTHY 2FA](assets/notext/16.webp)

Kliknite na "*Scan QR Code*". Zatim skenirajte QR kod na veb-sajtu.

![AUTHY 2FA](assets/notext/17.webp)

Takođe imate opciju da prilagodite svoje korisničko ime ako je potrebno. Nakon što izvršite izmene, kliknite na dugme "*SAVE*".

![AUTHY 2FA](assets/notext/18.webp)

Authy će zatim prikazati vaš dinamički 6-cifreni kod specifičan za taj nalog koji se osvežava svakih 30 sekundi.

![AUTHY 2FA](assets/notext/19.webp)

Unesite ovaj kod na vebsajt da završite podešavanje 2FA.

![AUTHY 2FA](assets/notext/20.webp)

Neki sajtovi će vam takođe obezbediti kodove za oporavak nakon aktiviranja 2FA. Ovi kodovi vam omogućavaju pristup nalogu ako izgubite pristup svojoj Authy aplikaciji. Preporučujem da ih sačuvate na sigurnom mestu.

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

Svaki put kada se prijavite na nalog, moraćete da unesete dinamički kod koji generiše Authy. Sada možete osigurati sve svoje naloge kompatibilne sa ovom 2FA metodom. Da biste dodali novi nalog na Authy, kliknite na tri male tačke u gornjem desnom uglu aplikacije.

![AUTHY 2FA](assets/notext/23.webp)

Zatim kliknite na "*Add Account*".

![AUTHY 2FA](assets/notext/24.webp)

Pratite iste korake kao one korišćene za prvi nalog. Vaši različiti dinamički kodovi će biti vidljivi na početnoj stranici aplikacije Authy.