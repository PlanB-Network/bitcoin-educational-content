---
name: Stonewall x2
description: Razumevanje i korišćenje Stonewall x2 transakcija
---
![cover stonewall x2](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, Stonewallx2 transakcije funkcionišu samo ručnom razmenom PSBT-ova između uključenih strana, pod uslovom da su oba korisnika povezana na svoj Dojo. Međutim, moguće je da bi ovi alati mogli biti ponovo pokrenuti u narednim nedeljama. U međuvremenu, možete i dalje konsultovati ovaj članak da biste razumeli teorijski rad Stonewallx2 i naučili kako ih ručno izvršiti.*


_Ako razmišljate o ručnom izvođenju Stonewallx2, procedura je vrlo slična onoj opisanoj u ovom vodiču. Glavna razlika leži u izboru tipa Stonewallx2 transakcije: umesto da izaberete `Online`, kliknite na `In Person / Manual`. Zatim ćete morati ručno Exchange PSBT-ove kako biste konstruisali Stonewallx2 transakciju. Ako ste fizički blizu svog saradnika, možete skenirati QR kodove uzastopno. Ako ste na udaljenosti, JSON fajlovi se mogu razmeniti putem sigurnog komunikacionog kanala. Ostatak vodiča ostaje nepromenjen._


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije postanu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> *Pretvorite svaku potrošnju u CoinJoin.*

## Šta je Stonewall x2 transakcija?


Stonewall x2 je specifičan oblik Bitcoin transakcije usmeren na povećanje privatnosti korisnika tokom trošenja, kroz saradnju sa trećom stranom koja nije uključena u to trošenje. Ova metoda simulira mini-CoinJoin između dva učesnika, dok se vrši plaćanje trećoj strani. Stonewall x2 transakcije su dostupne na Samourai Wallet aplikaciji i Sparrow Wallet softveru. Obe su međusobno kompatibilne.


Njegovo funkcionisanje je relativno jednostavno: koristimo UTXO koji posedujemo da izvršimo uplatu i tražimo pomoć treće strane koja takođe doprinosi svojim UTXO. Transakcija rezultira sa četiri izlaza: dva od njih su jednake sume, jedan namenjen Address primaoca uplate, drugi Address koji pripada saradniku. Treći UTXO se vraća na drugi Address saradnika, omogućavajući im da povrate početni iznos (neutralna akcija za njih, modulo Mining naknade), a poslednji UTXO se vraća na Address koji pripada nama, što predstavlja kusur od uplate.


Dakle, tri različite uloge su definisane u Stonewall x2 transakcijama:


- Pošiljalac, koji vrši stvarno plaćanje;
- Saradnik, koji obezbeđuje bitkoine kako bi poboljšao ukupnu anonimnost transakcije, dok u potpunosti povrati svoja sredstva na kraju (neutralna akcija za njih, modulo Mining naknade);
- Primalac, koji možda nije svestan specifične prirode transakcije i jednostavno očekuje uplatu od pošiljaoca.


Hajde da uzmemo primer da bismo bolje razumeli. Alisa je u pekari da kupi svoj baget, koji košta `4,000 Sats`. Ona želi da plati u bitkoinima, dok održava određeni nivo privatnosti za svoju uplatu. Stoga poziva svog prijatelja Boba, koji će joj pomoći u ovom procesu.

![schema stonewall x2](assets/en/1.webp)

Analizom ove transakcije, možemo videti da je pekar zaista primio `4,000 Sats` kao uplatu za baget. Alisa je koristila `10,000 Sats` kao ulaz i primila `6,000 Sats` kao izlaz, što rezultira neto saldom od `-4,000 Sats`, što odgovara ceni bageta. Što se tiče Boba, on je obezbedio `15,000 Sats` kao ulaz i primio dva izlaza: jedan od `4,000 Sats` i drugi od `11,000 Sats`, što rezultira saldom od `0`.

U ovom primeru, namerno sam zanemario Mining naknade kako bih olakšao razumevanje. U stvarnosti, transakcione naknade se dele jednako između pošiljaoca uplate i saradnika.


## Koja je razlika između Stonewall i Stonewall x2?


Transakcija StonewallX2 funkcioniše isto kao i Stonewall transakcija, osim što je prva kolaborativna dok druga nije. Kao što smo videli, Stonewall x2 transakcija uključuje učešće treće strane, koja je eksternalna u odnosu na plaćanje, i koja će obezbediti svoje bitkoine kako bi poboljšala privatnost transakcije. U tipičnoj Stonewall transakciji, ulogu saradnika preuzima pošiljalac.


Hajde da ponovo razmotrimo naš primer sa Alisom u pekari. Ako nije mogla da pronađe nekoga poput Boba da joj se pridruži u trošku, mogla je sama da obavi Stonewall transakciju. Dakle, dva ulazna UTXO-a bi bila njena, i ona bi primila 3 na izlazu.

![transaction stonewall](assets/en/2.webp)


Sa spoljašnje tačke gledišta, obrazac transakcije bi ostao isti.

![Stonewall or Stonewall x2?](assets/en/5.webp)

Stoga, logika bi trebala biti sledeća kada se koristi Samourai alat za trošenje:


- Ako trgovac ne podržava PayJoin Stowaway, kolaborativna transakcija može biti obavljena sa drugom osobom van plaćanja koristeći Stonewall x2.
- Ako se ne pronađe niko za obavljanje Stonewall x2 transakcije, Stonewall transakcija se može obaviti samostalno, imitirajući ponašanje Stonewall x2 transakcije.
- Konačno, poslednja opcija bi bila da izvršite transakciju sa JoinBot-om, serverom koji održava Samourai, a koji može, na zahtev, delovati kao saradnik u Stonewall x2 transakciji.


Ako želite pronaći saradnika koji je voljan da vam pomogne u Stonewall X2 transakciji, možete posetiti ovu Telegram grupu (nezvaničnu) koju održavaju korisnici Samourai-a kako biste se povezali sa pošiljaocima i saradnicima: [Make Every Spend a CoinJoin](https://t.me/EverySpendACoinjoin).


[**-> Saznajte više o Stonewall transakcijama**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## Koja je svrha Stonewall x2 transakcije?


Stonewall x2 struktura dodaje značajnu količinu entropije transakciji i zbunjuje analizu lanca. Sa spoljašnje strane, takva transakcija može biti interpretirana kao mali CoinJoin između dve osobe. Ali u stvarnosti, to je plaćanje. Ova metoda generiše nesigurnosti u analizi lanca, pa čak dovodi i do lažnih tragova.


Hajde da se vratimo na primer sa Alisom, Bobom i Pekarom. Transakcija na Blockchain bi izgledala ovako:

![stonewall x2 public](assets/en/3.webp)

Spoljni posmatrač koji se oslanja na uobičajene heuristike analize lanca mogao bi pogrešno zaključiti da su "Alice i Bob izveli mali CoinJoin, sa po jednim UTXO kao ulazom i po dva UTXO-a kao izlazom."![pogrešno tumačenje stonewall x2](assets/en/4.webp)

Ovo tumačenje je netačno jer, kao što znate, UTXO je poslat Bakeru, Alice ima samo jedan izlaz promene, a Bob ima dva.

![transaction stonewall x2](assets/en/1.webp)

Čak i ako spoljašnji posmatrač uspe da identifikuje obrazac Stonewall x2 transakcije, neće imati sve informacije. Neće moći da odrede koji od dva UTXO-a istih iznosa odgovara uplati. Štaviše, neće moći da znaju da li je Alice ili Bob izvršio uplatu. Na kraju, neće moći da utvrde da li dva ulazna UTXO-a dolaze od dve različite osobe ili pripadaju jednoj osobi koja ih je spojila. Ova poslednja tačka je zbog činjenice da klasične Stonewall transakcije, koje smo gore pomenuli, prate potpuno isti obrazac kao Stonewall x2 transakcije. Spolja i bez dodatnih informacija o kontekstu, nemoguće je razlikovati Stonewall transakciju od Stonewall x2 transakcije. Međutim, prve nisu kolaborativne transakcije, dok druge jesu. Ovo dodaje još više sumnji u vezi sa ovim troškom.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## Kako uspostaviti vezu između Paynyms da biste mogli sarađivati putem Sorobana?


Kao i kod drugih kolaborativnih transakcija na Samourai (*Cahoots*), izvođenje Stonewall x2 uključuje Exchange delimično potpisanih transakcija između pošiljaoca i saradnika. Ovaj Exchange može se obaviti ručno, ukoliko ste fizički sa svojim saradnikom, ili automatski putem Soroban komunikacionog protokola.


Ako izaberete drugu opciju, biće potrebno da uspostavite vezu između Paynyms pre nego što budete mogli da izvršite Stonewall x2. Da biste to uradili, vaš Paynym mora "pratiti" Paynym vašeg saradnika, i obrnuto.


**Pristupanje Paynym-u saradnika:**


Da biste započeli, potrebno je dobiti kod plaćanja Paynym-a vašeg saradnika. U aplikaciji Samourai Wallet, vaš saradnik mora pritisnuti ikonu svog Paynym-a (mali robot) koja se nalazi u gornjem levom uglu ekrana, a zatim kliknuti na svoj Paynym nadimak, počevši sa `+...`. Na primer, moj je `+namelessmode0aF`.


![samourai paynym](assets/notext/6.webp)

Ako vaš saradnik koristi Sparrow Wallet, treba da klikne na karticu 'Tools', a zatim na 'Show PayNym'.![paynym sparrow](assets/notext/7.webp)

**Pratite PayNym vašeg saradnika iz Samourai Wallet:**


Ako koristite Samourai Wallet, pokrenite aplikaciju i pristupite meniju 'PayNyms' na isti način. Ako prvi put koristite svoj PayNym, biće potrebno da dobijete njegov identifikator.


![request paynym samourai](assets/notext/8.webp)


Zatim kliknite na plavi '+' u donjem desnom uglu ekrana.

![add collaborator paynym](assets/notext/9.webp)

Zatim možete nalepiti kod za plaćanje vašeg saradnika tako što ćete odabrati 'NALEPI KOD ZA PLAĆANJE', ili otvoriti kameru da skenirate njihov QR kod pritiskom na 'SKENIRAJ QR KOD'.

![paste paynym identifier](assets/notext/10.webp)


Kliknite na dugme 'PRATI'.

![follow paynym](assets/notext/11.webp)

Potvrdite klikom na 'YES'.

![confirm follow paynym](assets/notext/12.webp)

Softver će vam zatim ponuditi dugme 'CONNECT'. Nije potrebno kliknuti na ovo dugme za naš vodič. Ovaj korak je potreban samo ako planirate da izvršite uplate drugom PayNym-u kao deo BIP47, što nije povezano sa našim vodičem.

![connect paynym](assets/notext/13.webp)

Kada vaš PayNym prati PayNym vašeg saradnika, ponovite ovaj proces u suprotnom smeru kako bi vaš saradnik mogao da prati vas. Tada možete izvršiti Stonewall x2 transakciju.


**Pratite PayNym vašeg saradnika iz Sparrow Wallet:**


Ako koristite Sparrow Wallet, otvorite svoj Wallet i pristupite meniju 'Show PayNym'. Ako prvi put koristite svoj PayNym, moraćete da dobijete identifikator klikom na 'Retrieve PayNym'.

![request paynym sparrow](assets/notext/14.webp)

Zatim unesite identifikator PayNym vašeg saradnika (bilo njihov nadimak '+...' ili njihov platni kod 'PM...') u polje 'Pronađi kontakt', i kliknite na dugme 'Dodaj kontakt'.

![add contact paynym](assets/notext/15.webp)

Softver će vam zatim ponuditi dugme 'Link Contact'. Nije potrebno kliknuti na ovo dugme za naš vodič. Ovaj korak je potreban samo ako planirate da izvršite uplate na navedeni PayNym kao deo BIP47, što nije povezano sa našim vodičem.


Kada vaš PayNym prati PayNym vašeg saradnika, ponovite ovaj proces u suprotnom smeru kako bi vas i vaš saradnik mogao pratiti. Zatim možete izvršiti Stonewall x2 transakciju.

## Kako napraviti Stonewall x2 transakciju na Samourai Wallet?


Ako ste završili prethodne korake povezivanja Paynyms-a, konačno ste spremni da izvršite Stonewall x2 transakciju! Da biste to uradili, pratite naš video tutorijal na Samourai Wallet:

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## Kako napraviti Stonewall x2 transakciju na Sparrow Wallet?


Ako ste završili prethodne korake povezivanja Paynyms-a, konačno ste spremni da izvršite Stonewall x2 transakciju! Da biste to uradili, pratite naš video tutorijal na Sparrow Wallet:

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**Spoljni resursi:**


- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.