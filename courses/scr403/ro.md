---
name: Pătrunzând în Simplicity
goal: Stăpânește filosofia de design, sistemul de tipuri și ciclul de viață complet al Simplicity
objectives:
  - Înțelege cele trei metode fundamentale de compunere și cei nouă combinatori care formează un limbaj complet
  - Construiește logica booleană, aritmetica și SHA-256 din sistemul de tipuri minimal al Simplicity
  - Înțelege modul în care efectele secundare Failure și Reader permit interacțiunea reală cu blockchain-ul
  - Învață cum programele Simplicity devin adrese Taproot și sunt răscumpărate cu date de witness
---

# Pătrunzând în Simplicity

O incursiune profundă în teoria și deciziile de design din spatele limbajului Simplicity, bazată pe seria completă de cinci articole ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) scrisă de [Dr. Russell O'Connor](https://r6.ca/), creatorul Simplicity la Blockstream Research. Acest curs explică *de ce* Simplicity a fost proiectat așa cum a fost, nu cum se scrie.

Cursul urmează articolele Dr. O'Connor prin cele trei modalități fundamentale de a combina computații, sistemul de tipuri minimal și teorema sa de completitudine, construcția tipurilor de date practice și a aritmeticii pornind de la principii fundamentale, introducerea atentă a efectelor secundare pentru interacțiunea cu blockchain-ul și, în final, modul în care programele sunt angajate în adrese și răscumpărate on-chain.

+++

# Introducere

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Prezentare generală a cursului

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Bine ai venit la SCR403 — Pătrunzând în Simplicity!

Acest curs se bazează pe seria de articole **"Delving Simplicity"** scrisă de [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer la [Blockstream](https://blockstream.com/) și creatorul Simplicity. Articolele originale au fost publicate pe forumul [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) și constituie materialul sursă principal al acestui curs. Îi suntem recunoscători pentru munca sa de pionierat, care a făcut posibil acest conținut educațional.

### Ce vei învăța

Acest curs explorează filosofia de design și fundamentele matematice din spatele Simplicity, limbajul de scripting de nouă generație activat pe [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) în iulie 2025. Urmează seria completă de cinci articole și este structurat în două secțiuni principale de conținut:

1. **Fundamentele Simplicity** — De ce computația pe blockchain necesită un limbaj fundamental diferit, cele trei moduri de a combina operații (secvențial, paralel, condițional) și cei nouă combinatori de bază care formează un limbaj complet din punct de vedere matematic
2. **De la tipuri de date la programe** — Construirea logicii booleene, a aritmeticii și a SHA-256 pornind de la principii fundamentale; înțelegerea efectelor secundare Failure și Reader care permit interacțiunea cu blockchain-ul; și învățarea modului în care programele sunt angajate în adrese Taproot prin Commitment Merkle Roots și răscumpărate cu date de witness

### Cerințe preliminare

Acesta este un curs de **nivel expert** (aproximativ 10 ore). Ar trebui să te simți confortabil cu:
- Concepte de bază despre scripting-ul Bitcoin (ce face validarea unei tranzacții)
- Concepte fundamentale de programare (tipuri, funcții, compunere)
- Este util, dar nu obligatoriu, să ai o oarecare familiaritate cu notația matematică. Introducem totul pe măsură ce înaintăm

### Resurse cheie

- **Articolele originale**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) de Dr. Russell O'Connor pe Delving Bitcoin
- **Repository-ul Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — cod sursă și demonstrații formale Rocq
- **Site-ul oficial**: [simplicity-lang.org](https://simplicity-lang.org/) — documentație și referință SimplicityHL
- **Blogul Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — prezentare tehnică

Ești pregătit să pătrunzi în una dintre cele mai elegante lucrări de inginerie Bitcoin? Să începem!

## Ce este Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Dacă vii la acest curs fără niciun background în Simplicity, acest capitol te va orienta înainte să pătrundem în profunzime.

### Simplicity pe scurt

Simplicity este un **limbaj de smart contract nativ Bitcoin**, activ astăzi pe Liquid Network. Imaginat pentru prima dată de Dr. Russell O'Connor în jurul anului 2012 și detaliat în lucrarea sa din 2017, *Simplicity: A New Language for Blockchains*, a fost activat pe Liquid Network în iulie 2025, după ani de verificare formală și dezvoltare.

Spre deosebire de Solidity de la Ethereum, care este un limbaj de contracte de nivel înalt, Turing-complet, Simplicity este intenționat minimal. Are:
- **Trei formatori de tip** (unit, sum, product)
- **Nouă combinatori** (operații de bază și reguli de compunere)
- **Fără bucle, fără recursivitate, fără memorie alocată dinamic**

Doar din aceste primitive, poți construi orice computație de care ai nevoie pentru validarea tranzacțiilor, de la logica booleană până la hashing-ul SHA-256 complet.

### Ce poți face cu Simplicity astăzi?

Simplicity alimentează deja aplicații reale pe Liquid Network. Cea mai notabilă este [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), o piață de opțiuni fără oracol, unde utilizatorii tranzacționează opțiuni call pe L-BTC folosind USDt drept colateral (contractul de bază acceptă și opțiuni put). Alte proiecte Simplicity live includ [Swaption](https://swaption.io/) de la SideSwap (opțiuni) și proiectul open-source [Deadcat](https://github.com/Resolvr-io/deadcat) de la Resolvr (piețe de predicție). Dincolo de DeFi, Simplicity permite condiții avansate de cheltuire, precum vaults, covenants și scheme multisig complexe care ar fi imposibile sau nesigure în Bitcoin Script.

### Ce este — și ce nu este — acest curs

Acesta **nu** este un tutorial practic de programare. Nu vei scrie programe Simplicity aici. Dacă asta cauți, consultă:
- [simplicity-lang.org](https://simplicity-lang.org/) — documentația oficială și limbajul de nivel înalt SimplicityHL
- [Repository-ul GitHub Simplicity](https://github.com/BlockstreamResearch/simplicity) — implementarea de referință, exemple și demonstrații Rocq
- [Postarea de pe blogul Blockstream](https://blog.blockstream.com/en-simplicity-github/) despre cum să începi

Despre ce **este** acest curs: **alegerile filosofice și tehnice** din spatele designului Simplicity. De ce a fost creat acest limbaj în acest fel? De ce doar nouă combinatori? De ce fără recursivitate? De ce contează faptul că sistemul de tipuri se leagă de calculul secvenților al lui Gentzen?

Gândește-te la asta ca la a înțelege **de ce motorul a fost construit așa** și nu ca la a învăța să conduci mașina.

### Cui i se adresează acest curs?

Acest curs este ideal pentru:
- **Dezvoltatori de protocoale** care vor să înțeleagă fundamentele Simplicity înainte de a scrie cod
- **Cercetători Bitcoin** interesați de abordarea verificării formale și de teoria tipurilor
- **Informaticieni** curioși despre legătura dintre calculul secvenților și computația pe blockchain
- **Bitcoineri avansați** care vor să depășească o înțelegere de suprafață a capacităților de scripting ale Liquid

Dacă termeni precum „tipuri sumă”, „combinatori” sau „calculul secvenților” sunt complet noi pentru tine, nu-ți face griji, explicăm totul de la zero. Dar pregătește-te pentru o călătorie densă și matematică.

### De la articole la curs

Seria originală „Delving Simplicity” a Dr. O'Connor este structurată în cinci articole tehnice. Acest curs reorganizează și adnotează acel material într-un parcurs de învățare progresiv, cu quiz-uri pentru a-ți testa înțelegerea pe parcurs. Ideile, definițiile și demonstrațiile îi aparțin, iar noi am adaptat formatul pentru o educație structurată.

# Fundamentele Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Moduri fundamentale de combinare a computațiilor

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Acum că Simplicity a fost activat pe Liquid Network, aș vrea să fac o incursiune profundă în filosofia și designul limbajului Simplicity.

Validarea tranzacțiilor Bitcoin este o aplicație semnificativ diferită de designul obișnuit al unui limbaj de programare. Spațiul de bloc este o resursă costisitoare, așa că programele trebuie să fie compacte. Programele din tranzacțiile Bitcoin sunt executate întotdeauna pe un singur input, iar toată lumea execută programul pe același input. De asemenea, agentul care autorizează tranzacția cunoaște deja rezultatul computației în avans: că tranzacția este validă.

De obicei, agentul care autorizează va rula computații mult mai costisitoare pentru a deriva date de witness care atestă validitatea tranzacției, în timp ce programele rulate pe blockchain trebuie să verifice validitatea acelor date de witness. Verificarea validității este adesea mult mai ieftină decât demonstrarea validității.

Am proiectat Simplicity ținând cont de acest tip de provocări unice de design al limbajului. De exemplu, Simplicity impune ca ramurile neexecutate să fie tăiate, astfel încât să nu apară pe blockchain. Pașii de preprocesare sunt proiectați cu atenție pentru a prezenta o complexitate temporală (cvasi-)liniară în raport cu dimensiunea programului Simplicity. Se folosește analiza statică în locul „gazului”, care nu poate fi calculat fără a executa codul într-un mod prescris, astfel încât detaliile modelului de execuție să nu devină critice pentru consens. Fără alocare dinamică de memorie în timpul execuției. Și așa mai departe.

Înainte de a intra în detaliile de design ale Simplicity, vreau să încep această serie cu ceva filosofie de programare despre modurile generale de a combina blocuri de construcție de bază pentru a crea funcționalitate nouă.

### Compunere

Să presupunem că cineva proiectează un limbaj pentru tranzacții programabile pentru un blockchain precum Bitcoin. În particular, programele au acces doar la datele tranzacției și la datele UTXO ale intrărilor, iar execuția determină doar validitatea tranzacției (ceea ce permite ca rezultatul execuției să fie stocat în cache). Să spunem că cineva pornește de la o mulțime de operații de bază care pot îndeplini diverse sarcini, precum computații de bază, citirea și/sau procesarea datelor din tranzacție și verificarea semnăturilor. Fiecare operație consumă un anumit tip de input (posibil gol) și returnează un anumit tip de output. Care sunt modurile în care putem combina aceste operații de bază în operații mai complexe?

### Compunere secvențială

![Sequential Composition](assets/en/001.webp)

Cea mai fundamentală metodă de compunere este compunerea secvențială. Dacă avem două operații de bază, dintre care tipul de date al output-ului uneia se potrivește cu tipul de date al input-ului celeilalte, atunci putem combina aceste două operații într-o nouă operație compusă. Această nouă operație rulează cele două operații de bază în secvență, luând ca input intrarea primei operații, transmițând output-ul acelei prime operații în intrarea celei de-a doua și, în final, returnând output-ul celei de-a doua operații.

Desigur, nu trebuie să ne limităm doar la combinarea operațiilor de bază. Acum că avem niște operații compuse, le putem combina și pe acestea folosind compunerea funcțională.

În matematică, această compunere secvențială este adesea numită pur și simplu „compunere”, și s-ar putea crede că aceasta este singura modalitate de a compune lucruri. Totuși, avem și alte moduri de a compune operații.

### Compunere paralelă

![Parallel Composition](assets/en/002.webp)

Să presupunem că avem două operații, care pot fi de bază sau complexe, și care ambele primesc același tip de input. Un al doilea mod fundamental de a compune aceste două operații este să le executăm pe amândouă pe același input. Aceasta se numește compunere paralelă, iar tipul output-ului este „produsul” tipurilor output-urilor operațiilor originale și conține perechea celor două output-uri.

Deși se numește compunere „paralelă”, iar cele două operații ar putea fi în principiu executate în paralel, execuția paralelă nu este o cerință operațională. Putem implementa compunerea paralelă „secvențial”, executând mai întâi o operație și apoi cealaltă. Nu ne interesează detaliile despre cum este implementată compunerea paralelă, atâta timp cât output-ul este același.

### Compunere condițională

![Conditional Composition](assets/en/003.webp)

Compunerea condițională este duala compunerii paralele. În acest caz avem două operații care produc același output, iar le compunem alegând una dintre ele pentru a fi executată. Input-ul acestei operații compuse este „suma” sau „uniunea etichetată” tipurilor de input ale operațiilor originale. În acest caz, eticheta, „Left” sau „Right”, este un singur bit din datele input-ului, care determină ce tip de date este transportat și, prin urmare, care dintre cele două operații poate fi executată.

Compunerea condițională funcționează în același mod chiar și atunci când input-ul este suma a două tipuri identice. Tipul sumă conține în continuare o etichetă, iar valoarea acelei etichete determină care dintre cele două operații urmează să fie executată.

### Compunerea în Bitcoin Script

Există multe moduri de a realiza aceste trei tipuri de compunere în diverse limbaje de programare. În Bitcoin Script, compunerea secvențială este realizată (aproximativ) prin concatenarea a două rutine (de aceea Bitcoin Script este numit un limbaj de programare concatenativ), deoarece output-ul unei rutine rămâne pe stivă pentru a fi consumat de rutina următoare. Compunerea paralelă este realizată prin utilizarea operațiilor de duplicare și interschimbare pentru a manipula stiva, astfel încât două rutine să poată rula pe același input. Lucrurile nu sunt complet directe, deoarece ceea ce numim „produsul” tipurilor este de obicei realizat folosind mai multe elemente de stivă. Sperăm că poți vedea ideea generală.

Compunerea condițională este, desigur, realizată prin `OP_IF`, care ramifică în funcție de valoarea de pe stivă. În acest caz, elementul din vârful stivei joacă rolul unei etichete, iar de obicei elementul sau elementele următoare de pe stivă sunt de „tipuri” diferite, în funcție de valoarea etichetei. Pentru fiecare caz, tipurile elementelor de stivă pot fi potrivite pentru procesare doar de una dintre ramurile din `OP_IF`. Totuși, după ce ajungem la `OP_ENDIF`, elementele de stivă trebuie să fie de un „tip” consistent, astfel încât restul scriptului să poată continua indiferent de ramura luată anterior.

### Compunerea în Simplicity

Am proiectat Simplicity cu combinatori care implementează direct aceste trei forme de compunere. Împreună cu câțiva combinatori suplimentari pentru a susține alte operații de bază legate de tipurile produs și sumă, limbajul de bază Simplicity ajunge să conste din nouă combinatori care sunt suficienți pentru a exprima orice computație finită. Vom discuta acest lucru mai în detaliu în capitolul următor.

### Un al patrulea tip de compunere

Înainte de a încheia, ar trebui să menționăm că mai există cel puțin un tip de compunere întâlnit în Informatică, și anume „compunerea recursivă”. În compunerea recursivă, o operație este iterată de mai multe ori.

Rețineți că Bitcoin Script nu suportă compunerea recursivă și, în mod similar, am exclus explicit recursivitatea nemărginită din designul Simplicity. Teza noastră este că o computație iterativă nemărginită este mai bine implementată folosind covenants recursive, care calculează pe mai multe tranzacții. Acest lucru le permite utilizatorilor să evite constrângerile legate de spațiul de bloc și de standardness și să prezică mai bine costurile tranzacțiilor.

Acestea fiind spuse, există moduri de a abuza de funcția de delegare a Simplicity pentru a oferi ceva asemănător compunerii recursive nemărginite, ceea ce am putea discuta mai târziu în această serie.

### Concluzie

Am trecut în revistă cele trei forme majore de compunere pentru transformarea operațiilor de bază în operații complexe:

- compunere secvențială
- compunere paralelă
- compunere condițională

Am discutat despre modul în care aceste forme de compunere sunt realizate în Bitcoin Script și am sugerat modul în care au influențat designul limbajului Simplicity. Am observat că al patrulea tip de compunere, compunerea recursivă, este exclus în mod specific atât din Simplicity, cât și din Bitcoin Script.

În capitolul următor vom descrie cei nouă combinatori care alcătuiesc nucleul limbajului Simplicity, modul în care aceștia servesc pentru a realiza direct aceste trei forme de compunere și modul în care aceștia formează un limbaj complet pentru a descrie orice computație finită.

## Completitudinea combinatorică a Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

În acest capitol introducem limbajul de bază Simplicity și arătăm că limbajul este complet, adică orice computație finită poate fi exprimată în cadrul lui.

### Tipurile Simplicity

Simplicity suportă trei constructori de tip fundamentali. Tipul produs `A × B` reprezintă output-urile compunerii paralele, în timp ce tipul sumă `A + B` (uniune etichetată) gestionează input-urile compunerii condiționale. Al treilea tip este tipul unit.

### Tipul unit

Tipul unit, notat `𝟙` sau `ONE`, conține exact o valoare: tuplul gol `⟨⟩` sau `()`. Acest tip de date de zero biți nu transportă nicio informație.

### Tipul sumă

Un tip sumă `A + B` combină două tipuri cu etichete care indică „stânga” sau „dreapta”. Valorile se scriu ca `σᴸ(a)` sau `inl(a)` pentru valorile etichetate la stânga și `σᴿ(b)` sau `inr(b)` pentru valorile etichetate la dreapta. Etichetele rămân distincte chiar și atunci când se combină tipuri identice.

#### Tipul boolean

Tipul `𝟙 + 𝟙`, notat `𝟚` sau `TWO`, reprezintă un tip de un bit cu două valori. Prin convenție, `σᴸ⟨⟩` reprezintă fals/zero, în timp ce `σᴿ⟨⟩` reprezintă adevărat/unu.

### Tipul produs

Tipurile produs `A × B` conțin perechi de valori scrise ca `⟨a, b⟩` sau `(a, b)`. Tipul `𝟚 × 𝟚` are patru valori, distincte de cele patru valori din `𝟚 + 𝟚`.

### Expresii Simplicity de bază

Operațiile sunt notate ca `f : A ⊢ B`, adică tip de input `A` și tip de output `B`. Simplicity este „de ordinul întâi” — nu are tipuri funcție.

### Două operații de bază

Limbajul de bază oferă două operații de bază:

**Identitate (`iden`).** Operația de identitate transmite input-ul nemodificat:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Operația unit ignoră input-ul și returnează tuplul gol:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Acestea formează familii cu câte o operație pentru fiecare tip.

### Trei combinatori de compunere

Compunerea secvențială folosește `comp f g` (scris `f ⨾ g` sau `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Compunerea paralelă folosește `pair f g` (scris `f ▵ g` sau `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Compunerea condițională folosește `case f g : (A + B) × C ⊢ D`, oferind ramurilor acces la mediul comun `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

De ce ia compunerea condițională această formă — o sumă asociată cu un mediu comun `C` — și nu o formă mai simplă, `copair f g : A + B ⊢ C`, care doar alege o ramură? Pentru că un `copair` simplu nu poate exprima **distribuția**: funcția `dist : (A + B) × C ⊢ A × C + B × C` care împinge un input comun în orice ramură este aleasă. Prin construirea mediului `C` direct în `case`, Simplicity obține compunerea condițională *și* distribuția dintr-un singur combinator — una dintre deciziile de design esențiale care mențin limbajul de bază la doar nouă combinatori.

### Alți patru combinatori

Consumul de produse folosește `take` și `drop`:

**take** extrage elementul stâng:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extrage elementul drept:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Producerea de sume folosește `injl` și `injr`:

**injl** înfășoară cu o etichetă stângă:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** înfășoară cu o etichetă dreaptă:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Cei nouă combinatori de bază

În total, Simplicity are exact nouă combinatori de bază:

| Combinator | Scop |
|---|---|
| `iden` | Transmite input-ul nemodificat |
| `unit` | Ignoră input-ul |
| `comp` | Compunere secvențială |
| `pair` | Compunere paralelă |
| `case` | Compunere condițională |
| `take` | Extrage elementul stâng dintr-un produs |
| `drop` | Extrage elementul drept dintr-un produs |
| `injl` | Injectează în partea stângă a unei sume |
| `injr` | Injectează în partea dreaptă a unei sume |

### Simplicity și calculul secvenților

Designul Simplicity derivă din fragmentul conjunctiv-disjunctiv al calculului secvenților al lui Gentzen. Mai precis, este o variantă a *interpretării funcționale* a calculului secvenților, care este ea însăși analogă corespondenței Curry-Howard dintre deducția naturală și calculul lambda. Regulile combinatorilor prezintă „tipuri mai mici în premise decât în concluzii”, ceea ce permite Bit Machine — interpretorul abstract al Simplicity, sub formă de mașină cu stivă — să minimizeze copierea datelor în timpul execuției.

### Valorile nu sunt expresii

Expresiile Simplicity denotă operații, nu valori. Notația `scribe b : A ⊢ B` reprezintă o expresie unică care returnează întotdeauna valoarea `b`, servind drept comoditate notațională, nu un combinator. Acest lucru oglindește Bitcoin Script, unde operații precum `OP_1` pun valori pe stivă, în loc să le exprime direct.

### Teorema de completitudine a Simplicity

Cu toți cei nouă combinatori la dispoziție, cum știm că nu ne lipsește ceva — că acești nouă sunt cu adevărat suficienți? Teorema de completitudine Simplicity răspunde la această întrebare: pentru orice funcție între tipuri Simplicity (finite), există o expresie Simplicity care o denotă. Demonstrația este constructivă — arată cum se construiește expresia:

1. **Descompune input-ul**: Folosind expresii `case` imbricate, descompune complet orice input de orice tip în biții săi componenți
2. **Construiește un tabel de căutare**: Pentru fiecare input posibil, folosește `scribe` pentru a produce output-ul corespunzător
3. **Asamblează**: Case-urile și scribe-urile imbricate formează împreună un tabel de căutare gigantic care implementează funcția

Această teoremă este verificată formal în asistentul de demonstrații Rocq (fost Coq). Demonstrația face parte din repository-ul oficial Simplicity și a fost verificată automat pentru corectitudine.

Deși teorema de completitudine garantează că cei nouă combinatori ai Simplicity pot exprima orice funcție între tipuri Simplicity (finite), expresiile rezultate din construcția tabelului de căutare sunt imposibil de mari în practică. O funcție pe input-uri de 256 de biți ar necesita un tabel de căutare cu 2²⁵⁶ intrări. De aceea capitolele următoare se concentrează pe construirea de expresii eficiente care exploatează structura computațiilor, în loc să forțeze totul prin tabele de căutare.

### Concluzie

Limbajul de bază al Simplicity include un sistem de tipuri și combinatori care permit orice computație finită. Deși teorema de completitudine garantează expresivitatea, expresiile rezultate din construcția generică sunt imposibil de mari în practică. Dezvoltarea practică în Simplicity presupune exploatarea structurii computaționale pentru expresii succinte. Capitolele următoare explorează structurile de date, interacțiunile cu tranzacțiile și combinatori suplimentari.

# De la tipuri de date la programe

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Construirea tipurilor de date

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

În capitolele anterioare am arătat cum mulțimea de bază a combinatorilor Simplicity este suficientă pentru a implementa orice computație pură finită. Acest capitol arată cum se construiesc structuri de date și computații practice din aceste primitive — la fel cum calculatoarele sunt construite din porți logice.

### Logica booleană

Tipul boolean, notat `𝟚`, este egal cu `𝟙 + 𝟙` și are două valori: `σᴸ⟨⟩` (fals) și `σᴿ⟨⟩` (adevărat). Folosind combinatorii de bază, pot fi construiți operatori de logică booleană.

#### Operația And

Operația logică `and : 𝟚 × 𝟚 ⊢ 𝟚` primește doi biți și returnează un bit. Implementarea ramifică pe baza primului bit: dacă este fals, returnează fals; altfel, returnează al doilea bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testare cu `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Testare cu `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Alte operații logice

Operația `not` necesită un combinator auxiliar:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

`iden ▵ unit : A ⊢ A × 𝟙` inițial adaugă un „mediu” gol la input, permițând combinatorului `case` să se aplice. Utilizarea lui `take` în cele două ramuri elimină acest mediu gol pentru a executa `f` sau `g`.

Alte operații logice booleene:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Adunătoare de biți

Un „semi-adunător” primește doi biți și îi adună, producând un output de doi biți: un bit de transport (carry) și un bit de sumă.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Un „adunător complet” adună trei biți, producând un output de doi biți. Input-ul folosește tuplul imbricat `(𝟚 × 𝟚) × 𝟚`.

Pentru tupluri imbricate, se folosește o notație compactă:

- `O f` denotă `take f`
- `I f` denotă `drop f`
- `H` denotă `iden`

De exemplu, `I O H` înseamnă `drop (take iden) : A × (B × C) ⊢ B`, extrăgând valoarea din mijloc. Notația evocă cifre binare: atunci când ne gândim la tuplurile imbricate ca la arbori binari, notația reprezintă cifrele binare inversate ale pozițiilor din arbore. Aceste expresii formează indici De Bruijn pentru Simplicity.

**Notă:** Notația `I`, `O` și `H` se aplică doar subexpresiilor formate exclusiv din `take`, `drop` și `iden`.

Adunătorul complet compune două semi-adunătoare, luând disjuncția logică (`or`) a biților de transport:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

În prima linie, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` rulează semi-adunătorul pe primii doi biți, salvând ultimul bit.

În a doua linie, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` salvează primul bit (carry-out-ul primului semi-adunător) și rulează semi-adunătorul pe ultimii doi biți.

În ultima linie, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` calculează disjuncția logică (OR) a primilor doi biți (carry-out-urile ambelor semi-adunătoare) și returnează bitul de sum-out al celui de-al doilea semi-adunător.

Acest lucru demonstrează programarea în Simplicity: folosirea notației `I`, `O` și `H` pentru a face referire la biții de date, formând „medii” potrivite pentru apelarea altor funcții prin compunere secvențială.

Utilizatorii nu definesc direct operații de nivel scăzut. Mai târziu în această serie sunt discutate jets-urile din biblioteca standard care implementează funcții comune. Utilizatorii finali nu sunt așteptați să programeze direct în Simplicity, similar cu Bitcoin Script. În schimb, limbaje de nivel înalt precum SimplicityHL generează cod Simplicity, gestionând „mediile” subexpresiilor și traducând variabilele numite în secvențele corespunzătoare de `take` și `drop`.

### Vectori

Vectorii de lungime fixă sunt definiți prin formarea de produse iterate ale tipului `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Aceștia pot fi scriși ca `A^2`, `A^4`, `A^8`, etc.

Vectorii sunt definiți doar pentru lungimi care sunt puteri ale lui doi. Alte lungimi ar necesita alegerea unor convenții de parantezare.

Dată fiind expresia `f : A ⊢ B`, asocierea repetată „mapează” expresia peste vectori de lungime fixă:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Dată fiind funcția `f : A × B ⊢ B`, iterarea sau „foldarea” peste vectori de lungime fixă:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Există multe variații. Dată fiind `f : A × B ⊢ C`, „zip” peste vectori asociați cu `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Dată fiind `f : (A × B) × C ⊢ C`, fold peste vectori asociați cu `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Combinarea `map` și `fold-right` creează combinatori de acumulare: `f : A × C ⊢ C × B` produce `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Sunt posibile multe alte variante.

#### Cuvinte pe mai mulți biți

Un vector de biți produce numere întregi pe mai mulți biți. De exemplu, `𝟚³²` este un tip de cuvânt pe 32 de biți. `𝟚²⁵⁶` este un tip de cuvânt pe 256 de biți, potrivit pentru hash-uri și operații criptografice.

Folosind adunătorul complet, o variantă a operațiilor pe vectori definește un „adunător cu propagare de transport” (ripple carry adder) peste cuvinte pe mai mulți biți:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` primește două numere binare de n biți și un input de transport de un bit, returnând un flag de carry-out de un bit și o sumă de n biți.

#### SHA-256

Prin definirea recursivă a operațiilor aritmetice pe cuvinte de mai mulți biți — scădere, înmulțire, împărțire — și a operațiilor logice pe biți precum AND, OR, XOR logice, și combinând repetat toate acestea, se poate construi chiar și funcția de compresie a blocurilor din SHA-256:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Compresia SHA-256 este definită formal folosind Simplicity în cadrul asistentului de demonstrații Rocq (fost Coq), cu o demonstrație formală că implementarea `sha256-hash-block` este corectă.

Compresia rulează prea lent ca Simplicity brut. Jets-urile execută nativ funcții comune precum compresia SHA-256. Implementările Simplicity pure servesc drept specificații formale pentru jets.

### Tipuri Option

Tipurile Option rezultă prin luarea unei sume cu tipul unit:

```
Option A ≔ 𝟙 + A
```

Tipul `Option A` poate fi scris ca `A?` sau `𝕊 A` (unde `𝕊` înseamnă „succesor”). Funcțiile mapează peste tipuri option:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Pot fi definiți combinatori monadici precum bind:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffere de lungime variabilă

„Bufferele” sunt tipuri pentru vectori parțial umpluți:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Tipul `Xᑉ⁸` se extinde la `(1 + X⁴) × ((1 + X²) × (1 + X))`. Tratând acest lucru ca pe un polinom și dezvoltându-l, obținem `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpretat ca tip, acesta reprezintă suma tuturor tuplurilor posibile de X până la 7, inclusiv tuplul gol. Acesta este exact tipul listelor cu lungimea strict mai mică de 8.

La fel ca vectorii, pot fi definite operații de mapare și fold peste buffere. Operațiile de stivă includ `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` și `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` adaugă un element la buffer, returnând un vector complet dacă apare depășire. `pop-<n` elimină un element, returnând bufferul mai mic și elementul eliminat, returnând opțional nimic dacă bufferul original era gol.

Definiția `push-<n`, recursivă:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Simplicity brut devine dificil de urmărit dincolo de anumite niveluri de complexitate. Utilizatorii finali folosesc limbaje de nivel înalt precum SimplicityHL pentru a genera aceste expresii idiomatice.

### Concluzie

Acest capitol a arătat cum se construiesc operații logice din biți. Din acestea, a apărut aritmetica la nivel de bit, permițând raționamentul despre execuție. Au fost dezvoltate tipuri de vectori, demonstrând iterația peste cuvinte pe mai mulți biți pentru definirea aritmeticii. Continuând, operații criptografice precum SHA-256 și validarea semnăturilor Schnorr pot fi definite folosind doar combinatori Simplicity — toate fiind, de fapt, definite folosind Simplicity.

Acest capitol nu este un ghid exhaustiv al tuturor tipurilor de date și operațiilor posibil de construit în Simplicity, ci ilustrează cum se poate obține funcționalitate practică în limitele Simplicity. În ciuda tipurilor finit mărginite, pot fi definiți vectori utili, tipuri de buffer și operații care iterează peste aceste structuri.

Specificațiile operațiilor reale din biblioteca standard diferă ușor de definițiile de aici. De exemplu, adunătorul complet folosește un XOR pe 3 căi și o funcție logică de „majoritate” în loc de două semi-adunătoare.

În practică, programele Simplicity folosesc jets pentru operații aritmetice și criptografice. Totuși, jets-urile înlocuiesc doar expresii. Combinatorii care iterează peste buffere și vectori nu pot fi înlocuiți de jets, apărând în programele Simplicity reale. Deși, în loc să folosească direct aceștia, utilizatorii finali folosesc limbaje de nivel înalt precum SimplicityHL pentru a genera astfel de expresii.

Combinatorii definiți recursiv par să crească exponențial în dimensiunea expresiei. Acest lucru nu este problematic. În timpul serializării, expresiile sunt codificate ca DAG-uri (grafuri direcționate aciclice) și nu ca arbori. Reprezentarea reală crește doar liniar.

Până acum au fost luate în considerare doar computații pure. Interacțiunea cu datele tranzacției pentru sarcini precum semnarea tranzacțiilor necesită o modalitate prin care programele să eșueze dacă semnăturile sunt invalide. Capitolul următor discută efectele secundare în Simplicity.

## Două efecte secundare

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

În capitolele anterioare am arătat cum se construiesc anumite structuri de date și computații folosind mulțimea de bază a combinatorilor Simplicity. Așa cum am observat, combinatorii de bază sunt suficienți pentru a implementa orice computație pură finită. Aceasta ridică întrebarea: ce altceva se poate obține? Putem adăuga efecte secundare suplimentare expresiilor noastre.

Există diverse tipuri de efecte secundare posibile pentru expresii: actualizarea stării, scrierea într-un jurnal, aruncarea unei excepții, citirea dintr-un mediu, apelarea unei continuări etc. Efectele secundare disponibile în Simplicity depind de aplicație.

Pentru aplicațiile Bitcoin și Liquid, avem în prezent două efecte secundare: efectul Failure, care este un efect de excepție unde excepția are tipul `𝟙`, și efectul Reader, care permite accesarea datelor din mediul tranzacției. Combinatorii noștri de bază sunt „puri”; nu au efecte secundare. Totuși, jets-urile pot introduce primitive noi care au efecte secundare.

### Jets cu efecte

Vom vorbi mai mult despre jets mai târziu în acest curs, dar aici introducem câteva jets exemplu pentru a ilustra efectele lor secundare.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` este un jet pentru o expresie care primește o cheie publică x-only, un mesaj de 256 de biți și o semnătură Schnorr, și nu returnează nimic! Conform tipului său, ar trebui să se comporte la fel ca un `unit`. Diferența constă în efectul secundar al jet-ului: dacă validarea semnăturii eșuează, atunci întreaga computație este întreruptă prin aruncarea unei excepții (de tip unit). Acesta este efectul Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` este un jet minimalist pentru exprimarea efectului Failure. Dacă input-ul lui `verify` este `false`, întreaga computație este întreruptă, prin aruncarea unei excepții. Dacă input-ul este `true`, nu se returnează nimic, dar computația poate continua.

#### Hash-uri de tranzacție

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` pare a fi o funcție constantă, deoarece există o singură valoare de input posibilă: tuplul gol. Totuși, acest jet citește din mediul tranzacției și produce un hash al datelor tranzacției, analog cu digest-ul de mesaj `SIGHASH_ALL` folosit în verificarea semnăturilor din Bitcoin Script. Acesta este un exemplu de efect Reader: valoarea returnată depinde de mediul tranzacției în care jet-ul este executat. Există mai multe alte jets de hashing care hash-uiesc diverse submulțimi ale datelor din mediul tranzacției pentru a ajuta la construirea de digest-uri de mesaj personalizate pentru semnături.

#### Jets de introspecție

`input-sequence : 𝟚³² ⊢ 𝟚³²?` este o funcție care primește un index de input și returnează numărul de secvență al tranzacției pentru acel input, returnând opțional nimic dacă indexul este în afara limitelor. Din nou, valoarea de output nu este o funcție pură a indexului de input, ci, mai degrabă, operația folosește efectul Reader pentru a accesa mediul tranzacției pentru a determina valoarea de output. Există mai multe alte jets de introspecție care returnează diverse fragmente ale datelor din mediul tranzacției.

### Clasificarea efectelor

Nu toate efectele secundare sunt create egale. Unele efecte secundare se comportă mai bine decât altele. Putem clasifica efectele în funcție de cât de pretabile sunt la transformări ale programului.

#### Efecte comutative

Un efect comutativ este unul în care, dacă interschimbi output-urile a două expresii, poți interschimba în siguranță și expresiile propriu-zise, fără a schimba efectul expresiei. Considerăm `swap = I H ▵ O H : A × B ⊢ B × A`. Dacă `f ▵ g ⨾ swap = g ▵ f` pentru orice expresii `f` și `g` cu efecte secundare, atunci efectele sunt comutative.

Citirea datelor tranzacției din mediu este un efect comutativ, deoarece rezultatul citirii din mediu este același, indiferent de ordinea în care executăm citirea.

În general, aruncarea unei excepții nu este un efect comutativ. Dacă `f` aruncă o excepție `e₁`, iar `g` aruncă o altă excepție `e₂`, atunci care excepție este aruncată din perechea lui `f` și `g` depinde de ordinea în care sunt executate.

Totuși, în cazul special al efectului Failure, în care poate fi aruncată doar o excepție de tip unit, efectul este comutativ. Indiferent dacă `f` sau `g` aruncă o excepție, excepția rezultată va fi aceeași, deoarece există o singură valoare de excepție posibilă.

#### Efecte idempotente

Un efect idempotent este unul în care, dacă duplici output-ul unei expresii, poți duplica în siguranță și expresia propriu-zisă, fără a schimba efectul expresiei. Considerăm `dup = iden ▵ iden : A ⊢ A × A`. Dacă `f ⨾ dup = dup ⨾ f ▵ f` pentru orice `f` cu efecte secundare, atunci efectele sunt idempotente.

Citirea datelor tranzacției din mediu este un efect idempotent. Aruncarea unei excepții este de asemenea un efect idempotent. Chiar dacă doar una dintre cele două expresii duplicate va fi executată, orice excepție aruncată de `dup ⨾ f ▵ f` va fi aceeași cu excepția aruncată de `f ⨾ dup`.

Totuși, scrierea într-un jurnal poate să nu fie idempotentă, deoarece duplicarea efectului ar face ca mesajul din jurnal să apară de două ori. Totuși, dacă jurnalul constă dintr-o *mulțime* de mesaje, în loc de o *listă* de mesaje, atunci efectul ar fi idempotent (și comutativ), deoarece inserarea într-o mulțime este ea însăși o operație idempotentă.

#### Efecte unitare

Un efect unitar este unul în care, dacă renunți la output-ul unei expresii, poți renunța în siguranță și la expresia propriu-zisă, fără a schimba efectele expresiei. Dacă este întotdeauna cazul că `f ⨾ unit = unit` pentru orice `f` cu efecte secundare, atunci efectele tale sunt unitare.

Citirea datelor din mediu este unul dintre puținele tipuri de efecte unitare. Dacă rezultatul citirii datelor tranzacției din mediu este ignorat, întreaga expresie care efectuează citirea poate fi ignorată.

Efectul Failure nu este unitar. Dacă `f` aruncă o excepție, la fel va face și `f ⨾ unit`; execuția nici măcar nu va ajunge la combinatorul `unit` înainte ca computația să fie întreruptă. Pe de altă parte, `unit` evident nu ar arunca nicio excepție, deci efectele lui `f ⨾ unit` și `unit` ar fi diferite.

Pentru a rezuma, iată cum se comportă efectele discutate mai sus în raport cu aceste trei proprietăți:

| Efect | Comutativ | Idempotent | Unitar |
| --- | :---: | :---: | :---: |
| Reader (mediul tranzacției) | ✓ | ✓ | ✓ |
| Failure (excepție de tip unit) | ✓ | ✓ | ✗ |
| Writer (jurnal ca mulțime) | ✓ | ✓ | ✗ |
| Excepții generale (tip arbitrar) | ✗ | ✓ | ✗ |

### Efecte permise în Simplicity

Cu cât un tip de efect are mai multe proprietăți bine comportate, cu atât un optimizator Simplicity are mai mult spațiu pentru a transforma programele care folosesc acele efecte. Ideal, am permite doar efecte care au toate cele trei proprietăți: comutativ, idempotent și unitar. Acest lucru ar permite unui optimizator să efectueze orice fel de transformare de program și-ar dori. Totuși, citirea dintr-un mediu este singurul efect care satisface toate cele trei proprietăți.

În schimb, cerem ca efectele Simplicity să fie comutative și idempotente. Ambele efecte pe care le folosim în Simplicity, efectul Failure și efectul Reader, sunt comutative și idempotente. Acest lucru permite efectuarea unei clase largi de optimizări asupra codului Simplicity.

Totuși, transformarea de „renunțare” descrisă mai sus, care încearcă să înlocuiască `f ⨾ unit` cu `unit`, sau orice transformare similară, nu este permisă dacă `f` poate produce un efect Failure. Într-adevăr, imaginați-vă că `f` conține o afirmație `bip0340-verify`. Ar fi dezastruos să încercăm să optimizăm acea verificare.

### De ce sunt permise efectele secundare?

De ce permite Simplicity efecte secundare? N-ar fi mai bine dacă fiecare program ar primi întreaga tranzacție ca input și ar returna un output boolean care decide dacă o tranzacție este validă sau nu?

#### Verificarea în lot (Batch Verification)

Unul dintre motivele pentru care avem efectul Failure este pentru a susține [verificarea în lot](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) a semnăturilor Schnorr. În verificarea în lot, multe verificări individuale de semnături Schnorr sunt grupate astfel încât, dacă orice singură verificare de semnătură eșuează, întregul lot eșuează.

Această procedură de grupare îmbunătățește eficiența față de verificarea individuală a fiecărei semnături. Dezavantajul este că, dacă verificarea lotului eșuează, nu aflăm care verificare (sau verificări) specifică de semnătură a eșuat.

Folosind efectul secundar Failure, `bip0340-verify` asigură că, dacă o verificare de semnătură eșuează, întreaga tranzacție eșuează. Dacă `bip0340-verify` ar returna în schimb `𝟚`, un tip boolean, pentru succes sau eșec, atunci o verificare de semnătură eșuată ar putea totuși duce la o ramură în care scriptul reușește. Într-un astfel de caz, ar trebui să știm dacă acea semnătură specifică este validă sau nu, și astfel nu am putea profita de verificarea în lot.

#### Date de tranzacție precalculate

O problemă în Bitcoin Script timpuriu era că funcția de hashing folosită pentru a crea digest-uri de mesaj pentru semnături era liniară în raport cu dimensiunea tranzacției. De obicei, fiecare input creează cel puțin un digest de mesaj pentru verificarea semnăturii, astfel încât, în ansamblu, cantitatea de hashing era pătratică în raport cu dimensiunea tranzacției.

Această problemă a fost rezolvată în Segwit și în iterațiile ulterioare ale Bitcoin Script prin redefinirea digest-urilor de mesaj astfel încât să poată fi calculate în timp constant per verificare de semnătură. Acest lucru se bazează pe existența `PrecomputedTransactionData`, care precalculează hash-urile datelor tranzacției o singură dată și este apoi partajat de calculele sighash ale fiecărui input. Jets-urile de hashing de tranzacție ale Simplicity se bazează pe același tip de date de tranzacție precalculate pentru a asigura că jets-urile rulează în timp constant.

Să presupunem că `sig-all-hash` nu ar folosi efectul Reader. Să presupunem că am reușit cumva să construim un tip Simplicity pentru mediul tranzacției. Să-l numim `TxEnv`, astfel încât `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` ar fi tipul jet-ului. O astfel de definiție ar cere jet-ului `sig-all-hash` să poată calcula hash-ul oricărei tranzacții, nu doar al tranzacției în care este implicat. Programele Simplicity ar putea copia `TxEnv`-ul dat și transmite o copie modificată a acestuia către `sig-all-hash`. Într-un astfel de caz, `sig-all-hash` nu s-ar putea baza pe `PrecomputedTransactionData`, și am reveni la a necesita timp liniar pentru orice date de tranzacție transmise acestei versiuni de `sig-all-hash`.

Deoarece `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` folosește efectul Reader pentru a accesa datele tranzacției, acesta obține acces _doar_ la un mediu de tranzacție fix. Din acest motiv, implementarea jet-ului poate folosi în siguranță `PrecomputedTransactionData` și poate opera în timp constant.

### Agregarea semnăturilor cross-input

Deși nici Liquid, nici Bitcoin nu suportă în prezent [agregarea semnăturilor cross-input](https://hrf.org/latest/cisa-research-paper/), am dori să verificăm că Simplicity poate fi compatibil cu aceasta atunci când va veni momentul.

Deși detaliile nu au fost stabilite, ne imaginăm implementarea semi-agregării folosind un efect Writer. Adică, un jet nou cu un tip precum `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` ar primi o cheie publică, un digest de mesaj și componenta `r` a unei semnături Schnorr (o semnătură Schnorr constă dintr-o componentă `r` și o componentă `s`) și ar scrie-o într-un jurnal de tranzacție înainte de a continua execuția. Apoi, în altă parte în cadrul tranzacției sau împreună cu tranzacția, ar fi furnizată o componentă `s` agregată pentru toate semnăturile Schnorr semi-agregate. Tranzacția ar fi validă doar atunci când o astfel de componentă `s` agregată este furnizată pentru toate cheile, mesajele și componentele `r` înregistrate.

Pentru a îndeplini cerințele Simplicity, acest efect Writer trebuie să fie idempotent și comutativ. Acest lucru poate fi asigurat tratând jurnalul writer-ului ca pe o mulțime de tupluri cheie, mesaj, componentă `r`. Acest lucru funcționează deoarece operațiile pe mulțimi sunt idempotente și comutative. Tratarea jurnalului ca pe o mulțime de valori ar fi compatibilă cu algoritmul de verificare a semi-agregării.

### Concluzie

În acest capitol am analizat adăugarea de efecte secundare la computațiile pe care le poate face Simplicity. Am clasificat diverse tipuri de efecte în funcție de cât de bine se comportă în raport cu diverse tipuri de transformări de program. Am decis să restrângem efectele Simplicity la cele care sunt comutative și idempotente.

Cele două efecte pe care le folosim pentru aplicațiile Bitcoin și Liquid sunt efectul Reader, pentru accesarea mediului tranzacției, și efectul Failure, pentru întreruperea și eșuarea programului. Unele jets folosesc operații primitive în care pot apărea aceste tipuri de efecte secundare.

Efectul Failure determină output-ul unui program Simplicity: programul fie eșuează, făcând tranzacția invalidă, fie programul reușește. Efectul Reader oferă un tip de input pentru un program Simplicity: mediul care conține datele tranzacției. Dar trebuie de asemenea să oferim și alte input-uri, precum semnăturile digitale, programelor Simplicity.

În capitolul următor vom analiza ce sunt programele Simplicity, cum devin acestea adrese și cum adăugăm alte input-uri, precum semnăturile, la programele Simplicity.

## Programe și adrese

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

În capitolul anterior am descris cele două efecte secundare folosite în Simplicity: efectul Failure, care determină succesul sau eșecul unui program, și efectul Reader, care oferă acces la mediul tranzacției. Acum ne îndreptăm către întrebarea practică: ce este exact un program Simplicity și cum devine o adresă pe blockchain?

### Programe Simplicity

Un program Simplicity este definit ca o expresie Simplicity de tipul `𝟙 ⊢ 𝟙`. Această semnătură de tip înseamnă că programul nu primește niciun input semnificativ (doar valoarea unit) și nu produce niciun output semnificativ (doar valoarea unit). Efectul Reader captează input-ul mediului tranzacției, în timp ce efectul Failure indică succesul sau eșecul. Aceste efecte gestionează I/O, nu tipurile Simplicity propriu-zise.

### Commitment Merkle Root

În loc să stocheze programe complete on-chain, Bitcoin folosește angajamente (commitments) — o practică ce se extinde de la Pay-to-Script-Hash (P2SH). Simplicity folosește un Commitment Merkle Root (CMR).

Fiecare combinator primește un tag SHA-256 derivat din tiparul: `Simplicity␟Commitment␟[identifier]`, unde `␟` reprezintă codul ASCII 31 (separatorul de unități).

Fiecare tag este hash-ul SHA-256 al string-ului preimagine corespunzător, listat mai jos:

| Combinator | Preimagine tag (string ASCII) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

O expresie Simplicity este apoi hash-uită recursiv într-un CMR de 256 de biți prin calcularea unui midstate SHA-256 tagged pentru fiecare combinator, împreună cu CMR-urile argumentelor sale (notăm `#ᶜ(e)` pentru CMR-ul expresiei `e`, și `∥` pentru concatenarea de bytes):

| Combinator | Regulă CMR |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Combinatorii binari (`comp`, `pair`, `case`) concatenează CMR-urile ambilor copii; combinatorii unari (`take`, `drop`, `injl`, `injr`) concatenează CMR-ul unicului lor copil după 32 de bytes de padding `0x00`; iar frunzele nulare (`iden`, `unit`) hash-uiesc doar propriul tag. Două convenții mențin acest calcul ieftin: se folosesc midstate-uri SHA-256, astfel încât **fiecare expresie necesită cel mult un apel al funcției de compresie SHA-256** (presupunând că midstate-ul până la tag-urile constante este precalculat), iar constructorii cu un singur argument prefixează argumentul lor cu 32 de bytes de padding `0x00`, ceea ce permite o precalculare suplimentară pentru implementările care o doresc.

Pentru combinatorul `unit` — un constructor nular fără sub-expresii de argument — această regulă se specializează la `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, unde `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag-ul este introdus de două ori). CMR-ul rezultat pentru programul trivial `unit` este:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

În mod esențial, CMR-ul nu se angajează la tipurile expresiilor Simplicity, bazându-se în schimb pe inferența de tip în timpul răscumpărării.

### Adrese

Adresele folosesc mecanismul Taproot din BIP-0341, cu CMR-uri angajate sub versiunea TapLeaf `0xbe`. Procesul implică:

1. Calcularea unui hash tagged TapLeaf care combină byte-ul de versiune, lungimea CMR-ului și CMR-ul propriu-zis
2. „Twist-uirea” (tweaking) unei chei publice interne (folosind un punct NUMS atunci când nu se dorește o cale de cheltuire prin cheie)
3. Convertirea în format bech32m
4. Adăugarea sumelor de control (checksum) corespunzătoare

Atunci când nu se dorește o cale de cheltuire prin cheie (key-spend path), cheia publică internă este setată la un punct **NUMS** („Nothing-Up-My-Sleeve”): un punct pe curbă ales deliberat astfel încât nimeni să nu-i cunoască logaritmul discret — cu alte cuvinte, un punct fără o cheie privată corespunzătoare. Deoarece nimeni nu poate produce vreodată o semnătură pentru acesta, calea de cheltuire prin cheie este demonstrabil neutilizabilă, iar output-ul poate fi cheltuit *doar* prin calea de script Simplicity angajată. Într-o aplicație reală, acest punct NUMS ar trebui randomizat conform recomandării din BIP-0341, astfel încât output-urile fără cale de cheltuire prin cheie să fie indistinguibile de output-urile Taproot obișnuite (un beneficiu pentru confidențialitate).

#### De la Simplicity la adresă

Să parcurgem întreaga derivare pentru cel mai simplu program posibil: `unit : 𝟙 ⊢ 𝟙`, un no-op care reușește întotdeauna.

**1. Tag-ul combinatorului.** Mai întâi se calculează tag-ul `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Se introduce tag-ul de două ori pentru a obține CMR-ul programului:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hash-ul TapLeaf.** Se prefixează CMR-ul cu versiunea TapLeaf a Simplicity `0xbe` și lungimea CMR-ului `0x20` (32 de bytes), apoi se calculează hash-ul tagged TapLeaf al Elements (un hash tagged este `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Cu o singură frunză nu există TapBranch-uri, deci acest hash este deja rădăcina TapTree.

**4. TapTweak.** Deoarece dorim să nu existe cale de cheltuire prin cheie, folosim punctul NUMS din BIP-0341 ca cheie internă și îl "twist-uim" (tweak) cu rădăcina TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Cheia de output.** Se "twist-uiește" (tweak) cheia internă pe curbă, `output_pk = lift_x(internal_pk) ⊕ t·G` (aritmetica pe curbă eliptică este rezumată aici), obținând cheia de output x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Adresa Bech32m.** Se codifică cheia de output x-only, se prefixează cu `p` (caracterul de versiune de witness SegWit v1), se adaugă prefixul lizibil pentru oameni al Liquid-testnet `tex1` și se adaugă checksum-ul Bech32m. Adresa finală este:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

A fost multă muncă — dar cea mai mare parte este impusă chiar de Taproot, nu de Simplicity.

### Expresii de witness

Un nou tip de combinator abordează absența unui input pentru programele Simplicity: expresia de witness. Combinatorul `witness` permite integrarea datelor de semnătură și a altor materiale de witness în programe.

```
      w : B
-----------------
witness w : A ⊢ B
```

Semantica expresiei witness este simplă: aceasta ignoră input-ul și returnează pur și simplu valoarea `w` (care poate fi de orice tip Simplicity), adică `⟦witness w⟧(a) = w`. Acest lucru nu adaugă **nicio nouă expresivitate** — conform teoremei de completitudine, Simplicity poate deja construi orice astfel de funcție constantă (amintiți-vă de macro-ul `scribe` din capitolele anterioare). Rostul combinatorului `witness` constă în întregime în **CMR-ul** său: valoarea `w` este **exclusă** din CMR-ul expresiei, astfel încât adresa poate fi calculată înainte ca `w` să fie cunoscut, iar `w` este furnizat în momentul răscumpărării.

Această alegere de design susține tăierea (pruning) — ramurile condiționale neexecutate nu trebuie dezvăluite on-chain, inclusiv expresiile de witness asociate acestora. Când o ramură este tăiată, verificatorul are nevoie doar de CMR-ul subarborelui tăiat, nu de conținutul său efectiv.

### Valori de witness

Ar putea părea o limitare faptul că o expresie witness poate conține doar o *valoare*, și nu o expresie Simplicity mai generală. Dar programele pentru blockchain-uri bazate pe UTXO sunt executate o singură dată. Nu este nevoie să transmiți o sub-expresie întreagă într-un nod witness: utilizatorul poate rula pur și simplu acea sub-expresie el însuși, off-chain, și transcrie output-ul ei în valoarea witness pentru a obține exact același rezultat.

(Mai târziu în acest curs vom întâlni combinatorul `disconnect`, care se comportă mult ca o expresie witness care *chiar* primește o expresie Simplicity întreagă drept argument.)

Un design alternativ ar transmite toate datele de witness ca argument programului Simplicity de nivel superior. Expresiile witness sunt preferate din două motive. În primul rând, **tăierea (pruning)**: ramurile neexecutate ale expresiilor `case` nu sunt niciodată dezvăluite on-chain, iar orice expresii witness din interiorul acelor ramuri sunt tăiate odată cu ele. În al doilea rând, **localitatea**: expresiile witness ne permit să plasăm fiecare valoare de witness exact acolo unde este folosită, în loc să o transmitem de la input-ul de nivel superior al programului.

### Inferența de tip

Deoarece CMR-urile nu se angajează la tipuri, sistemul de tipuri este reconstruit în timpul răscumpărării. Algoritmul de inferență de tip al Simplicity determină tipurile minime pentru fiecare subexpresie pe baza structurii combinatorilor. Mai precis, inferența calculează tipul *principal* (cel mai general) al fiecărei subexpresii; orice variabile de tip care rămân libere sunt apoi instanțiate la tipul unit `𝟙`, ceea ce produce un tip unic, minim, pentru program.

### Concluzie

În acest capitol am stabilit că programele Simplicity sunt expresii de tipul `𝟙 ⊢ 𝟙`, am explicat modul în care Commitment Merkle Root-urile sunt construite din hash-uri SHA-256 tagged ale fiecărui combinator și am arătat cum CMR-urile sunt transformate în adrese on-chain prin Taproot BIP-0341. Am introdus expresiile witness ca mecanism pentru furnizarea datelor de semnătură și a altor input-uri în momentul cheltuirii, fără a te angaja la valorile lor în momentul creării adresei.

# Secțiune finală

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Recenzii și evaluări

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Examen final

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Concluzie

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
