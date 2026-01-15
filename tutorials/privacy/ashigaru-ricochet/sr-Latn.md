---
name: Ashigaru - Ricochet
description: Razumevanje i korišćenje Ricochet transakcija
---
![cover ricochet](assets/cover.webp)



> *Premium alat koji dodaje dodatne korake istorije vašim transakcijama. Zbunite crne liste i pomozite u zaštiti od nepravednog zatvaranja naloga od strane trećih strana.*

## Šta je Ricochet?



Ricochet je tehnika koja se sastoji od izvođenja nekoliko fiktivnih transakcija prema sebi kako bi se simulirao prenos vlasništva nad bitcoinom. Ovaj alat se razlikuje od drugih transakcija Ashigaru-a (nasleđenih od Samurai Wallet) po tome što ne pruža perspektivnu anonimnost, već oblik retrospektivne anonimnosti. Zapravo, Ricochet zamagljuje specifičnosti koje mogu ugroziti fungibilnost dela Bitcoin.



Na primer, ako napravite coinjoin, vaš deo koji izlazi iz mešavine biće identifikovan kao takav. Alati za analizu lanca mogu otkriti obrasce coinjoin transakcija i dodeliti oznaku delovima koji iz njih izlaze. U suštini, coinjoin ima za cilj da prekine istorijske veze novčića, ali njegov prolazak kroz coinjoin ostaje detektabilan. Analogno tome, ovaj fenomen je sličan enkripciji teksta: iako se originalni tekst ne može pristupiti u čistom tekstu, lako je identifikovati da je primenjena enkripcija.



Oznaka "coinjoined" može uticati na fungibilnost UTXO. Regulirana lica, kao što su platforme za razmenu, mogu odbiti da prihvate coinjoined UTXO, ili čak zahtevati objašnjenja od njegovog vlasnika, uz rizik da vam nalog bude blokiran ili sredstva zamrznuta. U nekim slučajevima, platforma može čak prijaviti vaše ponašanje državnim vlastima.



Ovde dolazi do izražaja Ricochet metoda. Da bi se izbledeo otisak koji ostavlja coinjoin, Ricochet izvršava četiri uzastopne transakcije u kojima korisnik prenosi svoja sredstva na sebe na različite adrese. Nakon ove sekvence transakcija, Ricochet alat konačno usmerava bitkoine na njihovu krajnju destinaciju, kao što je platforma za razmenu. Cilj je stvoriti distancu između originalne coinjoin transakcije i konačnog čina trošenja. Na ovaj način, alati za analizu blockchaina će pretpostaviti da je verovatno došlo do prenosa vlasništva nakon coinjoin-a, te da stoga nema potrebe za preduzimanjem akcije protiv izdavaoca.



![image](assets/fr/01.webp)



Suočeni sa Ricochet metodom, moglo bi se zamisliti da bi softver za analizu lanaca produbio svoje ispitivanje izvan četiri skoka. Međutim, ove platforme se suočavaju sa dilemom u optimizaciji praga detekcije. Potrebno je da uspostave prag broja skokova nakon kojih prihvataju da je verovatno došlo do promene vlasništva i da bi veza sa prethodnim coinjoin-om trebalo da se ignoriše. Međutim, određivanje ovog praga je rizično: svako proširenje broja posmatranih skokova eksponencijalno povećava obim lažnih pozitivnih rezultata, tj. pojedinaca pogrešno označenih kao učesnika u coinjoin-u, kada je zapravo operaciju izveo neko drugi. Ovaj scenario predstavlja veliki rizik za ove kompanije, jer lažni pozitivni rezultati dovode do nezadovoljstva, što može navesti pogođene klijente da pređu kod konkurencije. Dugoročno, preambiciozan prag detekcije dovodi platformu do gubitka više klijenata nego njeni konkurenti, što bi moglo ugroziti njenu održivost. Stoga je komplikovano za ove platforme da povećaju broj posmatranih skokova, a 4 je često dovoljan broj da se suprotstave njihovim analizama.



Dakle, **najčešći slučaj upotrebe za Ricochet nastaje kada je potrebno prikriti prethodno učešće u coinjoin-u na UTXO koji posedujete.** Idealno bi bilo izbegavati prenos bitkoina koji su prošli kroz coinjoin ka regulisanim entitetima. Ipak, u slučaju da ne postoji druga opcija, naročito u hitnoj potrebi za likvidacijom bitkoina u državnu valutu, Ricochet nudi efikasno rešenje.



## Kako funkcioniše Ricochet na Ashigaru?



Ricochet je jednostavno metoda slanja bitcoina samom sebi, koju su prvobitno izmislili programeri Samurai Wallet. Stoga je savršeno moguće simulirati Ricochet ručno, bez potrebe za specijalizovanim alatom. Međutim, za one koji žele automatizovati proces uz uživanje u uglađenijem rezultatu, Ricochet alat dostupan putem Ashigaru aplikacije (koja je Samourai fork) predstavlja dobro rešenje.



Pošto Ashigaru naplaćuje svoju uslugu, Ricochet košta `100,000 sats` kao naknadu za uslugu, plus mining naknadu. Njegova upotreba se stoga preporučuje za transfere značajnih iznosa.



Aplikacija Ashigaru nudi dve varijante Ricochet:





- Ojačani Ricochet, ili "isporuka u fazama", nudi prednost raspodele troškova usluga Ashigaru-a preko pet uzastopnih transakcija. Ova opcija takođe osigurava da se svaka transakcija emituje u različito vreme i zabeleži u različitom bloku, imitirajući što je moguće bliže ponašanje promene vlasništva. Iako sporija, ova metoda je poželjna za one koji nisu u žurbi, jer maksimizira efikasnost Ricochet-a jačanjem njegove otpornosti na analizu lanca;





- Klasični Ricochet, koji je dizajniran da izvrši operaciju brzo, emitujući sve transakcije u smanjenom vremenskom intervalu. Ova metoda, dakle, nudi manje poverljivosti i manju otpornost na analizu od pojačane metode. Trebalo bi da se koristi samo za hitne pošiljke.



## Kako napraviti Ricochet na Ashigaru?



Pravljenje rikošeta na Ashigaru je veoma jednostavno: samo aktivirajte odgovarajuću opciju prilikom kreiranja transakcije slanja. Da biste započeli, kliknite na dugme `+`, zatim na `Pošalji`, i izaberite nalog sa kojeg želite poslati sredstva.



![Image](assets/fr/02.webp)



Popunite informacije o transakciji: iznos koji se šalje i krajnju adresu primaoca nakon Ricochet skokova. Zatim označite opciju `Ricochet`.



![Image](assets/fr/03.webp)



Zatim možete birati između dva Ricochet režima o kojima se raspravlja u teorijskom delu: ili klasični Ricochet, gde su sve transakcije uključene u isti blok, ili isporuka u fazama, koja poboljšava kvalitet Ricochet-a na račun dužeg kašnjenja.



Kada napravite svoj izbor, pritisnite strelicu na dnu ekrana da potvrdite.



![Image](assets/fr/04.webp)



Na sledećem ekranu, videćete kompletan pregled vaše transakcije. Ovde takođe možete prilagoditi stopu naknade za vaše Ricochet transakcije u skladu sa tržišnim uslovima. Ako vam sve odgovara, prevucite zelenu strelicu da potpišete i distribuirate Ricochet transakcije.



![Image](assets/fr/05.webp)



Sačekajte dok različiti skokovi automatski ne prođu.



![Image](assets/fr/06.webp)



Vaše transakcije su uspešno emitovane.



![Image](assets/fr/07.webp)



Sada ste potpuno upoznati sa opcijom Ricochet dostupnom u aplikaciji Ashigaru. Da biste išli dalje, preporučujem vam da pohađate moj BTC 204 kurs obuke, koji će vas detaljno naučiti kako da ojačate svoju onchain poverljivost.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c