---
name: Osallistuminen - Korjaus
description: Kuinka korjata virhe PlanB-verkostossa?
---
![cover](assets/cover.webp)

PlanB:n tehtävänä on tarjota johtavia koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen. Osallistumiset voivat ottaa eri muotoja: olemassa olevien tekstien korjaaminen ja oikoluku, kääntäminen toisille kielille, tiedon päivittäminen tai uusien opetusohjelmien luominen, joita ei vielä ole saatavilla sivustollamme.

Jos tunnistat virheen jossakin koulutussisällössämme (opetusohjelmat, koulutukset, resurssit...) olipa kyseessä kirjoitusvirhe, kielioppi, pieni käännösvirhe äidinkielelläsi tai jopa kirjoitusvirhe, olisimme erittäin kiitollisia, jos ehdottaisit itse nopeaa korjausta.

Tämä opas ohjaa sinut askel askeleelta läpi prosessin näiden pienten virheiden korjaamiseksi. Se on tarkoitettu aloittelijoille, jotka eivät halua syventyä Gitin monimutkaisuuksiin. Jos kuitenkin tunnet olosi mukavaksi Gitin kanssa, tässä on nopea yhteenveto: sinun tarvitsee vain tehdä haara [PlanB Networkin datavarastosta](https://github.com/PlanB-Network/bitcoin-educational-content), tehdä muutoksia omistetussa haarassa ja lähettää vetopyyntö `dev`-haaraan lähdevarastossa.

Huomaa, että jos aiot suorittaa koko asiakirjan tarkistuksen ja tarkistamisen, erityisesti sisällön käännösten osalta, kehotan sinua tutustumaan tähän toiseen yksityiskohtaisempaan oppaaseen.

https://planb.network/tutorials/others/contribution/content-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6

 Tässä keskitymme vain siihen, miten tehdä nopea korjaus pienelle virheelle.

- Ensinnäkin sinulla on oltava tili GitHubissa. Jos et tiedä, miten tili luodaan, olemme tehneet yksityiskohtaisen oppaan, joka opastaa sinua.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Mene [PlanB:n GitHub-varastoon, joka on omistettu datalle](https://github.com/PlanB-Network/bitcoin-educational-content):
![typos](assets/01.webp)
- Täällä löydät kaiken sisältömme järjestettynä osiin.
- Jos haluat muokata opetusohjelmaa, mene esimerkiksi `tutorials`-kansioon:
![typos](assets/02.webp)
- Löydät sitten eri kategoriat opetusohjelmista verkkosivustollamme. Jos haluat muokata opetusohjelmaa `Privacy`-kategoriassa, klikkaa vastaavaa kansiota:
![typos](assets/03.webp)
- Valitse sitten kansio, joka vastaa korjattavaa sisältöäsi:
![typos](assets/04.webp)
- Jokaisessa sisältökansiossa löydät tiedot saatavilla eri kielillä. Esimerkiksi `en.md`-tiedosto vastaa opetusohjelman englanninkielistä versiota, kun taas `fr.md`-tiedosto edustaa ranskankielistä versiota. Valitse tiedosto, jota haluat muokata: ![typos](assets/05.webp)
- Saavut sitten GitHub-sivulle, joka sisältää haluamasi sisällön. Varmista, että olet asiakirjassa, jota haluat muokata: ![typos](assets/06.webp)
- Klikkaa pientä kynäkuvaketta ylävasemmalla: ![typos](assets/07.webp)
- Jos et ole aiemmin osallistunut PlanB Networkin sisällön luomiseen, sinun on luotava oma haarasi alkuperäisestä varastosta. Varaston haarauttaminen tarkoittaa kyseisen varaston kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektissa työskentelyn alkuperäistä varastoa muuttamatta. Klikkaa `Fork this repository` -painiketta: ![typos](assets/08.webp)
- Saavut sitten GitHubin muokkaussivulle: ![typot](assets/09.webp)- Tee tekstiisi tarvittavat muutokset korjataksesi havaitsemasi virheet. Älä pelkää, olet tällä hetkellä omassa haarassasi, joten tämä ei muuta mitään PlanB Network -sivustolla toistaiseksi. Esimerkiksi tässä, kuvitellaan, että muutin sanaa "entrées", koska siinä oli kirjoitusvirhe: ![typot](assets/10.webp)
- Kun olet saanut dokumentin korjaukset valmiiksi, voit klikata vihreää `Commit Changes...` -painiketta. Commit on kuin välitön tilannekuva työstäsi tietyllä hetkellä, joka mahdollistaa muutosten historian säilyttämisen: ![typot](assets/11.webp)
- Lisää otsikko muutoksillesi sekä lyhyt description: ![typot](assets/12.webp)
- Klikkaa vihreää `Propose changes` -painiketta: ![typot](assets/13.webp)
- Saavut sitten sivulle, joka tiivistää kaikki tekemäsi muutokset: ![typot](assets/14.webp)
- Vierittämällä alas voit nähdä tekemäsi tarkat muutokset: ![typot](assets/15.webp)
- Jos kaikki on mielestäsi kunnossa ja olet saanut muutokset valmiiksi, voit klikata vihreää `Create Pull Request` -painiketta: ![typot](assets/16.webp)
- Saavut PR-sivulle. Pull Request on pyyntö, jonka avustaja lähettää ilmoittaakseen, että he ovat tehneet muutoksia haarassa etävarastossa ja että he toivovat näiden muutosten tulevan tarkastelluiksi ja mahdollisesti yhdistetyiksi varaston päähaaraan: ![typot](assets/17.webp)
- Voit lisätä otsikon ja lyhyen kuvauksen PR:lle: ![typot](assets/18.webp)
- Jos kaikki näyttää hyvältä, voit klikata vihreää `Create Pull Request` -painiketta: ![typot](assets/19.webp)
- Onnittelut, PR:si on lähetetty! Voit seurata sen etenemistä `Pull requests` -välilehdessä [PlanB Networkin GitHub-repositoriossa](https://github.com/PlanB-Network/bitcoin-educational-content/pulls) :![typot](assets/20.webp)
Kiitos paljon panoksestasi! Jos haluaisit tehdä muita tyyppisiä panostuksia PlanB Networkille, kuten sisällön kirjoittamista tai kääntämistä, tutustu vapaasti muihin oppaisiimme "Contribution" osiossa.

https://planb.network/tutorials/others


