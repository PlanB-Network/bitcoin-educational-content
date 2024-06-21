---
name: Bitcoin Core Node (linux)
description: Spuštění vlastního uzlu s Bitcoin Core
---

![cover](assets/cover.webp)

# Spuštění vlastního uzlu s Bitcoin Core

Úvod do Bitcoinu a konceptu uzlu, doplněný o komplexní průvodce instalací na Linuxu.

Jednou z nejvíce vzrušujících vlastností Bitcoinu je možnost spustit program sami a tím se na granulární úrovni podílet na síti a ověřování veřejného účetního rejstříku transakcí.

Bitcoin, projekt s otevřeným zdrojovým kódem, je veřejně distribuován a dostupný zdarma od roku 2009. Téměř 15 let od svého vzniku je Bitcoin nyní robustní a nezastavitelnou digitální měnovou sítí, která těží z silného organického síťového efektu. Za jejich úsilí a vizi si Satoshi Nakamoto zaslouží naši vděčnost. Mimochodem, whitepaper Bitcoinu hostujeme zde na Agora 256 (poznámka: také na univerzitě).

## Stát se vlastní bankou

Spuštění vlastního uzlu se stalo nezbytným pro přívržence axiomu Bitcoinu. Bez žádosti o povolení je možné stáhnout blockchain od začátku a tím ověřit všechny transakce od A do Z podle protokolu Bitcoinu.

Program také zahrnuje vlastní peněženku. Tím máme kontrolu nad transakcemi, které posíláme do zbytku sítě, bez jakéhokoli prostředníka nebo třetí strany. Jste vlastní bankou.

Zbytek tohoto článku je tedy průvodcem instalací Bitcoin Core — nejčastěji používané verze softwaru Bitcoin — konkrétně na distribucích Linuxu kompatibilních s Debianem, jako jsou Ubuntu a Pop!_OS. Postupujte podle tohoto průvodce, abyste se přiblížili k vaší individuální suverenitě.

## Průvodce instalací Bitcoin Core pro Debian/Ubuntu

> Předpoklady
>
> - Minimálně 6GB úložného prostoru (prořezaný uzel) — 1TB úložného prostoru (plný uzel)
> - Připravte se, že dokončení počátečního stahování bloků (IBD) zabere alespoň 24 hodin. Tato operace je povinná i pro prořezaný uzel.
> - Připravte přibližně 600GB šířky pásma pro IBD, i pro prořezaný uzel.

> 💡 Následující příkazy jsou předdefinovány pro verzi Bitcoin Core 24.1.

## Stahování a ověřování souborů

1. Stáhněte bitcoin-24.1-x86_64-linux-gnu.tar.gz, stejně jako soubory SHA256SUMS a SHA256SUMS.asc. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Otevřete terminál ve složce, kde jsou stažené soubory umístěny. Např., cd ~/Downloads/.
3. Ověřte, že kontrolní součet verze souboru je uveden v souboru s kontrolními součty pomocí příkazu sha256sum --ignore-missing --check SHA256SUMS.
4. Výstup tohoto příkazu by měl obsahovat název staženého souboru s verzi následovaný "OK". Příklad: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Nainstalujte git pomocí příkazu sudo install git. Poté naklonujte repozitář obsahující PGP klíče podepisovatelů Bitcoin Core pomocí příkazu git clone https://github.com/bitcoin-core/guix.sigs.
6. Importujte PGP klíče všech podepisovatelů pomocí příkazu gpg --import guix.sigs/builder-keys/\*
7. Ověřte, že soubor s kontrolními součty je podepsán PGP klíči podepisovatelů pomocí příkazu gpg --verify SHA256SUMS.asc.
Každý podpis vrátí řádek začínající s: gpg: Good signature a další řádek končící s Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (příklad otisku PGP klíče Pietera Wuille).
> 💡 Není nutné, aby všechny klíče podepisujících vrátily "OK". Ve skutečnosti může být nutný pouze jeden. Je na uživateli, aby určil vlastní prah ověření pro verifikaci PGP.
>
> Můžete ignorovat zprávy WARNING: This key is not certified with a trusted signature!

> Neexistuje žádný důkaz, že podpis patří vlastníkovi.

## Instalace grafického rozhraní Bitcoin Core

1. V terminálu, stále ve složce, kde se nachází soubor s verzí Bitcoin Core, použijte příkaz tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz k extrakci souborů obsažených v archivu.

2. Instalujte dříve extrahované soubory pomocí příkazu sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Instalujte potřebné závislosti pomocí příkazu sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Spusťte bitcoin-qt (grafické rozhraní Bitcoin Core) pomocí příkazu bitcoin-qt.

5. Chcete-li zvolit ořezaný uzel, zaškrtněte Limit blockchain storage a nakonfigurujte limit dat k uložení:

![welcome](assets/1.webp)

## Závěr části 1: Instalační příručka

Jakmile je Bitcoin Core nainstalován, doporučuje se jej nechat běžet co nejčastěji, aby přispíval do sítě Bitcoin ověřováním transakcí a přenášením nových bloků ostatním uzlům.

Nicméně, spouštění a synchronizace vašeho uzlu přerušovaně, i jen pro ověření přijatých a odeslaných transakcí, zůstává dobrou praxí.

![Creation wallet](assets/2.webp)

# Konfigurace Toru pro uzel Bitcoin Core

