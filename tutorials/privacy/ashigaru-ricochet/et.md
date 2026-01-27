---
name: Ashigaru - Ricochet
description: Ricocheti tehingute mõistmine ja kasutamine
---
![cover ricochet](assets/cover.webp)



> *Premium tööriist, mis lisab teie tehingule lisahüppeid ajaloo kohta. Tõrjuda mustad nimekirjad ja aidata kaitsta ebaõiglase 3. osapoole konto sulgemise eest.*

## Mis on Ricochet?



Ricochet on tehnika, mis seisneb mitme fiktiivse tehingu sooritamises enda suunas, et simuleerida bitcoini omandiõiguse üleandmist. See vahend erineb Ashigaru teistest tehingutest (mis on päritud Samurai Wallet-st) selle poolest, et see ei paku prospektiivset anonüümsust, vaid pigem tagantjärele anonüümsuse vormi. Tegelikult ähmastab Ricochet eripärasid, mis võivad ohustada Bitcoin osa asendatavust.



Näiteks kui teete coinjoini, siis tuvastatakse teie osa, mis tuleb segust välja, sellisena. Ahelaanalüüsi tööriistad suudavad tuvastada coinjoin-tehingute paternad ja omistada neist väljuvatele tükkidele sildi. Tegelikult on coinjoin'i eesmärk murda mündi ajaloolised sidemed, kuid selle läbimine coinjoin'ide kaudu jääb tuvastatavaks. Analoogiliselt on see nähtus sarnane teksti krüpteerimisega: kuigi algset teksti ei ole võimalik kasutada selge tekstina, on lihtne tuvastada, et seda on krüpteeritud.



Märgis "coinjoined" võib mõjutada UTXO asendatavust. Reguleeritud üksused, näiteks vahetusplatvormid, võivad keelduda coinjoined UTXO vastu võtmast või isegi nõuda selle omanikult selgitusi, millega kaasneb oht, et teie konto blokeeritakse või raha külmutatakse. Mõnel juhul võib platvorm isegi teatada teie käitumisest riigiasutustele.



Siinkohal tulebki mängu Ricochet-meetod. Rahaühendusest jääva jälje tuhmimiseks teostab Ricochet neli järjestikust tehingut, mille käigus kasutaja kannab oma raha endale üle erinevatel aadressidel. Pärast seda tehingute jada suunab Ricochet tööriist bitcoinid lõpuks nende lõppsihtkohta, näiteks vahetusplatvormile. Eesmärgiks on luua vahemaa esialgse mündiühendustehingu ja lõpliku kulutamistehingu vahel. Sel viisil eeldavad plokiahela analüüsivahendid, et pärast coinjoin'i on tõenäoliselt toimunud omandiõiguse üleminek ja seega ei ole vaja võtta meetmeid emitendi vastu.



![image](assets/fr/01.webp)



Seistes silmitsi Ricochet-meetodiga, võiks arvata, et ahelanalüüsi tarkvara süvendaks oma uurimist üle nelja põrgatuse. Siiski seisavad need platvormid avastamislävendi optimeerimisel dilemma ees. Nad peavad kehtestama lävendi hüpete arvu, mille järel nad aktsepteerivad, et tõenäoliselt on toimunud omanikuvahetus ja et seos varasema ühisliiduga tuleks ignoreerida. Selle künnise kindlaksmääramine on aga riskantne: iga täheldatud hüpete arvu suurenemine suurendab eksponentsiaalselt valepositiivsete leidude hulka, st isikud, kes on ekslikult märgitud coinjoin'is osalejateks, kuigi tegelikult tegi selle operatsiooni keegi teine. See stsenaarium kujutab endast suurt riski nende ettevõtete jaoks, sest valepositiivsed tulemused põhjustavad rahulolematust, mis võib mõjutada kliente konkurentide poole. Pikemas perspektiivis viib liiga ambitsioonikas tuvastamise künnis selleni, et platvorm kaotab rohkem kliente kui tema konkurendid, mis võib ohustada tema elujõulisust. Seetõttu on nende platvormide jaoks keeruline suurendada täheldatud tagasilöökide arvu ja 4 on sageli piisav arv, et nende analüüside vastu võidelda.



