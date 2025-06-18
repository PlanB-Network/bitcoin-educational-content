---
name: Sparrow Wallet
description: Instalace, konfigurace a používání Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet je software pro správu portfolia Bitcoin vyvinutý Craigem Rawem. Tento open-source software oceňují bitcoináři pro jeho mnoho funkcí a intuitivní Interface.

Sparrow můžete používat dvěma způsoby:


- Jako Hot Wallet, kde jsou vaše soukromé klíče uloženy v počítači.
- Jako správce Cold Wallet, kde jsou soukromé klíče uloženy v Hardware Wallet. V tomto režimu Sparrow pouze manipuluje s veřejnými informacemi Wallet, sleduje finanční prostředky, generuje adresy a vytváří transakce, ale pro platnost těchto transakcí je vyžadován podpis Hardware Wallet. Může tedy nahradit aplikace, jako je Ledger Live nebo Trezor Suite.

Sparrow podporuje peněženky s jedním podpisem a peněženky s více podpisy a umožňuje plynulou správu více peněženek. Například můžete současně ovládat jednu peněženku Wallet připojenou k peněžence Ledger, další k peněžence Trezor a také mít peněženku Hot Wallet.

Software také nabízí pokročilé funkce kontroly mincí, které vám umožní přesně zvolit, které UTXO se mají při transakcích použít, abyste optimalizovali svou důvěrnost.

Pokud jde o připojení, Sparrow umožňuje připojit se k vlastnímu uzlu Bitcoin, a to buď vzdáleně prostřednictvím serveru Electrum, nebo pomocí jádra Bitcoin. Pokud ještě nemáte vlastní uzel, je možné použít také veřejný uzel. Vzdálená připojení se uskutečňují přes Tor.

## Instalace Sparrow Wallet

