---
name: Proton rahakott
description: Proton Bitcoini rahakoti paigaldamine ja kasutamine
---
![cover](assets/cover.webp)

Proton on digitaalsele privaatsusele spetsialiseerunud Šveitsi ettevõte, mille asutasid 2014. aastal CERNi teadlased. Proton on tuntud oma avatud lähtekoodiga lahenduste poolest ja pakub mitmeid teenuseid, sealhulgas Proton Mail, Proton VPN ja Proton Drive.

Proton tutvustas hiljuti Proton Wallet'i, avatud lähtekoodiga, isehaldatavat Bitcoini rahakotti, mis on saadaval mobiilirakenduse või veebikliendina, mis on seotud teie Proton-kontoga. Rahakoti funktsioonid on hetkel suhteliselt klassikalised, sisaldades heast Bitcoini rahakotist oodatavaid olulisi vahendeid, nagu RBF (*Replace-By-Fee*), sildistamine või võimalus lisada BIP39 parooli.

Selle rahakoti eripära on võimalus saata bitcoine, kasutades saaja e-posti aadressi, mille jaoks Proton genereerib automaatselt kasutaja rahakotiga seotud tühja Bitcoini aadressi. Proton plaanib tulevikus lisada uusi funktsioone, sealhulgas Lightning ja coinjoins (tõenäoliselt kasutades Whirlpooli, nagu soovitas tegevus nende GitHubi repositooriumis).

## Looge Proton konto

Proton Walleti kasutamiseks on vaja Proton-kontot. Selle saate luua tasuta, järgides selle Proton-postkasti loomisele pühendatud õpetuse esimesi samme (ainult jaotis "*Proton-konto loomine*"). Kui teie konto on loodud, võite jätkata selle õpetuse ülejäänud osaga.

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
## Ühendage Proton Walletiga

