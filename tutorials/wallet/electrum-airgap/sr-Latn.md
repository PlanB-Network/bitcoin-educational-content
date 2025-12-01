---
name: Electrum Airgap
description: Prvi korak ka bezbednosti, cold wallet sa Electrumom
---
![cover](assets/cover.webp)



## Cold Wallet



U ovom vodiču ću objasniti kako napraviti svoj prvi uređaj za potpisivanje sa vazdušnim razmakom, isključen sa Interneta, čak i bez posvećenog Hardware Wallet. Sve što vam je potrebno je da imate dva dostupna računara:




- stari uređaj da zauvek bude sprečen da se poveže na Internet;
- vaš svakodnevni računar.



Ova konfiguracija omogućava veći stepen sigurnosti nego klasična `Hot Wallet`: stari računar--bez mrežne veze--je čuvar vaših privatnih ključeva, koji nikada nisu izloženi na Internetu, već su pohranjeni van mreže ("airgap" ili "Cold").



Umesto toga, instaliraćete Wallet displej ("samo za gledanje") na vašem svakodnevnom računaru, koji je povezan na mrežu i sa kojim možete, na primer, proveriti stanja i pripremiti transakcije priznanica.



## Wallet Airgap: Šta i Kako



Izvođenjem koraka iz ovog vodiča, instaliraćemo dva Software Wallet Electrum na dva različita računara i na kraju kreirati dva Novčanika sa različitim keystore-ima: Wallet airgap će koristiti celu hijerarhiju Wallet HD, dok će Wallet display biti generisan sa master javnim ključem.



Ova dva novčanika će se, u svakom pogledu, veoma razlikovati jedan od drugog. Jedina stvar koju će imati zajedničku, kao što ćemo videti, su adrese:




- gW-13 na računaru sa vazdušnim jazom može samo da potpisuje, ali, isključen sa mreže, ne zna saldo i korišćene adrese;
- Wallet na dnevnom računaru će moći samo da priprema i propagira transakcije, bez mogućnosti raspolaganja rashodima, u odsustvu privatnih ključeva.



## Preliminarne Pripreme



Da biste preuzeli Electrum, preporučujem da pratite prve korake u ovom vodiču:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Nakon preuzimanja uvek proverite izdanje pre nego što ga instalirate, zatim nastavite sa konfiguracijom "One Server", kao što ćete pronaći u odeljku za pomoć, pod `Start with a Dummy Wallet`.



Operacija konfiguracije "One Server" je potrebna samo za Wallet instaliran na dnevnom računaru, jer će drugi računar uvek biti van mreže.



Sledeće operacije uključuju vežbanje na dva različita računara (i Novčanika), pa sam radi praktičnosti i fokusa odlučio da postavim Wallet airgap sa svetlom temom, dok Wallet ekran ima tamnu temu.



## Wallet Kreiranje vazdušnog jaza



Nakon preuzimanja i verifikacije preuzimanja Electrum-a, uzmite kopiju izvršnog fajla i prenesite je na vaš računar koji nije povezan na internet. Zatim ga pokrenite i instalirajte Electrum.



Dvaput kliknite da pokrenete Electrum: računar na kojem ćete koristiti ovaj Wallet je offline, ignorišite mrežna podešavanja i pređite na kreiranje Wallet koji ćemo u ovom vodiču nazvati `airgap`.



![image](assets/en/01.webp)



Izaberite _Standard wallet_.



![image](assets/en/02.webp)



Zatim izaberite _Create a new seed_ da bi softver generate imao Mnemonic.



![image](assets/en/03.webp)



Tačno prepišite 12 generate reči iz Electrum-a na papirnu podlogu i nastavite sa korakom verifikacije, ponovo unesite reči redosledom kada Electrum to zatraži.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Nakon što je kreacija Wallet završena, postavite složenu lozinku (`Strong`) za šifrovanje Wallet fajla na uređaju sa vazdušnim jazom. Ovaj korak je veoma delikatan i važan, jer lozinka odabrana sada sprečava pristup Wallet koji ima dispozitivnu moć, omogućavajući trošenje sredstava i potpisivanje transakcija.



![image](assets/en/06.webp)



Klikom na _Finish_ Wallet je definisan i pojavljuje se na ekranu. Naravno, indikator mrežne veze, tj. obojena tačka u donjem desnom uglu, je crvena, jer je računar isključen i ne dozvoljava Wallet da izloži online ključeve.



![image](assets/en/07.webp)



## Kreacija Wallet Vizualizacije



Sada kada vaš Wallet ima offline privatne ključeve, potrebno je postaviti prikazni Wallet, ili `samo-za-gledanje`, koji će vam omogućiti da vidite stanje, kao i da pripremite transakcije prijema kako biste nastavili bezbedno akumulirati Sats.



