---
name: GnuPG
description: Kako proveriti integritet i autentičnost softvera?
---
![cover](assets/cover.webp)


Kada preuzimate softver, veoma je važno osigurati da nije izmenjen i da zaista dolazi iz zvaničnog izvora. Ovo je posebno važno za softver povezan sa Bitcoinom, kao što je novčanik softver, koji vam omogućava da osigurate ključeve koji daju pristup vašim sredstvima. U ovom vodiču ćemo videti kako da proverimo integritet i autentičnost softvera pre nego što ga instaliramo. Koristićemo Sparrow Wallet kao primer, omiljeni novčanik softver među bitkoinerima, ali procedura će biti ista za bilo koji drugi softver.


Provera integriteta uključuje osiguravanje da preuzeta datoteka nije izmenjena upoređivanjem njenog digitalnog otiska (tj. njenog heša) sa onim koji je obezbedio zvanični developer. Ako se ta dva poklapaju, to znači da je datoteka identična originalu i da nije oštećena ili izmenjena od strane napadača.


Provera autentičnosti, s druge strane, osigurava da datoteka zaista dolazi od zvaničnog programera, a ne od prevaranta. Ovo se postiže proverom digitalnog potpisa. Ovaj potpis dokazuje da je softver potpisan privatnim ključem legitimnog programera.


Ako se ove provere ne izvrše, postoji rizik od instaliranja malvera koji bi mogao sadržati izmenjeni kod. Ovaj kod bi mogao ili da ukrade informacije poput vaših privatnih ključeva ili da blokira pristup vašim fajlovima. Ova vrsta napada je prilično česta, posebno u kontekstu softvera otvorenog koda gde se lažne verzije mogu distribuirati.


Da bismo izvršili ovu verifikaciju, koristićemo dva alata: heš funkcije za proveru integriteta i GnuPG, alat otvorenog koda koji implementira PGP protokol, za proveru autentičnosti.


## Preduslovi


Ako ste na **Linux**-u, GPG je unapred instaliran na većini distribucija. Ako nije, možete ga instalirati sledećom komandom:


```bash
sudo apt install gnupg
```


Za **macOS**, ako već niste instalirali Homebrew upravitelj paketa, učinite to sa sledećim komandama:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


Zatim instalirajte GPG pomoću ove komande:


```bash
brew install gnupg
```

Za **Windows**, ako nemate GPG, možete instalirati softver [Gpg4win](https://www.gpg4win.org/).

![GnuPG](assets/notext/01.webp)


## Preuzimanje dokumenata


Da bismo počeli, biće nam potrebni različiti dokumenti. Posetite zvanični sajt [Sparrow Wallet u sekciji "*Download*"](https://sparrowwallet.com/download/). Ako želite da verifikujete drugi softver, idite na sajt tog softvera.


![GnuPG](assets/notext/02.webp)


Možete takođe otići [do GitHub repozitorijuma projekta](https://github.com/sparrowwallet/sparrow/releases).


![GnuPG](assets/notext/03.webp)


Preuzmite instalacioni program za softver koji odgovara vašem operativnom sistemu.


![GnuPG](assets/notext/04.webp)


Trebaće vam i datoteka sa hešom, često nazvana "*SHA256SUMS*" ili "*MANIFEST*".


![GnuPG](assets/notext/05.webp)


Preuzmite PGP potpis datoteke takođe. Ovo je dokument u `.asc` formatu.


![GnuPG](assets/notext/06.webp)


Pobrinite se da sve ove datoteke postavite u istu fasciklu za sledeće korake.


Na kraju, biće vam potreban javni ključ programera, koji ćemo koristiti za verifikaciju PGP potpisa. Ovaj ključ je često dostupan ili na vebsajtu softvera, na GitHub repozitorijumu projekta, ponekad na društvenim mrežama programera, ili na specijalizovanim sajtovima kao što je Keybase. U slučaju Sparrow Wallet-a, možete pronaći javni ključ Craig Raw programera [na Keybase](https://keybase.io/craigraw). Da biste ga preuzeli direktno iz terminala, izvršite komandu:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## Verifikacija potpisa


Proces verifikacije potpisa je isti na **Windows-u**, **macOS-u** i **Linux-u**. Obično ste već uvezli javni ključ tokom prethodnog koraka, ali ako niste, uradite to pomoću komande:


```bash
gpg --import [key path]
```


Zamenite `[key path]` sa lokacijom datoteke javnog ključa programera.


![GnuPG](assets/notext/08.webp)


Potvrdite potpis sledećom komandom:


```bash
gpg --verify [file.asc]
```


Zamenite `[file.asc]` sa putanjom do datoteke sa potpisom. U slučaju Sparrow-a, ova datoteka se zove "*sparrow-2.0.0-manifest.txt.asc*" za verziju 2.0.0.


![GnuPG](assets/notext/09.webp)


Ako je potpis važeći, GPG će vam to naznačiti. Zatim možete preći na sledeći korak, jer ovo potvrđuje autentičnost datoteke.


![GnuPG](assets/notext/10.webp)


## Verifikacija heša

Sada kada je autentičnost softvera potvrđena, takođe je potrebno proveriti njegov integritet. Uporedićemo heš softvera sa hešom koji je obezbedio programer. Ako se podudaraju, to garantuje da kod softvera nije izmenjen.


Na **Windows**-u, otvorite terminal i izvršite sledeću komandu:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


Zamenite `[file path]` sa lokacijom instalacionog fajla.


![GnuPG](assets/notext/11.webp)


Terminal će vratiti heš vrednost preuzetog softvera.


![GnuPG](assets/notext/12.webp)


Imajte na umu da je za neki softver možda potrebno koristiti drugačiju heš funkciju od SHA256. U tom slučaju, jednostavno zamenite naziv heš funkcije u komandi.


Zatim uporedite rezultat sa odgovarajućom vrednošću u datoteci "*sparrow-2.0.0-manifest.txt*".


![GnuPG](assets/notext/13.webp)


U mom slučaju, vidimo da se dva heša savršeno poklapaju.


Na **macOS-u** i **Linux-u**, proces verifikacije heša je automatizovan. Nije neophodno ručno proveravati podudaranje između dva heša kao na Windowsu.


Jednostavno izvršite ovu komandu na **macOS-u**:


```bash
shasum --check [file name] --ignore-missing
```


Zamenite `[file name]` sa imenom instalacionog fajla. Na primer, za Sparrow Wallet:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


Ako se heševi podudaraju, trebalo bi da vidite sledeći izlaz:


```bash
Sparrow-2.0.0.dmg: OK
```


Na **Linuxu**, komanda je slična:


```bash
sha256sum --check [file name] --ignore-missing
```


A ako se heševi podudaraju, trebalo bi da vidite sledeći izlaz:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


Sada ste sigurni da je softver koji ste preuzeli i autentičan i netaknut. Možete nastaviti sa njegovom instalacijom na vašem računaru.


Ako ste smatrali ovaj vodič korisnim, bio bih zahvalan na palcu gore ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Preporučujem da pogledate i ovaj drugi vodič o VeraCrypt-u, softveru koji vam omogućava šifrovanje i dešifrovanje uređaja za skladištenje.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5
