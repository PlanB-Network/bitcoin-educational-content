---
name: Lightning Smoke Machine
description: Spusťte kouřový automat pomocí platby Lightning přes ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Úvod



Přemění klasický kouřový stroj na zařízení, které lze platit v Bitcoin prostřednictvím Lightning Network. Každá platba automaticky spustí proud kouře!





- Úroveň: Středně pokročilý
- Předpokládaná doba: 2-3 hodiny
- Případy použití: Události Bitcoin, umělecká vystoupení, předváděcí akce Lightning, automatické pódiové efekty



## Předpoklady



### Znalosti





 - Základy elektroniky (zapojení, relé)
 - Svařování (nebo použití konektorů Dupont)
 - Konfigurace sítě (WiFi, WebSocket)



### Požadované účty





- Server BTCPay: Funkční instance (vlastní nebo hostovaná)
- Blink Wallet : Účet + přístup API



### Přístup na





- Přístup správce k serveru BTCPay
- Připojení WiFi pro ESP32



## Požadované materiály



### Hardware - Elektronické součástky





- 1 mikrokontrolér - ESP32-WROOM-32


*ESP32-WROOM-32 je kompaktní, levný mikrokontrolér WiFi/Bluetooth pro připojení elektronických zařízení k internetu a jejich vzdálené ovládání*



![ESP32](assets/fr/1.webp)





- 1 reléový modul - 5V s optočlenem


*Relé je jako spínač, kterým může ESP32 zapínat nebo vypínat kouřové zařízení*



![relay](assets/fr/2.webp)





- ~10 kabelů Dupont - samec/samec a samec/samice



![dupont-cables](assets/fr/3.webp)





- 1 Napájení pro ESP32 - 5V USB nebo Li-Po baterie



![battery](assets/fr/4.webp)





- 1 kabel micro-USB - propojení mezi ESP32 a zdrojem napájení



![micro-usb-cables](assets/fr/5.webp)





- 1 mlhový stroj na 220 V s dálkovým ovládáním na 12V baterii



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 lahvička kapaliny kompatibilní s vaším kouřovým zařízením



### Hardware - Nástroje





- Páječka + cín (pokud pájíte)
- Šroubovák
- Multimetr (doporučeno)



### Software





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Webový prohlížeč kompatibilní s WebSerial (Chrome/Edge/Brave)
- Konfigurace serveru BTCPay. Další informace o vytvoření instance BTCPay Serveru naleznete v tomto návodu: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Architektura systému



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **BEZPEČNOSTNÍ UPOZORNĚNÍ - PŘED POKRAČOVÁNÍM ČTĚTE** **⚠️**



Tento projekt zahrnuje mlhovač připojený k **220V síti**. Nesprávná obsluha může mít za následek **smrtelný úraz elektrickým proudem** nebo **požár**.



**Nezávazná pravidla:**



1. **VŽDY před otevřením dálkového ovladače nebo zásahem do kabeláže odpojte kouřostroj od elektrické sítě**


2. **Před manipulací vyjměte baterii z dálkového ovladače** (nebezpečí zkratu a poškození součástí)


3. **Před opětovným připojením zkontrolujte, zda jsou všechna připojení izolována**


4. ** Nikdy znovu nepřipojujte 220V**, dokud není skříňka dálkového ovládání uzavřena a zajištěna



Pokud se na takovou manipulaci necítíte, vezměte s sebou někoho, kdo se na ni cítí.



---

## ČÁST 1: Montáž hardwaru



### Krok 1: Příprava dálkového ovládání



Cíl: Připojte relé k tlačítku ON/OFF na dálkovém ovladači


1. Otevření dálkového ovládání




    - Identifikace tlačítka ON/OFF
    - Odšroubujte pouzdro a otevřete dálkový ovladač


2. Vyhledání připojení




 - Najděte svorky + a - na kabelu
 - Zkontrolujte spojitost pomocí multimetru (volitelně)



![smoke-machine-remote](assets/fr/8.webp)



3. Zapojení tlačítek (pájka nebo konektory)




    - Připájejte černý kabel ke svorce - tlačítka
    - Připájejte červený kabel ke společné svorce +



![smoke-machine-remote](assets/fr/9.webp)



### Krok 2: Připojení k reléovému modulu



**Připomínka: Terminologie relé



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Zapojení dálkového ovládání do reléového modulu:**




- Černý vodič od tlačítka ON/OFF **→** NO (normálně otevřený)
- Červený vodič (společný) **→** COM (společný)



**Logika:**


Když ESP32 aktivuje relé, propojí COM a NO, což je přesně totéž jako stisknutí tlačítka dálkového ovládání.


