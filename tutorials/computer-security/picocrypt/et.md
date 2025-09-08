---
name: Picocrypt
description: Avatud lähtekoodiga tööriist andmete krüpteerimiseks
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian BURNELi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaalsisu on muudetud.*



___



## I. Esitlus



Selles õpetuses tutvume Picocryptiga, mis on lihtne, kerge ja tõhus krüpteerimistarkvara andmete krüpteerimiseks kõrge turvalisuse tasemega.



Sobib **failide krüpteerimiseks**, saate sellega kaitsta **andmeid arvutis, USB-mälupulgal**, aga ka pilves salvestatud andmeid. Näiteks saate andmeid krüpteerida ja salvestada neid **Microsoft OneDrive'is, Google Drive'is, iCloudis või Dropboxis**, kuigi ma eelistan selleks otstarbeks teist tarkvara, mida tutvustame ühes tulevases artiklis.



Võite seda kasutada ka siis, kui teil on vaja **jagada andmeid kolmanda osapoolega**: tänu Picocryptile ja dekrüpteerimisvõtmele saavad nad oma masinas olevad andmed dekrüpteerida. Nii et kui teie konto või arvuti on ohustatud, on teie andmed kaitstud.



Picocrypt projekti jälgimiseks on ainult üks Address:





- [Picocrypt on GitHub](https://github.com/Picocrypt/Picocrypt)



Täiesti **vaba ja avatud lähtekoodiga**, PicoCrypt on saadaval **Windows, **Linux** ja **macOS** jaoks. Windowsis saate selle paigaldada oma masinasse või kasutada kaasaskantavat versiooni.



## II. Picocrypt, avatud lähtekoodiga krüpteerimistarkvara



Picocrypt** krüpteerimistarkvara on **alternatiiv** teistele tuntud lahendustele, nagu **VeraCrypt** ja **Cryptomator** (*on mõeldud andmete krüpteerimiseks pilvekeskkondades*) või **AxCrypt**. Muide, Picocrypti ametlikul GitHubil on võrdlus mõne konkurendiga:



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

Allikas: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt on **väga kerge**, kaaludes vaid **3 MB**, ja seda ei ole vaja paigaldada: see on **kandjalik rakendus**, mille eeliseks on see, et see ei nõua administraatori õigusi! Siiski ei unusta see turvalisust, kuna tugineb **kindlatele ja usaldusväärsetele algoritmidele**:





- XChaCha20** krüpteerimisalgoritm
- Klahvi ümberlülitusfunktsioon **Argon2**



Lisaks eelistele, mida äsja mainiti, on see, mis tõeliselt meeldib, **kasutamise lihtsus**!



See vajab ainult ühte asja: **koodiaudit**, kuid see on plaanis, nagu näete eespool esitatud võrdlustabelist (viimane rida). Aga kuna see on avatud lähtekoodiga, siis ei takista miski selle lähtekoodi vaatamist.



Kuigi seda võrreldakse ülaltoodud tabelis BitLockeriga, **on minu arvates BitLocker ja Picocrypt mõeldud erinevateks kasutusaladeks**: BitLocker täieliku mahu (näiteks Windowsi) krüpteerimiseks ja Picocrypt puustruktuuri või "Drive"-tüüpi salvestusruumi krüpteerimiseks.



## III. Pikokrüpti kasutamine



Selle demonstratsiooni jaoks kasutatakse Windows 11 masinat.



### A. Andmete krüpteerimine Picocryptiga



Kõigepealt tuleb Picocrypt.exe alla laadida ametlikust GitHubist ([vt seda lehekülge](https://github.com/Picocrypt/Picocrypt/releases)).



Avage rakendus, et kuvada ekraanil selle minimalistlik Interface. Andmete krüpteerimiseks, olgu see siis **fail, mitu faili või kaust**, lihtsalt **liigutage see Picocrypt'i Interface-sse**. See valib krüpteeritavad andmed.



![Image](assets/fr/020.webp)



Seejärel on teil andmete krüpteerimiseks juurdepääs mitmetele valikutele, sealhulgas krüpteerimisvõtmele. See võib olla **tugev parool** või **krüpteerimisvõti võtmefaili kujul** või **kumbki**. Kui võtame näiteks parooli, siis on teil võimalus valida, kas luua oma parool või genereerida see Picocryptiga.



See parool peab olema tugev, sest seda saab kasutada andmete dekrüpteerimiseks. Sisestage see "**Parool**" ja "**Kinnitage parool**", seejärel klõpsake andmete krüpteerimiseks "**Encrypt**"! Enne seda võite klõpsata nupule "**Change**" nupu "**Save output as**" kõrval, et määrata väljundkataloog.



**Märkus**: failiformaadis võtme kasutamiseks klõpsake võtme loomiseks "**Loo**" paremal pool "**Keyfiles**". Seejärel valige see, klõpsates "**Edit**" ja lohistades võtmefaili sobivale alale.



![Image](assets/fr/019.webp)



Kaks valitud faili on **krüpteeritud ja grupeeritud** faili "**Encrypted.zip.pcv**", kuna **PCV** on Picocrypt'i kasutatav laiendus. See ZIP-fail on tänu krüpteerimisele loetamatu. Et valitud faile ei saaks grupeerida ühte krüpteeritud ZIP-faili, tuleb märkida valik "**Rekursiivselt**", nii et krüpteeritud faile oleks nii palju, kui on krüpteeritavaid faile.



Et pääseda ligi meie andmetele, peame need Picocryptiga lahti krüptima.



![Image](assets/fr/023.webp)



Enne kui me räägime andmete dekrüpteerimisest, on siinkohal mõned andmed mõnede olemasolevate võimaluste kohta:





- Paranoiline režiim**: kasutage Picocrypti pakutavat kõrgeimat turvataset. Tööriist kasutab andmete autentimiseks BLAKE2b asemel mitmeid kaskaadkrüpteerimisalgoritme (XChaCha20 ja Serpent) ning HMAC-SHA3.
- Reed-Solomon**: rakendab *Reed-Solomon* veakorrektsioonikoode, et hõlbustada vigastatud andmete veaparandust. See võimaldab teil toetada umbes 3% ulatuses faili vigastust.
- Jagage tükkideks** või **jagage mitmeks osaks**: kui krüpteerite suurt faili, võite paluda Picocryptil jagada see mitmeks osaks. See võib muuta faili ülekandmise lihtsamaks.
- Compress Files** või **Compress files**: failide pakkimine, et vähendada krüpteeritud failide suurust.
- Kustutatud failid** või **Fichiers supprimés**: kustutage lähtefailid, et säilitada ainult krüpteeritud versioon



### B. Andmete dekrüpteerimine Picocryptiga



Kui teil on vaja andmeid dekrüpteerida, ei ole see keerulisem kui krüpteerimine. Lihtsalt avage Picocrypt ja **liigutage dekrüpteeritavat PCV-faili**. Seejärel sisestage parool ja/või valige võtmefail enne klõpsamist "**Decrypt**".



![Image](assets/fr/021.webp)



Krüptimata versioon "Encrypted.zip" ZIP-arhiiv võimaldab mul nüüd taastada minu kaks faili selge tekstiga!



![Image](assets/fr/022.webp)



## IV. Kokkuvõte



**Teid on hoiatatud: Picocrypt on väga lihtne kasutada ja see töötab! Kuigi Interface on minimalistlik, sisaldab see mõningaid väga kasulikke võimalusi krüpteerimise kohandamiseks! Ja kuna see on saadaval kaasaskantava versioonina, saate selle igale poole kaasa võtta, nii et saate oma andmeid kindlalt dekrüpteerida**



Andmete kaitsmiseks kasutage kindlasti tugevaid paroole ja kui kasutate võtmefaili, siis peate meeles pidama, et sellest tuleb teha varukoopia, sest vastasel juhul ei saa te enam Picocrypti poolt loodud PCV konteinerit dekrüpteerida. Lõpuks peaksite teadma, et on olemas ka [CLI versioon](https://github.com/Picocrypt/CLI) (vähemate funktsioonidega), mis võimaldab teil käivitada Picocrypti käsurealt: ka siin avab Picocrypt ukse uutele võimalustele.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5