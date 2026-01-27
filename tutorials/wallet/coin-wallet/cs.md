---
name: Coin Wallet
description: Výukový kurz o Coin Wallet a způsobech zvýšení ochrany soukromí a bezpečnosti
---

![cover](assets/cover.webp)


Tento tutoriál se zabývá [Coin Wallet](https://coin.space/) - samospustitelným šifrovacím modulem wallet pro mobilní zařízení a tím, jak zvýšit bezpečnost a soukromí při používání mobilních aplikací wallet.



## O Coin Wallet


**Coin Wallet** je otevřený zdrojový kód wallet, který vytvořil tým nadšenců Bitcoin v roce 2015. Začal jako webová aplikace, v roce 2017 následovala aplikace pro iOS a v roce 2020 aplikace pro Android - k dispozici na Google Play, Samsung Galaxy Store a Huawei AppGallery.


Hlavní výhody:


- Architektura bez vazby
- Plně [open-source kód](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Jednoduchý a čistý design
- Zaměřeno na hlavní účel - bezpečné ukládání kryptoměn bez zbytečných funkcí
- Podpora různých platforem: mobilní zařízení (iOS a Android), stolní počítače, web
- Podpora RBF (Replace-By-Fee) - urychlení zaseknutých transakcí kdykoli
- Hardwarová 2FA s klíčem [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2
- Vestavěná podpora sítě Tor - směrování veškerého provozu přes síť Tor pro maximální soukromí



## 1️⃣ Instalace Coin Wallet

Coin Wallet je k dispozici na všech hlavních platformách.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Všechny odkazy na vydání](https://github.com/CoinSpace/CoinSpace/releases)


K dispozici je také pro počítače (Windows, Linux, macOS), jako webová aplikace a přes Tor.


![image](assets/en/01.webp)


## 2️⃣ Vytvoření účtu Wallet a nastavení kódu PIN


Znak wallet se vytváří pomocí znaku passphrase - náhodné posloupnosti 12 slov oddělených mezerami, která se generuje ze [seznamu 2048 slov](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet podporuje 12, 15, 18, 21 nebo 24slovné přístupové fráze importované z jiných peněženek.


passphrase je lidsky čitelná forma hlavního soukromého klíče. Musí být bezpečně uložen. Pro přístup k serveru wallet nebo jeho obnovení je zapotřebí pouze klíč passphrase. Pokud dojde ke ztrátě klíče passphrase, je systém wallet a všechny finanční prostředky trvale ztraceny. Klíč passphrase nesmí být nikdy sdílen. Coin Wallet neukládá klíče na žádný server ani do žádné databáze.


**Je 12 slov passphrase bezpečných?**

S 2048 možnými slovy na pozici existuje 2048¹² ≈ 10³⁹ kombinací - což poskytuje ~128 bitů zabezpečení, srovnatelné s privátními klíči Bitcoin. Tato úroveň je všeobecně považována za dostatečnou.


![image](assets/en/02.webp)


Po zapsání a potvrzení kódu passphrase aplikace požádá o nastavení čtyřmístného kódu PIN** pro každodenní přístup. Pro větší pohodlí můžete místo kódu PIN povolit biometrické ověřování (otisk prstu nebo rozpoznání obličeje).


![image](assets/en/03.webp)



Neexistuje žádný účet, žádné obnovení klíče, žádný reset passphrase ani zrušení transakce. Za bezpečnost je plně odpovědný uživatel.


Podrobné osvědčené postupy pro uložení mnemotechnické fráze:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Fráze + PIN. Kdy a jak se používají


**Kdy je vyžadován passphrase?**

Pouze v těchto vzácných případech:


- Nastavení wallet v novém zařízení
- Přeinstalování aplikace Coin Wallet
- Vymazání dat aplikace/prohlížeče (místní úložiště)
- Odebrání hardwarového klíče z účtu
- Třikrát zadat špatný kód PIN (aplikace se z bezpečnostních důvodů uzamkne)


Při každodenním používání stačí k odemknutí wallet čtyřmístný kód PIN.


**Passphrase + PIN: Jak to funguje**

passphrase je skutečný hlavní soukromý klíč a funguje na jakémkoli zařízení.

Protože by bylo nepohodlné pokaždé zadávat 12-24 slov, používá Coin Wallet čtyřmístný kód PIN pro rychlý každodenní přístup k aktuálnímu zařízení.

Samotný kód PIN není dostatečně bezpečný pro přímou ochranu hlavního klíče, proto se k šifrování nikdy nepoužívá. Namísto toho se používá tzv:



- Kód PIN je odeslán na server a vyměněn za dlouhý kryptografický kód token.
- token dešifruje zašifrovaný hlavní klíč uložený pouze v zařízení.


Pokud je kód PIN zadán třikrát nesprávně, server trvale odstraní kód token. Lokálně uložený klíč se stane nepoužitelným a jediným způsobem, jak obnovit wallet, je zadání původního passphrase.

Tato konstrukce poskytuje pohodlí i silnou záložní ochranu.



## 4️⃣ Přijímání ₿itcoinů - typy Address a ochrana osobních údajů


Coin Wallet podporuje všechny tři formáty adres Bitcoin:



- Nativní SegWit (Bech32)** - začíná na **bc1q** - nejnižší poplatky, doporučeno
- Vložený SegWit (P2SH)** - začíná na **3**
- Legacy (P2PKH)** - začíná na **1**


![image](assets/en/04.webp)


**Proč se adresa po každém vkladu mění?**

Je to záměrné a chrání to soukromí. Při každém příjmu mincí generuje Coin Wallet automaticky novou nepoužitou adresu. Pokud by se stejná adresa používala opakovaně (například pro měsíční výplatu), mohl by kdokoli snadno sečíst všechny příchozí transakce v průzkumníku blockchainu a zjistit celkový příjem.


Staré adresy zůstávají navždy platné - můžete na ně stále přijímat, ale doporučuje se používat pokaždé novou adresu.


**Jak získat Bitcoin:**

1. Otevřete minci

2. Klepněte na položku **Příjem**

3. Vyberte požadovaný typ adresy (nejlépe **bc1q** - `Nativní SegWit`)

4. Zobrazte kód QR nebo zkopírujte adresu a odešlete ji plátci


**Volitelně - Mecto (pro osobní platby):**

Na stejné obrazovce Příjem je tlačítko `Mecto`.

Po zapnutí:


- Budete požádáni o zadání **nickname** (gravatar)
- Vaše aktuální poloha + adresa pro příjem jsou dočasně sdíleny s ostatními uživateli Coin Wallet, kteří mají také povolenou funkci Mecto
- Mohou vás objevit na malé mapě a poslat mince bez psaní nebo skenování


Data jsou viditelná pouze pro ostatní uživatele Mecto a jsou automaticky smazána po 1 hodině (nebo okamžitě po vypnutí).

Funkce Mecto je zcela volitelná - pokud dáváte přednost maximálnímu soukromí, nechte ji vypnutou.


![image](assets/en/05.webp)


## 5️⃣ Odesílání ₿itcoin


Odeslání Bitcoin:


1. Otevřete minci → klepněte na **Odeslat**

2. Vložte adresu nebo naskenujte QR kód

3. Zadejte částku (nebo klepněte na **Max**)

4. Zvolte rychlost transakce:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Potvrďte čtyřmístným kódem PIN → transakce se vysílá


### Jak urychlit čekající ₿itcoinovou transakci (RBF)


Pokud jste zvolili pomalý poplatek a transakce se zasekla:


1. Přejděte na kartu **Historie**

2. Klepněte na čekající transakci

3. Klepněte na tlačítko **Accelerate** (Replace-By-Fee)

4. Potvrdit → transakce bude přeposlána s vyšším poplatkem


Akcelerace RBF je v současné době podporována pro:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Více o Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Exportování soukromých klíčů


**Kdy vlastně potřebujete soukromý klíč?**

(99 % uživatelů to nikdy neudělá - stačí jim 12 slov passphrase)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Jak exportovat soukromé klíče v Coin Wallet


1. Otevřít **Bitcoin (BTC)**

2. Přejděte na konec stránky a klepněte na možnost **Exportovat soukromé klíče**

3. Aplikace zobrazuje každou adresu se zůstatkem + její soukromý klíč ve formátu **WIF** (začíná na 5, K nebo L) a kód QR.


Zobrazí se pouze neprázdné adresy.


**Příklad klíče WIF**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Co dělat dál (doporučeno)**


- Otevřít Electrum, Sparrow, BlueWallet nebo jakýkoli hardware wallet
- Importovat/vymazat soukromý klíč
- Všechny prostředky se okamžitě přesunou na novou zabezpečenou adresu pod vaším současným číslem seed


Nikdy neukládejte soukromý klíč digitálně v prostém textu. Po zametení jej můžete bezpečně smazat.


Kompletní průvodce soukromými klíči a cestami odvození: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Technické podrobnosti - BIP39, BIP32 a odvozené cesty


Coin Wallet striktně dodržuje oficiální standardy Bitcoin, které používají téměř všechny seriózní peněženky.


`BIP39` - jak se z passphrase stává hlavní soukromý klíč


- Výchozí počet slov: 12
- Volitelné heslo passphrase/password: žádné ("")
- Počáteční entropie: 128 bitů (12 slov) → 256 bitů (24 slov)
- Implementace s otevřeným zdrojovým kódem: https://github.com/paulmillr/scure-bip39
- Seznam slov: standardní anglický seznam 2048 slov
- Podporuje import 12, 15, 18, 21 a 24slovných frází z jakéhokoli jiného programu BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - deterministické generování všech adres

Z jednoho hlavního klíče wallet může generate získat miliardy adres v přesně definovaném pořadí. Proto stejných 12 slov zadaných do Electrum, Sparrow, Trezoru, Ledger, BlueWallet atd. zobrazí přesně stejné adresy a zůstatky.


**Derivační cesty používané v Coin Wallet pro Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Uvnitř každé cesty:


- `/0` - externí řetězec (adresy, na které chcete přijímat platby)
- `/1` - interní řetězec (změna adres, které používá samotný wallet)


Vzhledem k tomu, že Coin Wallet se těmito veřejnými normami řídí beze změn, budou vaše prostředky i za 10-20-30 let zpětně získatelné v jakémkoli jiném kompatibilním wallet.


## 8️⃣ Zlepšení anonymity pomocí Toru


**Proč používat Tor v Coin Wallet**

Tor skrývá vaši skutečnou IP adresu před uzly, výměnnými stanicemi a pozorovateli Bitcoin.

Veškerý provoz (zůstatky, transakce, swapy) probíhá přes síť Tor - žádná přímá spojení, žádné úniky IP.

To je implementováno přímo ve zdrojovém kódu aplikace (viz [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet má skrytou adresu .onion a od verze 6.6.3 (prosinec 2024) **vybavenou podporu Toru přímo v mobilní aplikaci**.


### Jak povolit Tor v systému Android a iOS


1. **Instalace Orbot** - oficiální aplikace projektu Tor (zdarma)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Otevřete Orbot → klepněte na Start**

V seznamu vyberte možnost **Coin Wallet**, aby Tor používal pouze wallet (volitelné, ale doporučené)

Počkejte, dokud se nezobrazí nápis **"Připojeno "** (10-30 sekund)


3. **Otevřete Coin Wallet → Nastavení → Síť**

Zapnutí funkce **Používat Tor**


4. **Zkontrolujte stav**

V horní liště se objeví **fialová ikona Tor onion** → veškerý provoz je nyní směrován přes Tor


![image](assets/en/06.webp)


To je vše - váš mobilní telefon Coin Wallet je plně anonymní.


Užijte si soukromou správu kryptoměn!


## 📝 Závěr


[Coin Wallet](https://coin.space/) - jeden ze skutečných průkopníků Bitcoin wallet s desetiletou historií vývoje.

Je záměrně jednoduchá a soustředí se na své hlavní poslání: bezpečné uložení vaší kryptoměny.

Neobjevuje se zde žádná reklama, žádný informační kanál, žádné odběry, žádné sociální funkce, žádné rozptylující prvky - pouze čistý, rychlý, samoobslužný wallet, který dělá přesně to, co má.

Coin Wallet klade na první místo jednoduchost a bezpečnost - vždycky to tak bylo a vždycky to tak bude.


## 📖 Zdroje


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39