Mine [Proton Walleti veebilehele](https://proton.me/wallet) ja klõpsa nupule "*Get Proton Wallet*".

![Image](assets/fr/01.webp)

Valige valik "*Free*", seejärel klõpsake "*Sign In*".

![Image](assets/fr/02.webp)

Sisestamiseks sisestage oma Proton-kontoga seotud e-posti aadress ja parool.

![Image](assets/fr/03.webp)

Nüüd peaks teie konto olema kuvatud. Klõpsake nupule "*Alusta Proton Walleti kasutamist nüüd*".

![Image](assets/fr/04.webp)

## Bitcoini rahakoti loomine

Valige oma konto jaoks vaikimisi fiat-valuuta, seejärel klõpsake "*Loo uus rahakott*".

![Image](assets/fr/05.webp)

Teie Bitcoini rahakott on nüüd loodud. Teoreetiliselt võite seda kohe kasutama hakata, kuid on väga oluline, et salvestaksite kõigepealt oma mnemo. Selleks klõpsake kasutajaliidese paremas ülanurgas nupule "*Turusta oma rahakott*".

![Image](assets/fr/06.webp)

Kui te pole seda veel Protonis teinud, palutakse teil luua oma konto varukoopia ja kaitsta see 2FA-meetodiga. Need turvameetmed kehtivad küll kogu teie Protoni konto suhtes, kuid on seda olulisemad, kui teie Bitcoini rahakott on sellesse integreeritud. Soovitan neid tungivalt rakendada.

![Image](assets/fr/07.webp)

Mälulause salvestamiseks klõpsake nuppu "*Kinnita selle rahakoti seemnefraas*".

![Image](assets/fr/08.webp)

Sisestage oma Proton parool.

![Image](assets/fr/09.webp)

Seejärel klõpsake "*View wallet seed phrase*", et kuvada oma rahakoti mälulause.

![Image](assets/fr/10.webp)

Proton Wallet kuvab teie 12-sõnalist mnemoonilist lauset. **See mnemonüüm annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele**. Igaüks, kes seda fraasi valdab, võib teie raha varastada, isegi ilma juurdepääsuta teie Proton-kontole. 12-sõnalist fraasi saab kasutada oma bitcoinidele juurdepääsu taastamiseks, kui kaotate juurdepääsu oma kontole. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.

Võite kirjutada selle paberile või täiendava turvalisuse tagamiseks soovitan graveerida selle roostevabast terasest alusele, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest.

![Image](assets/fr/11.webp)

Lisateavet selle kohta, kuidas oma mnemofraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
_**Kaasa ei tohiks muidugi kunagi neid sõnu pildistada, erinevalt sellest, mida ma selles õpetuses teen.**_

Kui olete oma lause salvestanud, klõpsake nupule "*Tehtud*".

![Image](assets/fr/12.webp)

## Avasta liides

Proton Walleti kasutajaliides on väga intuitiivne. Vasakult leiate oma erinevad rahakotid ja nendega seotud kontod. "*Primary*" konto on teie põhikonto. Konfidentsiaalsuse huvides paigutatakse Protoni e-posti aadressi kaudu saadud bitcoinid eraldi kontole, mille nimi on "*Bitcoin via Email*".

![Image](assets/fr/13.webp)

Uue konto lisamiseks klõpsake nupule "*Konto lisamine*".

![Image](assets/fr/14.webp)

Uue portfelli loomiseks klõpsake "*+*" sümbolil "*Pangakassad*" kõrval.

![Image](assets/fr/15.webp)

Siin saate lisada uuele rahakotile BIP39 parooli.

![Image](assets/fr/16.webp)

Selleks, et süvendada oma teadmisi salasõna kohta, soovitan seda õpetust:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
## Bitcoinide vastuvõtmine

Bitcoinide vastuvõtmiseks oma rahakotti valige vasakul kasutajaliideses soovitud konto, seejärel klõpsake nupul "*Vaata*".

![Image](assets/fr/17.webp)

Proton Wallet genereerib seejärel automaatselt uue, tühja aadressi.

![Image](assets/fr/18.webp)

Kui tehing on lõpetatud, leiate selle jaotisest "*Tehingud*". Tehingule sildi määramiseks klõpsake nuppu "*+lisada*".

![Image](assets/fr/19.webp)

## Bitcoinide saatmine

Nüüd, kui teil on bitcoinid rahakotis, saate neid saata. Valige kasutajaliidese vasakul poolel valitud konto, seejärel klõpsake "*Saatmine*".

![Image](assets/fr/20.webp)

Sisestage saaja Bitcoini aadress. QR-koodi saate skaneerida, klõpsates väikesel logol. Kui soovite saata e-posti aadressile, sisestage see otse sellele väljale. Kui olete Bitcoini aadressi sisestanud, klõpsake väikesel noolega ja seejärel "*Kinnitage*".

![Image](assets/fr/21.webp)

Sisestage saadetav summa kas fiat-valuutas või bitcoinides ja klõpsake seejärel nupule "*Review*".

![Image](assets/fr/22.webp)

Valige tehingutasu vastavalt hetke turuolukorrale.

![Image](assets/fr/23.webp)

Lisage oma tehingule silt, seejärel kontrollige kõiki üksikasju. Kui kõik on õige, klõpsake "*Kinnitage ja saatke*", et tehing allkirjastada ja saata.

![Image](assets/fr/24.webp)

Teie tehing ilmub nüüd teie konto jaotises "*Tehingud*" ja ootab kinnitust.

![Image](assets/fr/25.webp)

## Sisene rakendusse

Lisaks veebikliendile on Proton Wallet kättesaadav ka mobiilirakenduse kaudu. Kui ühendate rahakoti oma Proton-kontoga, saate oma rahakoti veebikliendi ja mobiilirakenduse vahel sünkroonida.

Laadige Proton Wallet oma rakenduste poest alla:


- [App Store'is](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [Google Play poes](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Pärast paigaldamist klõpsake "*Logi sisse*" ja sisestage oma e-posti aadress ja Proton parool.

![Image](assets/fr/27.webp)

Seejärel on teil juurdepääs oma Bitcoini rahakotile, millel on samad funktsioonid kui veebikliendil.

![Image](assets/fr/28.webp)

Palju õnne, te teate nüüd, kuidas Proton Wallet'i seadistada ja kasutada. Kui leidsid selle õpetuse kasulikuks, oleksin tänulik, kui jätaksid allpool rohelise pöidla. Jaga seda artiklit julgelt oma suhtlusvõrgustikes. Täname jagamise eest!

Et minna edasi, soovitan seda õpetust Jade Plus, Blockstream uusim riistvara rahakott:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262