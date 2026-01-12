---
name: 1ML
description: Õppige, kuidas kasutada 1ML-i ekspluateerijat, et mõista ja analüüsida Bitcoin Lightning-võrku.
---
![cover](assets/cover.webp)



## Sissejuhatus



Lightning Network on kiire ja odav makselahenduse, mis on ehitatud Bitcoin peal, võimaldades koheseid ja turvalisi tehinguid. Selle võrgu toimimise, selle topoloogia ja seda moodustavate sõlmede seisundi mõistmiseks on oluline jälgida seda võrku. Lightning explorer, nagu 1ML, võimaldab visualiseerida võrgu avalikke andmeid, sealhulgas aktiivseid sõlmi, avatud kanaleid ja vaba võimsust, andes väärtusliku ülevaate kasutajatele, arendajatele ja sõlmede operaatoritele.



## Juurdepääs 1ML-le ja arusaamine kodulehelt



1ML-i kasutamiseks avage lihtsalt oma veebilehitseja ja sisestage [https://1ml.com](https://1ml.com). See viib teid kodulehele, mis on Lightning Network üldine armatuurlaud.



![capture](assets/fr/03.webp)



Sellel lehel kuvatakse ekraani ülaosas mitu olulist statistikat, sealhulgas :





- **Aktiivsete sõlmede** koguarv võrgus, st arvutid, mis osalevad Lightning-maksete saatmises ja vastuvõtmises.
- Avatud kanalite **arv**, mis vastab nende sõlmede vahelistele ühendustele, mis võimaldavad rahaülekandeid.
- **Võrgu koguvõimsus**, väljendatuna bitcoinides (BTC), mis näitab kõigi avalike kanalite võimsuste summat.



Neid andmeid ajakohastatakse korrapäraselt, et kajastada võrgu hetkeseisu. Need annavad aimu võrgustiku suurusest, kasvust ja tugevusest.



![capture](assets/fr/04.webp)



Kohe allpool pakub lehekülg nimekirju koos pingereaga:





- **kõige ühendatud sõlmed**, millel on kõige rohkem avatud kanaleid teiste sõlmedega.
- Sõlmede **kõrgeim võimsus**, mis näitab, millised sõlmed suudavad edastada kõige suuremaid koguseid.
- Võimsuse seisukohalt kõige olulisemad kanalid.



Filtreid saab kasutada ka nende nimekirjade täpsustamiseks geograafilise asukoha või muude kriteeriumide alusel.



See lehekülg on ideaalne lähtepunkt Lightning Network uurimiseks ja selle üldise topoloogia mõistmiseks.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Lightning-sõlmede uurimine



1ML-i sõlme uurimiseks kasutage kõigepealt lehekülje ülaosas asuvat otsinguriba. Saate sisestada **Sõlme ID**, st sõlme unikaalse identifikaatori, või selle **alias**, mis on lihtsamini meeldejääv nimi.



Kui otsing on lõpetatud, klõpsake vastaval sõlmel, et pääseda selle üksikasjalikule lehele.



![capture](assets/fr/07.webp)



Sellel lehel kuvatakse mitu olulist teavet:





- Sõlme ID**: see unikaalne identifikaator on pikk tähemärkide jada, mis võimaldab sõlme kogu võrgus täpselt identifitseerida.



![capture](assets/fr/08.webp)





- Alias**: see on sõlme omaniku poolt valitud nimi, mis esindab seda avalikult.



![capture](assets/fr/09.webp)





- **Kanalite arv** näitab, kui palju ühendusi on sõlmel teiste sõlmedega avatud, samas kui **koguvõimsus** näitab nendes kanalites saadaolevate bitcoinide summat. Sõlm, millel on suur arv kanaleid ja suur võimsus, on üldiselt hästi ühendatud ja suudab kiiresti suuri rahasummasid üle võrgu kanda.



![capture](assets/fr/10.webp)





- **Koormusaja** ehk kättesaadavus mõõdab, kui kaua on sõlmpunkt olnud aktiivne ja ligipääsetav võrgus, peegeldades selle usaldusväärsust. Teisest küljest näitab sõlme **vanus**, kui kaua see on võrgus olnud, kajastades selle stabiilsust ja kogemust Lightning Network raames.



![capture](assets/fr/11.webp)



Need andmed aitavad teil mõista Lightning Network-sõlme olulisust ja usaldusväärsust. Näiteks on suure kanalite arvu, suure läbilaskevõime ja suure kasutusaegadega sõlmpunkt sageli oluline osaleja võrgus.



## Välgukanalite uurimine



### Mis on välgukanal?



Lightning-kanal on otsene ühendus kahe võrgusõlme vahel. See võimaldab neil kahel sõlmpunktil vahetada koheseid ja odavaid makseid, ilma et iga tehingu puhul oleks vaja läbida Bitcoin põhiahelat. Kanalid on alus, mis muudab Lightning Network kiireks ja skaleeritavaks.



### Lugege kanalite teavet 1ML kohta



1ML-is on igal kanalil oma lehekülg või kirjeldusleht, mis sisaldab mitmeid olulisi andmeid:



Sõlme leheküljelt saate juurdepääsu selle kanalite loetelule. Kui klõpsate kanalil, kuvab 1ML spetsiaalse lehekülje, millel on mitu olulist teavet.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Peamised nähtavad andmed on järgmised:





- Partnerlussõlmed**: iga kanal ühendab kahte sõlme. 1ML kuvab mõlemad identifikaatorid ja nende vastavad varjunimed.



![capture](assets/fr/14.webp)





- Kanali mahutavus**: see on selles kanalis lukustatud bitcoinide kogusumma. See võimsus kujutab endast maksimumpiiri makseid, mis võivad selle kanali kaudu läbida.



![capture](assets/fr/15.webp)





- Kanali vanus**: näitab, kui kaua kanal on olnud avatud. Vana kanal on sageli märk kahe sõlme vahelisest stabiilsest suhtest.



![capture](assets/fr/16.webp)



### Kanali nähtavuse piirangud



Oluline on mõista, et 1ML näitab ainult **osa** Lightning Network-st. Explorer näitab ainult **avalikke kanaleid**, st neid, mis on võrgus välja kuulutatud. Erakanalid, mida kasutatakse sageli konfidentsiaalsuse või strateegia tõttu, ei ole nähtavad. Lisaks ei näita 1ML kanalite täpseid jaotusi, tehtud makseid ega antud hetkel tegelikult olemasolevat likviidsust. Seega saab kuvatud teavet kasutada võrgustiku **üldstruktuuri** analüüsimiseks, kuid mitte selle tegeliku finantstegevuse või üksikasjaliku likviidsuse seisundi analüüsimiseks.



## Uurige Lightning Network asukoha järgi



### Sõlmed riikide ja piirkondade kaupa



1ML võimaldab teil uurida Lightning Network vastavalt **geograafilisele jaotusele**. Kodulehelt või spetsiaalsete jaotiste kaudu on võimalik kuvada sõlmi riikide või piirkondade kaupa. See funktsioon põhineb sõlmede operaatorite poolt deklareeritud asukohateabel.


Navigatsiooniribal näete linki **Koht**. Leheküljel on sõlmed grupeeritud kontinentide, riikide ja linnade kaupa.



![capture](assets/fr/17.webp)



Valides riigi, kuvab 1ML sellega seotud sõlmede loetelu koos koondstatistikaga, nagu sõlmede arv ja nähtav koguvõimsus selle geograafilise piirkonna kohta.



#### Mida see ütleb kohaliku vastuvõtmise kohta





- Tehnoloogia kasutuselevõtt**: Suur hulk sõlmpunkte piirkonnas näitab, et Bitcoin kasutajad, ettevõtted või teenused võtavad Lightning Network aktiivselt kasutusele. See näitab tehnoloogilist küpsust ja valmisolekut kasutada Lightning'i eeliseid (kiiremad tehingud, väiksemad kulud).
- Majanduslik ökosüsteem** : Sõlmede tihe olemasolu võib anda märku ka kohalikust majandusstruktuurist Bitcoin ümber: kaupmehed, kes võtavad vastu Lightning'i, idufirmad, kes arendavad tööriistu, kogukonna üritused jne.
- Turvalisus ja vastupidavus**: Mitmekülgne geograafiline jaotumine suurendab võrgu vastupidavust kohalike katkestuste või piirangute korral. Mida hajutatumad on sõlmed, seda detsentraliseeritum ja raskem on võrku tsenseerida.
- Poliitikad ja eeskirjad**: Mõnes riigis võib tänu soodsale reguleerivale raamistikule või ennetavale kogukonnale toimuda kiirem kasutuselevõtt. Seevastu piirkondades, kus eeskirjad on ranged või vaenulikud, on sõlmpunktide arv väiksem.



#### Geograafiliste andmete piirid



Pidage siiski meeles, et Lightning-sõlmede geograafilisel asukoha määramisel on omad piirangud ja eelarvamused:





- Ligikaudne IP asukoht**: 1ML kasutab üldiselt sõlmede avaliku IP-aadressi, et hinnata nende asukohta. Seda meetodit võib siiski moonutada VPNide, pilveserverite (AWS, Google Cloud) kasutamine või hostimine riikides, mis erinevad sõlme omaniku tegelikust elukohast.
- Virtuaalsed sõlmed**: Mõned operaatorid majutavad oma sõlmed usaldusväärsuse ja kättesaadavuse huvides kaugserveritesse, mis võib anda vale ettekujutuse füüsilisest asukohast.
- Kasutaja liikuvus**: Sõlmeoperaator võib muuta oma asukohta, viia oma infrastruktuuri ümber või avada mitu sõlme erinevates piirkondades, mis muudab andmete lugemise keerulisemaks.
- Erasõlmede nähtamatus**: Mõned sõlmed ei avalda oma IP-aadressi või kasutavad meetodeid oma asukoha varjamiseks, mis muudab geograafilise asukoha määramise võimatuks.



## 1ML konkreetsed kasutusjuhud



### Võrgu topoloogia mõistmine



1ML võimaldab visualiseerida Lightning Network **üldstruktuuri**. Jälgides sõlmedevahelisi ühendusi, kanalite arvu ja üldist läbilaskevõimet, on võimalik mõista, kuidas võrk on korraldatud, millised sõlmed mängivad keskset rolli ja kuidas maksevood teoreetiliselt võivad ringelda.



See arusaamine on oluline, kui tahame mõista, kuidas Lightning Network töötab, ja mitte ainult portfelli kasutamiseks.



### Oluliste sõlmpunktide tuvastamine



Tänu 1MLi pakutud pingereale (enim ühendatud sõlmed, suurim võimsus, vanus) on võimalik tuvastada sõlmed, mis on võrgus olulisel kohal. Need sõlmed toimivad sageli Lightning-maksete peamiste väravatena.



![capture](assets/fr/18.webp)



### Kontrollida sõlme avalikku nähtavust



Sõlmeoperaatorile võimaldab 1ML kontrollida, kas teie sõlme on Lightning Network-s **avalikult reklaamitud**. Kui sõlmpunkt on 1MLis, tähendab see, et see on nähtav ja teistele sõlmpunktidele avalike kanalite avamiseks kättesaadav.


See võib olla kasulik nähtavuse või ühenduvusprobleemide diagnoosimisel.



### Lightning Network arengu jälgimine aja jooksul



Võrreldes globaalset statistikat eri ajavahemike kohta, võimaldab 1ML jälgida Lightning Network arengut: sõlmede arvu suurenemist või vähenemist, koguvõimsuse muutusi või muutusi geograafilises jaotuses.


Need tähelepanekud pakuvad huvitavat vaatenurka Lightning Network kasvule, küpsusele ja suundumustele.



## 1ML parimad tavad ja piirangud



### Avalikud andmed ≠ täielik tegelikkus



1ML põhineb üksnes **avalikult avaldatud** andmetel Lightning Network kohta. See tähendab, et vahend näitab ainult osa tegelikkusest. Paljud kanalid võivad olla privaatsed, mõned sõlmed ei pruugi olla reklaamitud ja kanalite tegelik likviidsus ei ole nähtav. Seetõttu on oluline kasutada 1MLi kui üldist analüüsivahendit, mitte kui võrgu ammendavat esitust.



### Privaatsus ja välk



Lightning Network väljatöötamisel on pööratud suurt tähelepanu **maksete privaatsusele**. Üksikud tehingud ei ole 1ML-is nähtavad ja täpsed kanalisaldod ei ole avalikud. See piirang ei ole exploreri viga, vaid Lightning Network põhiline omadus, mis on loodud kasutajate privaatsuse kaitsmiseks.



### Ärge tehke rutiinseid järeldusi



Suure läbilaskevõimega või paljude kanalitega sõlmpunkt ei ole tingimata igal juhul "usaldusväärsem" või "tõhusam". Samamoodi ei tähenda võrgu üldise läbilaskevõime ajutine vähenemine tingimata struktuurilist probleemi. Arvnäitajaid tuleb alati tõlgendada tagantjärele ja asetada need konteksti.



### Täiendavus teiste vahenditega



1ML on suurepärane lähtepunkt Lightning Network uurimiseks, kuid seda on kõige parem kasutada koos teiste vahenditega, nagu Lightning portfellid, sõlmede haldusliidesed ja muud uurijad. Selline lähenemisviis annab võrgustikust terviklikuma ja nüansirikkama ülevaate.



## 1ML-ühenduse võimalus (täiustatud funktsionaalsus)



1ML pakub **sisselogimise / konto loomise** võimalust, mis on veebilehel nähtav, kuid see ei ole Lightning Network andmete vaatamiseks **vajalik**. Kõik selles juhendis seni käsitletud funktsioonid on saadaval **kasutuskontota**.



Ühendus on suunatud eelkõige **Välgussõlme operaatoritele**. Eelkõige võimaldab see siduda sõlme 1ML-kontoga, et hallata teatavat avalikku teavet, näiteks sõlme esitlust, kontaktlinde ja muid metaandmeid. Selle funktsiooni eesmärk on parandada sõlme nähtavust ja tuvastamist eksplortersüsteemis.



Oluline on märkida, et 1ML ei ole **ei ole hooldusteenus**. Konto loomine ei anna juurdepääsu sõlme rahalistele vahenditele, kanalitele või maksetele. Selle eesmärk on üksnes suhelda exploreriga deklaratiivsest ja informatiivsest vaatenurgast.



Lightning Network õppimise või avastamise kontekstis võib seda võimalust seega pidada **valikuliseks** ja reserveeritud edasijõudnute jaoks.



## Kokkuvõte



1ML on väärtuslik vahend Lightning Network jälgimiseks ja mõistmiseks selle avalike andmete põhjal. See võimaldab teil uurida võrgu struktuuri, analüüsida sõlmi ja kanaleid ning jälgida Lightning Network vastuvõtmise üldist arengut aja jooksul. Ilma et oleks vaja kontot või rahaliste vahendite käitlemist, pakub 1ML kõigile, kes soovivad süvendada oma arusaamist Lightning'i toimimisest, kättesaadava värava.


Kui soovite Lightning Network-ga edasi minna, siis soovitan täielikku kursust "Sissejuhatus Lightning Network-sse":



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb