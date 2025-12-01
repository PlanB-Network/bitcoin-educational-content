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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematika za Bitcoin Implementaciju

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kriptografija eliptičkih krivih

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transakcija Unutrašnji radovi

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Parsiranje transakcija i ECDSA potpisi

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skripta i Validacija Transakcija

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Izgradnja Transakcije i Plaćanje na Skriptu Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Mreža Unutrašnji Radovi

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Blokovi i Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Mrežna komunikacija i Merkleova stabla

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Napredna komunikacija čvorova i odvojeni svedok

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Završni deo


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recenzije i Ocene


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Zaključak


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
