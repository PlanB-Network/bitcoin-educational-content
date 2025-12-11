---
name: Programiranje Bitcoin
goal: Izgradite kompletnu Bitcoin biblioteku od nule i razumite kriptografske osnove Bitcoin
objectives: 

 - Implementirajte aritmetiku konačnih polja i operacije na eliptičkim krivama u Pythonu
 - Kreirajte i parsirajte Bitcoin transakcije programatski
 - Kreiraj Testnet adrese i emituj transakcije preko mreže
 - Savladajte matematičke osnove koje leže u osnovi Bitcoin sigurnosnog modela

---
# Putovanje u skripte i programe Bitcoin


Ovaj intenzivni dvodnevni kurs, koji vodi Jimmy Song, vodi vas duboko u tehničke osnove Bitcoin kroz izgradnju kompletne Bitcoin biblioteke od nule. Počevši od osnovne matematike konačnih polja i eliptičkih krivih, napredovaćete kroz parsiranje transakcija, izvršavanje skripti i mrežnu komunikaciju. Kroz praktične vežbe kodiranja u Jupyter beležnicama, kreiraćete svoj sopstveni Testnet Address, konstruisati transakcije ručno i emitovati ih direktno na mrežu—sve to dok stičete duboko razumevanje kriptografskih principa koji čine Bitcoin sigurnim i Trustless.


Uživaj u svom otkriću!


+++

# Uvod

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Pregled kursa

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Dobrodošli na kurs PRO 202 _**Programming Bitcoin**_, intenzivno putovanje koje vas vodi od aritmetike konačnih polja do izgradnje i emitovanja stvarnih transakcija na Bitcoin test mreži.

Na ovom kursu, postepeno ćeš izgraditi Bitcoin biblioteku u Pythonu, dok stičeš kriptografske, protokolarne i softverske osnove potrebne za precizno razumevanje sigurnosti i unutrašnjeg funkcionisanja Bitcoina. Pristup PRO 202 je potpuno praktičan: svaki koncept se odmah implementira u Jupyter beležnicama, obezbeđujući da se teorija i kod međusobno jačaju.

### Osnovni matematički koncepti za Bitcoin

Ovaj prvi odeljak uspostavlja neophodne matematičke osnove. Implementiraćeš aritmetiku konačnih polja i operacije na eliptičkim krivama (grupni zakon, sabiranje, dupliranje, skalarno množenje...) — preduslove za ECDSA. Cilj je dvostruk: razumeti algebarsku strukturu koja omogućava kriptografske potpise i izgraditi pouzdane Python alate za njihovu manipulaciju.

Zatim ćeš formalizovati komponente ECDSA: generisanje ključeva, formatiranje tačaka, heširanje, kreiranje i verifikaciju potpisa. Ovaj odeljak direktno povezuje teoriju i praksu, naglašavajući detalje implementacije i robusnost osnovnog bezbednosnog modela.

### Unutrašnje funkcionisanje Bitcoin transakcije

U drugom odeljku ćeš analizirati strukturu Bitcoin transakcije: UTXO-e, ulaze/izlaze, sekvence, skripte, enkodiranja i još mnogo toga. Pisaćeš kod za kreiranje, potpisivanje i verifikaciju transakcija, stičući precizno razumevanje toga šta hash potvrđuje i zašto.

Zatim ćeš implementirati minimalni _Script_ izvršilac, pregledati ključne opkode i verifikovati putanje trošenja. Cilj je da budeš sposoban da proveravaš ponašanje transakcija, dijagnostikuješ neuspehe validacije i razmišljaš o bezbednosti politika trošenja.

### Unutrašnje funkcionisanje Bitcoin mreže

U trećem odeljku ćeš smestiti transakciju u širi sistem: strukturu bloka, heder, težinu i Proof-of-Work mehanizam. Radićeš sa protokolnim porukama, hederima blokova i Merkle stablima.

Na kraju ćeš proučavati komunikaciju između peer-to-peer čvorova, optimizaciju poruka i uvođenje SegWit-a.

Kao i kod svakog kursa na Plan ₿ Academy, završni deo uključuje evaluaciju osmišljenu da učvrsti tvoje razumevanje. Spreman si da otkriješ unutrašnje funkcionisanje Bitcoina i napišeš kod koji ga pokreće? Hajde da počnemo!

# Osnovni matematički koncepti za Bitcoin

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matematika za Bitcoin Implementaciju

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kriptografija eliptičkih krivih

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transakcija Unutrašnji radovi

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Parsiranje transakcija i ECDSA potpisi

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skripta i Validacija Transakcija

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Izgradnja Transakcije i Plaćanje na Skriptu Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Mreža Unutrašnji Radovi

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin Blokovi i Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Mrežna komunikacija i Merkleova stabla

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Napredna komunikacija čvorova i odvojeni svedok

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Završni deo


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Recenzije i Ocene


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Zaključak


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
