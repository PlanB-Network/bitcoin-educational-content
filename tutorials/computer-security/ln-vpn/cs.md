---
name: LN VPN

description: Nastavte LN VPN s Lightningem pro anonymní a na míru přizpůsobené VPN
---

![image](assets/cover.webp)

LN VPN je přizpůsobitelná VPN služba, která přijímá pouze platby přes lightning. Dnes vám ukážu, jak ji používat a zanechávat při prohlížení internetu méně stop.

Existuje mnoho kvalitních poskytovatelů VPN služeb, ale LN VPN vyniká a nemohli jsme si nechat ujít příležitost ji vám představit.

Většina poskytovatelů VPN služeb, jako jsou ProtonVPN a Mullvad, nabízí možnost platby bitcoiny, ale vyžadují vytvoření účtu a zakoupení plánu na delší nebo kratší dobu, což nemusí vyhovovat každému rozpočtu.

LN VPN umožňuje použití VPN na vyžádání již od jedné hodiny díky implementaci plateb bitcoinem přes lightning network. Okamžité a anonymní, platby přes lightning otevírají svět možností pro mikroplatby.

> 💡 Tento průvodce popisuje, jak používat LN VPN z Linux Ubuntu 22.04 LTS systému.

## Předpoklady: Wireguard

Jednoduše řečeno, Wireguard se používá k vytvoření bezpečného tunelu mezi vaším počítačem a vzdáleným serverem, přes který budete prohlížet internet. IP adresa tohoto serveru se bude jevit jako vaše po dobu trvání nájmu, který uzavřete podle tohoto průvodce.

Oficiální průvodce instalací Wireguard: https://www.wireguard.com/install/

```
Instalace Wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Předpoklady: Lightning Bitcoin Peněženka

Pokud ještě nemáte Lightning Bitcoin peněženku, nebojte se, vytvořili jsme pro vás velmi jednoduchý průvodce zde. (sekce LN tutorial vám může pomoci)

## Krok 1: Uzavření nájmu

Na https://lnvpn.com budete muset vybrat zemi výstupní IP adresy VPN tunelu a dobu trvání. Jakmile jsou tyto parametry nastaveny, klikněte na Zaplatit přes lightning.

![image](assets/1.webp)

Zobrazí se lightning faktura a stačí ji naskenovat vaší lightning peněženkou.

Po zaplacení faktury budete muset počkat několik sekund až dvě minuty, než budou vygenerována vaše nastavení konfigurace Wireguard. Pokud to bude trvat trochu déle, nepanikařte, tento postup jsme prováděli desítkykrát a někdy to prostě chvíli trvá.
Na další obrazovce se objeví možnost "Stáhnout jako soubor" a obdržíte svůj konfigurační soubor, který bude mít název ve formátu lnvpn-xx-xx.conf, kde "xx" odpovídá aktuálnímu datu.
![image](assets/2.webp)

## Krok 2: Aktivace tunelu

Nejprve budete muset přejmenovat konfigurační soubor získaný v předchozím kroku, aby byl automaticky rozpoznán Wireguardem.

Přejděte do složky se staženými soubory, ať už v terminálu nebo pomocí průzkumníka souborů, a přejmenujte soubor lnvpn-xx-xx.conf na wg0.conf takto:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

A je to! Tunel je aktivován!

## Krok 3: Ověření

Použijte online službu jako whatismyip k ověření, že vaše veřejná IP adresa je nyní ta z VPN, kterou jste právě aktivovali.

## Krok 4: Deaktivace
Když váš pronájem vyprší, budete muset zablokovat připojení, abyste znovu získali přístup k internetu. Poté můžete kdykoli opakovat kroky 1 až 3, když budete chtít navázat pronájem s LN VPN.
Zablokování tunelu:

```
    $ sudo ip link delete dev wg0
```

A to je vše! Nyní víte, jak používat LN VPN, unikátní VPN službu!