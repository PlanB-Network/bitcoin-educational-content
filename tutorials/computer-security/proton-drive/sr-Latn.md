---
name: Proton Drive
description: Implementacija rezervne kopije
---
![cover](assets/cover.webp)


Danas je ključno uspostaviti strategiju kako bi se osigurala dostupnost, sigurnost i rezervna kopija vaših ličnih fajlova, kao što su vaši lični dokumenti, fotografije ili važni projekti. Gubitak ovih podataka može biti katastrofalan.


Da biste sprečili ove probleme, savetujem održavanje više rezervnih kopija vaših fajlova na različitim medijima. Uobičajena strategija u računarstvu je strategija rezervne kopije "3-2-1", koja osigurava zaštitu vaših fajlova:


- **3** kopije vaših fajlova;
- Sačuvano na najmanje **2** različite vrste medija;
- Sa najmanje **1** kopijom čuvanom van lokacije.


Drugim rečima, preporučljivo je čuvati vaše fajlove na 3 različite lokacije, koristeći različite tipove medija, kao što su vaš računar, eksterni hard disk, USB stik ili online servis za skladištenje. I na kraju, imati kopiju van lokacije znači da bi trebalo da imate rezervnu kopiju pohranjenu izvan vašeg doma ili poslovnog prostora. Ova poslednja tačka pomaže da se izbegne potpuni gubitak vaših fajlova u slučaju lokalnih katastrofa kao što su požari ili poplave. Eksterna kopija, udaljena od vašeg doma ili poslovnog prostora, osigurava da će vaši podaci preživeti bez obzira na lokalne rizike.


Da biste olakšali implementaciju strategije rezervne kopije 3-2-1, možete koristiti uslugu online skladištenja. Ova rešenja, obično nazvana "oblak", nude dodatnu zaštitu skladištenjem vaših podataka na sigurnim serverima dostupnim sa bilo kog uređaja. Termin "oblak" jednostavno se odnosi na skladištenje podataka na eksternim serverima.


Mnogi ljudi koriste rešenja za skladištenje velikih digitalnih kompanija: Google Drive, Microsoft OneDrive ili Apple iCloud.

![PROTON DRIVE](assets/notext/01.webp)

Ova rešenja su pogodna za svakodnevnu upotrebu i obezbeđuju dostupnost vaših podataka, ali ne garantuju poverljivost. U ovom vodiču predlažem da otkrijemo drugo rešenje, jednako lako za korišćenje kao alati za skladištenje velikih tehnoloških kompanija, ali sa dodatnim merama za zaštitu vaše privatnosti. Ovo rešenje je Proton Drive, alat za online skladištenje švajcarske kompanije Proton. Takođe ćemo videti kako lako implementirati 3-2-1 strategiju pogodnu za svakodnevnu upotrebu.


## Uvod u Proton Drive

Proton Drive je intrigantno rešenje za online skladištenje jer kombinuje jednostavnost korišćenja sa sigurnošću za vaše fajlove. Za razliku od tradicionalnih cloud servisa velikih tehnoloških kompanija, Proton Drive implementira mere za zaštitu vaše privatnosti. Osigurava end-to-end enkripciju za sve vaše fajlove, što znači da čak ni Protonovi timovi ne mogu pristupiti vašim podacima. Štaviše, Proton Drive je open-source, što omogućava nezavisnim stručnjacima da slobodno pregledaju kod softvera.

![PROTON DRIVE](assets/notext/02.webp)

Poslovni model Proton-a zasnovan je na sistemu pretplate, što je ohrabrujuće jer ukazuje na to da se kompanija finansira bez nužnog iskorišćavanja podataka svojih korisnika. U ovom vodiču, objasniću kako koristiti besplatnu verziju Proton Drive-a, ali postoje i nekoliko nivoa pretplate koji nude više funkcija. Ovaj poslovni model je poželjniji od besplatnog sistema u stilu Big Tech kompanija, koji bi mogao navesti na razmišljanje da li se naši lični podaci koriste za profit. Čini se da to nije slučaj sa Proton-om.


Proton Drive nudi mnogo više od jednostavnih opcija za skladištenje; takođe omogućava deljenje, uređivanje i saradnju na dokumentima online sa alatima za uređivanje, slično Google-ovom softverskom paketu.


