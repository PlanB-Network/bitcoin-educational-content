---
name: Bacca
description: Ledgeri konfigureerimine ilma Ledger Live'i tarkvarata
---
![cover](assets/cover.webp)

Kui kasutate Ledgeri, olete tõenäoliselt avastanud, et peate vähemalt seadme algse konfiguratsiooni jaoks läbima Ledger Live'i tarkvara, et kontrollida selle autentsust ja paigaldada sellele Bitcoini rakendus. Pärast seda konfigureerimist eelistavad paljud bitcoin'i kasutajad siiski Ledger Live'i asemel kasutada spetsiaalset Bitcoini rahakoti haldustarkvara, näiteks Sparrow või Liana. Kuigi Ledger toodab suurepäraseid riistvaralisi rahakotte, mis sisaldavad kiiresti uusimaid Bitcoini funktsioone, ei ole nende tarkvara tingimata kohandatud bitcoin'i kasutajate erivajadustele. Ledger Live sisaldab tõepoolest palju funktsioone, mis on mõeldud altcoinide jaoks, samas kui Bitcoini rahakoti haldamisele pühendatud võimalused on piiratud. Kuid Sparrow ja Liana puhul on (hetkel) probleemiks see, et nad ei võimalda Ledgerile Bitcoini rakendust paigaldada.

Selleks, et vältida Ledger Live'i kasutamist Ledgeri esmase konfigureerimise ajal, võite kasutada Bacca tööriista (või "Ledgeri paigaldaja"). See tarkvara võimaldab teil paigaldada ja uuendada Bitcoini rakendust, kontrollida oma Ledgeri autentsust ja isegi hiljem uuendada seadme püsivara. Bacca on loodud Antoine Poinsot (Darosior), Bitcoin Core'i arendaja Chaincode Labsis, [Revault'i ja Liana] (https://wizardsardine.com/) kaasasutaja ja Pythcoiner.

Selles õpetuses näitan teile, kuidas seda tööriista kasutada, nii et saate lõplikult ilma Ledger Live'i tarkvarata hakkama saada ja siiski Ledgeri seadmeid nautida. See töötab kõigis seadmetes: Nano S Classic, Nano S Plus, Nano X, Flex ja Stax.

---
*Pange tähele, et see tööriist on üsna uus ja selle arendajad täpsustavad, et see on veel **testimisjärgus**. Nad soovitavad seda kasutada ainult testimise eesmärgil ja mitte seadme jaoks, mis on mõeldud tõelise Bitcoini rahakoti majutamiseks, kuigi see on võimalik. Sellega seoses soovitan järgida selle tööriista arendajate soovitusi, mis on täpsustatud [nende GitHubi repositooriumi README-s](https://github.com/darosior/ledger_installer).*

---
## Eeltingimused

Bacca kasutamiseks on teie arvutis vaja kahte tööriista:


- Git ;
- Rooste.

Kui olete need juba paigaldanud, võite selle sammu vahele jätta.

**Linux:**

Linuxi distributsioonis on Git tavaliselt eelinstalleeritud. Et kontrollida, kas Git on teie süsteemi installeeritud, võite sisestada terminali järgmise käsu :

```bash
git --version
```

Kui Git ei ole teie süsteemi installeeritud, on siin käsk selle installeerimiseks Debianis :

```bash
sudo apt install git
```

Lõpuks, et installida oma Rust arenduskeskkonda, kasutage käsku :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**

Giti installimiseks minge [projekti ametlikule veebisaidile](https://git-scm.com/). Laadige tarkvara alla ja järgige paigaldusjuhiseid.

![BACCA](assets/fr/01.webp)

Jätkake samamoodi, et paigaldada Rust [ametlikul veebisaidil](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Kui Git pole veel teie süsteemi paigaldatud, avage terminal ja käivitage selle installimiseks järgmine käsk:

```bash
git --version
```

Kui Git ei ole teie süsteemi paigaldatud, avaneb aken, mis pakub teile Xcode'i installimist, mis sisaldab Git'i. Järgige lihtsalt ekraanil kuvatavaid juhiseid, et jätkata installimist.

Rusti installimiseks käivitage järgmine käsk:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Bacca paigaldus

Avage terminal ja minge kausta, kuhu soovite tarkvara salvestada, seejärel käivitage järgmine käsk:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Navigeerige tarkvarakataloogi:

```bash
cd ledger_installer
```

Seejärel kasutage Cargo projekti kompileerimiseks ja Bacca GUI käivitamiseks:

```bash
cargo run -p ledger_manager_gui
```

Nüüd on teil juurdepääs tarkvaraliidesele.

![BACCA](assets/fr/03.webp)

## Pearaamatu konfigureerimine

Kui teie Ledger on uus, veenduge enne alustamist, et olete seadistanud PIN-koodi ja salvestanud taastamislauset. Nende esialgsete sammude jaoks ei ole teil vaja Ledger Live'i. Lihtsalt ühendage oma Ledger USB-kaabli kaudu, et see saaks voolu. Kui te ei ole kindel, kuidas nende kahe sammuga edasi minna, võite vaadata oma mudelile vastava õpetuse algust:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Bacca kasutamine

Ühendage oma Ledger arvutiga ja vabastage see seatud PIN-koodi abil. Bacca peaks teie Ledgeri automaatselt tuvastama.

![BACCA](assets/fr/04.webp)

Pearaamatu autentsuse kinnitamiseks klõpsake nupule "*Kontrolli*". Jätkamiseks peate oma Ledgeri seadmes ühenduse autoriseerima.

![BACCA](assets/fr/05.webp)

Seejärel teavitab Bacca teid, kas teie Ledger on ehtne. Kui see ei ole, siis näitab see, et seade on kompromiteeritud või et tegemist on võltsinguga. Sellisel juhul lõpetage selle kasutamine kohe.

![BACCA](assets/fr/06.webp)

Menüüs "*rakendused*" saate vaadata oma Ledgeri juba paigaldatud rakenduste nimekirja.

![BACCA](assets/fr/07.webp)

Bitcoini rakenduse installimiseks klõpsake "*Install*", seejärel lubage paigaldus oma Ledgeri.

![BACCA](assets/fr/08.webp)

Rakendus on hästi paigaldatud.

![BACCA](assets/fr/09.webp)

Kui teil ei ole paigaldatud Bitcoini rakenduse uusimat versiooni, kuvab Bacca "*Update*" nupu asemel "*Latest*". Rakenduse uuendamiseks klõpsake lihtsalt sellel nupul.

![BACCA](assets/fr/10.webp)

Nüüd, kui teie Ledger on õigesti konfigureeritud koos Bitcoini rakenduse uusima versiooniga, olete valmis importima ja kasutama oma rahakotti haldustarkvaras nagu Sparrow või Liana, ilma et peaksite läbima Ledger Live'i!

Kui leidsid selle õpetuse kasulikuks, oleksin tänulik, kui jätaksid alla rohelise pöidla. Jaga seda artiklit julgelt oma suhtlusvõrgustikes. Tänan teid väga!

Samuti soovitan vaadata seda GnuPG õpetust, mis selgitab, kuidas kontrollida tarkvara terviklikkust ja autentsust enne selle paigaldamist. See on oluline tava, eriti kui paigaldate portfellihaldustarkvara nagu Liana või Sparrow :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

