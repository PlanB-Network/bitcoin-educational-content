---
name: Ashigaru - Stonewall x2
description: Razumevanje i korišćenje Stonewall x2 transakcija na Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Neka svaka potrošnja bude coinjoin

## Šta je Stonewall x2 transakcija?



Stonewall x2 je specifičan oblik Bitcoin transakcije dizajniran da poveća poverljivost korisnika prilikom trošenja, kroz saradnju sa trećom stranom koja nije uključena u trošak. Ova metoda simulira mini-coinjoin između dva učesnika, dok vrši plaćanje trećoj strani. Stonewall x2 transakcije su dostupne na Ashigaru aplikaciji, fork od Samourai Wallet (tima koji stoji iza kreacije ovog tipa transakcije).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Kako to funkcioniše je relativno jednostavno: koristite UTXO koji posedujete da izvršite plaćanje, i angažujete pomoć treće strane koja takođe doprinosi sa svojim UTXO. Transakcija se završava sa četiri izlaza: dva od njih u jednakim iznosima, jedan namenjen adresi primaoca, drugi adresi koja pripada saradniku. Treći UTXO se vraća na drugu adresu koja pripada saradniku, omogućavajući mu da povrati početni iznos (neutralna akcija za njega, modulo troškovi mining), i konačni UTXO se vraća na adresu koja pripada nama, što predstavlja razmenu plaćanja.



Tri različite uloge su tako definisane u Stonewall x2 transakcijama:




- Izdavalac, koji vrši stvarnu uplatu ;
- Saradnik, koji stavlja bitkoine na raspolaganje kako bi poboljšao anonimnost transakcije, dok na kraju u potpunosti povrati svoja sredstva (neutralna akcija za njega, modulo troškovi mining);
- Primalac, koji možda nije svestan specifične prirode transakcije i jednostavno očekuje uplatu od pošiljaoca.



Hajde da uzmemo primer. Alice je kod pekara da kupi svoju baget, koji košta `4,000 sats`. Ona želi da plati u bitkoinima, dok zadržava određenu poverljivost o svojoj uplati. Zato poziva svog prijatelja Bob, koji će joj pomoći u tome.



![image](assets/fr/01.webp)



Analizirajući ovu transakciju, možemo videti da je pekar zapravo primio `4,000 sats` kao uplatu za baget. Alice je koristio `10,000 sats` kao ulaz i povratio `6,000 sats` kao izlaz, što daje neto saldo od `-4,000 sats`, što odgovara ceni bageta. Što se tiče Bob, on je obezbedio `15,000 sats` kao ulaz i primio dva izlaza: jedan od `4,000 sats` i drugi od `11,000 sats`, što čini saldo od `0`.



U ovom primeru, namerno sam zanemario mining naknade kako bih olakšao razumevanje. U stvarnosti, transakcione naknade se dele jednako između izdavaoca plaćanja i saradnika.



## Koja je razlika između Stonewall i Stonewall x2?



Transakcija StonewallX2 funkcioniše na potpuno isti način kao i Stonewall transakcija, osim što je prva kolaborativna, dok druga nije. Kao što smo videli, Stonewall x2 transakcija uključuje učešće treće strane, koja je eksternalna u odnosu na plaćanje, i koja će staviti svoje bitkoine na raspolaganje kako bi poboljšala poverljivost transakcije. U klasičnoj Stonewall transakciji, ulogu saradnika preuzima pošiljalac.



Hajde da se vratimo na naš primer Alice u pekari. Da nije uspela da pronađe nekoga poput Bob da je prati u njenom trošenju, mogla je sama da izvede Stonewall. Na taj način, dva UTXO-a na ulazu bi bila njena, a pokupila bi 3 na izlazu.



![image](assets/fr/02.webp)




Iz perspektive autsajdera, transakcija bi ostala ista.



![image](assets/fr/05.webp)



Logika bi stoga trebala biti sledeća kada želite da koristite alat za trošenje Ashigaru:




- Ako trgovac ne podržava Payjoin Stowaway, možete napraviti kolaborativnu transakciju sa drugom osobom van plaćanja zahvaljujući Stonewall x2 ;
- Ako ne možete pronaći nikoga za Stonewall x2 transakciju, možete napraviti samo Stonewall transakciju, koja će oponašati ponašanje Stonewall x2 transakcije.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Koja je svrha Stonewall x2 transakcije?



