---
termi: RESYNKRONISOINTI
---

Viittaa ilmiöön, jossa lohkoketju kokee rakenteensa muutoksen kilpailevien lohkojen esiintyessä samalla korkeudella. Tämä tapahtuu, kun osa lohkoketjusta korvataan toisella ketjulla, jolla on suurempi määrä kumuloitunutta työtä.

Nämä resynkronisoinnit ovat osa Bitcoinin luonnollista toimintaa, jossa eri louhijat saattavat löytää uusia lohkoja lähes samanaikaisesti, jakamalla näin Bitcoin-verkon kahtia. Tällaisissa tapauksissa verkko voi tilapäisesti jakautua kilpaileviin ketjuihin. Lopulta, kun yksi näistä ketjuista kumuloi enemmän työtä, muut ketjut hylätään solmujen toimesta, ja niiden lohkot muuttuvat niin kutsutuiksi "vanhentuneiksi lohkoiksi" tai "orpolohkoiksi". Tämän prosessin, jossa yksi ketju korvataan toisella, nimi on resynkronisointi.

![](../../dictionnaire/assets/9.png)

Resynkronisoinneilla voi olla erilaisia seurauksia. Ensinnäkin, jos käyttäjän transaktio vahvistettiin lohkossa, joka myöhemmin hylätään, mutta tätä transaktiota ei löydy lopulta voimassa olevasta ketjusta, hänen transaktionsa muuttuu jälleen vahvistamattomaksi. Tämän vuoksi suositellaan odottamaan aina vähintään 6 vahvistusta pitääkseen transaktion todella muuttumattomana. Kuuden lohkon syvyydessä resynkronisoinnit ovat niin epätodennäköisiä, että niiden tapahtumisen mahdollisuus voidaan pitää käytännössä olemattomana.

Lisäksi globaalilla järjestelmätasolla resynkronisoinnit merkitsevät louhijoiden laskentatehon hukkaan heittämistä. Todellakin, kun jakautuminen tapahtuu, jotkut louhijat ovat ketjussa `A` ja toiset ketjussa `B`. Jos ketju `B` lopulta hylätään resynkronisoinnin aikana, kaikki tämän ketjun louhijoiden käyttämä laskentateho on määritelmän mukaan hukkaan heitettyä. Jos Bitcoin-verkossa on liikaa resynkronisointeja, verkon kokonaisturvallisuus vähenee tämän vuoksi. Tämä on osittain syy siihen, miksi lohkon koon kasvattaminen tai lohkojen välisen ajan lyhentäminen (10 minuuttia) voi olla vaarallista.

> ► *Jotkut bitcoin-käyttäjät suosivat termiä "orpolohko" viittaamaan vanhentuneeseen lohkoon. Lisäksi, vaikka se on anglismi, yleiskielessä "uudelleenjärjestely" tai "reorg" on usein suositumpi kuin "resynkronisointi".*