---
name: Koordinátor Coinjoin - WabiSabi
description: Jak nastavit a spustit koordinátor coinjoin podle protokolu WabiSabi (použitého v Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Úvod 👋


V tomto odborném průvodci vám pomůžeme nastavit coinjoin koordinátora, což je v podstatě server, který sdružuje lidi, kteří chtějí ušetřit na transakčních poplatcích nebo zvýšit své soukromí v onchainu při společných transakcích. Vzhledem k tomu, že s Wasabi Wallet již není dodáván koordinátor provozovaný společností, musí si uživatelé najít a vybrat svůj vlastní preferovaný server koordinátora. Objevilo se jen několik koordinátorů, které požadují 0% koordinační poplatek, takže vývojáři Wasabi Wallet usilovně pracují na tom, aby bylo co nejjednodušší začít provozovat vlastní komunitní koordinátor (na tak malém hardwaru, jako je Raspberry Pi5!). Aktuálně aktivní koordinátory, kteří žádají 0% koordinační poplatek, najdete na [LiquiSabi](https://liquisabi.com) a hlavně na [nostr](https://github.com/Kukks/WasabiNostr).


## Požadavky 🫴



- VPS (hostovaný uzel) nebo počítač/server (samostatně hostovaný uzel)
- Ořezaný/úplný uzel jádra Bitcoin (testováno s verzí 29.0)


Volitelně:


- (sub)doména předávající provoz do uzlu (např. coinjoin.[yourdomain].io)


Doporučujeme mít určité zkušenosti s příkazovým řádkem a bashem, protože ne všechny kroky lze automatizovat.


Z hlediska hardwaru se doporučuje mít systém s:


- 4 jádra
- 16 GB RAM
- 2 TB SSD nebo NVMe (pro celý uzel) / 128 GB SSD (pro uzel pruned)


Takové požadavky může splnit Raspberry Pi 5 za pouhých 120 dolarů, bez úložiště, které stojí asi 100 dolarů za 2TB NVMe disk.


Levné VPS jsou obvykle vybaveny pouze 1 jádrem a 4 GB RAM, což je podle mého názoru příliš málo na synchronizaci a ověření celého bitcoinového blockchain na blockheight 911817.


Z hlediska úložiště bude plný uzel vyžadovat minimálně 2 TB diskového úložiště, nejlépe typu SSD nebo NVMe. Při ořezávání blockchain je přijatelný mnohem menší úložný disk (např. 128GB SSD).


Pokud máte v úmyslu spustit koordinátor pro velké (300+ vstupů) spojení mincí, doporučujeme zvolit systém s rychlejšími/novějšími jádry s vyšším výkonem pro všechna ověření podpisu.


## Instalace 🛠️


Na uzlu chceme stáhnout a nainstalovat nejnovější vydanou verzi Wasabi Wallet, která obsahuje backend a koordinátor jako samostatné spustitelné soubory vedle wallet.


Najděte nejnovější verzi: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) a ověřte podpis PGP verze pomocí klíčů: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Podrobnosti o nasazení se liší v závislosti na hardwaru (architektuře procesoru) a výběru operačního systému, níže jsou uvedeny různé podrobnosti pro Raspberry Pi (ARM-64) s Debian založeným na RaspiBlitz jako výchozím bodem. Pro nasazení operačního systému Ubuntu (X86-64) pomocí Nixu přeskočte.


Pokyny k instalaci najdete zde: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Nasazení RaspiBlitz/Debian


Pro uzly RaspiBlitz (testováno s verzí v1.11) lze použít nasazení script sestavené ze zdrojového kódu: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Snadné nasazení


Pro minimální nasazení stačí rozbalit spustitelné soubory pro vaši platformu do složky.

Příklady kódů příkazového řádku pro Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Výsledkem by měla být následující platná podpisová zpráva:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Stažený balíček můžete nainstalovat:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfigurace 🧾


Před spuštěním koordinátoru je třeba upravit soubor Config.json pomocí vašeho:


- Bitcoin RPC pověření
- Preferované parametry kola
- Rozšířený veřejný klíč koordinátora (vytvoření nového SegWit wallet pro příjem shromážděného prachu)

**Upozornění**: Taproot wallet budou mít za následek nevyužitelné UTXO! Zde použijte nativní Segwit wallet.


- Povolené typy vstupních a výstupních adres
- Konfigurace oznamovatele pro publikování přes nostr (název, popis, Uri, minimální vstupy, nostr relay, nostr privátní klíč)


Můžete spustit koordinátora přístupného pouze přes adresu .onion nebo použít vlastní doménu clearnetu.


Najděte nebo vytvořte konfigurační soubor na této cestě:


`~/.walletwasabi/coordinator/Config.json`


Upravte jej pomocí příkazu:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Viz tento příklad souboru Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Konfigurace Tor 🧅


Chcete-li vyplnit klíč OnionServicePrivateKey, budete jej pravděpodobně muset nejprve vygenerovat.


Wasabi Wallet vám vygeneruje soukromý klíč, pokud jej poprvé spustíte s nastavením ```"PublishAsOnionService": true,``` v souboru Config.json.


Spusťte koordinátor jednou příkazem:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Chcete-li zjistit adresu skryté služby Onion, zkontrolujte protokoly koordinátora pomocí:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


a najdete něco jako:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Dlouhá adresa URL končící na .onion je vaše skrytá adresa služby nebo CoordinatorUri.


Nebo znovu zkontrolujte konfigurační soubor koordinátoru pomocí:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Ta by se nyní měla vyplnit automaticky.


## Běh ⚡


Po nastavení všech konfiguračních parametrů můžete spustit službu koordinátora a začít oznamovat první kolo 🕶️


Stačí spustit koordinátor příkazem:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Aktuální kolo a počet registrovaných UTXO/monet můžete sledovat (v prohlížeči Tor pro .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Volitelné: ladění serveru koordinátora


Případné problémy nebo chyby můžete sledovat v souboru protokolu na adrese ```~/.walletwasabi/backend/Logs.txt````


Mezi typické problémy patří problémy s připojením RPC, které je třeba povolit v ```~/.bitcoin/bitcoin.conf``` pomocí:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Volitelně: Spuštění backendového serveru


Spolu s koordinátorem můžete také poskytnout backendový server pro uživatele, kteří nemají vlastní bitcoinový uzel, ke kterému se mohou připojit pro odhady poplatků a blokové filtry.


Spusťte tuto službu příkazem:


```
wbackend
```


## Pozvání uživatelů Wasabi k vašemu koordinátorovi 🫂


Aby vaši službu našli i ostatní uživatelé, můžete se spolehnout na oznamovatele nostr nebo sdílet kouzelný odkaz s vaší doménou (clearnet) nebo skrytou službou (.onion link) a kulatými parametry, jako je tento:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Když uživatel zkopíruje kouzelný odkaz a otevře svůj program Wasabi Wallet, software automaticky zobrazí dialogové okno koordinátora s vaší doménou a parametry.


![detected](assets/en/02.webp)


💚🍣 Gratulujeme k decentralizaci soukromí bitcoinu 🕶️


Nezapomeňte na svůj výcvik [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet je určen pouze pro obranu 🛡️