Struktura Stonewall x2 dodaje ogromnu količinu entropije transakciji, zbunjujući analizu lanca. Gledano spolja, takva transakcija može biti interpretirana kao mali Coinjoin između dve osobe. Ali u stvarnosti, to je plaćanje. Ova metoda stoga stvara nesigurnosti u analizi lanca, ili čak dovodi do lažnih tragova.



Hajde da uzmemo primer Alice, Bob i Boulanger. Transakcija na blockchain-u bi izgledala ovako:



![image](assets/fr/03.webp)



Spoljašnji posmatrač koji se oslanja na uobičajene heuristike analize lanca mogao bi pogrešno zaključiti da "*Alice i Bob su napravili mali coinjoin, sa po jednim UTXO ulazom i po dva UTXO izlaza*".



![image](assets/fr/04.webp)



Ovo tumačenje je netačno jer, kao što znate, UTXO je poslat Boulangeru, Alice ima samo jedan izlaz za razmenu, a Bob ima dva.



![image](assets/fr/01.webp)



Čak i ako spoljašnji posmatrač uspe da identifikuje paterne Stonewall x2 transakcije, neće imati sve informacije. Neće moći da odredi koji od dva UTXO-a istih iznosa odgovara uplati. Takođe, neće moći da odredi da li je uplatu izvršio Alice ili Bob. Na kraju, neće moći da odredi da li su dva uneta UTXO-a od dve različite osobe, ili pripadaju jednoj osobi koja ih je spojila. Ova poslednja tačka je zbog činjenice da klasične Stonewall transakcije, o kojima je gore bilo reči, prate tačno isti paterne kao Stonewall x2 transakcije. Gledano spolja i bez dodatnih kontekstualnih informacija, nemoguće je razlikovati Stonewall transakciju od Stonewall x2 transakcije. Prve nisu kolaborativne transakcije, dok druge jesu. Ovo dodaje još više sumnje na trošak.



![image](assets/fr/05.webp)




## Kako da uspostavim vezu između Paynyms?



Kao i kod drugih kolaborativnih transakcija na Ashigaru (*Cahoots*), Stonewall x2 uključuje razmenu delimično potpisanih transakcija između pošiljaoca i saradnika. Ova razmena može se obaviti ručno, ako ste fizički prisutni sa svojim saradnikom, ili automatski koristeći Soroban komunikacioni protokol.



Ako izaberete drugu opciju, moraćete da uspostavite vezu između Paynyms pre nego što možete da izvršite Stonewall x2. Da biste to uradili, vaš Paynym mora "*pratiti*" Paynym vašeg saradnika, i obrnuto. Da biste saznali kako to da uradite, možete pratiti početak ovog drugog tutorijala:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Kako da napravim Stonewall x2 transakciju na Ashigaru?



Da biste izvršili Stonewall x2 transakciju, kliknite na sliku vašeg Paynym-a u gornjem levom uglu ekrana, zatim otvorite meni `Collaborate`. Osoba koja učestvuje u transakciji sa vama mora uraditi isto, osim ako lično razmenjujete QR kodove.



![Image](assets/fr/06.webp)



Imate dve opcije: izaberite `Initiate` ako ste pošiljalac uplate, ili `Participate` ako ste osoba koja učestvuje u transakciji, ali niste ni platiša ni stvarni primalac.



![Image](assets/fr/07.webp)



Ako imate ulogu saradnika, procedura je veoma jednostavna. Za daljinsku saradnju putem Soroban mreže, kliknite na `Participate`, izaberite nalog koji želite da koristite, zatim pritisnite `LISTEN FOR CAHOOTS REQUESTS` da biste sačekali zahtev koji šalje platiša.



![Image](assets/fr/08.webp)



S druge strane, za ličnu saradnju putem skeniranja QR koda, idite na početnu stranicu vašeg wallet, pritisnite ikonu QR koda na vrhu ekrana, a zatim skenirajte QR kod koji je obezbedio platiša koji inicira transakciju.



![Image](assets/fr/09.webp)



