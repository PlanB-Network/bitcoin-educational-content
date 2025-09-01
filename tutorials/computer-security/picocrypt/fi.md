---
name: Picocrypt
description: Avoimen lähdekoodin työkalu tietojen salaamiseen
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian BURNELin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen sisältöön on tehty muutoksia.*



___



## I. Esittely



Tässä opetusohjelmassa tutustumme Picocryptiin, yksinkertaiseen, kevyeen ja tehokkaaseen salausohjelmistoon, jolla voit salata tietoja korkealla turvallisuustasolla.



Soveltuu **tiedostojen salaamiseen**, voit käyttää sitä suojaamaan **tietokoneella, USB-tikulla** olevia tietoja, mutta myös pilvipalveluun tallennettuja tietoja. Voit esimerkiksi salata tietoja ja tallentaa ne **Microsoft OneDriveen, Google Driveen, iCloudiin tai Dropboxiin**, vaikka tähän tarkoitukseen suosin toista ohjelmistoa, joka esitellään tulevassa artikkelissa.



Voit käyttää sitä myös silloin, kun haluat **jakaa tietoja kolmannen osapuolen kanssa**: Picocryptin ja salausavaimen ansiosta he voivat purkaa tiedot koneellaan. Jos tilisi tai tietokoneesi vaarantuu, tietosi ovat siis suojattuja.



Picocrypt-projektin seuraamiseksi on vain yksi Address:





