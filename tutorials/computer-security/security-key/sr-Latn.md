---
name: YubiKey 2FA
description: Kako koristiti fizički sigurnosni ključ?
---
![cover](assets/cover.webp)


Danas je dvofaktorska autentifikacija (2FA) postala neophodna za poboljšanje sigurnosti online naloga protiv neovlašćenog pristupa. Sa porastom sajber napada, oslanjanje isključivo na lozinku za zaštitu vaših naloga ponekad nije dovoljno.


2FA uvodi dodatni nivo bezbednosti zahtevajući drugi oblik autentifikacije pored tradicionalne lozinke. Ova verifikacija može imati različite oblike, kao što je kod poslat putem SMS-a, dinamički kod generisan od strane posebne aplikacije, ili korišćenje fizičkog sigurnosnog ključa. Korišćenje 2FA značajno smanjuje rizike od kompromitovanja vaših naloga, čak i u slučaju da vaša lozinka bude ukradena.


U drugom vodiču, objasnio sam kako postaviti i koristiti TOTP 2FA aplikaciju:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Ovde ćemo videti kako koristiti fizički sigurnosni ključ kao drugi faktor autentifikacije za sve vaše naloge.


## Šta je fizički sigurnosni ključ?


Fizički sigurnosni ključ je uređaj koji se koristi za poboljšanje sigurnosti vaših online naloga putem dvofaktorske autentifikacije (2FA). Ovi uređaji često liče na male USB ključeve koji se moraju umetnuti u port računara kako bi se potvrdilo da je zaista legitimni korisnik taj koji pokušava da se poveže.

![SECURITY KEY 2FA](assets/notext/01.webp)

Kada se prijavite na nalog zaštićen 2FA i koristite fizički sigurnosni ključ, morate ne samo uneti svoju uobičajenu lozinku već i umetnuti fizički sigurnosni ključ u svoj računar i pritisnuti dugme da biste potvrdili autentifikaciju. Ova metoda tako dodaje dodatni nivo sigurnosti, jer čak i ako neko uspe da dobije vašu lozinku, neće moći da pristupi vašem nalogu bez fizičkog posedovanja ključa.


Fizički sigurnosni ključ je posebno efikasan jer kombinuje dve različite vrste faktora autentifikacije: dokaz znanja (lozinka) i dokaz posedovanja (fizički ključ).


Međutim, ova metoda 2FA takođe ima nedostatke. Prvo, morate uvek imati sigurnosni ključ dostupan ako želite pristupiti svojim nalozima. Možda ćete ga morati dodati na svoj privezak za ključeve. Drugo, za razliku od drugih 2FA metoda, korišćenje fizičkog sigurnosnog ključa podrazumeva početni trošak jer morate kupiti mali uređaj. Cena sigurnosnih ključeva obično varira između €30 i €100 u zavisnosti od odabranih karakteristika.


## Koji fizički sigurnosni ključ odabrati?


Da biste odabrali svoj sigurnosni ključ, potrebno je uzeti u obzir nekoliko kriterijuma.

Prvo i najvažnije, treba da proverite protokole koje uređaj podržava. Kao minimum, savetujem da izaberete ključ koji podržava OTP, FIDO2 i U2F. Ove detalje obično ističu proizvođači u opisima proizvoda. Da biste proverili kompatibilnost svakog ključa, možete takođe posetiti [dongleauth.com](https://www.dongleauth.com/dongles/).

Takođe, osigurajte da je ključ kompatibilan sa vašim operativnim sistemom, iako poznati brendovi poput Yubikey-a generalno podržavaju sve široko korišćene sisteme.


Takođe treba da izaberete ključ na osnovu tipa portova dostupnih na vašem računaru ili pametnom telefonu. Na primer, ako vaš računar ima samo USB-C portove, izaberite ključ sa USB-C konektorom. Neki ključevi takođe nude opcije povezivanja putem Bluetooth-a ili NFC-a.

![SECURITY KEY 2FA](assets/notext/02.webp)

Takođe možete uporediti uređaje na osnovu njihovih dodatnih karakteristika kao što su otpornost na vodu i prašinu, kao i oblik i veličinu ključa.


Što se tiče brendova sigurnosnih ključeva, Yubico je najpoznatiji sa svojim [YubiKey uređajima](https://www.yubico.com/), koje lično koristim i preporučujem. Google takođe nudi uređaj sa [Titan Security Key](https://store.google.com/fr/product/titan_security_key). Za open-source alternative, [SoloKeys](https://solokeys.com/) (non OTP) i [NitroKey](https://www.nitrokey.com/products/nitrokeys) su zanimljive opcije, ali nikada nisam imao priliku da ih testiram.


## Kako koristiti fizički sigurnosni ključ?


Kada primite svoj sigurnosni ključ, nije potrebno posebno podešavanje. Ključ je obično spreman za upotrebu odmah po prijemu. Možete ga odmah koristiti za osiguranje svojih online naloga koji podržavaju ovu vrstu autentifikacije. Na primer, pokazaću vam kako da osigurate svoj Proton mail nalog ovim fizičkim sigurnosnim ključem.

![SECURITY KEY 2FA](assets/notext/03.webp)

Opciju za aktivaciju 2FA pronaći ćete u postavkama naloga, često pod sekcijom "*Lozinka*" ili "*Sigurnost*". Kliknite na polje za potvrdu ili dugme koje vam omogućava da aktivirate 2FA sa fizičkim ključem.

![SECURITY KEY 2FA](assets/notext/04.webp)

Priključite ključ u svoj računar.

![SECURITY KEY 2FA](assets/notext/05.webp)

Dodirnite dugme na vašem sigurnosnom ključu da biste potvrdili.

![SECURITY KEY 2FA](assets/notext/06.webp)

Unesite ime da zapamtite koji ste ključ koristili.

![SECURITY KEY 2FA](assets/notext/07.webp)

I eto ga, vaš sigurnosni ključ je uspešno dodat za 2FA autentifikaciju vašeg naloga.

![SECURITY KEY 2FA](assets/notext/08.webp)

U mom primeru, ako pokušam ponovo da se povežem na svoj Proton mail nalog, prvo će mi biti zatraženo da unesem svoju lozinku zajedno sa korisničkim imenom. Ovo je prvi faktor autentifikacije.

![SECURITY KEY 2FA](assets/notext/09.webp)

Zatim, od mene se traži da priključim svoj sigurnosni ključ za drugi faktor autentifikacije.

![SECURITY KEY 2FA](assets/notext/10.webp)

Dalje, treba da dodirnem dugme na fizičkom ključu da bih potvrdio autentifikaciju, i ponovo sam povezan na svoj Proton mail nalog.

![SECURITY KEY 2FA](assets/notext/11.webp)

Ponovite ovu operaciju za sve online naloge koje želite da osigurate na ovaj način, posebno za kritične naloge kao što su vaši email nalozi, vaši menadžeri lozinki, vaši cloud i online servisi za skladištenje, ili vaši finansijski nalozi.