Když ESP32 přeruší relé, COM a NO se oddělí, což odpovídá uvolnění tlačítka.



![remote-relay](assets/fr/10.webp)



### Krok 3: Připojení ESP32 k reléovému modulu



**Schéma zapojení:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Ověřování:**




- VCC a GND jsou dobře propojeny (polarita)
- GPIO 21 slouží pro řídicí signál
- Žádný viditelný zkrat



![relay-esp32](assets/fr/11.webp)



**Kontrolní bod Hardware**


Před přepnutím na software zkontrolujte :




- Správně zapojené dálkové ovládání
- Reléový modul připojený k ESP32
- Žádné holé vodiče se nedotýkají jiných součástí
- 220V vždy odpojeno



![relay-esp32](assets/fr/12.webp)





---


## ČÁST 2: Konfigurace softwaru



Jako příklad použijeme *Blink*, ale pokud dáváte přednost jiné možnosti, *BTCPay Server* nabízí také *Strike, Breez a Boltz*.



### Krok 1: Pluginy, instalace *BitcoinSwitch* + *Blink



1 - Přejděte do instance *BTCPay Server* s účtem správce



2 - Vytvoření první rolety



3 - Na levé straně *BTCPay Serveru* přejděte dolů a přejděte na *"Spravovat zásuvné moduly "*



![btcpay-plugins](assets/fr/13.webp)



4 - Nainstalujeme pluginy *BitcoinSwitch* a *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Přejděte dolů na seznam zásuvných modulů a klikněte na *"Instalovat "* : *BitcoinSwitch a Blink* (nebo dostupný wallet podle vašeho výběru)



![btcpay-plugins](assets/fr/15.webp)



6 - Po dokončení instalace restartujte *BTCPay Server* a počkejte 1 minutu, než se instance restartuje



![btcpay-plugins](assets/fr/16.webp)



7 - Po návratu do *"Správa zásuvných modulů "* zkontrolujte, zda byly oba zásuvné moduly nainstalovány



![btcpay-plugins](assets/fr/17.webp)



### Krok 2: Konfigurace backendu: *BTCPay Server + Blink*



**1 - Vytvoření modelu wallet *Blink***




- Navštivte https://www.blink.sv
- Vytvořte si účet. Podívejte se na návod :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Generování klíče API *Blink***




- Přístup k rozhraní API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** a přihlaste se pod stejným účtem, který jste použili při vytváření wallet *Blink*



![blink-api](assets/fr/18.webp)





   - Po připojení přejděte na kartu *API Keys*



![blink-api](assets/fr/19.webp)





   - Klikněte na *" + "* v pravém horním rohu pro přístup ke konfiguraci klíče API



![blink-api](assets/fr/20.webp)





   - Dejte klíči API název a ponechte výchozí nastavení. Poté si ve třetím kroku poznamenejte svůj klíč API - uvidíte jej pouze jednou: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Po vytvoření by se měl objevit v aktivním seznamu klíčů API.



![blink-api](assets/fr/22.webp)



**3 - Připojení *Blink* k *BTCPay serveru***




- Otevřete svůj *BTCPay server*
- Přejděte na : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Klikněte na *Použít vlastní uzel*
- Vložte následující připojovací řetězec:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Důležité** :




- První část neupravujte: `type=blink;server=https://api.blink.sv/graphql`;
- Vyměňte pouze :
    - api-key= *podle vašeho klíče API Blink*
    - wallet-id= *podle vašeho wallet Blink* ID
- Poté klikněte na *Test připojení* a poté na *Uložit*



![btcpay-server](assets/fr/24.webp)





 - Zkontrolujte, zda je spojení navázáno (zelený stav)



![btcpay-server](assets/fr/25.webp)



**4 - Vytvoření prodejního místa (PoS)**




- Na serveru BTCPay přejděte na kartu *Plugins* a klikněte na *Point of sale*



![btcpay-server](assets/fr/26.webp)





- Pojmenujte svůj PoS a klikněte na *Vytvořit*



![btcpay-server](assets/fr/27.webp)





- Konfigurace PoS :
    - Zvolte styl prodejního místa = *Tiskové zobrazení*
    - Měna = *SATS*
    - Klikněte na *Uložit*



![btcpay-server](assets/fr/28.webp)





- Konfigurace výrobku :
    - Odstranění všech výchozích produktů
    - Pak klikněte na *přidat položku*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Konfigurace produktu:
    - Název : *kouřový stroj*
    - Cena : *10 sats*
    - Bitcoin Přepínač GPIO : 21
    - Doba trvání přepínače Bitcoin (v milisekundách) : 5000
    - Kliknutím na *Zavřít* a poté na *Uložit* uložte nový produkt



