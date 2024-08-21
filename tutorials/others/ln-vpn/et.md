---
name: LN VPN

description: Seadista oma VPN
---

![pilt](assets/cover.webp)

LN VPN on kohandatav VPN-teenus, mis aktsepteerib ainult välgu makseid. Täna näitan teile, kuidas seda kasutada ja jätta veebis surfates vähem jälgi.

Kvaliteetseid VPN-teenuse pakkujaid on palju ja oleme selles artiklis teinud põhjaliku ülevaate (hyperlink). Siiski paistab LN VPN silma ja me ei saanud kasutamata jätta võimalust seda teile tutvustada.

Enamik VPN-teenuse pakkujaid, nagu ProtonVPN ja Mullvad, pakuvad võimalust maksta bitcoinidega, kuid nõuavad konto loomist ja plaani ostmist pikemaks või lühemaks ajaks, mis ei pruugi sobida kõigi eelarvega.

LN VPN võimaldab nõudmisel VPN-i kasutamist nii lühikeseks ajaks kui üks tund, tänu selle rakendamisele bitcoinide maksete jaoks välguvõrgu kaudu. Kohene ja anonüümne, välgu maksed avavad mikromaksete maailma võimalused.

> 💡 See juhend kirjeldab, kuidas kasutada LN VPN-i Linux Ubuntu 22.04 LTS süsteemis.

## Eeltingimused: Wireguard

Lihtsustatult öeldes kasutatakse Wireguardi turvalise tunneli loomiseks teie arvuti ja kaugserveri vahel, mille kaudu te internetis surfate. Just selle serveri IP-aadress ilmub teie omaks nii kaua, kui te järgite seda juhendit järgides sõlmitud lepingut.

Ametlik Wireguardi paigaldusjuhend: https://www.wireguard.com/install/

```
Wireguardi paigaldamine
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Eeltingimused: Lightning Bitcoin Rahakott

Kui teil pole veel Lightning Bitcoin rahakotti, pole muret, oleme teile siin loonud väga lihtsa juhendi. (LN õpetuste jaotis võib teid aidata)

## 1. samm: Lepingu sõlmimine

Aadressilt https://lnvpn.com peate valima VPN-tunneli väljumise IP riigi ja kestuse. Kui need parameetrid on määratud, klõpsake Maksa välguvõrgu kaudu.

![pilt](assets/1.webp)

Kuvatakse välguarve ja peate selle lihtsalt skaneerima oma välgu rahakotiga.

Kui arve on makstud, peate ootama mõned sekundid kuni kaks minutit, et teie Wireguardi konfiguratsiooni seaded genereeritaks. Kui see võtab veidi kauem aega, ärge paanitsege, oleme seda protseduuri teinud kümneid kordi ja mõnikord lihtsalt võtab see natuke kauem aega.
Järgmine ekraan ilmub ja peate lihtsalt klõpsama "Laadi alla failina", et saada oma konfiguratsioonifail, mille nimi näeb välja nagu lnvpn-xx-xx.conf, kus "xx" vastab praegusele kuupäevale.
![pilt](assets/2.webp)

## 2. samm: Tunneli aktiveerimine

Esmalt peate eelmises etapis saadud konfiguratsioonifaili ümber nimetama, et Wireguard saaks selle automaatselt ära tunda.

Minge oma allalaadimiskausta, kas terminaliaknas või failihalduriga, ja nimetage lnvpn-xx-xx.conf fail ümber wg0.conf-iks nii:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

On tehtud! Tunnel on aktiveeritud!

## 3. samm: Kontrollimine

Kasutage veebiteenust nagu whatismyip, et kontrollida, kas teie avalik IP-aadress on nüüd see, mille just VPN-i kaudu aktiveerisite.

## 4. samm: Keelamine
Kui teie rendiperiood lõppeb, peate ühenduse keelama, et taastada juurdepääs internetile. Seejärel saate korrata samme 1 kuni 3, kui soovite LN VPN-iga uuesti rendilepingu sõlmida.
Tunneli keelamine:

```
    $ sudo ip link delete dev wg0
```

Nüüd teate, kuidas kasutada LN VPN-i, ainulaadset VPN-teenust!