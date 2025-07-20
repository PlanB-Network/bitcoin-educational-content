---
name: Profesor Plan ₿ Network
description: Kako da dodam ili izmenim svoj profil nastavnika na Plan ₿ Network?
---
![cover](assets/cover.webp)


Ako planirate da doprinesete Plan ₿ Network pisanjem novog tutorijala ili kursa, biće vam potreban profil nastavnika. Ovaj profil će vam omogućiti da dobijete odgovarajuće kredite za sadržaj koji doprinosite platformi.


Za one od vas koji su već bili uključeni u kreiranje edukativnog sadržaja na Plan ₿ Network, verovatno već imate profil nastavnika. Možete ga pronaći u folderu `/professors` [na našem GitHub repozitorijumu](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Ako vaš profil već postoji, pronađite svoj login u `professor.yml` fajlu.


Da biste izvršili izmene na svom profilu, idite na odeljak "Uredi profil nastavnika" na kraju ovog vodiča.


## Dodajte novog nastavnika pomoću našeg softvera


Najlakši način da kreirate svoj profil nastavnika na Plan ₿ Network je korišćenje našeg integrisanog Python alata. Evo kako funkcioniše.


### 1 - Konfigurišite vaše lokalno okruženje


Morate imati svoj Fork iz [Plan ₿ Network repozitorijuma na GitHub-u](https://github.com/PlanB-Network/Bitcoin-educational-content).


Sinhronizujte glavnu granu (`dev`) vašeg Fork sa izvornim repozitorijumom.


Ažurirajte svoju lokalnu kloniranu verziju.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - Kreiraj novu granu


Uverite se da ste na grani `dev`. Kreirajte novu granu sa opisnim imenom (npr. `add-professor-loic-morel`).


Objavi ovu granu na svom Fork online.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - Kreirajte svoj profil nastavnika


Idite u fasciklu `scripts/tutorial-related/data-creator/` na vašoj lokalnoj kopiji. Uverite se da ste instalirali sve zavisnosti potrebne za softver, nakon što ste prvo instalirali Python :


```bash
pip install -r requirements.txt
```


Zatim pokrenite softver komandom :


```bash
python3 main.py
```


Jednom kada ste na početnoj stranici, unesite lokalnu putanju do kloniranog repozitorijuma, jezik na kojem pišete i vaš GitHub ID. Ako kreirate ovaj profil za nekog drugog i već imate profil Profesora, unesite vaš ID u polje "*PBN Professor's ID*". Ako kreirate svoj profil, još uvek nećete imati Profesorov ID, jer ste u procesu kreiranja, pa ostavite ovo polje prazno.


Zatim kliknite na dugme "*New Professor*".


![Image](assets/fr/01.webp)


Popunite potrebne informacije (imajte na umu da će sve ove informacije biti javne na našoj platformi kao i na GitHub-u):




- ime vaše datoteke učitelja (koristite svoje ime i prezime ili pseudonim, malim slovima) ;
- Vaše ime ili nadimak ;
- Vaša veb stranica i profil X (opciono) ;
- A Lightning Address za primanje donacija od čitalaca (opciono) ;
- Odaberite 2 ili 3 oznake sa liste;
- Kliknite na "*Select Image*" da biste izabrali profilnu sliku iz vaših lokalnih foldera (bilo koje ime i format mogu biti korišćeni za sliku, a softver će je automatski prilagoditi. Samo se uverite da je slika kvadratna);
- Napišite kratak opis svog profila.


Finalizirajte kreiranje klikom na "*Create Professor*". Ovo će automatski generate sve fajlove potrebne za vaš profil.


![Image](assets/fr/02.webp)


Sačuvajte svoje izmene lokalno kreiranjem commita sa objašnjavajućom porukom. Podesite izmene na vaš Fork GitHub.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


Kada završite, kreirajte Pull Request (PR) na GitHub-u kako biste predložili integraciju vaših izmena. Dodajte naslov i kratak opis PR-u.


### 4 - Lektorisanje i spajanje


Sačekajte validaciju ili povratne informacije od administratora. Ako je potrebno, izvršite ispravke i pošaljite nove komitove.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


Kada je PR spojen, možete obrisati svoju radnu granu.


## Izmenite svoj profil nastavnika


Ako ste savladali korišćenje Git-a, izmenite svoj profil nastavnika kreiranjem nove grane i direktnim uređivanjem relevantne datoteke u postojećem folderu. Izmene se mogu izvršiti ili u datoteci `professor.yml` ili u markdown datoteci, u zavisnosti od informacija koje treba ispraviti. Kada lokalno izvršite izmene, pošaljite ih na svoj Fork i podnesite PR.


Za početnike, preporučujem da napravite izmene direktno putem GitHub-ovog Interface weba. Uverite se da imate GitHub nalog. Ako ne znate kako da ga kreirate, pratite ovaj vodič :


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Idi na [Plan ₿ Network GitHub repozitorijum posvećen podacima](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).


![Image](assets/fr/03.webp)


Kliknite na fasciklu "*professors*", zatim idite u vašu ličnu fasciklu.


![Image](assets/fr/04.webp)


Da biste promenili metapodatke profila, kao što su Lightning Address, ime ili linkovi, izaberite datoteku "*professor.yml*". Da biste promenili svoj opis, kliknite na YAML datoteku za vaš jezik (npr. "*en.yml*" ili "*fr.yml*").


Ako izmenite svoj opis, ne zaboravite da uklonite sve zastarele prevode. Zatim možete ili prevesti svoj opis na druge jezike uz pomoć LLM-a, ili ostaviti opis samo na svom maternjem jeziku i napomenuti u svom Pull Request-u da vaš opis zahteva prevod od strane našeg tima.


![Image](assets/fr/05.webp)


Kada se nađete na datoteci koju želite izmeniti, kliknite na ikonu olovke.


![Image](assets/fr/06.webp)


Ako već nemate Fork iz spremišta Plan ₿ Network, GitHub će vam predložiti da ga kreirate. Kliknite na "*Fork this repository*".


![Image](assets/fr/07.webp)


Napravite željene izmene u datoteci. Kada završite, kliknite na "*Commit changes*".


![Image](assets/fr/08.webp)


Unesite poruku koja opisuje vašu izmenu, a zatim izaberite "*Predloži izmene*".


![Image](assets/fr/09.webp)


Prikaz sažetka vaših izmena će biti prikazan. Ako želite da napravite dodatne izmene na svom profilu, možete se vratiti u foldere i napraviti dodatne izmene. Kada završite, kliknite na "*Create pull request*".


Zahtev za povlačenje je zahtev za integraciju izmena iz vaše grane u glavnu granu repozitorijuma Plan ₿ Network, omogućavajući pregled i diskusiju o izmenama pre nego što budu spojene.


![Image](assets/fr/10.webp)


Uverite se da je, na vrhu Interface, vaša radna grana spojena sa `dev` granom repozitorijuma Plan ₿ Network (koja je glavna grana).


Unesite naslov koji ukratko rezimira izmene koje želite da spojite sa izvornim repozitorijumom. Dodajte kratak komentar koji opisuje ove izmene, zatim kliknite na Green "*Create pull request*" dugme da potvrdite zahtev za povlačenje:


![Image](assets/fr/11.webp)


Vaš PR će tada biti vidljiv na kartici "*Pull Request*" glavnog repozitorijuma Plan ₿ Network. Sve što sada treba da uradite je da sačekate da administrator spoji vašu izmenu.


![Image](assets/fr/12.webp)


Ako naiđete na bilo kakve tehničke poteškoće prilikom podnošenja vaše izmene, slobodno zatražite pomoć na [našoj Telegram grupi posvećenoj doprinosima](https://t.me/PlanBNetwork_ContentBuilder). Hvala vam puno!