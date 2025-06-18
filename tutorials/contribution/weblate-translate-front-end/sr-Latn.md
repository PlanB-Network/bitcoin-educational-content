---
name: Weblate - prevođenje statičkog Elements
description: Kako možete učestvovati u prevođenju statičkog Elements na planb.network?
---
![cover](assets/cover.webp)


Misija Plan ₿ Network je da obezbedi prvoklasne obrazovne resurse o Bitcoin i prevede ih na što više jezika. Veći deo sadržaja objavljenog na sajtu je otvorenog koda i hostovan na GitHub-u, omogućavajući svakome da učestvuje u obogaćivanju platforme. Doprinosi mogu biti u raznim oblicima: ispravljanje i lektura postojećeg sadržaja, ažuriranje informacija ili kreiranje novih tutorijala za dodavanje na platformu.


U ovom vodiču pokazaćemo vam kako lako doprineti prevođenju statičkog Elements na našem sajtu. Podaci na platformi su podeljeni u dve glavne kategorije:


- frontend podaci/statika Elements (stranice, dugmad, itd.);
- obrazovni sadržaj (tutoriali, kursevi, resursi...).


Da bismo preveli obrazovni sadržaj, koristimo [veštačku inteligenciju](https://github.com/Asi0Flammeus/LLM-Translator). Zatim, da bismo ispravili eventualne greške u ovim fajlovima, pozivamo lektore da doprinesu. Ako želite da lektorišete neki sadržaj, pogledajte sledeći tutorijal:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6

S druge strane, ako ste zainteresovani za prevođenje statičkog Elements sajta (isključujući edukativni sadržaj), na pravom ste mestu! Za efikasno prevođenje frontend-a koristimo alat Weblate, koji je veoma jednostavan za korišćenje i olakšava pristup prevođenju.


Ako želite da dodate potpuno novi jezik u Plan ₿ Network, obavezno kontaktirajte Plan ₿ Network tim putem naše [Telegram grupe](https://t.me/PlanBNetwork_ContentBuilder). Ako nemate telegram, možete poslati e-mail na mari@planb.network. Obavezno napišite malu prezentaciju o tome ko ste i koje jezike govorite.

Članovi našeg tima će vam dati specifična uputstva i otvoriće povezane "issues" na Githubu kako bi koordinisali vaš rad.


Pre nego što pratite ovaj specifičan vodič za dodavanje novog jezika u Weblate.


https://planb.network/tutorials/contribution/content/weblate-add-new-language-eef2f5c0-1aba-48a3-b8f0-a57feb761d86

Kada budete spremni da počnete sa prevođenjem, vratite se ovom vodiču i prođite kroz sledeće tačke.


## Registrujte se na Weblate



- Idite na [samohostovani Weblate Plan ₿ Network](https://weblate.planb.network/):

![weblate](assets/01.webp)


- Ako već imate Weblate nalog, kliknite na `Prijavi se`:

![weblate](assets/02.webp)


- Ako nemate nalog, kliknite na `Registrujte se`:

![weblate](assets/03.webp)


- Unesite svoj email Address, kao i korisničko ime i puno ime (možete koristiti pseudonim), zatim kliknite na `Registruj se`:

![weblate](assets/04.webp)


- U vašem email inboxu, trebalo bi da ste primili poruku za potvrdu od Weblate-a. Kliknite na link da potvrdite vašu registraciju:

![weblate](assets/05.webp)


- Izaberite jaku lozinku, zatim kliknite na `Promeni moju lozinku`:

![weblate](assets/06.webp)


- Sada se možete vratiti na Plan ₿ Network kontrolnu tablu:

![weblate](assets/07.webp)


## Počni prevoditi



- Kliknite na projekat `Website Elements` (ne na rečnik):

![weblate](assets/08.webp)


- Doći ćete do Interface, gde možete videti jezike u toku:

![weblate](assets/09.webp)


- Izaberite svoj jezik. Na primer, uzmimo francuski:

![weblate](assets/10.webp)


- Da biste započeli prevođenje, jednostavno kliknite na dugme `Translate`:

![weblate](assets/11.webp)


- Bićete preusmereni na rad Interface:

![weblate](assets/12.webp)


- Weblate će zatim automatski predložiti rečenice, paragrafe ili čak reči za prevođenje u `language` polje. U vašem slučaju, verovatno ćete videti glavnu rečenicu na engleskom i još jedan tekstualni okvir za vaš jezik:

![weblate](assets/13.webp)


- Vaš zadatak se sastoji u prevođenju označenih nizova. Morate uneti svoj tekst u polje koje odgovara jeziku koji ste izabrali. Na primer, ako radite na francuskoj verziji, napišite svoj prevod u `French` polje:

![weblate](assets/14.webp)


- Kliknite na karticu `Automatic suggestion`:

![weblate](assets/15.webp)


- Ovde, Weblate vam prikazuje prevod napravljen veštačkom inteligencijom:

![weblate](assets/16.webp)


- Ako vam se predloženi prevod čini relevantnim, možete kliknuti na dugme `Kloniraj u prevod`:

![weblate](assets/17.webp)


- Predlog je sada postavljen u vaš radni okvir:

![weblate](assets/18.webp)


- Zatim možete ručno izmeniti predlog:

![weblate](assets/19.webp)


- Kada vam se prevod učini zadovoljavajućim, kliknite na dugme `Sačuvaj i nastavi`. Obavezno poništite izbor u polju "Potrebno uređivanje" kada ste sigurni u svoj prevod:

![weblate](assets/20.webp)


- Evo ga! Vaš prevod je uspešno sačuvan. Weblate će vas automatski preusmeriti na sledeću stavku za prevođenje. Ako se vratite na kontrolnu tablu koja odgovara vašem jeziku, možete videti da bilo koja vrsta niza ima različit status prevođenja. Na primer, ako treba da se fokusirate samo na "neprevedene nizove", možete kliknuti na određenu karticu:

![weblate](assets/21.webp)


- Ako treba da potražiš određenu reč, bilo na svom jeziku ili na originalnom, klikni na "search" i unesi je tamo:

![weblate](assets/22.webp)


## Smernice za prevođenje



- Kada pronađete reči umetnute unutar vitičastih zagrada "{", ne morate ih prevoditi. Na primer, u rečenici "Vaš nalog je kreiran, {{userName}}!", prevešćete celu rečenicu, ali ćete zadržati "userName" na engleskom.
- Kada pronađete "Plan ₿ Network" u nizu, pobrinite se da NE prevodite reč "network" (smatrajte Plan ₿ Network kao zaštitni znak). Osim toga, uvek koristite Bitcoin's ₿!
- Ako pronađete reč "network" samu, možete je prevesti, umesto toga.
- Ne prevodite "B-CERT", jer je to još jedna fiksna reč.
- Ako pronađeš stringove koji se završavaju razmakom, možeš ih ostaviti.
- Neki nizovi mogu sadržati razmak između poslednje reči i znaka interpunkcije: nemojte ga ostavljati u ciljanom jeziku osim ako to gramatika ne zahteva. Na primer, "Contact information :" treba ispraviti u "Contact information:". U ovom slučaju, prevedite to na ispravan način. Takođe možete dodati komentar da obavestite administratore o ovom problemu u originalnoj verziji na engleskom jeziku.


## Nove funkcije


- Radimo na dodavanju odeljka "objašnjenje" za bilo koji niz, zajedno sa snimkom ekrana, kako bismo vam pomogli da pronađete gde se određena rečenica/reč pojavljuje na veb-sajtu. Trenutno, ako imate bilo kakvu sumnju u vezi sa nekim rečima i treba vam da pronađete njihovu specifičnu lokaciju na veb-sajtu, možete postaviti pitanje u odeljku "komentari" ili pitati koordinatora za prevod u Telegram grupi pomenutoj na početku ovog tutorijala.

![weblate](assets/23.webp)


Hvala unapred na vašem doprinosu prevodu Plan ₿ Network! Ako imate bilo kakva specifična pitanja ili komentare za nas, slobodno nas kontaktirajte putem [Telegram grupe](https://t.me/PlanBNetwork_ContentBuilder).