---
name: Zeus Embedded
description: Lightning Zeus Embedded Wallet:n käyttäminen
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS on alun perin salamasolmujen etähallintaan tarkoitettu mobiilisovellus, jonka avulla voit hallita etäpalvelimelle asennettua solmua


Sovelluksessa on kuitenkin myös "Sulautettu solmu".



**Tässä opetusohjelmassa tutustumme juuri tähän sovelluksen osa-alueeseen. Näin kenellä tahansa voi olla oma salamasolmunsa matkapuhelimessa ilman erillistä palvelinta, samalla tavalla kuin ACINQ tarjoaa uskomatonta Wallet-salamaa Phoenix.**



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Muistutettakoon, että Lightning on verkko, joka toimii rinnakkain Bitcoin:n kanssa ja mahdollistaa bitcoinien vaihdon ilman On-Chain:n järjestelmällisiä transaktioita. Tuloksena on lähes välittömiä transaktioita, eikä lohkon validointia tarvitse odottaa 10 minuuttia. Tämä on erityisen hyödyllistä, kun maksetaan kauppiaalle fyysisessä maailmassa. Lisäksi Lightning tarjoaa huomattavan tason **luottamuksellisuutta**, jota Bitcoin-verkossa ei ole*.



**Zeus "Integroitu "** on suunnattu Bitcoiners, jotka haluavat maksimoida yksityisyytensä ja itsenäisyytensä.


Lyhyesti sanottuna se on **potentiaalisesti** salakirjoittajien unelmien Wallet-mobiili. Vaikka se on vielä lapsenkengissä (alfaversio) ja siinä on muutamia virheitä, sen ominaisuudet ovat lukuisat, eikä ole epäilystäkään siitä, että se ilahduttaa kaikkein pelottomimpia meistä, jotka haluavat maksimaalisen hallinnan ja valinnaisuuden.



Toisaalta en usko, että se soveltuu tällä hetkellä aloittelijoille, jotka eivät tunne Bitcoin:tä ja jotka haluavat vain yksinkertaisen tavan lähettää/vastaanottaa satosheja. Tosin tämä saattaa muuttua tulevaisuudessa, sillä Cashu (chaumian Ecash) -protokollan kautta on toteutumassa aloittelijoille tarkoitettu huoltajuusominaisuus...



## Asenna sovellus



