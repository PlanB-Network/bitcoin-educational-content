---
name: NOSTR

description: Otkrijte i počnite koristiti NOSTR
---

Na kraju ovog vodiča, razumećete šta je Nostr, kreiraćete nalog i moći ćete da ga koristite.


![A new challenger has arrived](assets/1.webp)


## Šta je Nostr?


Nostr je protokol koji ima moć da zameni Twitter, Telegram i druge platforme društvenih medija. To je jednostavan otvoreni protokol sposoban da stvori globalno otporan društveni mrežni sistem jednom zauvek.


## Kako to funkcioniše?


Nostr se zasniva na tri komponente: parovi ključeva, klijenti i releji.


Svaki korisnik ima jedan ili više identiteta, a svaki identitet je određen kriptografskim parom ključeva.


Da biste pristupili mreži, potrebno je koristiti klijentski softver i povezati se sa relejima za primanje i prenos sadržaja.


![Key system](assets/2.webp)


## 1. Kriptografski ključevi


Za razliku od Facebooka ili Twittera, gde korisnici moraju da pruže email Address i mnoštvo informacija privatnoj kompaniji, Nostr funkcioniše bez centralnog autoriteta. Korisnici generate kriptografski par ključeva, tajni ključ (poznat i kao privatni ključ) i javni ključ.


Tajni ključ, nsec, poznat samo korisniku, koristi se za autentifikaciju i objavljivanje sadržaja.


Javni ključ, npub, je jedinstveni identifikator za koji je sav sadržaj objavljen od strane korisnika vezan. Vaš javni ključ je poput korisničkog imena koje omogućava drugim korisnicima da vas pronađu i pretplate se na vaš Nostr feed.


## 2. Klijenti


Klijenti su softver koji omogućava interakciju sa Nostr. Glavni klijenti su:



- iOS: damus
- Android: ametist
- Web: iris.to; snort.social; astral.ninja


Klijenti omogućavaju korisnicima da generate novi par ključeva (što je ekvivalentno kreiranju naloga) ili da se autentifikuju sa postojećim parom ključeva.


## 3. Releji


Releji su jednostavni serveri koje možete napustiti u bilo kom trenutku ako vam se ne sviđa sadržaj koji vam isporučuju. Takođe možete pokrenuti svoj sopstveni relej ako želite.


💡 **Pro tip:** Plaćeni releji su generalno efikasniji u filtriranju spama i neželjenog sadržaja.


### Vodič


Sada znate dovoljno o Nostr-u da započnete i kreirate svoj prvi identitet na ovom protokolu.


Za potrebe ovog vodiča koristićemo iris.to (https://iris.to/) jer ovaj veb klijent radi na bilo kojoj platformi.


## Korak 1: Generisanje ključeva


ris će kreirati skup ključeva za vas bez potrebe da uradite bilo šta više osim da unesete ime (pravo ili izmišljeno) za vaš profil. Zatim kliknite na GO i to je to!


![Main menu](assets/3.webp)


⚠️ **Pažnja!** Moraćete da pratite svoje ključeve ako želite ponovo da pristupite svom profilu nakon što vaša sesija bude zatvorena. Pokazaću vam kako to da uradite na samom kraju ovog vodiča.


## Korak 2: Objavite sadržaj


Da biste objavili sadržaj, to je jednostavno i intuitivno kao pisanje nekoliko reči u polju za objavljivanje.


![Publication](assets/4.webp)


Evo ga! Objavili ste svoju prvu belešku na Nostr-u.


![Post](assets/5.webp)


## Korak 3: Pronađi prijatelja


Pronađi me na Nostr-u i nikada više nećeš biti sam. Pretplatiću se nazad na svakoga ko se pretplati na moj feed. Da to uradiš, jednostavno unesi moj javni ključ


npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 u traku za pretragu.


![My profile](assets/6.webp)


Klikni na "prati" i za nekoliko dana najviše, i ja ću se pretplatiti na tvoj feed. Bićemo prijatelji. Takođe ću rado pročitati tvoju poruku ako želiš da mi napišeš.


Na kraju, obavezno se pretplatite na feed Agora256 da biste primili obaveštenje svaki put kada objavimo nešto novo: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx


## Korak 4: Prilagodite svoj profil


Još uvek imate posla oko prilagođavanja svog profila. Da biste to uradili, kliknite na avatar koji je iris automatski generisao za vas u gornjem desnom uglu ekrana, a zatim kliknite na "uredi profil".


![Profile](assets/7.webp)


Sve što sada treba da uradiš je da kažeš irisu gde da pronađe tvoju sliku i profilni baner na internetu. Preporučujem da hostuješ svoj sadržaj: zaštiti ono što je tvoje.


![Another option](assets/8.webp)


Ako više voliš, možeš takođe da otpremiš slike, one će biti sačuvane za tebe od strane iris na nostr.build, besplatnoj usluzi za hosting vizuelnog sadržaja za Nostr.


Kao što možete videti, možete takođe konfigurisati svog klijenta da može primati i slati Sats. Na ovaj način, možete nagraditi autore sadržaja koji vam se dopao ili, još bolje, akumulirati Sats za sjajan sadržaj koji ćete objaviti.


## Korak 5: Napravite rezervnu kopiju para ključeva


Ovaj korak je ključan ako želite da zadržite pristup svom profilu nakon što se odjavite iz klijenta ili vaša sesija istekne.

Prvo, kliknite na ikonu "podešavanja" predstavljenu zupčanikom

![Setting](assets/9.webp)


Zatim, kopirajte i nalepite jedan po jedan vaš npub, npub hex, nsec i nsec hex u tekstualnu datoteku koju ćete čuvati na sigurnom. Preporučujem da šifrujete ovu datoteku ako znate kako to da uradite.


![Key](assets/10.webp)


⚠️ **Obratite pažnju na upozorenje koje vam iris daje:** dok svoj javni ključ možete deliti bez straha, priča je drugačija za vaš privatni ključ. Svako ko ima potonji moći će da pristupi vašem nalogu.


## Zaključak


Evo ga, mala noju, napravio si svoje prve korake na Nostr-u. Sada ćeš morati naučiti da trčiš brzinom munje. Uskoro ćemo objaviti vodiče koji će ti pokazati kako da upravljaš svojim ključevima i kako da integrišeš lightning u svoje Nostr iskustvo koristeći getalby.