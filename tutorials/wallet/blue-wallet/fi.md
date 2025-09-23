---
name: Blue Wallet

description: Bitcoin Radikaalisti yksinkertainen ja tehokas portfolio
---
![cover](assets/cover.webp)



Bitcoin:n käytön aloittaminen näyttää olevan suuri haaste ihmisille, jotka suhtautuvat epäilevästi sen käytön yksinkertaisuuteen. Oikeiden välineiden löytäminen tämän yksinkertaisuuden varmistamiseksi on siksi ensiarvoisen tärkeää, jotta Bitcoin voidaan ottaa paremmin käyttöön Exchange:n välineenä eikä vain arvovarastona.



Tässä opetusohjelmassa tutustumme Blue Wallet:een, yksinkertaiseen mutta erittäin tehokkaaseen Bitcoin Wallet:een, jonka avulla voit hallita bitcoinejasi henkilökohtaisesti ja myös luoda [Multisig](https://planb.network/resources/glossary/multisig) -periaatteeseen perustuvia hallinto-osuuskuntia (älä huoli, palaamme siihen vielä).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Blue Wallet:n käytön aloittaminen



Blue Wallet on avoimen lähdekoodin Bitcoin Wallet, jonka avulla voit hallita bitcoinejasi. Se on saatavilla mobiilisovelluksena sekä Android- että iOS-alustoilla. Tässä opetusohjelmassa tukeudumme Android-versioon, mutta kaikki kehitettävät prosessit ovat kuitenkin yhtä päteviä iOS:ssä.



![download](assets/fr/01.webp)



⚠️ Varmista, että lataat Blue Wallet Bitcoin Wallet -sovelluksen viralliselta alustalta, jotta voit taata sen aitouden ja suojata bitcoinisi mahdollisilta vuodoilta ja hakkeroinnilta.



Kun olet asentanut sen, voit luoda uuden Wallet:n ja tallentaa 12 palautussanaa tai tuoda olemassa olevan Bitcoin Wallet:n. Selvitä, miten voit tehdä tehokkaan varmuuskopion avainsanoistasi, jotta et menetä pääsyä bitcoineihisi.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Blue Wallet:n avulla voit luoda erillisiä, omia Bitcoin-salkkuja. Voit esimerkiksi käyttää samassa sovelluksessa yhtä Wallet-salkkua säästöjäsi varten ja toista päivittäisiä menojasi varten.



![home](assets/fr/02.webp)



## Salkkutyypit



Blue Wallet:ssä on kaksi alkuperäistä Bitcoin-salkkutyyppiä.



### Bitcoin-salkku



Jos olet tottunut muihin Bitcoin-salkkuihin, kuten Phoenixiin tai Aqua:een, et ole lainkaan ulkona Interface:stä Blue Wallet:n Bitcoin-salkun kanssa.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Blue Wallet:n Bitcoin Wallet edustaa Bitcoin-ekosysteemin vakio-Wallet:tä. Voit käyttää bitcoineja, kunhan sinulla on hallussasi palautussanat, jotka antavat verkossa pätevän allekirjoituksen, jolla todennat, että omistat bitcoinit.



Jos haluat luoda Bitcoin-salkun, napsauta **Lisää nyt**-painiketta, anna salkun nimi ja valitse Bitcoin-tyyppi.



![bitcoin-wallet](assets/fr/03.webp)



Kun napsautat Bitcoin Wallet -esikatseluasi, voit tarkastella tapahtumahistoriaasi sekä lähettää ja vastaanottaa bitcoineja.



⚠️ Kaikki Bitcoin Wallet:n tapahtumat ovat Bitcoin-protokollan pääketjussa (Mainnet).





- Bitcoinien vastaanottaminen Bitcoin Blue Wallet Wallet:lla on intuitiivista. Napsauta näytön alareunassa olevaa **Vastaanota**-painiketta. Jaa QR-koodi tai Bitcoin Address lähettäjän kanssa, jotta hän voi lähettää sinulle bitcoinit.



Voit myös määrittää ennalta määritetyn määrän, jolla voit määrittää haluamasi Bitcoin:n määrän.



![receive-bitcoin](assets/fr/04.webp)





- Lähetä bitcoineja Bitcoin Address:lle **lähetä**-painikkeella, aseta haluamasi summa ja vahvista tapahtuma.



![send-bitcoin](assets/fr/05.webp)



Blue Wallet:n avulla voit määrittää Bitcoin-lähetyksen parametrit haluamallasi tavalla.



Voit siis valita sinulle sopivan transaktiomaksusuhteen, jos haluat, että transaktiosi validoidaan nopeasti Mempool:ssä ja louhijat sisällyttävät sen lohkoon. Valitsemastasi suhteesta riippuen louhijat priorisoivat transaktiosi enemmän tai vähemmän. Lue lisää Mempool-avaruuden oppaasta.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Blue Wallet:n avulla voit lisätä useita vastaanottajia yhteen lähetykseen.



Kun lisäät ensimmäisen vastaanottajan Bitcoin Address:n, valitse vaihtoehdoissa **Lisää vastaanottaja**, lisää Bitcoin Address ja aseta sitten tälle vastaanottajalle lähetettävä summa jne. Blue Wallet lähettää bitcoinit useita lähetyksiä varten yhden toimenpiteesi perusteella.



![add-recipients](assets/fr/07.webp)



Voit poistaa yhden tai kaikki vastaanottajat napsauttamalla **Poista vastaanottaja** ja **Poista kaikki vastaanottajat**.



![remove-recipient](assets/fr/08.webp)





- **Paisuta maksuja**: Oletko tehnyt tapahtuman, jonka vahvistaminen kestää kauan? Ottamalla maksujen inflaation käyttöön voit lisätä ylimääräisiä maksutapahtumamaksuja vireillä olevaan tapahtumaan nopeuttaaksesi sen vahvistamista.



![bumping](assets/fr/09.webp)



### Multisig Salkku



Multisig (usean allekirjoituksen) Wallet edustaa Wallet:ää, joka on luotu ryhmittämällä tietty määrä (vähintään 2) Bitcoin-lompakoita. Tämäntyyppisessä Wallet:ssä bitcoinien kuluttamisesta tulee valitusta kokoonpanosta ja menetelmästä riippuen kollektiivinen ja yhteistoiminnallinen toiminta.



Blue Wallet:ssa voit luoda useita allekirjoituksia sisältäviä salkkuja yhdistyksellesi, perheellesi ja yrityksellesi. Tutustumme tässä osiossa tämän erityyppisen salkun kaikkiin osa-alueisiin.



Lisää uusi salkku ja valitse tyyppi **Multisig Holvi** luodaksesi monisalkun.



![multisig-vault](assets/fr/10.webp)



Määritä m-de-n-konfiguraatio usean allekirjoituksen organisaatiossasi napsauttamalla **Vault Settings**.



⚠️ M-of-n-kokoonpanossa **m** on tapahtuman hyväksymiseen tarvittavien allekirjoitusten vähimmäismäärä ja **n** organisaatiossasi olevien salkkujen määrä.



Muista määritellä allekirjoitusten vähimmäismäärä (m) organisaatiosi enemmistölle. Esimerkiksi 2:3 monisignaattorikokoonpano edellyttää, että organisaatiossasi kaksi lompakkoa allekirjoittaa tapahtuman, ennen kuin se voidaan suorittaa.



❗M-of-n-kokoonpanon määrittely, jossa n on yhtä suuri kuin m, on suuri riski. Kun jäsen menettää pääsyn Wallet:eensä, menetät oikeuden käyttää bitcoineja Wallet:ssä.



Seuraavassa on muutamia esimerkkejä optimaalisista kokoonpanoista, joilla varmistetaan bitcoinien turvallisuus ja saatavuus:





- 2-de-3 multi signature.





- 5-de-7 multi signature.



![vault-settings](assets/fr/11.webp)



Noudata parhaita käytäntöjä valitsemalla P2WSH-muoto.



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) tai Pay to Witness Script Hash** on lukitusmenetelmä, joka lukitsee transaktiosi lähtevät bitcoinit (tuotokset) Blue Wallet:n asettaman mukautetun skriptin Hash:een. Tämän tyyppisen lukituksen tärkein etu on se, että se pienentää transaktiotietojen kokoa ja mahdollistaa epäsuorasti pienempien transaktiomaksujen maksamisen.