![btcpay-server](assets/fr/31.webp)



### Krok 3: Firmware: Flashování ESP32



**1 - Přejít na stránku flash




- Přejít na : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash firmware BitcoinSwitch**




- Připojte ESP32 k počítači pomocí kabelu USB/Micro-USB
- Pak klikněte na *Připojit k zařízení*
- Otevře se okno, vyberte port USB na vašem ESP32 a klikněte na *Připojit*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Po připojení ESP32 provedeme flashování firmwaru BitcoinSwitch. V sekci *T-Display* klikněte na *Upload Firmware* pro nejnovější dostupnou verzi (aktuálně: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Počkejte na odeslání, proces je dokončen, když se v protokolech zobrazí *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Odpojení ESP32



**3 - Zkontrolujte instalaci firmwaru BitcoinSwitch




- Znovu načíst stránku: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Znovu připojte ESP32 k počítači pomocí kabelu USB/Micro-USB
- Pak klikněte na *Připojit k zařízení
- Vyberte port USB na vašem ESP32 a klikněte na *Připojit*, jak je popsáno výše
- Po připojení stiskněte tlačítko **RESET** na ESP32
- Zkontrolujte v protokolech, zda se v posledních řádcích zobrazuje :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(To je normální, znamená to, že zatím není k dispozici konfigurace, ale že firmware byl nainstalován.)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Generování adresy URL WebSocket LNURL**



Očekávaný konečný formát :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Kroky generování :




- Otevřete instanci serveruBTCPay a přejděte do PoS, kterou jsme vytvořili později.
- Poté klikněte na "Zobrazit" a otevřete PoS v prohlížeči



![btcpay-server-https](assets/fr/37.webp)





- Zkopírujte adresu URL stránky, například :



![btcpay-server-https](assets/fr/38.webp)



Rozbalme tuto adresu URL:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → doména vaší instance BTCPay Serveru
- `46XXXXXXXXXXXXXXXXXXXXwFB` → váš jedinečný identifikátor PoS
- `/pos` → označuje prodejní místo



Přeměňte ji:




- Nahraďte `https://` za `wss://`
- Na konec přidejte `/bitcoinswitch`



Výsledek:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Tuto adresu URL si ponechte pro budoucí konfiguraci, protože umožní vašemu ESP32 komunikovat v reálném čase se serverem BTCPay. Protokol WebSocket (`wss://`) vytváří mezi nimi trvalé spojení: jakmile je na vašem PoS potvrzena platba Lightning, BTCPay okamžitě odešle informaci do ESP32, který pak může spustit váš kouřový automat.



**5 - Konfigurace WiFi a WebSocket




- Zpět na stránku: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) s připojeným ESP32
- Přejděte na *Konfigurace zařízení* → *Nastavení Wi-Fi*



Informovat :




- SSID WiFi: název vaší sítě WiFi
- Heslo WiFi: vaše heslo WiFi



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Do části *LNbits Device URL* vložte adresu WebSocket URL vytvořenou v předchozím kroku
- Klikněte na *Nahrát konfiguraci*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Počkejte na dokončení nahrávání; v protokolech by se měly zobrazit právě zadané parametry (SSID, heslo a adresa URL WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Počkejte, než ESP32 naváže spojení WebSocket. Měli byste vidět :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Nyní můžete odpojit ESP32



---
## Checkpoint Software



Před závěrečným testem zkontrolujte :





- Blink připojený k BTCPay
- PoS vytvořená s alespoň 1 položkou
- ESP32 flashnutý pomocí BitcoinSwitch
- Konfigurace WiFi na ESP32
- Správná adresa URL WebSocket
- Protokoly ESP32 bez chyb



---

## Testování a ladění



### Dokončení závěrečného testu



1. Zapojte udírnu (220 V) a zapněte ji


2. Napájení ESP32 (baterie nebo USB)


3. Otevřete svůj BTCPay PoS v prohlížeči


4. Skenování položky "smoke-machine"


5. Platba pomocí blesku wallet (Blink nebo jiného wallet)


6. Pozorujte:




 - Relé cvakne (slyšitelný zvuk a rozsvítí se kontrolka LED relé)
 - Kouřový stroj je aktivován
 - Vzniká kouř!



### Problémy a řešení spravedlnosti



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Zdroje



### Užitečné odkazy





- Firmware BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Dokumenty serveru BTCPay : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- Rozvržení vývodů ESP32 : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Komunita a podpora





- Server BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Official Mattermost
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Oficiální Telegram, aktivní komunita
- BitcoinSwitch (chyby firmwaru)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Zdrojový kód





- Zdrojový kód firmwaru BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Stack sats, make smoke, have fun, stay humble! **⚡**