Što se tiče [cena](https://proton.me/pricing), besplatna verzija nudi do 5 GB skladišnog prostora i uključuje osnovne funkcije. Da biste proširili mogućnosti na 200 GB skladišnog prostora, dostupna je specifična pretplata na Proton Drive za 4 € mesečno. Paket Proton Unlimited, s druge strane, nudi za 10 € mesečno skladišni prostor do 500 GB na Proton Drive-u, pored uključivanja svih Proton-ovih plaćenih usluga, kao što su VPN i menadžer lozinki, kao i dodatne pogodnosti na besplatnim alatima (e-pošta i kalendar).

![PROTON DRIVE](assets/notext/03.webp)

## Kako napraviti Proton nalog?


Ako još uvek nemate Proton nalog, biće potrebno da ga kreirate. Upućujem vas na naš Proton Mail vodič u kojem detaljno objašnjavamo kako kreirati besplatan Proton nalog i postaviti ga:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![PROTON DRIVE](assets/notext/04.webp)

## Kako postaviti Proton Drive?


Kada se prijavite u svoj Proton mail, kliknite na ikonu sa četiri mala kvadrata u gornjem levom uglu ekrana.

![PROTON DRIVE](assets/notext/05.webp)

Zatim kliknite na "*Drive*".

![PROTON DRIVE](assets/notext/06.webp)

Sada ste na svom Proton Drive-u.

![PROTON DRIVE](assets/notext/07.webp)

## Kako koristiti Proton Drive?

Da biste dodali fajlove u vaš Proton Drive, kada isključivo koristite web verziju (o korišćenju lokalne verzije ćemo razgovarati kasnije), jednostavno treba da prevučete i otpustite vaše dokumente direktno u interfejs. 

![PROTON DRIVE](assets/notext/08.webp) 

Zatim možete pronaći vaš dokument na početnoj stranici. 

![PROTON DRIVE](assets/notext/09.webp)

Da biste dodali novi predmet, kliknite na dugme "*New*" u gornjem levom uglu ekrana.

![PROTON DRIVE](assets/notext/10.webp) 

Funkcija "*Upload file*" otvara vaš lokalni istraživač fajlova, omogućavajući vam da izaberete i uvezete nove dokumente u Proton Drive, baš kao što biste uradili prevlačenjem i otpuštanjem.

![PROTON DRIVE](assets/notext/11.webp) 

"*Upload folder*" vam omogućava da uvezete čitav folder.

![PROTON DRIVE](assets/notext/12.webp) 

"*New folder*" vam omogućava da kreirate folder kako biste bolje organizovali vaše dokumente na Proton Drive. 

![PROTON DRIVE](assets/notext/13.webp) 

Kliknite na ovu opciju, da dodelite ime vašem folderu. 

![PROTON DRIVE](assets/notext/14.webp) 

Zatim ćete ga pronaći direktno na početnoj stranici Proton Drive. 

![PROTON DRIVE](assets/notext/15.webp) 

Na kraju, "*New document*" vam omogućava da kreirate novi tekstualni dokument direktno u Proton Drive.

![PROTON DRIVE](assets/notext/16.webp) 

Klikom na njega, otvara se novi prazan dokument. 

![PROTON DRIVE](assets/notext/17.webp) 

Možete pisati na njemu i uređivati ga. 

![PROTON DRIVE](assets/notext/18.webp) 

Ako kliknete na dugme "*Share*" u gornjem desnom uglu, možete podeliti dokument. 

![PROTON DRIVE](assets/notext/19.webp) 

Samo treba da unesete email saradnika kojem želite da date pristup dokumentu, bilo u režimu samo za čitanje ili sa pravima uređivanja. 

![PROTON DRIVE](assets/notext/20.webp) 

Ako se vratite na vaš Proton Drive, možete videti da je dokument uspešno sačuvan. 

![PROTON DRIVE](assets/notext/21.webp) 

U kartici "*Shared*", možete pronaći dokumente koje ste podelili sa drugima. 

![PROTON DRIVE](assets/notext/22.webp) 

A u kartici "*Shared with me*", možete videti dokumente koje su drugi podelili sa vama.

![PROTON DRIVE](assets/notext/23.webp) 

Na kraju, u kartici "*Trash*", možete pronaći vaše nedavno obrisane dokumente. 

![PROTON DRIVE](assets/notext/24.webp) 

Većina podešavanja za vaš Proton Drive je integrisana u vaš Proton nalog. Za detaljna uputstva o podešavanju vašeg naloga, pozivam vas da pogledate ovaj tutorijal:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Kako instalirati Proton Drive softver?

Proton Drive takođe nudi softver koji omogućava sinhronizaciju vaših lokalnih fajlova sa vašim onlajn prostorom za skladištenje. Ova funkcija olakšava i automatizuje implementaciju naše 3-2-1 strategije bekapa. Sa Proton Drive softverom, dobijate 2 sinhronizovane kopije vaših fajlova: jednu na vašem računaru i drugu na Protonovim serverima, čime se ispunjavaju kriterijumi 2 tipa medija i bekapa van lokacije. Biće potrebno samo da kreirate treću kopiju, koju ćemo kasnije postaviti.

Da biste koristili softver, kliknite na karticu "*Computers*" na vašem Proton Drive nalogu i odaberite dugme koje odgovara vašem operativnom sistemu da biste nastavili sa preuzimanjem.

![PROTON DRIVE](assets/notext/25.webp)

Jednom kada je instaliran, potrebno je da se prijavite kako biste otključali svoj nalog, zatim kliknite na "*Sign in*".

![PROTON DRIVE](assets/notext/26.webp)

Izaberite lokalne datoteke koje želite da sinhronizujete sa svojim Proton Drive-om.

![PROTON DRIVE](assets/notext/27.webp)

Na primer, izabrao sam samo folder "*Proton Backup*". Zatim kliknite na dugme "*Continue*".

![PROTON DRIVE](assets/notext/28.webp)

Zatim ćete stići do softver interfejsa, koji je sličan veb aplikaciji.

![PROTON DRIVE](assets/notext/29.webp)

Od sada ćete imati folder pod nazivom "*Proton Drive*" lokalno na vašem računaru, koja će prikupljati sve vaše dokumente sačuvane na Proton online. Ako dodate fajl u ovaj folder sa vašeg računara, automatski ćete ga pronaći na početnoj stranici web aplikacije Proton Drive, i obrnuto. Za foldere koje ste odabrali da sinhronizujete tokom instalacije softvera, možete ih pronaći online tako što ćete otići u sekciju "*Computers*" Proton Drive-a i zatim odabrati vaš računar.

![PROTON DRIVE](assets/notext/30.webp)

Dakle, sve vaše datoteke su rezervisane i sinhronizovane kako lokalno na vašem računaru, tako i na Proton Drive-ovim onlajn serverima.


## Kako napraviti rezervnu kopiju Proton Drive-a?


Ako ste pratili prethodne korake, sada imate 2 različite lokacije za rezervne kopije vaših važnih fajlova. Da bismo kompletirali našu 3-2-1 strategiju bekapa, potrebno je dodati treću kopiju.

Predlažem da izvršite ovu dodatnu rezervnu kopiju na eksternom mediju, kao što je eksterni hard disk ili USB stik, na primer. U zavisnosti od intenziteta vaše upotrebe, postavite odgovarajuću učestalost ažuriranja rezervne kopije (nedeljno, mesečno, polugodišnje...). U svakom izabranom intervalu, potrebno je da preuzmete celokupan sadržaj vašeg Proton Drive-a kako biste napravili rezervnu kopiju podataka na izabranom eksternom mediju. Na taj način, čak i u slučaju krađe vašeg računara i istovremenog uništenja Proton-ovih servera, i dalje ćete imati siguran pristup vašim fajlovima zahvaljujući kopiji na USB stiku.


Da biste to uradili, idite na svoj Proton Drive.

![PROTON DRIVE](assets/notext/31.webp)

Odaberite sve svoje datoteke.

![PROTON DRIVE](assets/notext/32.webp)

Zatim kliknite na malu strelicu da ih preuzmete.

![PROTON DRIVE](assets/notext/33.webp)

Zatim ćemo ponoviti operaciju sa našim fajlovima sinhronizovanim sa našeg računara.

![PROTON DRIVE](assets/notext/34.webp)

Zatim ćete pronaći .zip datoteke u svojim preuzimanjima. Jednostavno povežite eksterni medij po vašem izboru sa računarom, a zatim prenesite te datoteke na njega.

![PROTON DRIVE](assets/notext/35.webp)

Ako ste zabrinuti da bi ovaj USB stik mogao biti ukraden, razmislite o enkripciji pomoću softvera kao što je VeraCrypt (uskoro ćemo napraviti tutorijal o ovom softveru).


Čestitamo, sada imate veoma robustnu 3-2-1 strategiju bekapa, koja vam omogućava da drastično smanjite rizik od gubitka pristupa vašim ličnim dokumentima, bez obzira na okolnosti. Odabirom Proton Drive-a za vaše onlajn rezervne kopije, takođe imate koristi od end-to-end enkripcije, koja garantuje zaštitu vaše privatnosti.


Da biste saznali više o zaštiti vašeg online prisustva i izbegavanju hakovanja, takođe preporučujem da pogledate naš detaljni vodič o Bitwarden menadžeru lozinki:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9