Přejděte na [oficiální stránku pro stažení Sparrow Wallet](https://sparrowwallet.com/download/) a vyberte verzi softwaru odpovídající vašemu operačnímu systému.

![Image](assets/fr/01.webp)

Před instalací je důležité zkontrolovat integritu a pravost softwaru. Pokud nevíte, jak to udělat, kompletní návod najdete zde :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Po instalaci aplikace Sparrow můžete přeskočit úvodní vysvětlující obrazovky a přejít rovnou na obrazovku správy připojení.

![Image](assets/fr/02.webp)

## Připojení k síti Bitcoin

Chcete-li komunikovat se sítí Bitcoin a vysílat své transakce, musí být Sparrow připojen k uzlu Bitcoin. Existují tři hlavní způsoby, jak toto spojení navázat:


- 🟡 Použití veřejného uzlu, tj. připojení k uzlu třetí strany, který takové připojení umožňuje. Pokud nemáte vlastní uzel Bitcoin, tato možnost vám umožní rychle začít se Sparrowem pracovat. Uzel, ke kterému se připojíte, však uvidí všechny vaše transakce, což by mohlo ohrozit důvěrnost vašich informací. Mít kontrolu nad svými klíči je nezbytné, ale mít vlastní uzel je ještě lepší. Tuto možnost proto používejte pouze v případě, že teprve začínáte, a zároveň si buďte vědomi rizik pro vaše soukromí.
- 🟢 Připojení k uzlu Bitcoin Core. Pokud máte vlastní uzel Bitcoin Core, můžete jej připojit ke Sparrow Wallet, a to buď lokálně, pokud je Bitcoin Core nainstalován na stejném počítači, nebo vzdáleně.
- 🔵 Připojení přes server Electrum. Pokud je váš uzel Bitcoin vybaven serverem Electrs, jako je tomu v případě řešení node-in-a-box, například Umbrel nebo Start9, můžete se k němu připojit vzdáleně ze Sparrow.

**Vhodnější je používat připojení prostřednictvím Electrs nebo Bitcoin Core ve vlastním uzlu, abyste snížili potřebu důvěřovat třetí straně a optimalizovali důvěrnost**

### Připojení k veřejnému uzlu 🟡

Připojení k veřejnému uzlu je velmi jednoduché. Klikněte na kartu "*Veřejný server*".

![Image](assets/fr/03.webp)

Vyberte uzel z rozevíracího seznamu.

![Image](assets/fr/04.webp)

Poté klikněte na možnost "*Testovat připojení*".

![Image](assets/fr/05.webp)

Po připojení se na displeji Sparrow Wallet zobrazí v pravém dolním rohu modulu Interface žluté zaškrtnutí, které signalizuje, že jste připojeni k veřejnému uzlu.

![Image](assets/fr/06.webp)

### Připojení k jádru Bitcoin 🟢

Druhým způsobem připojení k uzlu Bitcoin je propojení Sparrow s jádrem Bitcoin. Pokud je jádro Bitcoin nainstalováno na stejném počítači, ověřování bude probíhat prostřednictvím souboru cookie. Pokud je jádro Bitcoin Core na vzdáleném počítači, bude třeba použít heslo definované v souboru `Bitcoin.conf`.

Upozorňujeme, že pokud použijete ořezaný uzel Bitcoin Core, nebudete moci obnovit uzel Wallet obsahující transakce, které předcházely lokálně uloženým blokům. Pro nový uzel Wallet vytvořený v uzlu Sparrow to však nebude problém: vaše nové transakce budou viditelné i s ořezaným uzlem.

Konfiguraci uzlu Bitcoin Core můžete provést podle některého z následujících návodů v závislosti na operačním systému:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

V aplikaci Sparrow přejděte na kartu "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**S místním jádrem Bitcoin:**

Pokud je v počítači nainstalováno jádro Bitcoin, vyhledejte soubor `Bitcoin.conf` mezi softwarovými soubory. Pokud tento soubor neexistuje, můžete jej vytvořit. Otevřete jej pomocí textového editoru a vložte následující řádek:

```ini
server=1
```

Poté změny uložte.

Můžete to také provést prostřednictvím grafiky Bitcoin-QT Interface, když přejdete na "*Nastavení*" > "*Možnosti...*" a aktivujte možnost "*Povolit server RPC*".

Po provedení těchto změn nezapomeňte restartovat software.

![Image](assets/fr/08.webp)

Poté se vraťte do Sparrow Wallet a zadejte cestu k souboru cookie, který se v závislosti na operačním systému obvykle nachází ve stejné složce jako soubor `Bitcoin.conf`:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Ostatní parametry ponechte jako výchozí, tedy URL `127.0.0.1` a port `8332`, a klikněte na "*Test Connection*".

![Image](assets/fr/10.webp)

Spojení je navázáno. V pravém dolním rohu se objeví zaškrtnutí Green, které označuje, že jste připojeni k uzlu Bitcoin Core.

![Image](assets/fr/11.webp)

**S dálkovým ovladačem Bitcoin Core:**

Pokud je jádro Bitcoin nainstalováno na jiném počítači připojeném ke stejné síti, vyhledejte nejprve soubor `Bitcoin.conf` mezi softwarovými soubory. Pokud tento soubor ještě neexistuje, můžete jej vytvořit. Otevřete tento soubor v textovém editoru a přidejte následující řádek:

```ini
server=1
```

Po úpravě souboru se ujistěte, že jste jej uložili do příslušné složky operačního systému:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Tuto operaci lze provést také prostřednictvím grafického Bitcoin-QT Interface. Přejděte do nabídky "*Nastavení*", poté do nabídky "*Možnosti...*" a aktivujte možnost "*Povolit server RPC*" zaškrtnutím příslušného políčka. Pokud soubor `Bitcoin.conf` neexistuje, můžete jej vytvořit přímo z tohoto Interface kliknutím na "*Otevřít konfigurační soubor*".

![Image](assets/fr/12.webp)

V místní síti vyhledejte IP adresu Address počítače, který je hostitelem jádra Bitcoin. K tomu můžete použít nástroj, například [Angry IP Scanner](https://angryip.org/). Pro představu předpokládejme, že IP adresa Address vašeho uzlu je `192.168.1.18`.

Do souboru `Bitcoin.conf` přidejte následující řádky a nastavte `rpcbind=192.168.1.18` tak, aby odpovídal IP adrese Address vašeho uzlu.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

V souboru `Bitcoin.conf` přidejte uživatelské jméno a heslo pro vzdálená připojení. Nezapomeňte nahradit `loic` svým uživatelským jménem a `my_password` silným heslem:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Po úpravě a uložení souboru restartujte software Bitcoin-QT.

Nyní se můžete vrátit do Sparrow Wallet. Přejděte na záložku "*Uživatel/Pas*". Zadejte uživatelské jméno a heslo, které jste nakonfigurovali v souboru `Bitcoin.conf`. Ostatní parametry ponechte jako výchozí, tj. adresu URL `127.0.0.1` a port `8332`. Poté klikněte na tlačítko "*Test Connection*".

![Image](assets/fr/15.webp)

Spojení je navázáno. V pravém dolním rohu se objeví zaškrtnutí Green, které označuje, že jste připojeni k uzlu Bitcoin Core.

![Image](assets/fr/16.webp)

### Připojení k serveru Electrum 🔵

Poslední možností připojení je použití vzdáleného serveru Electrum. Tato metoda umožňuje připojit se k uzlu přes Tor z jiného zařízení a využít indexátor k rychlejšímu procházení portfolií na Sparrow. Je vhodná zejména v případě, že máte řešení typu uzel v krabici, jako je Umbrel nebo Start9, které umožňují instalaci Electra jediným kliknutím.

Za tímto účelem získejte Tor `.onion' Address serveru Electrum. Například v aplikaci Umbrel ji najdete v aplikaci Electrs.

![Image](assets/fr/17.webp)

V aplikaci Sparrow Wallet přejděte na kartu "*Soukromé Electrum*".

![Image](assets/fr/18.webp)

Do vyhrazeného prostoru zadejte svůj kód Tor Address. Ostatní nastavení mohou zůstat výchozí. Poté klikněte na "*Test Connection*".

![Image](assets/fr/19.webp)

Spojení je potvrzeno. Pokud toto okno zavřete, v pravém dolním rohu se objeví modré zaškrtnutí, které znamená, že jste připojeni k serveru Electrum.

![Image](assets/fr/20.webp)

## Vytvoření teplého portfolia

Nyní, když je Sparrow Wallet nakonfigurován pro komunikaci se sítí Bitcoin, jste připraveni vytvořit svůj první Wallet. Tato část vás provede vytvořením Hot Wallet, tj. Wallet, jehož soukromé klíče jsou uloženy ve vašem počítači. Vzhledem k tomu, že váš počítač je složitý stroj připojený k internetu, představuje velmi velkou plochu pro útok. V důsledku toho by měl být Hot Wallet používán pouze pro omezené množství bitcoinů. Chcete-li ukládat větší částky, zvolte si bezpečný počítač Wallet s kódem Hardware Wallet. Pokud je to to, co hledáte, můžete přeskočit na další část.

Chcete-li vytvořit Hot Wallet, klikněte na domovské obrazovce Sparrow Wallet na kartu "*File*" a poté na "*New Wallet*".

![Image](assets/fr/21.webp)

Zadejte název svého portfolia a klikněte na "*Vytvořit Wallet*".

![Image](assets/fr/22.webp)

V horní části okna Interface si můžete vybrat, zda chcete vytvořit portfolio "*Jediný podpis*" nebo "*Více podpisů*". Hned pod tím vyberte typ skriptu pro uzamčení UTXO. Doporučuji použít nejnovější standard: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Poté klikněte na "*Nový nebo importovaný Software Wallet*".

![Image](assets/fr/24.webp)

Zvolte standard BIP39, protože je podporován prakticky veškerým softwarem portfolia Bitcoin. Dále zvolte délku fráze pro obnovení. V současné době postačuje 12slovná fráze, protože obě nabízejí podobné zabezpečení, ale 12slovná fráze se jednodušeji ukládá.

![Image](assets/fr/25.webp)

Klepnutím na tlačítko "*generate New*" zobrazíte větu generate svého Wallet. Tato fráze poskytuje plný, neomezený přístup ke všem vašim bitcoinům. Kdokoli, kdo tuto frázi vlastní, může vaše prostředky ukrást, a to i bez fyzického přístupu k vašemu počítači.

Dvanáctislovná fráze obnoví přístup k bitcoinům v případě ztráty, krádeže nebo rozbití počítače. Je proto velmi důležité ji pečlivě uložit a uchovávat na bezpečném místě.

Můžete ho vyrýt na papír nebo pro větší bezpečnost na nerezovou ocel, která ho ochrání před požárem, povodní nebo zřícením. Volba média pro váš Mnemonic bude záviset na vaší bezpečnostní strategii, ale pokud používáte Sparrow jako teplý výdaj Wallet obsahující mírné množství, měl by papír stačit.

Pro více informací o správném způsobu ukládání a správy fráze Mnemonic vřele doporučuji sledovat tento další návod, zejména pokud jste začátečníci:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Samozřejmě nesmíte tato slova nikdy sdílet na internetu, jak to dělám v tomto návodu. Tento příklad Wallet bude použit pouze na Testnet a na konci návodu bude odstraněn.**

Kliknutím na pole "*Použít passphrase*" můžete také zvolit možnost přidání passphrase BIP39. Varování: Použití passphrase může být velmi užitečné, ale pokud nerozumíte tomu, jak funguje, může to být velmi riskantní. Proto vám důrazně doporučuji přečíst si tento krátký teoretický článek na toto téma:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Po uložení Mnemonic a passphrase na fyzické médium klikněte na "*Potvrdit zálohu*".

![Image](assets/fr/27.webp)

Znovu zadejte svých 12 slov, abyste potvrdili, že byla správně uložena, a klikněte na "*Vytvořit úložiště klíčů*".

![Image](assets/fr/28.webp)

Poté klikněte na "*Import Keystore*", abyste z fráze Mnemonic získali klíče portfolia generate.

![Image](assets/fr/29.webp)

Kliknutím na tlačítko "*Použít*" dokončete vytváření portfolia.

![Image](assets/fr/30.webp)

Nastavte si silné heslo pro zabezpečení přístupu do svého portfolia Sparrow. Toto heslo je vhodné uložit do správce hesel, abyste ho nezapomněli. Všimněte si, že toto heslo nehraje žádnou roli při odvozování vašich klíčů. Používá se pouze pro přístup k vašemu klíči Wallet prostřednictvím klíče Sparrow Wallet. Takže i bez tohoto hesla bude vaše fráze Mnemonic stačit k přístupu k vašim bitcoinům z jakékoli aplikace kompatibilní s BIP39.

![Image](assets/fr/31.webp)

Nyní je vytvořena vaše karta Hot Wallet. Pokud nemáte v plánu používat Hardware Wallet se Sparrowem, můžete přeskočit na část *Příjem bitcoinů* tohoto návodu.

## Správa portfolia Cold

Druhým způsobem, jak využít Sparrow Wallet, je nastavit jej jako správce portfolia s Hardware Wallet. V této konfiguraci zůstávají soukromé klíče vašeho Bitcoin Wallet výhradně na Hardware Wallet, zatímco Sparrow má přístup pouze k veřejným informacím. Tento přístup nabízí vyšší úroveň zabezpečení než výše diskutované peněženky Hot, protože soukromé klíče jsou uchovávány ve specializovaném zařízení, často se zabezpečeným čipem, které není připojeno k internetu, a proto představuje mnohem menší plochu pro útoky než tradiční počítač.

Existují dva hlavní způsoby připojení zařízení Hardware Wallet ke službě Sparrow:


- Pomocí kabelu, který se běžně používá se základními modely, jako je Trezor Safe 3 nebo Ledger Nano S Plus ;
- V režimu Air-Gap, tj. bez přímého kabelového připojení, prostřednictvím karty MicroSD nebo QR kódu Exchange.

Sparrow podporuje všechny tyto komunikační metody a je kompatibilní s většinou hardwarových peněženek na trhu.

V tomto návodu budu používat model Ledger Nano S s kabelem, ale postup je podobný i v režimu Air-Gap. Podrobnosti specifické pro model Hardware Wallet najdete ve speciálním tutoriálu věnovaném modelu Plan ₿ Network.

Před zahájením se ujistěte, že je Wallet již nakonfigurován na vašem Hardware Wallet. Pokud používáte kabelové připojení, připojte jej k počítači pomocí kabelu.

Chcete-li do Sparrow Wallet importovat takzvaný "*Keystore*" (veřejné informace potřebné pro správu portfolia), klikněte na kartu "*File*" a poté na "*New Wallet*".

![Image](assets/fr/32.webp)

Pojmenujte své portfolio a klikněte na "*Vytvořit Wallet*". Doporučuji zadat název vašeho portfolia Hardware Wallet, abyste jej později snadno identifikovali.

![Image](assets/fr/33.webp)

V horní části zařízení Interface si můžete vybrat mezi portfoliem "*Single Signature*" nebo "*Multi Signature*". Pro náš příklad nakonfigurujeme portfolio s jedním podpisem.

Níže vyberte typ skriptu pro uzamčení jednotek UTXO. Pokud to váš Hardware Wallet podporuje, doporučuji zvolit "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Dále se postup liší podle způsobu připojení. Pokud používáte metodu Air-Gap, vyberte možnost "*Airgapped Hardware Wallet*". Poté postupujte podle pokynů specifických pro vaše zařízení.

![Image](assets/fr/35.webp)

Pokud používáte kabelové připojení, jako v mém případě, vyberte možnost "*Připojeno Hardware Wallet*".

![Image](assets/fr/36.webp)

Klikněte na "*Scan*", aby Sparrow zjistil vaše zařízení. Ujistěte se, že je připojeno a odemčeno. U některých modelů, jako je například Ledger, budete muset otevřít aplikaci "*Bitcoin*", abyste umožnili detekci.

![Image](assets/fr/37.webp)

Vyberte možnost "*Importovat úložiště klíčů*".

![Image](assets/fr/38.webp)

Kliknutím na tlačítko "*Použít*" dokončete vytváření portfolia.

![Image](assets/fr/39.webp)

Nastavte silné heslo pro zabezpečení přístupu k zařízení Sparrow Wallet. Toto heslo ochrání vaše veřejné klíče, adresy a historii transakcí. Doporučujeme jej uložit do správce hesel. Upozorňujeme, že toto heslo nehraje žádnou roli při odvozování vašich klíčů. I bez něj můžete obnovit přístup ke svým bitcoinům pomocí Mnemonic prostřednictvím jakéhokoli softwaru kompatibilního s BIP39.

![Image](assets/fr/40.webp)

Vaše portfolio pro správu je nyní nakonfigurováno ve službě Sparrow.

![Image](assets/fr/41.webp)

## Přijímání bitcoinů

Nyní, když je váš Wallet nastaven na Sparrow, můžete přijímat bitcoiny. Stačí vstoupit do nabídky "*Příjem*".

![Image](assets/fr/42.webp)

Sparrow zobrazí první nepoužitý Address ve vašem Wallet. K tomuto Address můžete přidat "*Label*", který vám v budoucnu připomene původ těchto satošů.

![Image](assets/fr/43.webp)

Používáte-li zařízení Hot Wallet, můžete zobrazený kód Address okamžitě použít, a to buď jeho zkopírováním, nebo naskenováním souvisejícího kódu QR.

Pokud používáte zařízení Hardware Wallet, je velmi důležité, abyste před jeho použitím zkontrolovali na obrazovce zařízení Address. V případě kabelových zařízení připojte a odemkněte zařízení Hardware Wallet a poté v aplikaci Sparrow klikněte na možnost "*Zobrazit Address*". Ujistěte se, že číslo Address zobrazené na displeji zařízení Hardware Wallet odpovídá číslu zobrazenému na obrazovce Sparrow.

![Image](assets/fr/44.webp)

Pro uživatele Hardware Wallet Air-Gap se ověření Address liší podle modelu zařízení. Přesné pokyny naleznete ve specializovaném návodu Plan ₿ Network.

Jakmile je transakce odeslána plátcem, zobrazí se na kartě "*Transakce*". Můžete na ni kliknout, abyste získali další podrobnosti, jako je například txid.

![Image](assets/fr/45.webp)

Na kartě "*Adresy*" najdete seznam všech svých doručených adres. Můžete zjistit, zda již byly použity a zda byl přidán štítek. *Adresy "Receive*" jsou ty, které Sparrow zobrazí po kliknutí na "*Receive*" a jsou určeny pro příchozí platby. Adresy "*Změna*" se používají pro Exchange ve vašich transakcích, tj. pro obnovení nevyužité části vašich UTXO na vstupu.

![Image](assets/fr/46.webp)

Na kartě "*UTXOs*" jsou zobrazeny všechny vaše UTXOs, tj. fragmenty Bitcoin, které máte v držení. U každého fragmentu UTXO vidíte jeho množství a související označení.

![Image](assets/fr/47.webp)

## Odeslat bitcoiny

Nyní, když máte v Wallet několik satošů, máte také možnost některé poslat. Ačkoli existuje několik způsobů, jak to provést, doporučuji vám použít nabídku "*UTXOs*" pro přesnější kontrolu nad utracenými mincemi (*kontrola mincí*), spíše než přejít přímo do nabídky "*Odeslat*" (i když ta může stačit, pokud jste začátečník).

![Image](assets/fr/48.webp)

Vyberte UTXO, které chcete použít jako vstupy pro tuto transakci, a klikněte na "*Odeslat vybrané*". Tento přístup vám umožní vybrat nejvhodnější zdroje mezi UTXO podle vašich výdajů a štítků použitých při jejich přijetí, abyste optimalizovali důvěrnost vašich plateb. Ujistěte se, že součet vybraných UTXO je vyšší než částka, kterou chcete odeslat.

![Image](assets/fr/49.webp)

Do pole "*Platba příjemci*" zadejte číslo Address příjemce. Příkaz Address můžete také naskenovat pomocí webové kamery kliknutím na ikonu kamery. Tlačítko "*+Přidat*" umožňuje zaplatit více adres v rámci jedné transakce.

![Image](assets/fr/50.webp)

Přidejte k transakci štítek, který vám připomene její účel. Tento štítek bude také přiřazen k vaší případné transakci Exchange.

![Image](assets/fr/51.webp)

Zadejte částku, která má být zaslána na tento účet Address.

![Image](assets/fr/52.webp)

Upravte sazbu poplatku podle aktuálních podmínek na trhu. To můžete provést zadáním absolutní hodnoty poplatku nebo úpravou sazby poplatku pomocí posuvníku.

![Image](assets/fr/53.webp)

V dolní části displeje Interface si můžete vybrat mezi možnostmi "*Efficiency*" a "*Privacy*". V mém případě není možnost "*Privacy*" k dispozici, protože mám v tomto portfoliu pouze jeden model UTXO. "*Efficiency*" odpovídá klasické transakci, zatímco "*Privacy*" je transakce typu Stonewall, tedy struktura transakce, která posiluje vaši důvěrnost tím, že simuluje mini-CoinJoin, což činí analýzu řetězce složitější.

![Image](assets/fr/54.webp)

Sparrow zobrazí souhrnný diagram zobrazující vaše vstupy, výstupy a transakční poplatky (všimněte si, že poplatky ve skutečnosti nejsou výstupem, na rozdíl od toho, co naznačuje tento diagram). Pokud jste se vším spokojeni, klikněte na "*Vytvořit transakci*".

![Image](assets/fr/55.webp)

Tím se dostanete na stránku s podrobnými informacemi o transakci Elements. Zkontrolujte, zda jsou všechny informace správné, a poté klikněte na "*Finalizovat transakci k podpisu*".

![Image](assets/fr/56.webp)

Je důležité zachovat výchozí nastavení Sighash. Chcete-li pochopit proč, podívejte se na toto školení, ve kterém vysvětluji vše, co potřebujete vědět o systému Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Na další obrazovce se možnosti liší podle typu používaného zařízení Wallet:


- Pro Hardware Wallet Air-Gap klikněte na "*Show QR*", aby se zobrazil PSBT, který můžete podepsat pomocí zařízení, a poté načtěte podepsaný PSBT do Sparrow pomocí "*Scan QR*". Možnost "*Uložit transakci*" funguje podobně, ale s výměnami na kartě microSD ;
- V případě Hot Wallet jednoduše klikněte na "*Podepsat*" a zadejte heslo Wallet pro podepsání ;
- V případě kabelového připojení Hardware Wallet klikněte také na "*Podepsat*" a odešlete nepodepsanou transakci do svého zařízení.

![Image](assets/fr/57.webp)

Na svém účtu Hardware Wallet zkontrolujte účet Address příjemce, odeslanou částku a poplatky. Pokud je vše v pořádku, pokračujte v podpisu.

Jakmile je transakce podepsána, objeví se znovu v systému Sparrow a je připravena k vysílání v síti Bitcoin pro následné zařazení do bloku. Pokud je vše v pořádku, klikněte na tlačítko "*Vysílat transakci*".

![Image](assets/fr/58.webp)

Vaše transakce se nyní vysílá a čeká na potvrzení.

![Image](assets/fr/59.webp)

## Správa a konfigurace portfolií v aplikaci Sparrow

Na kartě "*Nastavení*" najdete podrobné informace o svém portfoliu, jako např. :


- Typ portfolia (single-sig nebo multi-sig) ;
- Typ použitého skriptu ;
- Název, který jste portfoliu přiřadili ;
- Otisk hlavního klíče;
- Objízdná trasa ;
- Rozšířený veřejný klíč účtu.

![Image](assets/fr/60.webp)

Tlačítko "*Export*" umožňuje exportovat informace o portfoliu tak, abyste je mohli použít v jiném softwaru a zároveň zachovat informace nastavené ve Sparrow.

Tlačítko "*Přidat účet*" umožňuje přidat do portfolia další účet. Účet odpovídá samostatné sadě doručených adres. Tato funkce může být užitečná, například pokud chcete oddělit osobní a firemní účet pomocí jediné fráze Mnemonic.

Tlačítko "*Pokročilé*" umožňuje přístup k pokročilým nastavením, jako je například přizpůsobení vyhledávání Sparrow Address a změna hesla portfolia.

![Image](assets/fr/61.webp)

Když zavřete Sparrow Wallet, váš Wallet se automaticky uzamkne. Při příštím otevření softwaru se zobrazí okno s výzvou k odemknutí Wallet pomocí hesla.

![Image](assets/fr/62.webp)

Pokud se toto okno neotevře nebo pokud chcete otevřít jiné portfolio v aplikaci Sparrow, klikněte na kartu "*File*" a vyberte možnost "*Otevřít Wallet*".

![Image](assets/fr/63.webp)

Tím otevřete Správce souborů ve složce, kam Sparrow ukládá vaše peněženky. Jednoduše vyberte Wallet, kterou chcete otevřít, a zadáním hesla ji odemkněte.

![Image](assets/fr/64.webp)

V nabídce "*File*" v části "*Settings*" najdete parametry síťového připojení Bitcoin, které již byly prozkoumány v předchozích částech. Můžete také upravit různé parametry, jako je použitá jednotka, fiat měna pro převody a zdroje informací.

![Image](assets/fr/65.webp)

Karta "*Pohled*" nabízí možnosti přizpůsobení a přístup k některým užitečným příkazům, jako je například "*Obnovit Wallet*", který obnoví vyhledávání transakcí ve vašem portfoliu.

![Image](assets/fr/66.webp)

Karta "*Nástroje*" sdružuje několik pokročilých nástrojů, včetně :


- "*Podepsat/ověřit zprávu*" umožňuje prokázat vlastnictví přijímajícího Address nebo ověřit podpis.
- "*Odeslat na mnoho*" nabízí zjednodušenou funkci Interface pro provádění transakcí na více přijímacích adres najednou, což je vhodné pro dávkové výdaje.
- "*Sweep Private Key*" umožňuje získat bitcoiny zabezpečené jednoduchým soukromým klíčem a převést je do vašeho Sparrow Wallet. To může být užitečné zejména pro ty, kteří mají bitcoiny z počátku roku 2010, tedy z doby před érou HD peněženek.
- "Ověřit stahování" ověří integritu a pravost staženého softwaru před jeho instalací do zařízení.
- "*Restart In*" umožňuje přepnout na peněženky v sítích Testnet nebo Signet. To může být užitečné, pokud chcete přistupovat k testovacím sítím s mincemi bez reálné hodnoty.

![Image](assets/fr/67.webp)

Nyní víte vše o softwaru Sparrow Wallet, který je vynikajícím nástrojem pro každodenní správu portfolia Bitcoin.

Pokud pro vás byl tento návod užitečný, budu vám vděčný, pokud níže zanecháte palec Green. Neváhejte jej sdílet na svých sociálních sítích. Moc vám děkuji!

Doporučuji také tento další tutoriál, ve kterém vysvětluji, jak nakonfigurovat kartu Hardware Wallet COLDCARD Q pomocí Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3