---
name: KaleidoSwap
description: Pokročilý průvodce obchodováním s aktivy RGB na Lightning Network pomocí KaleidoSwapu
---

![cover](assets/cover.webp)


KaleidoSwap je sofistikovaná desktopová aplikace s otevřeným zdrojovým kódem, která překlenuje mezeru mezi protokolem RGB a Lightning Network. Slouží jako komplexní rozhraní pro správu uzlů RGB Lightning, interakci s poskytovateli služeb RGB Lightning (LSP) prostřednictvím specifikace LSPS1 a provádění atomických výměn aktiv RGB.


KaleidoSwap je řešení, které neomezuje správu, a uživatelé si tak mohou zachovat plnou kontrolu nad svými klíči a daty. Využitím paradigmatu ověřování na straně klienta RGB umožňuje uzavírat privátní a škálovatelné chytré smlouvy nad Bitcoin. Tento tutoriál se ponoří do pokročilých funkcí KaleidoSwapu a provede vás složitostmi správy "barevných" UTXO, likvidity kanálů pro konkrétní aktiva a obchodního modelu taker-maker, čímž zajistí, že budete moci tento výkonný decentralizovaný směnný protokol plně využívat.


## Instalace


KaleidoSwap poskytuje předpřipravené binární soubory pro hlavní operační systémy, ale pro pokročilé uživatele je sestavení ze zdrojových kódů zárukou, že budete používat nejnovější kód s konkrétními konfiguracemi.


### Stáhnout binární soubory