Sa Wallet koji se nalazi na offline uređaju, izaberite meni _Wallet_ -> _Information_



![image](assets/en/08.webp)



Prozor koji sadrži sve vaše Wallet informacije će se pojaviti, gde možete proveriti `derivation path` i `master fingerprint`, na primer da ih označite pored reči u Mnemonic rečenici (snažno preporučeno).



![image](assets/en/09.webp)



Zapamtite da uzimate ove podatke sa računara koji nije povezan, tako da ćete morati kopirati/nalepiti `zpub` u tekstualnu datoteku i sačuvati je na USB memoriju.



Sada možete preći na računar povezan na Internet, pokrenuti Electrum i kreirati novi Wallet.



Iz _Datoteka_ menija, izaberite _Novo/Obnovi_.



![image](assets/en/10.webp)



Novi Wallet je samo za pregled, tako da ćemo ga u ovom vodiču nazvati `watch-only`.



![image](assets/en/12.webp)



Na sledećem ekranu izaberite _Standard wallet_ i nastavite klikom na _Next_.



![image](assets/en/13.webp)



Pri odabiru `Keystore` budite pažljivi: za kreiranje prikaza Wallet izaberite _Use a master key_. Zatim nastavite sa _Next_.



![image](assets/en/14.webp)



Nalepite ovde `zpub` kopiran sa Wallet offline i koji ste doneli na ovaj računar putem USB medija.



![image](assets/en/15.webp)



Zaključite postavljanjem jake lozinke za ovaj Wallet, koja će se možda razlikovati od one izabrane za odgovarajući Cold.



Videćete prikaz Wallet sa upozorenjem. Poruka vas podseća da je ovo samo prikaz Wallet i da ne možete sa njim trošiti povezane fondove.



**Dobro Zapamti**: **zato ćeš uvek morati da poseduješ privatne ključeve da bi raspolagao UTXO-ima ovog Wallet**. Sa dobrim sistemom za bekap, neće ti biti teško da ostaneš u potpunom vlasništvu svojih Bitcoina.



![image](assets/en/16.webp)



Ovo upozorenje će se pojaviti svaki put kada otvorite ovaj Wallet. Kliknite _Ok_ i pređimo na korak verifikacije.



## Verifikacija dva Wallet



Kao što smo naučili na početku ovog vodiča, Wallet airgap i njegov displej Wallet su dva portfolija koja imaju različite funkcije, ali **dele iste adrese**.



Ako pogledamo dva Novčanika jedan pored drugog, vizuelno primećujemo da u Wallet airgap postoji simbol "seed", dok u watch-only nema. Čak i ovaj detalj će vam pomoći da zapamtite da Wallet prikaz Wallet nema privatne ključeve.



![image](assets/en/17.webp)



Da biste napravili tačnu prvu proveru, međutim, izaberite u oba Novčanika meni `Adrese`: pošto dele iste adrese, lista adresa bi trebalo da bude identična za oba.



![image](assets/en/18.webp)



⚠️ **PAŽNJA**: **ne može biti srednjeg puta; adrese moraju biti iste. U slučaju da su različite, potrebno je obrisati sav dosadašnji rad i početi ispočetka**.



Sada možete nastaviti sa dva različita provera. Prvo, pokušajte da obrišete dva Novčanika i da ih obnovite od nule, svaki na odgovarajućem računaru. U slučaju da nastavite sa ovom proverom, procedure za prikaz Wallet su identične onima navedenim gore.



Za Wallet airgap, međutim, na ekranu `keystore` moraćete da izaberete _Već imam seed_ i unesete reči kopiranjem sa vašeg papirnog backup-a.



Nakon što se završi probni period "bez opterećenja", možete pokušati da izvršite transakciju male sume i odmah je potrošite.



## Primanje i Trošenje Transakcija



Da biste počeli koristiti svoj Electrum airgap, možete napraviti transakciju prijema s malim iznosom, a zatim ga potrošiti prema vlastitom Address. Tada se možete upoznati s postupkom, potvrđujući da imate potpunu kontrolu nad sredstvima.



**Napomena**: Ne preporučujem da položite veliku količinu sredstava na Wallet pre nego što budete sigurni da možete glatko obavljati sve operacije.



Koraci objašnjeni u nastavku mogu, na prvi pogled, delovati komplikovano. Nemojte da vas to obeshrabri: kada ih prvi put isprobate, videćete da je potrebno samo nekoliko minuta da ih završite.



Da biste primili sredstva, morate obavezno koristiti displej Wallet koji se nalazi na vašem računaru povezanom na Internet. Iz menija `Receive` kliknite na _Create request_ da bi Electrum generate prvi dostupan Address i koristite ga da nam pošaljete nekoliko Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Jednom kada je transakcija propagirana, možete već videti da-je prirodno- ona je vidljiva samo na ekranu Wallet, a ne na Wallet airgap.



