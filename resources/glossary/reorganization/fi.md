---
termi: UUDELLEENJÄRJESTELY
---

Viittaa ilmiöön, jossa lohkoketju kokee rakenteensa muutoksen kilpailevien lohkojen olemassaolon vuoksi samalla korkeudella. Tämä tapahtuu, kun osa lohkoketjusta korvataan toisella ketjulla, jolla on suurempi määrä kumuloitunutta työtä.

Nämä uudelleenjärjestelyt ovat osa Bitcoinin luonnollista toimintaa, jossa eri louhijat voivat löytää uusia lohkoja lähes samanaikaisesti, jakamalla näin Bitcoin-verkon kahtia. Tällaisissa tapauksissa verkko voi tilapäisesti jakautua kilpaileviin ketjuihin. Lopulta, kun yksi näistä ketjuista kumuloi enemmän työtä, muut ketjut hylätään solmujen toimesta, ja niiden lohkot muuttuvat niin kutsutuiksi "vanhentuneiksi lohkoiksi" tai "orpolohkoiksi". Tämän prosessin, jossa yksi ketju korvataan toisella, nimi on uudelleenjärjestely.

![](../../dictionnaire/assets/9.png)

Uudelleenjärjestelyillä voi olla erilaisia seurauksia. Ensinnäkin, jos käyttäjän transaktio oli vahvistettu lohkossa, joka osoittautuu hylätyksi, mutta tätä transaktiota ei näy lopullisesti voimassa olevassa ketjussa, hänen transaktionsa muuttuu jälleen vahvistamattomaksi. Tämän vuoksi on suositeltavaa odottaa aina vähintään 6 vahvistusta pitääkseen transaktion todella muuttumattomana. Kuuden lohkon syvyydessä uudelleenjärjestelyt ovat niin epätodennäköisiä, että niiden tapahtumisen mahdollisuus voidaan pitää käytännössä olemattomana.

Lisäksi, globaalilla järjestelmätasolla, uudelleenjärjestelyt merkitsevät louhijoiden laskentatehon hukkaan heittämistä. Todellakin, kun jakautuminen tapahtuu, jotkut louhijat ovat ketjussa `A`, ja toiset ketjussa `B`. Jos ketju `B` lopulta hylätään uudelleenjärjestelyn aikana, kaikki tämän ketjun louhijoiden käyttämä laskentateho on määritelmän mukaan hukkaan heitettyä. Jos Bitcoin-verkossa on liikaa uudelleenjärjestelyjä, sen kokonaisturvallisuus vähenee näin ollen. Tämä on osittain syy siihen, miksi lohkon koon kasvattaminen tai lohkojen välisen ajan lyhentäminen (10 minuuttia) voi olla vaarallista.

> ► *Jotkut bitcoin-käyttäjät suosivat termiä "orpolohko" viittaamaan vanhentuneeseen lohkoon. Yleisessä kielenkäytössä "reorg" viittaa "uudelleenjärjestelyyn". Termi "uudelleenjärjestely" on anglismi. Tarkemmin voitaisiin puhua "uudelleensynkronoinnista".*