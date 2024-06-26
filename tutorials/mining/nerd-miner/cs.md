---
name: Nerdminer
description: Začněte těžit bitcoin s šancí na výhru blízkou 0
---

![obal](assets/cover.webp)

> Nastavení vašeho NerdMiner_v2

V tomto návodu vás provedeme nezbytnými kroky k nastavení NerdMiner_v2, což je hardwarové zařízení (ESP-32 S3) určené pro těžbu bitcoinů.
Samozřejmě, výpočetní výkon takového zařízení nemůže konkurovat ASICům amatérských nebo profesionálních těžařů. Přesto je NerdMiner perfektním vzdělávacím nástrojem, který zpřístupňuje těžbu bitcoinů. A kdo ví, s (velkým) štěstím, můžete najít blok a odměnu, která k němu patří. Pro zvídavé se podíváme v sekci [Odhad pravděpodobnosti výhry](#estimation-de-la-probabilite-de-gain). Pokud jde o spotřebu energie, NerdMiner spotřebuje 0,5W; pro srovnání, LED lampa spotřebuje v průměru 20krát více.

Než projdeme různými kroky, pojďme si vypsat potřebné vybavení:

- [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- [USB-C napájecí zdroj](https://amzn.eu/d/gIOot90)
- 3D pouzdro: pokud máte 3D tiskárnu, můžete si stáhnout [3D soubor](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons), jinak si jej můžete koupit v [online obchodě Silexperience](https://silexperience.company.site/NerdMiner_V2-p544379757).
- PC s nainstalovaným prohlížečem Chrome
- internetové připojení
- bitcoinová adresa

Také si můžete koupit předem sestavený kit NerdMiner od několika prodejců, jako jsou:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Nejprve se podíváme, jak nahrát software do ESP-32 S3, a poté uvidíme, jak jej restartovat pro změnu wifi sítě. Tyto kroky jsou pro uživatele Windows, pokud používáte Linux OS, prosím, proveďte [předběžné kroky](#etapes-preliminaires-pour-utilisateurs-linux) pro rozpoznání ESP-32 S3 vaším systémem.

# Instalace softwaru NerdMiner_v2

Instalace softwaru je velmi zjednodušena díky použití webflasheru.

## Krok 1: Příprava webflasheru

Nejprve musíte jít na [online NM2 flasher](https://bitmaker-hub.github.io/diyflasher/).

Poté vyberte firmware odpovídající vašemu ESP-32. Většinou je to výchozí: T-Display S3. Poté klikněte na "Flash".

> ⚠️ Je důležité, abyste používali prohlížeč Chrome - umožňuje standardně použití flash a přístup k vašim USB portům.

![](assets/webflasher.webp)

## Krok 2: Připojení ESP-32

Jakmile je webflasher spuštěn, otevře se vyskakovací okno zobrazující různé USB porty rozpoznané prohlížečem.
Poté můžete připojit váš ESP-32 a zobrazí se nový port (v tomto případě je to port ttyACM0). Musíte ho vybrat a kliknout na "připojit".
![](assets/flasher-port-serial.webp)

Software bude poté do vašeho ESP32 stažen během několika sekund.

![](assets/NM2-sucessfully-installed.webp)

## Krok 3: Konfigurace NerdMiner

Konfigurace vašeho NerdMineru bude provedena prostřednictvím smartphonu nebo počítače.
Povolte WiFi a připojte se k lokální síti NerdMinerAP. Pokud používáte smartphone, konfigurační portál se otevře automaticky. V opačném případě zadejte do prohlížeče adresu 192.168.4.1.
Poté vyberte "Konfigurovat WiFi".

Nyní můžete konfigurovat svůj NerdMiner.
Nejprve se připojte k vaší WiFi síti výběrem názvu vaší sítě a zadáním příslušného hesla.

Poté si můžete vybrat těžební pool, ve kterém chcete participovat. Je běžné, že v průmyslu těžby bitcoinů se výpočetní výkon spojuje za účelem zvýšení šancí na nalezení bloku výměnou za sdílení odměny proporcionálně k poskytnutému hashrate.
Pro NerdMinery si můžete vybrat připojení k jednomu z těchto poolů:

| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Výchozí Solo a open-source těžební pool  |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Udržován CHMEX                           |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Udržován djerfy                          |

Jakmile si vyberete svůj pool, musíte zadat svou bitcoinovou adresu pro příjem odměny v případě (výjimečně) nalezení bloku.

Také si vyberte svou časovou zónu, aby NerdMiner mohl správně zobrazovat čas.
Nyní můžete kliknout na "uložit".

![](assets/wifi-configuration.webp)

Gratulujeme, nyní jste součástí sítě těžby Bitcoinů!

## Provoz NerdMiner

Software NerdMinerv2 má 3 různé obrazovky, ke kterým můžete přistupovat kliknutím na horní tlačítko na pravé straně obrazovky:

- Hlavní obrazovka poskytuje přístup k statistikám vašeho NerdMineru.
- Druhá obrazovka poskytuje přístup k času, vašemu hashrate, ceně bitcoinu a výšce bloku.
- Třetí obrazovka poskytuje přístup k statistikám celosvětové sítě těžby bitcoinů.
  ![](assets/NM2-screens.webp)

Pokud chcete restartovat svůj NerdMiner, například kvůli změně WiFi sítě, musíte stisknout horní tlačítko na 5 sekund.

Stisknutím spodního tlačítka jednou vypnete svůj NerdMiner. Dvojité kliknutí otočí orientaci obrazovky.

### Předběžné kroky pro uživatele Linuxu

Zde jsou kroky, aby Chrome detekoval váš sériový port na Linuxu.

1. Identifikujte přidružený port:

- Připojte váš ESP-32 k počítači.
- Otevřete terminál.
- Zadejte následující příkaz pro výpis všech portů:
  - `dmesg | grep tty`
  - nebo `ls /dev/tty*`
- Aby jste si byli jisti portem, můžete postupovat eliminací opakováním příkazu bez připojeného ESP-32.

2. Změňte oprávnění přidruženého portu:
- Ve výchozím nastavení může vyžadovat přístup k sériovým portům oprávnění root, takže je uděláme dostupnými přidáním vašeho uživatele do skupiny `dialout`.
  - `sudo usermod -a -G dialout VAŠE_UŽIVATELSKÉ_JMÉNO`, nahraďte `VAŠE_UŽIVATELSKÉ_JMÉNO` vaším uživatelským jménem.
  - poté se odhlaste a znovu přihlaste jako tento uživatel, nebo restartujte systém, aby se změny ve skupině projevily.

Nyní, když je váš ESP-32 rozpoznán vaším systémem, můžete se vrátit k [prvnímu kroku](#etape-1-preparation-du-webflasher) pro instalaci softwaru.

## Závěr

A máte to! Váš NerdMiner_v2 je nyní nakonfigurován a připraven k použití.

Šťastný těžení a ať je štěstí na vaší straně!

### Odhad pravděpodobnosti výhry

Pojďme se trochu pobavit odhadem pravděpodobnosti výhry blokové odměny. Tento odhad bude hrubý a snaží se získat pouze řádovou velikost pravděpodobnosti.
Pool, ke kterému se může NerdMiner připojit, jsou pouze "solo mining pool", což znamená, že pool nesdružuje hashrate všech připojených těžařů, ale jednoduše funguje jako koordinátor.
Nyní předpokládejme, že náš NerdMiner má hashrate přibližně 45kH/s.

Vědě, že celkový hashrate je přibližně 450 EH/s (nebo 4,5 x 10^20 hashů za sekundu), můžeme uvažovat, že pravděpodobnost nalezení dalšího bloku je 1 ze 100 milionů miliard, což je velmi velmi velmi nepravděpodobné. Takže kromě toho, že je NerdMiner vzdělávacím nástrojem a předmětem zvědavosti, může sloužit jako los v bitcoinové těžbě za okrajovou elektrickou cenu 0,5 W - i když, jak jsme právě viděli, pravděpodobnost výhry je směšně nízká. Přesto, proč nevyzvat své štěstí?

### Další informace

Zde jsou odkazy, pokud chcete o tématu zjistit více:

- [Stránka projektu NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Kompletní dokumentace NerdMinerů](https://docs.bitwater.ch/nerd-miner-v2/)