![image](assets/en/21.webp)



Nakon što vaša transakcija dobije neku potvrdu, možete pripremiti trošak i tako pokušati proceduru potpisivanja sa Wallet izvan mreže. Zatim pripremite transakciju na samo-za-gledanje i pritisnite _Preview_ da je proverite.



![image](assets/en/22.webp)



Dobijate prozor za napredne transakcije gde možete videti da:




- transakcija nije potpisana (`Status: Unsigned);
- `Sign` i `Broadcast` komande su inhibirane.



Jedina stvar koju možete da uradite je da izvezete transakciju takvu kakva jeste, da je odnesete na Wallet airgap i potpišete.



Umetnite USB fleš disk u svoj računar i, iz menija u donjem levom uglu, izaberite _Share_.



![image](assets/en/23.webp)



Nakon toga izaberite _Save to file_.



![image](assets/en/24.webp)



Sačuvaj transakciju na USB memoriju.



Primetićete da Electrum daje datoteci ime koje nosi prve cifre transaction ID, a ekstenzija datoteke je `.PSBT`, što znači `Partially Signed Bitcoin Transaction`.



Izvucite medij sa datotekom `.PSBT` i povežite ga sa računarom van mreže.



Sa Wallet airgap-a, sada izaberite meni _Tools_, zatim _Load transaction_ i potom _From file_.



![image](assets/en/25.webp)



Pomoću upravitelja datoteka odaberite `.PSBT` iz njegove lokacije.



![image](assets/en/29.webp)



Softver za računar van mreže automatski će otvoriti prozor za napredne transakcije, potpuno identičan onome kako ste ga videli na Wallet ekranu. Status je `Nepotpisano`, ali razlika je u tome što je ovde komanda `Potpiši` aktivna. I to je upravo ono što ćete morati izvršiti.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Sada kada je transakcija potpisana, zapamtite da je vaš Wallet na offline mašini. Stoga-čak i ako vidite da je komanda `Broadcast` aktivna-vaš Wallet neće moći da propagira transakciju na Bitcoin mrežu.



Šta treba da uradiš sada je da ponoviš operaciju izvoza potpisane transakcije na USB stik, kako bi mogao da je uvezeš na računar povezan na Internet i propagiraš je.



Iz donjeg levog menija, ponovo izaberite _Share_ i zatim _Save to file_.



![image](assets/en/28.webp)



Sada datoteka ima drugačiju ekstenziju: **umesto `.PSBT` sada transakcija ima ekstenziju `.txn`. Od sada će vam Electrum na ovaj način omogućiti da prepoznate potpisane transakcije od nepotpisanih**.



![image](assets/en/30.webp)



Za konačnu propagaciju transakcije, izvadite USB stik iz računara koji nije povezan na mrežu i ubacite ga u računar povezan na Internet.



Sa sata samo za gledanje, ponovite proceduru uvoza, to jest, iz menija _Alati_ izaberite _Učitaj transakciju_ i na kraju _Iz datoteke_.



![image](assets/en/31.webp)



Electrum će otvoriti prozor transakcije za vas, što je značajno drugačije od onog prikazanog ranije na ovom Wallet, jer je sada potpisan (`Status: Signed`) i komanda `Broadcast` je dostupna.



Poslednja operacija koju treba da uradite je upravo to:



![image](assets/en/32.webp)



## Zaključci



Vaši testovi su sada završeni. Ako ste pratili vodič i dobili iste rezultate, kreirali ste Wallet Cold sa Electrum-om, na dva različita računara, koje možete koristiti u airgap režimu za čuvanje vaših Bitcoina.



Jedine stvari na koje ćete morati obratiti posebnu pažnju su dve:


1) **nikada ne koristite Wallet airgap za generate adrese primanja**. Pošto je offline, uvek će vam ponuditi prvi Address, koji se poklapa sa onim koji ste upravo koristili za testnu transakciju;



![image](assets/en/33.webp)



_Kao što možete videti na slici iznad, offline Wallet ne zna svoju sopstvenu Address istoriju. U tom pogledu je potpuno slep. **Jedini zadatak koji može da uradi za vas je da čuva vaše offline ključeve i potpisuje vaše transakcije**_.



2) Koristite USB fleš disk posvećen samo za ovu svrhu, **ne koristite medij koji često koristite**. Svakodnevni alati su podložniji sajber napadima, i nenamerno, mogli biste napasti čak i računar koji držite isključenim sa mreže. USB stik koji koristite samo za ovu svrhu ima vrlo malo prilika da dođe u kontakt sa vašim računarom online, posebno ako ste hodler koji ne mora da troši, čime se smanjuje verovatnoća primanja i prenosa virusa, malvera, itd.