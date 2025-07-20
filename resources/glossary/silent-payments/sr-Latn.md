---
term: TIHI PLAĆANJA
---

Metod za korišćenje statičkih Bitcoin adresa za primanje uplata bez ponovne upotrebe Address, bez interakcije, i bez vidljive On-Chain veze između različitih uplata i statičkog Address. Ova tehnika eliminiše potrebu za generate novim, neiskorišćenim adresama za primanje za svaku transakciju, čime se izbegavaju uobičajene interakcije u Bitcoin gde primalac mora da obezbedi novi Address platiocu.


Kod Silent Payments, platiša koristi javne ključeve primaoca (javni ključ za trošenje i javni ključ za skeniranje) i zbir svojih privatnih ključeva kao ulaz za generate svež Address za svaku uplatu. Samo primalac, sa svojim privatnim ključevima, može izračunati privatni ključ koji odgovara ovoj uplati Address. ECDH (*Elliptic-Curve Diffie-Hellman*), kriptografski algoritam ključa Exchange, koristi se za uspostavljanje zajedničke tajne koja se zatim koristi za izvođenje primajućeg Address i privatnog ključa (samo na strani primaoca). Da bi identifikovali Silent Payments namenjene njima, primaoci moraju skenirati Blockchain i ispitati svaku transakciju koja odgovara kriterijumima protokola. Za razliku od BIP47, koji koristi obaveštavajuću transakciju za uspostavljanje kanala plaćanja, Silent Payments eliminišu ovaj korak, štedeći jednu transakciju. Međutim, kompromis je da primalac mora skenirati sve potencijalne transakcije kako bi utvrdio, primenom ECDH, da li su adresirane njima.


Na primer, Bobov statički Address $B$ predstavlja konkatenaciju njegovog javnog ključa za skeniranje i njegovog javnog ključa za trošenje:


$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$


Ovi ključevi su jednostavno izvedeni iz sledeće putanje:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


Ovaj statični Address objavljuje Bob. Alisa ga preuzima kako bi izvršila tihu uplatu Bobu. Ona izračunava Bobovu uplatu Address $P_0$ na sledeći način:


$$  P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$


Gde:


$$  \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖ } A)  $$


Sa:


- $B_{\text{scan}}$: Bobov javni ključ skeniranja (staticki Address);
- $B_{\text{spend}}$: Bobov javni ključ za trošenje (staticki Address);
- $A$: Zbir javnih ključeva u ulazu (tweak);
- $a$: Privatni ključ izmene, to jest, zbir svih parova ključeva korišćenih u `scriptPubKey` UTXO-a koji su korišćeni kao ulazi u Alisinoj transakciji;
- $\text{outpoint}_L$: Najmanji UTXO (leksikografski) korišćen kao ulaz u Alisinu transakciju;
- $\text{ ‖ }$: Konkatenacija (operacija spajanja operanada krajem uz kraj);
- $G$: Generator tačka eliptičke krive `secp256k1`;
- $\text{Hash}$: SHA256 Hash funkcija označena sa `BIP0352/SharedSecret`;
- $P_0$: Prvi javni ključ / jedinstveni Address za plaćanje Bobu;
- $0$: Celi broj korišćen za generate više jedinstvenih adresa za plaćanje.


Bob skenira Blockchain da pronađe svoju Silent Payment na sledeći način:


$$  P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$


Sa:


- $b_{\text{scan}}$: Bobov privatni ključ skeniranja.


Ako pronađe $P_0$ kao Address koji sadrži Silent Payment upućen njemu, on izračunava $p_0$, privatni ključ koji mu omogućava da potroši sredstva koja je Alisa poslala na $P_0$:


$$ p_0 = (b_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$


Sa:


- $b_{\text{spend}}$: Bobov privatni ključ za trošenje;
- $n$: redosled eliptičke krive `secp256k1`.


Pored ove osnovne verzije, etikete se takođe mogu koristiti za generate nekoliko različitih statičkih adresa iz iste osnovne statičke Address, sa ciljem razdvajanja višestrukih upotreba bez nerazumnog umnožavanja posla potrebnog tokom skeniranja.