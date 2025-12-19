---
name: Bitcoin Core (Linux)
description: Spuštění vlastního uzlu s Bitcoin core v systému Linux
---

![cover](assets/cover.webp)


## Spuštění vlastního uzlu pomocí Bitcoin core


Úvod do systému Bitcoin a konceptu uzlu doplněný komplexním průvodcem instalací v systému Linux.


Jedním z nejzajímavějších aspektů Bitcoin je možnost spustit program sám a podílet se tak na granulární úrovni na síti a ověřování veřejné transakce Ledger.


Bitcoin je jako projekt s otevřeným zdrojovým kódem volně dostupný a veřejně šířený od roku 2009. Téměř 17 let po svém vzniku je nyní Bitcoin robustní a nezastavitelnou digitální peněžní sítí, která těží ze silného organického síťového efektu. Za své úsilí a vizi si Satoshi Nakamoto zaslouží náš vděk. Mimochodem, whitepaper Bitcoin hostujeme zde na Agora 256 (poznámka: také na univerzitě).


### Stát se vlastní bankou


Provozování vlastního uzlu se stalo pro stoupence étosu Bitcoin zásadní. Aniž byste kohokoli žádali o svolení, je možné stáhnout Blockchain od začátku a ověřit tak všechny transakce od A do Z podle protokolu Bitcoin.


Součástí programu je i vlastní Wallet. Máme tak kontrolu nad transakcemi, které posíláme do zbytku sítě, bez jakéhokoli prostředníka nebo třetí strany. Jste svou vlastní bankou.


Zbytek tohoto článku je proto průvodcem instalací Bitcoin core - nejrozšířenější verze softwaru Bitcoin - konkrétně v distribucích Linuxu kompatibilních s Debianem, jako jsou Ubuntu a Pop!OS. Postupujte podle tohoto průvodce a přibližte se o krok blíže své individuální suverenitě.


## Průvodce instalací Bitcoin core pro Debian/Ubuntu


**Předpoklady**


- Minimálně 6 GB datového úložiště (uzel pruned) - 1 TB datového úložiště (Full node)
- Počítejte s tím, že *Initial Block Download* (IBD) bude trvat nejméně 24 hodin. Tato operace je povinná i pro uzel pruned.
- Povolte pro IBD ~600 GB šířky pásma, a to i pro uzel pruned.


**Poznámka:💡** následující příkazy jsou předdefinovány pro Bitcoin core verze 24.1.


### Stahování a ověřování souborů