Nejnovější verzi pro svůj operační systém si můžete stáhnout z [oficiální webové stránky](https://kaleidoswap.com/) nebo ze [stránky GitHub releases](https://github.com/kaleidoswap/desktop-app/releases).


### Metody instalace


1.  **Windows**: Stáhněte si instalační program `.exe` a spusťte jej.

2.  **macOS**: Stáhněte si soubor `.dmg`, otevřete jej a přetáhněte KaleidoSwap do složky Aplikace.

3.  **Linux**: Stáhněte si soubor `.AppImage` nebo `.deb` a nainstalujte jej/spusťte.



## Možnosti nastavení uzlu


Při prvním spuštění aplikace KaleidoSwap se zobrazí **Připojovací obrazovka**. Jedná se o první krok při konfiguraci vašeho prostředí.


![Node Selection Screen](assets/en/01.webp)


Je třeba zvolit způsob připojení k zařízení RGB Lightning Network. Tato volba ovlivňuje úroveň vašeho ovládání a soukromí.


### Možnost 1: Místní uzel (doporučeno pro vlastní úschovu)


**Pro úplnou kontrolu a soukromí** spusťte uzel přímo na svém počítači, viz výhody níže:


- Samosprávný**: Klíče jsou ve vašich rukou. Žádná třetí strana nemůže zmrazit vaše prostředky ani cenzurovat vaše transakce.
- Soukromí**: Vaše data zůstanou ve vašem zařízení.
- Nezávislost**: Žádná závislost na externích poskytovatelích služeb.


Pokud vyberete možnost **Místní uzel**, přejdete na obrazovku nastavení, kde můžete vytvořit nový uzel wallet nebo obnovit stávající.


![Local Node Setup Screen](assets/en/02.webp)


### Možnost 2: Vzdálený uzel


Připojte se ke vzdálenému serveru RGB Lightning Node (hostovanému na serveru VPS nebo u hostovaného poskytovatele).


- Výhody**: Dostupnost 24 hodin denně, 7 dní v týdnu.
- Výměna**: Vyžaduje důvěryhodnost hostitele nebo správu vzdáleného serveru.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap je navržen tak, aby umožňoval vlastní úschovu.** Důrazně doporučujeme provozovat vlastní uzel - buď lokálně (možnost 1), nebo hostovat vzdálený uzel - abyste plně využili vlastnosti Bitcoin a RGB odolné vůči cenzuře.


## Vytvoření modelu Wallet


Společnost KaleidoSwap spravuje aktiva Bitcoin i RGB. Proces vytváření wallet inicializuje úložiště klíčů, které zabezpečuje vaše prostředky on-chain a stavy kanálu Lightning.


Zde je podrobný postup:

1. Otevřete aplikaci KaleidoSwap a vyberte možnost **Místní uzel**.

2. Klikněte na možnost **Vytvořit nový Wallet**.

3. **Nastavení účtu**: Zadejte **Název účtu** a vyberte **Síť** (např. Bitcoin Mainnet, Testnet, Signet).

4. **Pokročilá konfigurace** (volitelná): Pokud jste zkušený uživatel, můžete v části "Pokročilá nastavení" nakonfigurovat vlastní koncové body RPC, adresy URL indexátoru nebo nastavení proxy serveru.

5. Klikněte na tlačítko **pokračovat**.

6. **Heslo**: Nastavte silné heslo pro lokální zašifrování souboru wallet.

7. **Fráze pro obnovu**: Zapište si frázi seed a bezpečně ji uložte.


    - Kritické**: Tato věta je nutná k obnovení prostředků on-chain a identity uzlu.
    - Upozornění**: **Stav bleskového kanálu nelze plně obnovit pouze z seed**. Pro obnovu prostředků zablokovaných v kanálech je nutné udržovat také statické zálohy kanálů (SCB).


![Wallet Creation Screen](assets/en/04.webp)



## Přehled přístrojového panelu


Po vytvoření účtu wallet budete přesměrováni na hlavní panel **Dashboard**.


![KaleidoSwap Dashboard](assets/en/05.webp)


_Poznámka: Na výše uvedeném snímku obrazovky je zobrazena již financovaná služba wallet s aktivními kanály. Čerstvý wallet bude vykazovat nulové zůstatky a žádné aktivní kanály, dokud jej nezafinancujete


## Financování vašeho Wallet


Chcete-li pracovat s prostředky RGB, musíte financovat svůj wallet. KaleidoSwap podporuje vkládání aktiv Bitcoin i RGB prostřednictvím transakcí on-chain nebo Lightning Network.


### Uložení Bitcoin


1. V nabídce Rychlé akce klikněte na možnost **Vklad**.

2. V seznamu aktiv vyberte **BTC**.


![Select BTC Asset](assets/en/06.webp)


3. Vyberte si způsob vkladu: *vyberte si možnost vkladu: *Na řetězu** nebo **Blesk**.


![BTC Deposit Options](assets/en/07.webp)



- Na řetězu**: Pro odeslání Bitcoin z jiného wallet naskenujte QR kód nebo zkopírujte adresu.
- Blesk**: Vygenerujte fakturu na požadovanou částku.


![BTC On-chain Deposit](assets/en/08.webp)


### Ukládání aktiv RGB a barevných UTXO


Abyste mohli přijímat aktiva RGB (například USDT), potřebujete mít k dispozici konkrétní UTXO, které budou "obarveny" (bude jim přiřazeno aktivum).


1. Klikněte na tlačítko **Vklad** a vyberte aktivum RGB (např. USDT). **Důležité**: Pokud je to **poprvé**, co váš uzel přijímá toto konkrétní aktivum, **ponechte pole ID aktiva prázdné**. Zadání ID neznámého aktiva způsobí, že uzel vrátí chybu, protože jej zatím nerozpoznal.

2. Zvolte možnost **Na řetězu** nebo **Blesk**.


![USDT Deposit Options](assets/en/09.webp)


#### Režimy příjmu v řetězci: Svědek vs. zaslepený


Při příjmu prostředků RGB on-chain máte k dispozici dva režimy ochrany soukromí:



- Slepý příjem (doporučeno pro ochranu soukromí)**: Odesílateli poskytnete "blinded" UTXO. Žádáte odesílatele, aby odeslal prostředky na existující UTXO, který vlastníte, ale skutečný identifikátor UTXO zakrýváte. To nabízí lepší ochranu soukromí.
- Svědek přijímá**: Zadáte standardní adresu Bitcoin. Žádáte odesílatele, aby pro vás vytvořil *nový* UTXO odesláním prostředků na tuto adresu. To umožňuje připojit aktiva RGB přímo k novému UTXO vytvořenému transakcí.


#### Bleskový vklad


V případě bleskových záloh stačí vystavit fakturu generate. Aktivum RGB vám bude zasláno prostřednictvím otevřených kanálů.


![USDT Lightning Invoice](assets/en/10.webp)



## Otevírání kanálů s aktivy RGB


Pro směrování aktiv RGB přes Lightning Network potřebujete kanál s dostatečnou likviditou a alokací aktiv. Nejjednodušší způsob, jak začít, je **koupit kanál** od poskytovatele bleskových služeb (LSP).


### Nákup kanálu od společnosti Kaleido LSP


1. Přejděte na kartu **Kanály**. Zobrazí se možnosti "Otevřít kanál" (ručně) nebo "Koupit kanál" (LSP).

2. Klikněte na tlačítko **Koupit kanál**.


![Channels Dashboard](assets/en/11.webp)


3. **Připojení k LSP**: Aplikace se připojí k výchozímu LSP Kaleido. Tento poskytovatel nabízí příchozí likviditu a podporuje směrování aktiv RGB.


![Connect to LSP](assets/en/12.webp)


4. **Konfigurace kanálu**:


    - Kapacita**: Zvolte celkovou kapacitu Bitcoin pro kanál.
    - Přidělení RGB**: USDT), které chcete přijímat nebo odesílat. LSP zajistí, aby byl kanál nakonfigurován tak, aby toto aktivum podporoval.


![Configure Channel](assets/en/13.webp)



    - Přidělení RGB**: USDT), které chcete přijímat nebo odesílat. LSP zajistí, aby byl kanál nakonfigurován tak, aby toto aktivum podporoval.


![RGB Allocation](assets/en/14.webp)


5.  **Platba**: Za otevření kanálu a poskytnutí likvidity je nutné zaplatit LSP poplatek. Platit můžete pomocí **Lightning** nebo **On-chain** Bitcoin. Platbu lze provést z vašeho interního KaleidoSwap wallet nebo externího wallet.


![Complete Payment](assets/en/15.webp)


6. Jakmile je platba potvrzena, LSP zahájí transakci otevření kanálu. Zobrazí se obrazovka **Objednávka dokončena**.


![Order Completed](assets/en/16.webp)


7. Po potvrzení v blockchainu bude váš kanál aktivní a připravený pro převody RGB.



## Obchodování: Obchodování: model "taker-maker


Obchodní systém KaleidoSwap funguje na modelu **Taker-Maker**. Aktiva můžete vyměňovat ručně s partnerem nebo použít tvůrce trhu (LSP).


### Výměna s tvůrcem trhu (LSP)


Jedná se o nejběžnější způsob obchodování. Vystupujete v roli **Takera** a provádíte příkazy proti dostupné likviditě poskytované poskytovatelem služeb elektronických peněz (**Tvůrcem**).


1. Přejděte na kartu **Trade** a vyberte možnost **Market Maker**.

2. **Zadejte částku**: Vložte částku Bitcoin, kterou chcete odeslat (nebo aktivum, které chcete přijmout). V rozhraní se zobrazí odhadovaný směnný kurz a poplatky.


![Market Maker Swap](assets/en/17.webp)


3. **Potvrdit výměnu**: Zkontrolujte podrobnosti, včetně směnného kurzu a přesné částky, kterou obdržíte. Klikněte na tlačítko **Potvrdit výměnu**.


![Confirm Swap](assets/en/18.webp)


4. **Zpracování**: Výměna se na Lightning Network provádí atomicky. Zobrazí se stavová obrazovka s informací, že výměna probíhá.


![Swap Pending](assets/en/19.webp)


5. **Úspěch**: Po vypořádání HTLC je výměna dokončena a aktiva jsou ve vašem kanálu.


![Swap Success](assets/en/20.webp)



## Vývojář API


Vývojáři, kteří staví nad aplikací KaleidoSwap, mají k dispozici aplikaci API, která podporuje:



- RGB LSPS1**: Pro automatizované služby likvidity.
- Výměna API**: Pro programové obchodování a tvorbu trhu.
- WebSocket**: Pro odběry tržních dat v reálném čase.


Úplné koncové body a specifikace naleznete v [Dokumentaci API](https://docs.kaleidoswap.com/api/introduction).


## Závěr


KaleidoSwap vám umožní využít soukromí a škálovatelnost prostředků RGB na Lightning Network. Pochopením barevných UTXO a alokace kanálových aktiv můžete plně využít tento výkonný decentralizovaný směnný protokol.