---
name: KeePass
description: Kako postaviti lokalni menadžer lozinki?
---
![cover](assets/cover.webp)


U digitalnom dobu, moramo upravljati mnoštvom online naloga koji pokrivaju različite aspekte naših svakodnevnih života, uključujući bankarstvo, finansijske platforme, emailove, skladištenje fajlova, zdravlje, administraciju, društvene mreže, video igre, itd.


Da bismo se autentifikovali na svakom od ovih naloga, koristimo identifikator, često email, praćen lozinkom. Suočeni sa nemogućnošću pamćenja velikog broja jedinstvenih lozinki, mogli bismo biti u iskušenju da ponovo koristimo istu lozinku ili da malo modifikujemo zajedničku osnovu kako bismo je lakše zapamtili. Međutim, ove prakse ozbiljno ugrožavaju bezbednost vaših naloga.


Prvi princip koji treba slediti za lozinke je da ih ne koristite ponovo. Svaki online nalog treba da bude zaštićen jedinstvenom i potpuno različitom lozinkom. Ovo je važno jer, ako napadač uspe da kompromituje jednu od vaših lozinki, ne želite da ima pristup svim vašim nalozima. Imati jedinstvenu lozinku za svaki nalog izoluje potencijalne napade i ograničava njihov domet. Na primer, ako koristite istu lozinku za platformu za video igre i za vaš email, i ta lozinka bude kompromitovana putem fišing sajta povezanog sa platformom za igre, napadač bi tada lako mogao da pristupi vašem emailu i preuzme kontrolu nad svim vašim drugim online nalozima.


Drugi suštinski princip je jačina lozinke. Lozinka se smatra jakom ako je teško probiti je metodom silovite pretrage, tj. pogađanjem kroz mnoštvo pokušaja i grešaka. To znači da vaše lozinke moraju biti što nasumičnije, duge i uključivati raznovrsne karaktere (mala slova, velika slova, brojeve i simbole).


Primena ova dva principa bezbednosti lozinki (jedinstvenost i robusnost) može biti teška u svakodnevnom životu, jer je gotovo nemoguće zapamtiti jedinstvenu, nasumičnu i jaku lozinku za sve naše naloge. Tu na scenu stupa menadžer lozinki.


Menadžer lozinki generiše i sigurno čuva jake lozinke, omogućavajući vam pristup svim vašim online nalozima bez potrebe da ih pojedinačno pamtite. Potrebno je da zapamtite samo jednu lozinku, glavnu lozinku, koja vam daje pristup svim sačuvanim lozinkama u menadžeru. Korišćenje menadžera lozinki poboljšava vašu online sigurnost jer sprečava ponovnu upotrebu lozinki i sistematski generiše nasumične lozinke. Ali takođe pojednostavljuje vašu svakodnevnu upotrebu naloga centralizovanjem pristupa vašim osetljivim informacijama.

U ovom vodiču ćemo naučiti kako postaviti i koristiti lokalni menadžer lozinki kako bismo poboljšali vašu online sigurnost. Ovdje ću vas upoznati sa KeePass-om. Međutim, ako ste početnik i želite imati online menadžer lozinki sposoban za sinhronizaciju na više uređaja, preporučujem da pratite naš vodič o Bitwardenu:

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Upozorenje: Menadžer lozinki je odličan za čuvanje lozinki, ali **nikada ne bi trebalo da čuvate svoju Bitcoin bezbednosnu frazu u njemu!** Zapamtite, bezbednosna fraza treba da bude isključivo sačuvana u fizičkom formatu, kao što je papir ili metal.*


---

## Uvod u KeePass


KeePass je besplatan i open-source menadžer lozinki, savršen za one koji žele besplatno i sigurno rešenje za lokalno upravljanje. To je softver koji se instalira na vašem računaru i, bez dodataka, ne komunicira sa Internetom. Ovo je radikalno drugačiji pristup od onog koji koristi Bitwarden, koji smo pokrili u prethodnom vodiču. Bitwarden, za razliku od KeePass-a, omogućava sinhronizaciju na više uređaja i stoga zahteva čuvanje vaših lozinki na online serveru.