Siirry [hankkeen verkkosivustolle] (https://zeusln.com/) ja lataa sovellus älypuhelimesi käyttöjärjestelmään:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Portfolion luominen



Kun sovellus on käynnistynyt, napsauta "Quick Start" -painiketta aloittaaksesi Wallet:n luomisen.



![image](assets/fr/03.webp)





Tämän jälkeen näyttöön tulee joukko aloitusnäyttöjä. Odota hetki ja sitten muutama minuutti, kunnes solmu on 100-prosenttisesti synkronoitu Neutrinon kautta.



Tämä voi kestää muutaman minuutin. Tiedoksi neutrino on tapa, jolla mobiililompakot voivat käyttää Blockchain Bitcoin-tietoja ilman Full node:n käyttöä.



![image](assets/fr/04.webp)





Muutaman hetken kuluttua olet valmis lähtemään.



![image](assets/fr/05.webp)




## Sovelluksen asennus



Valmiina, no ei aivan, sillä on sanomattakin selvää, että nimensä veroinen Zeus-käyttäjä navigoi Wallet:llä tyylikkäästi ja tyylikkäästi. Joten meidän on vaihdettava hänen avatarinsa.



Napsauta avatariasi näytön oikeassa yläkulmassa:



![image](assets/fr/06.webp)





Napsauta hammaspyörää ja sitten plussaa "+" :



![image](assets/fr/07.webp)





Valitse kaunein Zeuksen kuva, joka edustaa tätä Wallet:tä, ja napsauta "VALITSE KUVA" ruudun alareunassa ja palaa sitten takaisin napsauttamalla oikeassa yläkulmassa olevaa nuolta.



![image](assets/fr/08.webp)





Anna lopuksi Wallet:lle lempinimi ja napsauta "SAVE Wallet CONFIG", jotta muutos tulee voimaan. Palaa aloitusnäyttöön napsauttamalla vasemmassa yläkulmassa olevaa takaisin-nuolta.



![image](assets/fr/09.webp)





Tällä kertaa voimme todella aloittaa.



![image](assets/fr/10.webp)



### Biometria



Voit suojata Wallet:n käytön lisäämällä PIN-koodin/salasanan ja aktivoimalla biometriikan.



Siirry Wallet:n päävalikkoon napsauttamalla vasemmassa yläkulmassa olevia vaakaviivoja.



![image](assets/fr/11.webp)





Valitse "Asetukset", sitten "Suojaus" ja lopuksi "Aseta/muuta PIN-koodi".



![image](assets/fr/12.webp)





Luo PIN-koodi, vahvista se ja aktivoi biometria painamalla vastaavaa "Biometria"-painiketta.  Palaa päävalikkoon vasemmassa yläkulmassa olevan nuolen avulla.



![image](assets/fr/13.webp)




### Tallenna Mnemonic-lause



Kun olet päässyt takaisin päävalikkoon, napsauta "Varmuuskopioi Wallet" ja lue sitten varoitusteksti, jossa kerrotaan, että 24 saamasi sanan menettäminen on sama kuin menettäisit pääsyn varoihisi ja että kuka tahansa, jolla on nämä sanat, pääsee käsiksi varoihisi. Älä koskaan anna niitä kenellekään.



Valitse "I UNDERSTAND" näytön alareunasta. Klikkaa sitten kutakin 24 sanaa, jotta ne tulevat esiin, ja merkitse ne huolellisesti muistiin.



Voit kirjoittaa sen paperille tai ehkä kaiverruttaa sen ruostumattomaan teräkseen, jotta se on suojattu tulipalolta, tulvalta tai romahdukselta. Välineen valinta Mnemonic:ään riippuu turvallisuusstrategiastasi, mutta jos käytät Zeusta kohtuullisia summia sisältävänä kulusalkkuna, paperin pitäisi riittää.



Jos haluat lisätietoja oikeasta tavasta tallentaa ja hallita Mnemonic-lauseesi, suosittelen lämpimästi seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Kun olet valmis, napsauta näytön alareunassa olevaa "I'VE BACKUP MY 24 WORDS" -painiketta, ja olemme takaisin aloitusnäytöllä, valmiina vastaanottamaan ensimmäiset bitcoinit.




## Vaihtoehto 1 - Vastaanota On-Chain-bittikolikoita ja avaa Lightning-kanava



**Zeus Embedded** on ensisijaisesti suunniteltu sulautetuksi salamasolmuksi, mutta sitä voidaan käyttää myös Wallet On-Chain:nä.



Jos haluat vastaanottaa On-Chain-bittikolikoita, napsauta "On-Chain"-painiketta ja sitten "Vastaanota".


Skannaa lopuksi QR-koodi tai kopioi Bitcoin Address tallettaaksesi varoja.



![image](assets/fr/15.webp)





Kun varat on vahvistettu ja hyvitetty Wallet:ään, voit avata niillä **Valamakanavan**. Lightning-kanava on porttisi Lightning Network:een, jonka kautta voit käyttää Exchange-bittikolikoita paljon luottamuksellisemmin ja nopeammin.





- Voit tehdä niin klikkaamalla "SIIRRÄ On-Chain RAHOITUS LIGHTNINGiin"



Seuraavassa näytössä sinua pyydetään avaamaan kanava yhteistyössä **"Olympus by Zeus "** kanssa, joka on Wallet:n suosima LSP (Lightning Service Provider).


Tässä oppaassa valitsemme tämän vaihtoehdon yksinkertaisuuden vuoksi, mutta on täysin mahdollista avata kanavia mihin tahansa verkon solmuun.


On jopa mahdollista avata useita kanavia yhdellä tapahtumalla valitsemalla "OPEN ADDITIONAL CHANNEL". *Mutta tarkastelemme tätä* **Zeus Embedded** *-oppikirjan "edistyneemmissä" versioissa.*





- Valitse sitten summa, jonka haluat osoittaa tälle kanavalle. Meidän tapauksessamme kaikki On-Chain-varat käytetään, joten aktivoimme "Käytä kaikki mahdolliset varat" -painikkeen.





- Valitse lopuksi "OPEN CHANNEL" -painike näytön alareunasta.



![image](assets/fr/16.webp)





Kanava on luotu muutamassa sekunnissa, ja olemme valmiita tekemään ensimmäiset Lightning-tapahtumat. Aloitusnäytössä näemme pienen kellon Wallet-saldomme vieressä. Tämä johtuu siitä, että meidän on vielä odotettava 3 On-Chain-vahvistusta, ennen kuin kanava on todella toiminnassa.



![image](assets/fr/17.webp)





Kolmen vahvistuksen jälkeen huomaamme, että saldomme on nyt hyvitetty Lightning-lisäosaan.



![image](assets/fr/18.webp)



Pieni yksityiskohta: kun klikkaamme näytön alareunassa olevaa valikkoa nähdäksemme salamakanaviemme tilan, näemme, että pieni osa saldostamme ei ole käytettävissä: voimme käyttää vain 208253 satoshia sen 210370 satoshin sijaan, joka meillä todellisuudessa on. Tämä on normaalia, sillä se on salamaprotokollan ominaisuus.



Lopuksi on huomattava, että yhteistyökumppanimme Olympus pidättää oikeuden sulkea kanavan oman harkintansa mukaan, jos sitä ei esimerkiksi käytetä. Varmistaaksemme, että kanavamme säilyy, meidän on maksettava LSP:lle (Lightning Service Provider), kuten näemme seuraavassa kappaleessa, kanavan avaamisen 2. tavan kautta.





## Lähetä bitcoineja Lightningin kautta



Nyt kun olemme saaneet kanavamme toimimaan, katsotaanpa, miten voimme käyttää sitä Invoice (Invoice) -salaman maksamiseen.



Tee tämä napsauttamalla "Salama"-painiketta ja sitten "Lähetä".



![image](assets/fr/19.webp)





Kopioi Invoice-korttisi seuraavalla näytöllä sille varattuun kenttään tai skannaa se napsauttamalla oikeassa yläkulmassa olevaa kuvaketta. Liu'uta lopuksi "Slide to Pay" -painiketta oikealle maksaaksesi.



![image](assets/fr/20.webp)






Odota muutama sekunti, niin Invoice on maksettu, ja satoshisi ovat matkanneet valon nopeudella.



![image](assets/fr/21.webp)





Zeuksen avulla voit sitten lisätä maksun nimellisarvoksi setelin tai tarkastella reittiä, jonka satelliittisi ovat kulkeneet ennen määränpäähänsä saapumista (ja kaikkien välikohtien perimiä maksuja). Juuri tällaisista toiminnoista pidämme Wallet:ssa.



![image](assets/fr/22.webp)



Huomaa, että toisin kuin Wallet:ssa, kuten [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), Zeuksen tapauksessa reitti lasketaan paikallisesti eikä sitä delegoida kolmannelle osapuolelle (Phoenixin tapauksessa ACINQ:lle). Olet siis ainoa, joka tietää maksun vastaanottajan. Menetämme hieman tehokkuutta (maksujen suorittaminen kestää hieman kauemmin, mutta voitamme paljon yksityisyyden kannalta).





Klikkaamalla aloitusnäytön alareunassa olevaa pientä nuolta voit myös tarkastella maksuhistoriaamme. Tässä näemme Green:ssä On-Chain:stä saadun 212 121 Sats:n, sitten punaisella vastaavasti kanavamme avaamiseen käytetyt 211 756 Sats ja sitten 121 212 satoshia, jotka käytettiin Invoice-salamamme maksamiseen.



![image](assets/fr/23.webp)





## Vaihtoehto 2 - Vastaanota bitcoineja suoraan Lightningin kautta



Sen sijaan, että avaisit kanavan manuaalisesti, kuten äsken näimme, on mahdollista vastaanottaa varoja suoraan Lightningin kautta jopa ilman olemassa olevaa kanavaa käyttämällä Olympusta, Zeus LSP:tä.




- Tee tämä napsauttamalla aloitusnäytön "Salama"-painiketta ja sitten "Vastaanota".
- Valitse sitten haluamasi summa "Amount"-ruutuun ja valitse "CREATE Invoice"-painike näytön alareunasta.



![image](assets/fr/24.webp)





Seuraavalla näytöllä näkyy Invoice, joka on maksettava satoshien saamiseksi. Meille kerrotaan, että LSP pidättää 10 000 Sats:tä, jos maksu suoritetaan Lightningilla. Näemme myöhemmin, miten nämä kanavan avausmaksut ovat perusteltuja.



Maksa Invoice tai anna jonkun muun maksaa se, niin kanava avataan automaattisesti, mutta siitä vähennetään 10 000 Sats sovitulla tavalla.



![image](assets/fr/25.webp)





Olemme nyt kahden salamakanavan johdossa, joiden tilan voi tarkistaa napsauttamalla aloitusnäytön alareunassa valkoisella nuolella merkittyä painiketta.



Voimme nähdä, että toisin kuin On-Chain-asteikosta avatussa kanavassa, suoraan salaman kautta avatussa kanavassa ei näy varoitusta.


Koska olet maksanut tämän kanavan perustamisesta, Lightning-palveluntarjoaja (LSP) sitoutuu ylläpitämään kanavaa 3 kuukauden ajan ja tarjoaa sinulle "tulevaa likviditeettiä". Alemmassa kanavassa näet, että vastaanottokapasiteetti on 96383 satoshia. LSP on siis sitonut pääomaa, jotta voit vastaanottaa maksuja heti kanavan avaamisen jälkeen.



Maksetut 10 000 Satoshi kattavat siis kanavan avaamisesta aiheutuvat kustannukset (Bitcoin On-Chain transaktio, takuu kanavan ylläpidosta kolmen kuukauden ajan ja pääoman lukitseminen).



![image](assets/fr/26.webp)





Onneksi olkoon, olet nyt valmis käyttämään Zeus Embeddediä, Wallet-mobiilivalaistusjärjestelmää, jossa on markkinoiden kehittyneimmät ominaisuudet.





Jos haluat lisätietoja Lightning Network:n teknisestä toiminnasta, löydät Fanis Michalakisin erinomaisen ilmaisen Plan ₿ Academy-koulutuksen:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb