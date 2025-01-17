---
name: Ledger Nano S

description: Jak nastavit vaše zařízení Ledger Nano S
---

![image](assets/cover.webp)

Fyzická peněženka pro chladné uchování – 60 € – Začátečník – Pro zabezpečení od 2 000 € do 50 000 €

Ledger je francouzské řešení pro jednoduché zabezpečení bitcoinů.

V tomto návodu také diskutujeme o sekci s heslovými frázemi, pokročilém bezpečnostním řešení pro uchovávání velkých částek: 20 000 € – 100 000 €.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Připojení Ledgeru k Sparrow Bitcoin Wallet (průvodce nastavením)

Nejprve se ujistěte, že jste prošli dalším článkem „Používání hardwarových peněženek pro Bitcoin“. Některé kroky zde budu probírat jen stručně a zaměřím se především na to, co je specifické pro Ledger.

## Nastavení zařízení

Ledger je dodáván s vlastním USB kabelem. Ujistěte se, že používáte právě tento a ne jen nějaký starý kabel. Některé USB kabely slouží pouze k napájení. Tento přenáší data I napájení. Když jsem zařízení používal s USB kabelem na nabíjení telefonu, který jsem měl po ruce, zařízení se nepodařilo připojit.

Připojte jej k počítači a zařízení se zapne.

![image](assets/1.webp)

Procházejte možnostmi. Uvidíte

1. Nastavit jako nové zařízení
2. Obnovit z obnovovací fráze

V podstatě se vás ptá, jestli chcete, aby zařízení pro vás vytvořilo seed, nebo jestli už máte vlastní, který byste chtěli použít. Nejlepší praxí je vytvořit si vlastní seed, ale bezpečné to udělat je velmi pokročilé a vybočuje z rozsahu tohoto článku. Vyberte „Nastavit jako nové zařízení“

Poté budete vyzváni k výběru PINu. Tento PIN není součástí vašeho Bitcoin seedu a je specifický pouze pro toto zařízení. Zařízení tímto uzamknete.

Poté se vám zobrazí 24 slov, která musíte projít a zapsat.

Zvláštní je, že když dojdete na konec, řekne „stiskněte vlevo pro ověření vašich slov“. To nevysvětluje, jak potvrdit pokračování, znamená to jen, že se můžete vrátit a slova znovu prohlédnout. Místo toho stiskněte vpravo a potvrďte stiskem vlevo a vpravo současně.

Další část je opravdu otravná. Zamíchá 24 slovy a musíte potvrdit každé z nich, od 1 do 24, procházením všech slov pro každý výběr. Jakmile skončíte, umožní vám to potvrdit stiskem obou tlačítek a pokračovat.

![image](assets/2.webp)

Na vašem řídicím panelu uvidíte tlačítko nastavení a tlačítko s pluskem, které umožňuje instalovat aplikace. Ale nejprve se musíte připojit k Ledger Live. To uděláme následující…

## Stáhnout Ledger Live

Ledger Live si můžete stáhnout z jejich webové stránky, ale lepší je získat jej z GitHubu, kde je uložen zdrojový kód.

Google „ledger live GitHub“ nebo klikněte na tento odkaz https://github.com/LedgerHQ/ledger-live-desktop

![image](assets/3.webp)

Rolujte dolů, dokud neuvidíte nadpis „Downloads“…

![image](assets/4.webp)

Dole uvidíte odkaz: Návod na ověření hash a podpisů instalačních balíčků je k dispozici na této stránce. Klikněte na tento odkaz.(https://live.ledger.tools/lld-signatures)

![image](assets/5.webp)

Nahoře jsou odkazy na software, který potřebujete, v závislosti na vašem operačním systému. Klikněte na ten, který potřebujete, a stáhněte.

Dále chceme ověřit hash staženého souboru pro extra zabezpečení.
Ledger zveřejňuje hash každého ze souborů dostupných na této stránce. Nyní zahashujeme stažený soubor a porovnáme výstup. Musí být identický, abychom si byli jisti, že soubor nebyl pozměněn.

Otevřete terminál na Macu nebo CMD na Windows. Postupujte podle těchto příkazů…

cd Downloads

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Pro Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Pro Windows
```

<Enter>

Doufejme, že je zřejmé, že příkazy začínají za šipkami. Ujistěte se, že pokud je tento článek zastaralý, změníte název souboru v příkazech přesně na název souboru, který jste stáhli. Po každém příkazu musíte stisknout klávesu <Enter>. Příkazy, jak jsou zde vidět, nemusí na jedné řádce ve vašem webovém prohlížeči vejít. Poznámka, vše je napsáno na jedné řádce.

Podívejte se na výstup hash a ujistěte se, že je identický s tím, který byl zveřejněn na GitHubu.

Ideálně byste chtěli být ještě důkladnější a ujistit se, že zveřejněné hashe nejsou falešné. Děláme to pomocí gpg podpisů, ale to je mimo rozsah tohoto článku. Pokud se o tom chcete dozvědět (a doporučuji, abyste to nakonec udělali), pak si projděte tento článek.

## Připojení k Ledger Live

Před spuštěním Ledger Live pomůže soukromí trochu zapnout VPN. Ledger stále získá všechny vaše adresy, ale nebudou znát vaši IP adresu, která prozradí vaši domácí adresu. Mullvad VPN je vynikající VPN služba a není velmi drahá (neudělám reklamu, jen to používám).

Nainstalujte software na svůj počítač a spusťte ho.

![image](assets/6.webp)

Vyberte své zařízení a vyberte "Poprvé používám…"

![image](assets/7.webp)

Poté budete provedeni průvodcem, ale my jsme tyto kroky již provedli, takže můžete postupovat dál.

![image](assets/8.webp)

Po mnoha krocích a kvízu se ověří, že zařízení je pravé. Musíte se ujistit, že jste připojeni a zadali PIN, a poté se na zařízení zeptá, zda dovolíte Ledger Live se připojit. To samozřejmě musíte potvrdit.

![image](assets/9.webp)

V dalším vyskakovacím okně byla nějaká reklama na shitcoin přestrojená za "poznámky k vydání". Zavřete ji a poté byste měli dostat tento obrazovku.

![image](assets/10.webp)

Musíte kliknout na "Přidat účet", abyste získali Bitcoinovou peněženku.

![image](assets/11.webp)

Ujistěte se, že vyberete Bitcoin, a ne Bitcoin Cash nebo jakýkoliv jiný shitcoin. Zařízení se zkontroluje a musíte potvrdit pokračování NA ZAŘÍZENÍ. Adresy se budou počítat několik minut. Poté klikněte na DOKONČENO.

![image](assets/12.webp)
![image](assets/13.webp)

Skvělé. Nyní máte na svém počítači správce peněženek pro shitcoiny obsahující Bitcoinovou peněženku. Ve skutečnosti to už nepotřebujete a můžete se toho zbavit. Skutečným účelem bylo získat Bitcoinovou aplikaci přímo na zařízení, a to byl jediný způsob, jak toho dosáhnout, kromě použití nějakých extrémních softwarových inženýrských technik.

Pamatujte, že jsme dříve na zařízení měli tlačítko nastavení a tlačítko s pluskem. Nyní máme další tlačítko - tlačítko Bitcoinové aplikace.

Nyní můžete Ledger Live vypnout.

## Přidání heslové fráze
Nyní, když máme Bitcoin aplikaci, můžeme k naší seed frázi přidat heslovou frázi. Dříve, když byla seed fráze poprvé vytvořena, to nešlo, protože jsme na začátku neměli Bitcoin aplikaci a museli jsme se připojit k Ledger Live, abychom ji získali.
Přejděte v zařízení do menu „nastavení“, poté do podmenu „bezpečnost“. Poté vyberte heslovou frázi. Uvidíte „Pokročilá funkce“. Klikněte na pravé tlačítko, uvidíte „přečtěte si manuál...“ a poté po kliknutí na pravé tlačítko uvidíte „zpět“. Ale to není konec. Intuitivně byste si mysleli, že ano, ale klikněte znovu na pravé tlačítko. Uvidíte „nastavit heslovou frázi“.

Můžete se rozhodnout „připojit k PINu“ nebo „Nastavit dočasně“. Doporučuji „připojit k PINu“. Tímto způsobem můžete přistupovat k různým peněženkám v závislosti na PINu, který zadáte při prvním zapnutí zařízení. Pokud „nastavíte dočasně“, budete muset heslovou frázi zadávat pokaždé, když budete chtít přistupovat k této peněžence, ale vždy to bude z výchozího PINu.

Zadejte heslovou frázi a potvrďte ji.

Zařízení vás požádá o „Aktuální PIN“. To není PIN, který spojujete s novou heslovou frází. Je to PIN, který jste zadali, když jste zařízení pro tuto relaci zapnuli.

Nyní můžete výběrem možnosti zpět několikrát opustit hlavní menu.

## Sledování peněženky

V předchozích článcích jsem vysvětlil, jak stáhnout a ověřit Sparrow peněženku a jak ji připojit k vašemu vlastnímu uzlu nebo veřejnému uzlu. Měli byste postupovat podle těchto návodů:

- Instalace Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Instalace Sparrow Bitcoin Peněženky (https://armantheparman.com/download-sparrow/)

- Připojení Sparrow Bitcoin Peněženky k Bitcoin Core (https://armantheparman.com/sparrowcore/)

Alternativou k používání Sparrow Bitcoin Peněženky je Electrum Desktop Peněženka, ale budu pokračovat ve vysvětlování Sparrow Bitcoin Peněženky, protože ji považuji za nejlepší pro většinu lidí. Pokročilí uživatelé mohou jako alternativu použít Electrum.

Nyní ji načteme a připojíme Ledger s peněženkou obsahující heslovou frázi. Tato peněženka nikdy nebyla vystavena Ledger Live, protože byla vytvořena PO připojení zařízení k Ledger Live. Ujistěte se, že ji nikdy znovu nepřipojíte k Ledger Live, abyste nevystavili vaši novou soukromou peněženku.

Vytvoření nové peněženky:

![obrázek](assets/14.webp)

Pojmenujte ji nějak pěkně

![obrázek](assets/15.webp)

Všimněte si zaškrtávacího políčka „Má existující transakce“. Pokud jde o peněženku, kterou jste již dříve používali, pak toto políčko zaškrtněte, jinak se váš zůstatek bude nesprávně zobrazovat jako nula. Zaškrtnutím tohoto políčka se Sparrow zeptá databáze Bitcoin Core (blockchainu) na předchozí transakce. Pro tento návod používáme zcela novou peněženku, takže můžete políčko nechat nezaškrtnuté.

Klikněte na „Připojená hardwarová peněženka“ a ujistěte se, že je zařízení skutečně připojeno, zapnuto, PIN zadán a že jste vstoupili do Bitcoin aplikace.

Klikněte na „Skenovat“ a poté na další obrazovce na „Importovat úložiště klíčů“.

![obrázek](assets/18.webp)

Na další obrazovce není co upravovat, Ledger to za vás vyplnil. Klikněte na „Použít“

![obrázek](assets/19.webp)
Další obrazovka vám umožní přidat heslo. Nezaměňujte to s "heslovou frází"; mnoho lidí to udělá. Název je bohužel nešťastný. Heslo vám umožní zamknout tuto peněženku na vašem počítači. Je specifické pro tento software na tomto počítači. Není součástí vašeho soukromého klíče Bitcoinu.
![image](assets/20.webp)

Po krátké pauze, kdy počítač zpracovává data, uvidíte, že tlačítka vlevo změní barvu z šedé na modrou. Gratulujeme, vaše peněženka je nyní připravena k použití. Provádějte a odesílejte transakce, jak jen chcete.

![image](assets/21.webp)

## Přijímání

Chcete-li přijmout nějaké bitcoiny, přejděte na záložku Adresy vlevo a vyberte jednu z adres pro přijetí. Stačí kliknout pravým tlačítkem na adresu, kterou chcete, a vybrat "kopírovat adresu". Poté přejděte na burzu, odkud se peníze posílají, a vložte ji tam. Nebo můžete adresu poskytnout zákazníkovi, který ji může použít k zaplacení.

Při prvním použití peněženky byste měli přijmout velmi malou částku, vyzkoušet ji poslat na jinou adresu, buď uvnitř peněženky nebo zpět na burzu, abyste ověřili, že peněženka funguje podle očekávání.

Jakmile to uděláte, musíte zálohovat slova, která jste si zapsali. Jedna kopie nestačí. Mějte alespoň dvě papírové kopie (kov je lepší) a uchovávejte je na dvou různých, dobře zabezpečených místech. To snižuje riziko zničení vaší HW peněženky a papírové zálohy při jedné přírodní katastrofě. Viz "Používání hardwarových peněženek Bitcoin" pro úplnou diskusi na toto téma.

## Odesílání

![image](assets/22.webp)

Při provádění platby musíte do pole "Platit na" vložit adresu, na kterou platíte. Ve skutečnosti nemůžete pole Označení nechat prázdné, je to jen pro záznamy vaší vlastní peněženky, ale Sparrow to nedovoluje - stačí zadat cokoli (uvidí to jen vy). Zadejte částku a můžete také ručně upravit poplatek, který chcete.

Peněženka nemůže transakci podepsat, pokud není připojena HW peněženka. To je úkol HW peněženky - přijmout transakci, podepsat ji a vrátit ji podepsanou. Ujistěte se, že když podepisujete na zařízení, vizuálně kontrolujete, že adresa, na kterou platíte, je stejná na zařízení i na obrazovce počítače, a také fakturu, kterou obdržíte (například jste mohli obdržet e-mail s platbou na určitou adresu).

Dávejte také pozor, pokud se rozhodnete použít minci, která je větší než částka platby, pak zbytek bude odeslán zpět na jednu z vašich adres pro změnu peněženky. Někteří lidé to nevěděli a když si vyhledali svou transakci na veřejném blockchainu, mysleli si, že nějaké bitcoiny byly poslány na adresu útočníka, ale ve skutečnosti to byla jejich vlastní adresa pro změnu.

## Firmware

Pro aktualizaci firmware potřebujete připojit k Ledger Live. Pokud to chcete udělat, měli byste zařízení nejprve vymazat a ujistit se, že máte k dispozici záložní slova a heslovou frázi pro obnovení zařízení. Důvod, proč raději zařízení nejprve vymažu, je, že musíte zařízení připojit k Ledger Live pro aktualizaci firmware, a raději nevystavuji svou novou peněženku (tu s heslovou frází) Ledger Live, vůbec. Prostě nedůvěřuji, že Ledger neextrahuje informace o mém veřejném klíči ze zařízení, když se připojím k Ledger Live. Tvrdí, že to nedělají, ale nemohu to ověřit, pokud si nepřečtu kód a nepochopím vnitřní hardware.

## Závěr
Tento článek vám ukázal, jak používat Ledger HWW bezpečněji a soukroměji, než je inzerováno – ale tento článek sám o sobě není dostatečný. Jak jsem řekl na začátku, měli byste jej kombinovat s informacemi poskytnutými v článku „Používání hardwarových peněženek Bitcoin“. Tipy:

Statická Lightning adresa: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/

Pro hlubší pochopení tohoto tématu a posílení bezpečnosti vaší peněženky na Ledger Nano s BIP39 passphrase vás zvu k přečtení tohoto kompletního tutoriálu:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49