- [Stáhnout](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, stejně jako soubory `SHA256SUMS` a `SHA256SUMS.asc` (samozřejmě je třeba stáhnout nejnovější verzi softwaru).



- Otevřete terminál v adresáři, kde jsou umístěny stažené soubory. Příklad: `cd ~/Downloads/`.



- Pomocí příkazu `sha256sum --ignore-missing --check SHA256SUMS` ověřte, zda je kontrolní součet souboru verze uveden v souboru s kontrolním součtem.



- Výstup tohoto příkazu by měl obsahovat název staženého souboru s verzí, za kterým následuje `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Nainstalujte git pomocí příkazu `sudo apt install git`. Poté naklonujte úložiště obsahující klíče PGP signatářů Bitcoin core pomocí příkazu `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Import klíčů PGP všech podepisujících osob pomocí příkazu `gpg --import guix.sigs/builder-keys/*`



- Pomocí příkazu `gpg --verify SHA256SUMS.asc` ověřte, zda je soubor s kontrolním součtem podepsán klíči PGP podepisujících osob.



U každého platného podpisu se zobrazí řádek začínající: `gpg: Dobrý podpis` a další řádek končící: `Primární otisk klíče: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (příklad otisku klíče PGP Pietera Wuilleho).


**Poznámka💡:** není nutné, aby všechny podepisovací klíče vracely "OK". Ve skutečnosti může být nutný pouze jeden. Je na uživateli, aby si určil vlastní práh validace pro ověření PGP.


Varování můžete ignorovat:



- `Tento klíč není certifikován důvěryhodným podpisem!`



- `Neexistuje žádný údaj o tom, že podpis patří majiteli.`


### Instalace grafického modulu Bitcoin core Interface



- V terminálu, stále v adresáři, kde se nachází soubor verze Bitcoin core, použijte příkaz `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` pro rozbalení souborů obsažených v archivu.



- Nainstalujte dříve rozbalené soubory pomocí příkazu `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Nainstalujte potřebné závislosti pomocí příkazu `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Spusťte _bitcoin-qt_ (grafický Bitcoin core Interface) pomocí příkazu `Bitcoin-qt`.



- Chcete-li vybrat uzel pruned, zaškrtněte políčko _Omezit úložiště Blockchain_ a nakonfigurujte limit ukládaných dat:


![welcome](assets/fr/02.webp)


### Závěr části 1: Průvodce instalací


Jakmile je Bitcoin core nainstalován, doporučuje se udržovat jej v provozu co nejvíce, aby přispíval do sítě Bitcoin ověřováním transakcí a předáváním nových bloků ostatním peerům.


Dobrou praxí však zůstává občasné spouštění a synchronizace uzlu, a to i za účelem ověření přijatých a odeslaných transakcí.


![Creation wallet](assets/fr/03.webp)


## Konfigurace Tor pro uzel Bitcoin core


**Poznámka💡:** tato příručka je určena pro Bitcoin core 24.0.1 na distribucích Linux kompatibilních s Ubuntu/Debian.


### Instalace a konfigurace Tor pro Bitcoin core


Nejprve je třeba nainstalovat službu Tor (The Onion Router), síť používanou pro anonymní komunikaci, která nám umožní anonymizovat naše interakce se sítí Bitcoin. Úvodní informace o nástrojích pro ochranu soukromí na internetu, včetně služby Tor, naleznete v našem článku na toto téma.


Chcete-li nainstalovat Tor, otevřete terminál a zadejte `sudo apt -y install tor`. Po dokončení instalace se služba automaticky spustí na pozadí. Zkontrolujte, zda běží správně, příkazem `sudo systemctl status tor`. Odpověď by měla ukázat `Active: active (exited)`. Stisknutím kláves `Ctrl+C` tuto funkci ukončíte.


**Tip:** V každém případě můžete Tor spustit, zastavit nebo restartovat pomocí následujících příkazů v terminálu:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Dále spustíme grafický modul Bitcoin core pomocí příkazu `Bitcoin-qt`. Poté povolíme automatickou funkci softwaru, která směruje naše připojení přes proxy server Tor: _Nastavení > Síť_ a zde zaškrtněte políčka _Connect through SOCKS5 proxy (default proxy)_ a také _Use a separate SOCKS5 proxy to reach peers via Tor onion services_.


![option](assets/fr/04.webp)


Bitcoin core automaticky detekuje, zda je nainstalován Tor, a pokud ano, ve výchozím nastavení vytvoří odchozí spojení s jinými uzly, které také používají Tor, a navíc vytvoří spojení s uzly používajícími sítě IPv4/IPv6 (clearnet).


**Poznámka💡:** chcete-li změnit jazyk zobrazení na francouzštinu, přejděte na kartu Zobrazení v Nastavení.


### Pokročilá konfigurace Tor (volitelné)


Je možné nakonfigurovat Bitcoin core tak, aby ke spojení s vrstevníky používal pouze síť Tor, čímž se optimalizuje anonymita prostřednictvím našeho uzlu. Protože v grafickém prostředí Interface není k dispozici žádná vestavěná funkce, budeme muset ručně vytvořit konfigurační soubor. Přejděte na Nastavení a poté na Možnosti.


![option 2](assets/fr/05.webp)


Zde klikněte na _Otevřít konfigurační soubor_. V textovém souboru `Bitcoin.conf` jednoduše přidejte řádek `onlynet=onion` a soubor uložte. Aby se tento příkaz projevil, je třeba restartovat Bitcoin core.


Poté nakonfigurujeme službu Tor tak, aby Bitcoin core mohl přijímat příchozí spojení prostřednictvím proxy serveru, což umožní ostatním uzlům v síti používat náš uzel ke stahování dat Blockchain, aniž by bylo ohroženo zabezpečení našeho počítače.


V terminálu zadejte `sudo nano /etc/tor/torrc` pro přístup ke konfiguračnímu souboru služby Tor. V tomto souboru vyhledejte řádek `#ControlPort 9051` a odstraňte `#` pro jeho povolení. Nyní do souboru přidejte dva nové řádky:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Chcete-li soubor během ukládání ukončit, stiskněte `Ctrl+X > Y > Enter`. Zpět v terminálu restartujte Tor zadáním příkazu `sudo systemctl restart tor`.


Při této konfiguraci bude moci Bitcoin core navazovat příchozí a odchozí spojení s ostatními uzly v síti pouze prostřednictvím sítě Tor (Onion). Chcete-li to potvrdit, klepněte na kartu _Okno_ a poté na _Peers_.


![Nodes Window](assets/fr/06.webp)


### Další zdroje


Používání pouze sítě Tor (`onlynet=onion`) by vás nakonec mohlo učinit zranitelnými vůči Sybil Attack. Proto někteří doporučují udržovat konfiguraci s více sítěmi, aby se tento typ rizika zmírnil. Kromě toho budou všechna připojení IPv4/IPv6 směrována přes proxy server Tor, jak již bylo uvedeno dříve.


Chcete-li zůstat výhradně v síti Tor a snížit riziko Sybil Attack, můžete do souboru `Bitcoin.conf` přidat Address jiného důvěryhodného uzlu přidáním řádku `addnode=důvěryhodná_adresa.onion`. Tento řádek můžete přidat vícekrát, pokud se chcete připojit k více důvěryhodným uzlům.


Chcete-li zobrazit protokoly uzlu Bitcoin týkající se konkrétně jeho interakce s Tor, přidejte do souboru `Bitcoin.conf` příkaz `debug=tor`. Nyní budete mít příslušné informace o Toru v protokolu ladění, který si můžete zobrazit v okně _Informace_ pomocí tlačítka _Debug File_. Tyto protokoly je také možné zobrazit přímo v terminálu příkazem `bitcoind -debug=tor`.


**Tip💡:** zde je několik zajímavých odkazů:


- [stránka na Wiki vysvětlující Tor a jeho vztah ke Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Generátor konfiguračních souborů Bitcoin core od Jamesona Loppa](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Průvodce konfigurací Toru od Jona Atacka](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Pokud máte nějaké dotazy, neváhejte se o ně podělit s komunitou Agora256. Učíme se společně, abychom byli zítra lepší než dnes!