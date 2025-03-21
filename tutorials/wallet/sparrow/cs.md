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

Upozorňujeme, že pokud použijete ořezaný uzel Bitcoin Core, nebudete moci obnovit uzel Wallet obsahující transakce, které předcházely lokálně uloženým blokům. Pro nový uzel Wallet vytvořený v uzlu Sparrow to však nebude problém: vaše nové transakce budou viditelné i v případě ořezaného uzlu.

Konfiguraci uzlu Bitcoin Core můžete provést podle některého z následujících návodů v závislosti na operačním systému:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
V aplikaci Sparrow přejděte na kartu "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**S místním jádrem Bitcoin:**

Pokud je v počítači nainstalováno jádro Bitcoin, vyhledejte soubor `Bitcoin.conf` mezi softwarovými soubory. Pokud tento soubor neexistuje, můžete jej vytvořit. Otevřete jej pomocí textového editoru a vložte následující řádek:

```ini
server=1
````
Sauvegardez ensuite vos modifications.
Vous pouvez également effectuer cette configuration via l'interface graphique de Bitcoin-QT en naviguant dans "*Settings*" > "*Options...*" et en activant l'option "*Enable RPC server*".
N'oubliez pas de redémarrer le logiciel après ces modifications.
![Image](assets/fr/08.webp)
Revenez ensuite à Sparrow Wallet et renseignez le chemin vers votre fichier de cookie, généralement situé dans le même dossier que le `bitcoin.conf`, selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
![Image](assets/fr/09.webp)
Laissez les autres paramètres par défaut, l'URL `127.0.0.1` et le port `8332`, puis cliquez sur "*Test Connection*".
![Image](assets/fr/10.webp)
La connexion est établie. Une coche verte apparaîtra en bas à droite pour indiquer que vous êtes connecté à un nœud Bitcoin Core.
![Image](assets/fr/11.webp)
**Avec Bitcoin Core à distance :**
Si Bitcoin Core est installé sur une autre machine connectée sur le même réseau, commencez par localiser le fichier `bitcoin.conf` parmi les fichiers du logiciel. Si ce fichier n'existe pas encore, vous pouvez le créer. Ouvrez ce fichier avec un éditeur de texte et ajoutez la ligne suivante :
```

server=1

```
Après avoir modifié le fichier, assurez-vous de l'enregistrer dans le dossier approprié selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
Il est également possible de réaliser cette manipulation via l'interface graphique de Bitcoin-QT. Accédez au menu "*Settings*", puis "*Options...*", et activez l'option "*Enable RPC server*" en cochant la case correspondante. Si le fichier `bitcoin.conf` n'existe pas, vous pouvez le créer directement depuis cette interface en cliquant sur "*Open Configuration File*".
![Image](assets/fr/12.webp)
Trouvez l'adresse IP de la machine qui héberge Bitcoin Core dans votre réseau local. Pour cela, vous pouvez utiliser un outil tel que [Angry IP Scanner](https://angryip.org/). Supposons, pour l'exemple, que l'adresse IP de votre nœud soit `192.168.1.18`.
Dans le fichier `bitcoin.conf`, ajoutez les lignes suivantes, en configurant `rpcbind=192.168.1.18` pour correspondre à l'adresse IP de votre nœud.
```

[ruka]

rpcbind=127.0.0.1

rpcbind=192.168.1.18

rpcallowip=127.0.0.1

rpcallowip=192.168.1.0/24

```
![Image](assets/fr/13.webp)
Ajoutez également dans le fichier `bitcoin.conf` un identifiant et un mot de passe pour les connexions à distance. Assurez-vous de remplacer `loic` par votre nom d'utilisateur et `my_password` par un mot de passe fort :
```

rpcuser=loic

rpcpassword=my_password

```