Luo tai tuo kaikki **n** salkkua kokoonpanossasi. Ohjeessamme käytämme 2-of-3 monialkakirjoituskokoonpanoa. Muista tallentaa palautussanat jokaiselle salkulle erikseen.



![vault-keys](assets/fr/12.webp)





- Vastaanottaa bitcoineja



Multisig Wallet-sivulla on tapahtumahistoria sekä Vastaanota- ja Lähetä-painikkeet.



Bitcoinien vastaanottaminen monisignatuurisessa Wallet:ssa on sama prosessi kuin tavallisessa Bitcoin Wallet:ssa.





- **Lähetä bitcoineja**:



Hallitsemalla usean allekirjoituksen Wallet:ää, bitcoinien käyttämisestä tulee yhdistelmätoimi, joko muiden ihmisten tai toisen oman Wallet:n kanssa. Wallet:n yksi allekirjoitus ei enää riitä. Tämä lisää bitcoinien turvallisuutta Layer:lla, koska pahantahtoinen henkilö ei voi käyttää bitcoineja, kun hän saa haltuunsa vain yhden yksityisistä avaimista.



Sinisen Wallet:n tavallisen Bitcoin-salkun tapaan voit määrittää useita vastaanottajia **Lisää vastaanottajia** -vaihtoehdossa.



Kun vahvistat tapahtuman, tarvitset toisen allekirjoituksen, jolla hyväksyt bitcoinien käytön. Muista, että kyseessä on 2-de-3-moninkertaisen allekirjoituksen konfiguraatio.



Jos toinen Wallet:n allekirjoittaja on myös käyttäjä, hän voi allekirjoittaa tapahtuman, vaikka hän ei olisi internetissä (ei Wi-Fi-yhteyttä, ei mobiilidataa), skannaamalla juuri luomasi [osittain allekirjoitetun tapahtuman] (https://planb.network/resources/glossary/psbt) QR-koodin.



![mutisig-send](assets/fr/13.webp)





- Mene pidemmälle **Multi signature** -salkun avulla:



Napsauta Wallet:n Interface:n monikäyttöisen Wallet:n **Hallitse näppäimiä**-painiketta.



Kun unohdat yhden allekirjoittajasalkun palautussanan (**Unohda tämä seed...**), ilmoitat Blue Wallet:lle, että sen on poistettava näiden sanojen varmuuskopiot muististaan. Olet siis tehnyt ulkoisen varmuuskopion.



![revoke-key](assets/fr/14.webp)



Tällä toiminnolla säilytät vain näihin palautussanoihin liittyvän julkisen avaimen.



⚠️ Vain julkisten avainten säilyttäminen (XPUB) antaa sinulle mahdollisuuden lisätä ylimääräisen turvallisuustason 2-of-3-monisignaattorikokoonpanoon. Kaikkien palautussanojen pitäminen yhdessä paikassa voi olla vahingollista, kun puhelimeen hyökätään. Hyökkääjät, joilla on pääsy vain yhteen **VAULT** (avainsanaan), jota käytät transaktioiden allekirjoittamiseen, eivät voi varastaa bitcoinejasi (vaaditaan vähintään 02 allekirjoitusta), koska julkisia avaimia ei voi käyttää transaktioiden allekirjoittamiseen.



## Lisää vaihtoehtoja Blue Wallet:n kanssa



### Salkun käyttöoikeuksien turvallisuuden parantaminen



Asetuksissa **Turvallisuus** -vaihtoehdon avulla voit määrittää sormenjäljen käytön tapahtuman suorittamiseen, Wallet:n vientiin tai poistamiseen. Tämä todentaa älypuhelinta käyttävän henkilön.



![biometry](assets/fr/15.webp)



## Aktivoi Lightning Network



Lightning Network ei ole enää natiivisti tuettu Blue Wallet -sovelluksessa.



Asetukset > **Lightning-asetukset** -kohdassa voit liittää Lightning Wallet:n manuaalisesti, kun käytät Lightning Network Daemon (LND) -solmua. Asenna LND-keskitin ja yhdistä sitten Wallet syöttämällä keskittimen luoma linkki.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Olet nyt suorittanut Blue Wallet -kierroksen, ja olet valmis käyttämään Bitcoin:tä kaikessa yksinkertaisuudessaan ja tehossaan. Suosittelemme, että otat seuraavan askeleen ja otat selvää, miten voit hyväksyä Bitcoin-maksuja myymälöissäsi Lightningin voiman ansiosta.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06