- [Picocrypt on GitHub](https://github.com/Picocrypt/Picocrypt)



Täysin **vapaa ja avoimen lähdekoodin** PicoCrypt on saatavilla **Windowsille**, **Linuxille** ja **macOSille**. Windowsissa voit asentaa sen omalle koneellesi tai käyttää siirrettävää versiota.



## II. Picocrypt, avoimen lähdekoodin salausohjelmisto



Picocrypt**-salausohjelmisto on **vaihtoehto** muille tunnetuille ratkaisuille, kuten **VeraCrypt** ja **Cryptomator** (*suunniteltu salaamaan tietoja pilviympäristöissä*) tai **AxCrypt**. Picocryptin virallisesta GitHubista löytyy muuten vertailu joihinkin kilpailijoihin:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Lähde: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt on **erittäin kevyt**, vain **3 MB**, eikä sitä tarvitse asentaa: se on **kannettava sovellus**, jonka etuna on, ettei se vaadi järjestelmänvalvojan oikeuksia! Se ei kuitenkaan laiminlyö tietoturvaa, sillä se luottaa **kestäviin ja luotettaviin algoritmeihin**:





- XChaCha20**-salausalgoritmi
- Avaimen ohitustoiminto **Argon2**



Juuri mainittujen etujen lisäksi se, mikä todella viehättää, on ** sen helppokäyttöisyys**!



Se tarvitsee vain yhden asian: **mutta se on jo suunniteltu, kuten yllä olevasta vertailutaulukosta (viimeinen rivi) näkyy. Mutta koska se on avointa lähdekoodia, mikään ei estä sinua tutustumasta sen lähdekoodiin.



Vaikka sitä verrataan BitLockeriin yllä olevassa taulukossa, **minusta BitLocker ja Picocrypt on tarkoitettu eri käyttötarkoituksiin**: BitLocker on tarkoitettu kokonaisen tietueen (esimerkiksi Windowsin) salaamiseen ja Picocrypt puurakenteen tai "Drive"-tyyppisen tallennustilan salaamiseen.



## III. Picocryptin käyttö



Tässä esittelyssä käytetään Windows 11 -konetta.



### A. Tietojen salaus Picocryptillä



Ensinnäkin sinun on ladattava Picocrypt.exe virallisesta GitHubista ([katso tämä sivu](https://github.com/Picocrypt/Picocrypt/releases)).



Avaa sovellus, jolloin sen minimalistinen Interface näkyy näytöllä. Jos haluat salata tietoja, olipa kyseessä sitten **tiedosto, useita tiedostoja tai kansio**, yksinkertaisesti **vedä ja pudota se Picocryptin Interface:een**. Tämä valitsee salattavat tiedot.



![Image](assets/fr/020.webp)



Tietojen salausta varten sinulla on useita vaihtoehtoja, kuten salausavain. Se voi olla **vahva salasana** tai **salausavain avaintiedoston muodossa** tai **kumpikin**. Jos otamme esimerkin salasanasta, voit valita, luotko oman salasanasi vai luotko salasanan Picocryptin avulla.



Salasanan on oltava vahva, sillä sitä voidaan käyttää tietojen salauksen purkamiseen. Kirjoita se kohtaan "**Salasana**" ja "**Vahvista salasana**" ja napsauta sitten "**Salaa**" salataksesi tiedot! Sitä ennen voit napsauttaa "**Muuta**"-painiketta "**Tallenna tuloste nimellä**" -kohdan vieressä määrittääksesi tulostushakemiston.



**Huomautus**: Jos haluat käyttää tiedostomuotoista avainta, napsauta "**Luo**" oikealla puolella "**Avaintiedostot**" luodaksesi avaimen. Valitse se sitten napsauttamalla "**Muokkaa**" ja vetämällä ja pudottamalla avaintiedosto sopivalle alueelle.



![Image](assets/fr/019.webp)



Kaksi valittua tiedostoa **salataan ja ryhmitellään yhteen** tiedostoon "**Encrypted.zip.pcv**", koska **PCV** on Picocryptin käyttämä tiedostopääte. Tämä ZIP-tiedosto on lukukelvoton salauksen ansiosta. Jos haluat estää valittujen tiedostojen ryhmittelyn yhteen salattuun ZIP-tiedostoon, sinun on valittava "**Recursively**"-vaihtoehto, jotta salattuja tiedostoja on yhtä monta kuin on salattavia tiedostoja.



Jotta pääsemme käsiksi tietoihin, meidän on purettava niiden salaus Picocryptin avulla.



![Image](assets/fr/023.webp)



Ennen kuin puhumme tietojen salauksen purkamisesta, tässä on tietoa joistakin käytettävissä olevista vaihtoehdoista:





- Paranoid-tila**: käytä Picocryptin tarjoamaa korkeinta turvallisuustasoa. Työkalu käyttää useita portaittaisia salausalgoritmeja (XChaCha20 ja Serpent) ja HMAC-SHA3:a BLAKE2b:n sijasta tietojen todentamiseen.
- Reed-Solomon**: toteuttaa *Reed-Solomon*-virheenkorjauskoodit, jotka helpottavat virheenkorjausta vioittuneessa datassa. Näin voit tukea noin 3 %:n korruptoitumisastetta tiedostossasi.
- Jaa palasiksi** tai **jakaa useisiin osiin**: Jos salaat suurta tiedostoa, voit pyytää Picocryptiä jakamaan sen useisiin osiin. Tämä voi helpottaa tiedoston siirtämistä.
- Pakkaa tiedostot** tai **Pakkaa tiedostot**: Pakkaa tiedostot salattujen tiedostojen koon pienentämiseksi.
- Poistetut tiedostot** tai **Fichiers supprimés**: poista lähdetiedostot ja säilytä vain salattu versio



### B. Tietojen purkaminen Picocryptillä



Jos tiedot on purettava, se ei ole sen monimutkaisempaa kuin salaaminenkaan. Avaa vain Picocrypt ja **vedä ja pudota purettava PCV-tiedosto**. Syötä sitten salasana ja/tai valitse avaintiedosto ennen kuin napsautat "**Purkaminen**".



![Image](assets/fr/021.webp)



Encrypted.zip ZIP-arkiston salaamaton versio antaa minulle nyt mahdollisuuden palauttaa kaksi tiedostoani selvänä tekstinä!



![Image](assets/fr/022.webp)



## IV. Päätelmät



**Teitä on varoitettu: Picocrypt on erittäin helppokäyttöinen, ja se toimii! Vaikka Interface on minimalistinen, se sisältää joitakin erittäin hyödyllisiä vaihtoehtoja salauksen mukauttamiseen! Ja koska se on saatavana kannettavana versiona, voit ottaa sen mukaasi kaikkialle, jotta voit purkaa tietosi luottavaisin mielin****



Muista käyttää vahvoja salasanoja tietojen suojaamiseen, ja jos käytät avaintiedostoa, sinun on muistettava varmuuskopioida se, muuten et voi enää purkaa Picocryptin tuottamaa PCV-säiliötä. Lopuksi sinun on hyvä tietää, että on olemassa myös [CLI-versio](https://github.com/Picocrypt/CLI) (jossa on vähemmän ominaisuuksia), jonka avulla voit käyttää Picocryptiä komentoriviltä: tässäkin Picocrypt avaa oven uusille mahdollisuuksille.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5