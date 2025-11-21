---
term: XOR
---

Akronim za operaciju "Exclusive or," na francuskom "Ou exclusif." To je fundamentalna funkcija Booleove logike. Ova operacija uzima dva Booleova operanda, svaki može biti $true$ ili $false$, i proizvodi $true$ izlaz samo kada se dva operanda razlikuju. Drugim rečima, izlaz XOR operacije je $true$ ako je tačno jedan (ali ne oba) od operanda $true$. Na primer, XOR operacija između $1$ i $0$ će rezultirati u $1$. Beležimo:


$$
1 \oplus 0 = 1
$$


Slično tome, XOR operacija se može izvesti na dužim sekvencama bitova. Na primer:


$$
10110 \oplus 01110 = 11000
$$


Svaki bit u sekvenci se poredi sa svojim parnjakom, i primenjuje se XOR operacija. Ovde je istinita tabela za XOR operaciju:


<div align="center">


| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>


Operacija XOR se koristi u mnogim oblastima računarstva, posebno u kriptografiji, zbog svojih zanimljivih osobina kao što su:


- Njegova komutativnost: redosled operanada ne utiče na rezultat. Za dve date promenljive $D$ i $E$: $D \oplus E = E \oplus D$;
- Njegova asocijativnost: grupisanje operanada ne utiče na rezultat. Za tri data varijable $A$, $B$, i $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Ima neutralni element $0$: operacija xor sa $0$ će uvek biti jednaka operandu. Za datu promenljivu $A$: $A \oplus 0 = A$;
- Svaki element je svoj inverz. Za datu promenljivu $A$: $A \oplus A = 0$.


U kontekstu Bitcoin, XOR operacija se očigledno koristi na mnogim mestima. Na primer, XOR se masovno koristi u SHA256 funkciji, koja se široko koristi u Bitcoin protokolu. Neki protokoli kao što je Coldcard's *SeedXOR* takođe koriste ovu primitivu za druge primene. Takođe se nalazi u BIP47 za enkripciju višekratnog koda za plaćanje tokom njegove transmisije.

U širem polju kriptografije, XOR se može koristiti kao simetrični enkripcioni algoritam. Ovaj algoritam se zove "One-Time Pad" ili "Vernam šifra," nazvan po svom pronalazaču. Iako nepraktičan zbog dužine ključa, ovaj algoritam je jedan od retkih enkripcionih algoritama priznatih kao bezuslovno sigurni.