Seega **Ricocheti kõige tavalisem kasutusjuhtum tekib siis, kui on vaja varjata varasemat osalemist coinjoinis UTXO-l, mis on teie omanduses.** Ideaalis on kõige parem vältida coinjoini läbinud bitcoinide ülekandmist reguleeritud üksustele. Sellegipoolest pakub Ricochet tõhusat lahendust juhul, kui muud võimalust ei ole, eriti kui on vaja kiiresti likvideerida bitcoinid riiklikus vääringus.



## Kuidas töötab Ricochet Ashigaru puhul?



Ricochet on lihtsalt meetod bitcoinide saatmiseks iseendale, mille leiutasid algselt Samurai Wallet arendajad. Seega on täiesti võimalik Ricochet'i simuleerida käsitsi, ilma et selleks oleks vaja spetsiaalset tööriista. Kuid neile, kes soovivad protsessi automatiseerida ja samal ajal nautida lihvitud tulemust, on hea lahendus Ashigaru rakenduse (mis on Samourai fork) kaudu saadaval olev Ricochet tööriist.



Kuna Ashigaru võtab oma teenuse eest tasu, maksab Ricochet 100 000 sats teenustasu, millele lisandub mining tasu. Seetõttu on selle kasutamine soovitatav suuremate summade ülekandmiseks.



Ashigaru rakendus pakub kahte Ricochet-varianti:





- Tugevdatud rikošett ehk "astmeline tarne", mille eeliseks on Ashigaru teenustasude hajutamine viie järjestikuse tehingu peale. See võimalus tagab ka selle, et iga tehing edastatakse eraldi ajal ja salvestatakse erinevas plokis, jäljendades võimalikult täpselt omaniku vahetuse käitumist. Kuigi see meetod on aeglasem, on see eelistatav neile, kes ei kiirusta, sest see maksimeerib Ricocheti tõhusust, tugevdades selle vastupidavust ahelanalüüsile;





- Klassikaline Ricochet, mis on mõeldud operatsiooni kiireks teostamiseks, edastades kõiki tehinguid vähendatud ajavahemiku jooksul. Seetõttu pakub see meetod vähem konfidentsiaalsust ja vähem vastupidavust analüüsile kui tugevdatud meetod. Seda tuleks kasutada ainult kiireloomuliste saadetiste puhul.



## Kuidas teha Ricochet Ashigarule?



Ashigarul on rikošeti tegemine väga lihtne: lihtsalt aktiveeri vastav valik saatetehingu loomisel. Alustamiseks klõpsake nupule `+`, seejärel nupule `Send` ja valige konto, millelt soovite raha saata.



![Image](assets/fr/02.webp)



Täitke tehingu andmed: saadetav summa ja saaja lõplik aadress pärast Ricochet-hüppeid. Seejärel märkige valik "Ricochet".



![Image](assets/fr/03.webp)



Seejärel saate valida kahe teoorias käsitletud Ricochet-režiimi vahel: kas klassikaline Ricochet, kus kõik tehingud sisalduvad samas plokis, või etapiviisiline edastamine, mis parandab Ricocheti kvaliteeti pikema viivituse hinnaga.



Kui olete oma valiku teinud, vajutage kinnitamiseks ekraani allosas olevale noolele.



![Image](assets/fr/04.webp)



Järgmisel ekraanil näete oma tehingu täielikku kokkuvõtet. Siin saate ka kohandada oma Ricochet-tehingute tasumäärasid vastavalt turutingimustele. Kui kõik on teiega rahul, lohistage rohelist noolt, et allkirjastada ja levitada Ricochet-tehinguid.



![Image](assets/fr/05.webp)



Oodake, kuni erinevad hüpped automaatselt läbi jooksevad.



![Image](assets/fr/06.webp)



Teie tehingud on edukalt edastatud.



![Image](assets/fr/07.webp)



Nüüd oled sa täielikult kursis Ashigaru rakenduses saadaval oleva Ricochet-variandiga. Et minna kaugemale, soovitan teil läbida minu BTC 204 koolituskursus, mis õpetab teile üksikasjalikult, kuidas tugevdada oma onchaini konfidentsiaalsust.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c