> 💡 Tento průvodce je určen pro Bitcoin Core 24.0.1 na Linuxových distribucích kompatibilních s Ubuntu/Debian.

## Instalace a konfigurace Toru pro Bitcoin Core

Nejprve potřebujeme nainstalovat službu Tor (The Onion Router), síť používanou pro anonymní komunikaci, která nám umožní anonymizovat naše interakce se sítí Bitcoin. Pro úvod do nástrojů na ochranu soukromí online, včetně Toru, se odkazujte na náš článek na toto téma.

Pro instalaci Toru otevřete terminál a zadejte sudo apt -y install tor. Po dokončení instalace by služba měla být normálně automaticky spuštěna na pozadí. Zkontrolujte, že běží správně s příkazem sudo systemctl status tor. Odpověď by měla ukázat Active: active (exited). Stiskněte Ctrl+C pro ukončení této funkce.

> V každém případě můžete použít následující příkazy v terminálu pro spuštění, zastavení nebo restartování Toru:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Dále spusťme grafické rozhraní Bitcoin Core s příkazem bitcoin-qt. Poté povolme automatickou funkci softwaru pro směrování našich spojení přes Tor proxy: Nastavení > Síť, a odtud můžeme zaškrtnout Connect through SOCKS5 proxy (default proxy) stejně jako Use a separate SOCKS5 proxy to reach peers via Tor onion services.

![option](assets/3.webp)

Bitcoin Core automaticky detekuje, jestli je Tor nainstalován a pokud ano, výchozí nastavení vytvoří odchozí spojení s ostatními uzly také používajícími Tor, kromě spojení s uzly používajícími sítě IPv4/IPv6 (clearnet).
> 💡 Pro změnu jazyka zobrazení na francouzštinu přejděte na kartu Zobrazení v Nastavení.
## Pokročilá konfigurace Tor (volitelné)

Je možné nakonfigurovat Bitcoin Core tak, aby používal pouze síť Tor pro spojení s peerů, čímž optimalizujeme naši anonymitu prostřednictvím našeho uzlu. Jelikož v grafickém rozhraní není pro toto vestavěná funkce, budeme muset ručně vytvořit konfigurační soubor. Přejděte do Nastavení, poté do Možnosti.

![možnost 2](assets/4.webp)

Zde klikněte na Otevřít konfigurační soubor. Jakmile se dostanete do textového souboru bitcoin.conf, jednoduše přidejte řádek onlynet=onion a soubor uložte. Je nutné restartovat Bitcoin Core, aby tento příkaz nabyl účinku.
Poté nakonfigurujeme službu Tor tak, aby Bitcoin Core mohl přijímat příchozí spojení přes proxy, což umožní ostatním uzlům v síti používat náš uzel pro stahování dat blockchainu bez ohrožení bezpečnosti našeho počítače.

V terminálu zadejte sudo nano /etc/tor/torrc pro přístup k souboru konfigurace služby Tor. V tomto souboru hledejte řádek #ControlPort 9051 a odstraňte # pro jeho aktivaci. Nyní přidejte do souboru dva nové řádky: HiddenServiceDir /var/lib/tor/bitcoin-service/ a HiddenServicePort 8333 127.0.0.1:8334. Pro opuštění souboru s jeho uložením stiskněte Ctrl+X > Y > Enter. Zpět v terminálu restartujte Tor zadáním příkazu sudo systemctl restart tor.

S touto konfigurací bude moci Bitcoin Core navazovat příchozí a odchozí spojení s ostatními uzly v síti pouze prostřednictvím sítě Tor (Onion). Pro potvrzení toho klikněte na kartu Okno, poté Peerové.

![Okno uzlů](assets/5.webp)

## Další zdroje

Používání pouze sítě Tor (onlynet=onion) by vás mohlo vystavit riziku Sybilova útoku. Proto někteří doporučují udržovat konfiguraci více sítí, aby se tomuto typu rizika předešlo. Navíc, jakmile je Tor proxy nakonfigurováno, všechna spojení IPv4/IPv6 budou směrována přes Tor proxy, jak bylo dříve uvedeno.

Alternativně, pro zůstání výhradně na síti Tor a minimalizaci rizika Sybilova útoku, můžete do svého souboru bitcoin.conf přidat adresu dalšího důvěryhodného uzlu přidáním řádku addnode=trusted_address.onion. Tento řádek můžete přidat vícekrát, pokud chcete být spojeni s více důvěryhodnými uzly.

Pro zobrazení logů vašeho Bitcoin uzlu specificky souvisejících s jeho interakcí s Tor, přidejte do vašeho souboru bitcoin.conf debug=tor. Nyní budete mít v logu ladění relevantní informace o Tor, které můžete zobrazit v okně Informace s tlačítkem Soubor ladění. Tyto logy je také možné přímo zobrazit v terminálu s příkazem bitcoind -debug=tor.

> 💡 Několik zajímavých odkazů:
>
> - Wiki stránka vysvětlující Tor a jeho vztah k Bitcoinu
> - Generátor konfiguračního souboru Bitcoin Core od Jamesona Loppa
> - Průvodce konfigurací Tor od Jona Atacka

Jak vždy, pokud máte jakékoli otázky, neváhejte je sdílet s komunitou Agora256. Učíme se společně, abychom byli zítra lepší než dnes!