Ako ste u ulozi platioca, tj. onoga koji inicira transakciju, idite na meni `Collaborate`, zatim izaberite `Initiate`.



![Image](assets/fr/10.webp)



Za tip transakcije, pošto želimo da izvršimo Stonewall x2, izaberite ovu opciju.



![Image](assets/fr/11.webp)



Zatim možete birati između online saradnje (*Cahoots* putem *Soroban*) ili saradnje licem u lice, uz razmenu QR kodova.



![Image](assets/fr/12.webp)



### Cahoots online



Ako ste izabrali opciju `Online`, onda izaberite svog saradnika iz Paynyms koje pratite.



![Image](assets/fr/13.webp)



Kliknite na `Set up transaction`, zatim izaberite račun sa kojeg želite izvršiti trošak.



![Image](assets/fr/14.webp)



Na sledećoj stranici unesite detalje transakcije: adresu stvarnog primaoca uplate, iznos koji se šalje i stopu naknade. Zatim kliknite na `Pregledaj postavke transakcije`.



![Image](assets/fr/15.webp)



Proverite informacije pažljivo, uverite se da vaš saradnik sluša *Cahoots* zahteve, zatim kliknite na zeleni `BEGIN TRANSACTION` dugme da započnete razmenu PSBT-ova putem Sorobana.



![Image](assets/fr/16.webp)



Sačekajte dok oba učesnika ne potpišu transakciju, zatim je emitujte na Bitcoin mreži.



![Image](assets/fr/17.webp)



### Razgovori licem u lice



Ako želite da izvršite razmenu lično, izaberite tip transakcije `STONEWALL X2`, a zatim opciju `In Person / Manual`.



![Image](assets/fr/18.webp)



Kliknite na `Set up transaction`, zatim izaberite račun sa kojeg želite izvršiti trošak.



![Image](assets/fr/19.webp)



Na sledećoj stranici unesite detalje transakcije: adresu stvarnog primaoca uplate, iznos koji se šalje i stopu naknade. Zatim kliknite na `Pregledaj postavke transakcije`.



![Image](assets/fr/20.webp)



Proverite detalje, zatim pritisnite zeleni taster `BEGIN TRANSACTION` da biste započeli razmenu PSBT-ova putem skeniranja QR koda.



![Image](assets/fr/21.webp)



Razmena se vrši naizmeničnim skeniranjem sa saradnikom: kliknite na `PRIKAŽI QR KOD` da prikažete vaš QR kod saradniku, koji će ga skenirati. On će zatim kliknuti na `PRIKAŽI QR KOD` da prikaže svoj, a vi ćete ga skenirati pomoću `POKRENI QR Skeniranje`. Ponavljajte ovaj proces dok svih pet koraka razmene ne bude završeno.



![Image](assets/fr/22.webp)



Kada su sve razmene završene, proverite detalje transakcije, zatim je oslobodite povlačenjem zelene strelice na dnu ekrana.



![Image](assets/fr/23.webp)



[Transakcija je objavljena](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Njena struktura je sledeća:



![Image](assets/fr/24.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Možemo uočiti dva ulaza iz mog portfolija, odnosno `91,869 sats` i `64,823 sats`, dok druga dva ulaza dolaze iz wallet mog saradnika. Na izlaznoj strani, jedan UTXO od `100,000 sats` šalje se stvarnom primaocu, a dva UTXO-a od `100,000 sats` i `159,578 sats` vraćaju se u portfolio mog saradnika. Za njega je operacija neutralna, jer povrati pun iznos sredstava koja je uložio u ulaz (isključujući mining troškove kojima je doprineo). Na kraju, dobijam razmenu UTXO od `56,270 sats`, što odgovara razlici između mojih ukupnih ulaza i plaćanja od `100,000 sats` poslatog primaocu.



Očigledno, mogu opisati ovu strukturu jer sam sam izgradio transakciju. Ali za spoljnog posmatrača, generalno je nemoguće odrediti koji UTXO pripada kojem učesniku, bilo u ulazima ili izlazima.



Da biste produbili svoje znanje o upravljanju privatnošću na lancu na Bitcoin, preporučujem da pohađate moj BTC 204 trening na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c