Podrazumevano, KeePass ne podržava korišćenje ekstenzija za pregledače kao što to ima Bitwarden; stoga ćete morati ručno da kopirate i nalepite svoje lozinke iz softvera. Iako ovo može delovati kao ograničenje, kopiranje i lepljenje lozinki umesto korišćenja automatskog popunjavanja je dobra praksa za vašu onlajn bezbednost.


KeePass je dizajniran da bude lagan i jednostavan za korišćenje, dok se pridržava visokih sigurnosnih standarda. Softver šifrira vašu bazu podataka lokalno za optimalnu zaštitu vaših kredencijala. KeePass je takođe jedini menadžer lozinki koji je validiran od strane ANSSI (francuske agencije za sajber bezbednost).


Jedna od glavnih prednosti KeePass-a je njegova fleksibilnost. Može se koristiti na mnogo različitih načina, kao što je na USB memoriji bez potrebe za instalacijom na računar. Štaviše, zahvaljujući svom [plugin okruženju](https://keepass.info/plugins.html), KeePass se može prilagoditi kako bi zadovoljio specifičnije potrebe.

![KEEPASS](assets/notext/01.webp)

## Kako preuzeti KeePass?


Proces instalacije za KeePass varira u zavisnosti od operativnog sistema koji koristite. Za korisnike Windows ili Linux sistema, instalacija je relativno jednostavna. Međutim, ako koristite macOS, potreban je dodatni korak zbog razvoja KeePass-a na .NET platformi, koja nije direktno podržana od strane macOS-a. Stoga, biće potrebno da konfigurišete kompatibilno okruženje kako biste omogućili pokretanje KeePass-a na Apple uređajima.


Za korisnike Debian/Ubuntu, otvorite terminal i unesite sledeće komande:


```bash
sudo apt-get update

sudo apt-get install keepass2

```

Za Fedora:

```

sudo dnf install keepass

```

Za Arch Linux:

```

sudo pacman -S keepass

```

Ako koristite Windows računar, [idite na zvaničnu stranicu za preuzimanje KeePass-a](https://keepass.info/download.html), i preuzmite najnoviju verziju instalacionog programa:
![KEEPASS](assets/notext/02.webp)
Kliknite na preuzetu datoteku da biste je pokrenuli, a zatim sledite uputstva čarobnjaka za instalaciju kako biste dovršili instalaciju (pogledajte naredno poglavlje).

Za korisnike macOS-a, instalacija je nešto složenija. Ako želite da koristite originalnu verziju KeePass-a kao na Windowsu, pratite uputstva u nastavku. 
U suprotnom, možete se opredeliti za [KeePassXC](https://keepassxc.org/), alternativnu verziju kompatibilnu sa macOS-om, koja nudi nešto drugačiji interfejs.

Da biste koristili KeePass, biće vam potrebno izvršno okruženje za .NET aplikacije. Preporučujem da instalirate Mono u tu svrhu. Idite na [zvaničnu Mono stranicu](https://www.mono-project.com/download/stable/#download-mac) i u odeljku "macOS" i kliknite na link za preuzimanje instalacionog paketa (.pkg).
![KEEPASS](assets/notext/03.webp)
Otvorite preuzetu `.pkg` datoteku i pratite uputstva kako biste instalirali Mono na svom Mac-u.
![KEEPASS](assets/notext/04.webp)
Zatim idite na zvaničnu KeePass veb stranicu i preuzmite najnoviju prenosivu verziju u `.zip` formatu.
![KEEPASS](assets/notext/05.webp)
Nakon preuzimanja `.zip` datoteke, dvaput kliknite da biste je raspakovali. Dobićete folder
koja sadrži više datoteka, uključujući `KeePass.exe`. Otvorite terminal i pređite u KeePass folder (zamenite `xx` odgovarajućim brojem verzije):


```

cd ~/Downloads/KeePass-2.xx

```

I na kraju, pokrenite KeePass pomoću Mono okruženja:

```

mono KeePass.exe

```
