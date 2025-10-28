---
name: Spectre Desktop
description: Spravujte svá portfolia Bitcoin s více podpisy zcela suverénně pomocí vlastního uzlu
---

![cover](assets/cover.webp)



Specter Desktop je open source aplikace (licence MIT) vyvíjená společností Cryptoadvance od roku 2019, která usnadňuje správu peněženek Bitcoin s hardwarovými peněženkami (Ledger, Trezor, Coldcard, BitBox02, Passport atd.) a vlastní infrastrukturou Bitcoin (uzel Bitcoin core nebo Electrum Server). Aplikace vyniká zejména v konfiguracích s více podpisy a umožňuje zabezpečit velké částky rozdělením podpisového výkonu mezi několik nezávislých hardwarových peněženek.



**V tomto kurzu se dozvíte, jak:**




- Instalace a konfigurace aplikace Specter Desktop v počítači (Windows, macOS nebo Linux)
- Připojte Spectre k zařízení Electrum Server (v tomto příkladu použijeme Umbrel)
- Vytvoření jednoduché karty Wallet pomocí karty Hardware Wallet (Coldcard)
- Přijímání a odesílání bitcoinů s naprostou suverenitou
- Nastavení vícepodpisového systému Wallet 2 na 3 s několika hardwarovými peněženkami
- Instalace programu Spectre na server Umbrel (bonus pro pokročilé)



Všechny vaše transakce budou ověřovány lokálně prostřednictvím vaší vlastní infrastruktury, bez přenosu informací na externí servery, což zaručuje důvěrnost a finanční suverenitu. Před podpisem vždy zkontrolujte transakce na obrazovce Hardware Wallet.



## Stažení a instalace



Navštivte oficiální webové stránky aplikace Specter Desktop a stáhněte si ji.



![Page d'accueil Specter](assets/fr/01.webp)



Na stránce pro stažení vyberte verzi odpovídající vašemu operačnímu systému: MacOS, Windows nebo Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Po stažení nainstalujte aplikaci podle obvyklých pokynů operačního systému. V případě systému macOS přetáhněte ikonu do složky Aplikace. V případě systému Windows spusťte instalační program. V případě Linuxu postupujte podle pokynů v balíčku.



## Počáteční konfigurace



Při prvním spuštění vás aplikace Specter Desktop vyzve k výběru typu připojení. Můžete se připojit k uzlu Electrum Server nebo k vlastnímu uzlu Bitcoin core.



![Choix du type de connexion](assets/fr/03.webp)



V tomto příkladu použijeme připojení k serveru Electrum Server se systémem Umbrel.



Další informace naleznete v našem výukovém programu Umbrel:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Tato možnost nabízí rychlejší synchronizaci než Bitcoin core. Pokud dáváte přednost, můžete zvolit "Bitcoin core" a nakonfigurovat připojení k místnímu uzlu. Následující kroky zůstávají stejné bez ohledu na vaši volbu.



Vyberte možnost "Electrum Connection" a poté zvolte "Enter my own" pro konfiguraci vlastního Electrum Server.



![Configuration Electrum](assets/fr/04.webp)



Zadejte číslo Address svého modelu Electrum Server. V našem případě s Umbrel bude Address `umbrel.local` s portem `50001`. Klepnutím na tlačítko "Connect" (Připojit) navažte spojení.



Po připojení se zobrazí uvítací obrazovka s kontrolním seznamem, který vám pomůže začít. Nyní je třeba přidat hardwarové peněženky.



![Écran d'accueil](assets/fr/05.webp)



## Přidání zařízení Hardware Wallet



V levé nabídce klikněte na možnost "Add device" a přidejte zařízení Hardware Wallet.



Spectre Desktop podporuje řadu hardwarových peněženek: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault a mnoho dalších.



Pokud se chcete dozvědět více, podívejte se na naše výukové programy Hardware Wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Vyberte si Hardware Wallet. V tomto příkladu používáme kartu Coldcard MK4.



Níže naleznete náš výukový program pro tento Hardware Wallet :



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

V případě karty Coldcard je třeba exportovat veřejné klíče z Hardware Wallet buď prostřednictvím připojení USB, nebo karty microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Při exportu klíčů z karty Coldcard postupujte podle zobrazených pokynů. Pojmenujte svůj Hardware Wallet (zde "MK4 Tuto"). Po importu klíčů můžete vytvořit Wallet s jediným klíčem nebo přidat další hardwarové peněženky pro Wallet s více podpisy.



![Dispositif ajouté](assets/fr/08.webp)



## Vytvoření portfolia



Po přidání Hardware Wallet klikněte na "Create single key Wallet" a vytvořte Wallet s jedním podpisem.



Pojmenujte své portfolio (např. "Wallet pro tuto") a vyberte typ Address. Chcete-li používat nativní adresy BECH32, které optimalizují transakční náklady, vyberte možnost "SegWit".



![Configuration du portefeuille](assets/fr/09.webp)



Po vytvoření portfolia vám společnost Specter nabídne uložení záložního souboru PDF obsahujícího všechny veřejné informace potřebné k obnovení portfolia (deskriptory, rozšířené veřejné klíče). Tento soubor neobsahuje vaše soukromé klíče.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Přijímání bitcoinů



Chcete-li přijímat bitcoiny, vyberte v levém menu svůj účet Wallet a klikněte na kartu "Přijmout".



Spectre automaticky vygeneruje nový příjem Address s QR kódem.



![Génération d'une adresse de réception](assets/fr/11.webp)



Kód Address můžete zkopírovat nebo naskenovat QR kód. Vždy zkontrolujte Address na obrazovce Hardware Wallet, než jej někomu předáte.



## Zobrazení historie a adres



Jakmile obdržíte bitcoiny, můžete si své transakce prohlédnout na kartě "Transakce".



![Historique des transactions](assets/fr/12.webp)



Na kartě "Adresy" si můžete prohlédnout všechny adresy vygenerované vaším portfoliem, jejich stav využití a související částky.



![Liste des adresses](assets/fr/13.webp)



## Odeslat bitcoiny



Chcete-li poslat bitcoiny, klikněte na kartu "Odeslat". Zadejte číslo Address příjemce, částku, která má být odeslána, a zaškrtněte rozšířené možnosti, pokud si přejete ručně vybrat UTXO (kontrola Coin).



![Création d'une transaction](assets/fr/14.webp)



Kliknutím na tlačítko "Vytvořit nepodepsanou transakci" vytvoříte transakci. Spectre vás poté požádá o podepsání transakce pomocí Hardware Wallet.



![Signature de la transaction](assets/fr/15.webp)



Pokud používáte kartu Coldcard, máte na výběr mezi podpisem přes USB a kartou microSD (s air-gapped). Potvrďte transakci na obrazovce Hardware Wallet a pečlivě zkontrolujte cílové místo Address a částku.



Po podepsání transakce ji můžete vysílat v síti Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Kliknutím na "Odeslat transakci" transakci odešlete. Spectre potvrdí, že transakce byla odeslána, a její stav můžete sledovat na kartě Transakce.



![Diffusion de la transaction](assets/fr/17.webp)



## Vytvoření a používání portfolia s více podpisy



Jednou z hlavních předností aplikace Specter Desktop je její schopnost zjednodušit správu portfolií s více podpisy. Multisig Wallet vyžaduje k autorizaci transakce více podpisů, čímž se eliminuje jediný bod selhání. Například konfigurace 2 na 3 vyžaduje k potvrzení jakéhokoli výdaje dva podpisy ze tří samostatných hardwarových peněženek.



Chcete-li vytvořit Multisig Wallet, začněte přidáním všech podepisujících hardwarových peněženek prostřednictvím "Přidat zařízení". V tomto příkladu budeme používat tři různé hardwarové peněženky: Coldcard MK4 (již přidaná dříve), Passport a Ledger. Tato diverzifikace výrobců posiluje bezpečnost tím, že zabraňuje závislosti na jediném řetězci nebo firmwaru Supply.



Zde jsou odkazy na výukové programy Ledger a Passport:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Přidejte zařízení Passport pojmenováním Hardware Wallet (např. "Passport multi") a importem jeho klíčů prostřednictvím karty microSD nebo kódu QR. Poté pokračujte kliknutím na "Continue" (Pokračovat).



![Ajout du Passport](assets/fr/23.webp)



Poté přidejte zařízení Ledger připojením přes USB a otevřením aplikace Bitcoin na zařízení Hardware Wallet. Pojmenujte jej (např. "Ledger multi") a kliknutím na "Get via USB" a poté na "Continue" importujte jeho veřejné klíče.



![Ajout du Ledger](assets/fr/24.webp)



Po registraci tří hardwarových peněženek ve Spectru klikněte na "Add Wallet" a výběrem možnosti "Multiple Signature" vytvořte Wallet s více podpisy.



![Choix du type de wallet](assets/fr/25.webp)



Vyberte tři hardwarové peněženky, které chcete zahrnout do svého multipodpisového kvora: Vyberte MK4 Tuto, Passport multi a Ledger multi. Kliknutím na tlačítko "Pokračovat" přejděte k dalšímu kroku.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Zvolte konfiguraci více podpisů. Vyberte "SegWit" jako typ Address, abyste mohli využívat optimalizované poplatky. Parametr "Požadované podpisy pro autorizaci transakcí (m ze 3)" umožňuje definovat prahovou hodnotu: pro konfiguraci 2 na 3 jsou vyžadovány 2 podpisy. U každého Hardware Wallet se zobrazí odpovídající klíč Multisig. Klepnutím na "Create Wallet" (Vytvořit Wallet) dokončíte vytváření.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Vaše portfolio s více podpisy "Multi tuto" je nyní vytvořeno. Společnost Specter okamžitě doporučuje uložit záložní soubor PDF obsahující portfolio Descriptor. Kliknutím na "Save Backup PDF" (Uložit záložní soubor PDF) si tento kritický soubor stáhněte.



![Wallet multisig créé](assets/fr/28.webp)



Spectre také umožňuje exportovat informace o Wallet do každé z vašich hardwarových peněženek prostřednictvím QR kódu nebo souboru. To umožňuje některým hardwarovým peněženkám (například Coldcard nebo Passport) ukládat konfiguraci Multisig přímo do jejich paměti.



Pro Passport odemkněte zařízení a poté přejděte na "Spravovat účet" > "Připojit Wallet" > "Specter" > "Multisig" > "QR kód" a naskenujte QR kód vygenerovaný aplikací Specter. Passport vás poté požádá o naskenování přijímacího Address z vašeho Wallet, abyste potvrdili konfiguraci Multisig.



Pokud jde o MK4, připojte jej k počítači a odemkněte jej. Poté klikněte na "Save MK4 Tuto file" a uložte soubor do MK4. Při příštím přihlášení Hardware Wallet použije MK4 tento soubor k dokončení konfigurace Multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Pro vaši informaci můžete kdykoli přistupovat k zálohám na kartě "Nastavení" svého portfolia a poté "Exportovat":



![Accès au backup PDF](assets/fr/30.webp)



Každodenní používání zůstává podobné jako u jednoduchého Wallet: vy generate přijímáte adresy jako obvykle. Chcete-li poslat bitcoiny, přejděte na kartu "Odeslat", zadejte Address příjemce a částku a poté klikněte na "Vytvořit nepodepsanou transakci".



![Création d'une transaction multisig](assets/fr/31.webp)



Spectre sestaví PSBT (Partially Signed Bitcoin Transaction) a zobrazí "Acquired 0 of 2 signatures". Nyní musíte podepsat alespoň dvě ze tří hardwarových peněženek. Klikněte na první Hardware Wallet (např. "MK4 Tuto"), abyste získali podpis pomocí karty Coldcard, a poté na druhou (např. "Passport multi"), abyste získali druhý požadovaný podpis.



![Signature de la transaction](assets/fr/32.webp)



Once you have obtained the 2 required signatures (Interface displays "Acquired 2 of 2 signatures" and "Transaction is ready to send"), click on "Send Transaction" to broadcast the transaction on the Bitcoin network.



![Transaction prête à être diffusée](assets/fr/33.webp)



This multi-signature approach is particularly well suited to companies (several managers need to approve expenditure), families (protection of a multi-generational inheritance), or individuals managing large sums (geographical distribution of hardware wallets to withstand localized disasters).



### The critical importance of multisignature backups



**Please note**: backing up a multi-signature portfolio is fundamentally different from backing up a single portfolio. Your recovery phrases (seed phrases) alone are not sufficient to restore a Multisig portfolio. You must also back up the **output descriptor** (output descriptor), which contains the configuration information for your multisignature portfolio.



The output descriptor includes essential data: the extended public keys (xpubs) of each co-signer, the signature threshold (2-on-3 in our example), the type of script used (SegWit native, nested or legacy), and the derivation paths for each Hardware Wallet. Without this Descriptor, even if you have two of your three recovery phrases, you won't be able to rebuild your Wallet or access your bitcoins. The Descriptor lets your software know how to combine the public keys to generate the Bitcoin addresses corresponding to your funds.



Specter Desktop automatically generates a backup PDF file when you create your Multisig portfolio. This PDF contains the complete Descriptor, the fingerprints of each Hardware Wallet, and all the public information required for restoration. **This file does not contain your private keys** and therefore does not by itself allow you to spend your bitcoins, but it does allow anyone accessing it to see your complete transaction history and balance.



To back up your multisignature configuration correctly, follow this procedure: after creating your portfolio, click on the "Settings" tab, then "Export" and select "Save Backup PDF". Create several copies of this PDF: print at least two copies on paper, and also keep an encrypted digital copy. Store one copy of the PDF with each of your recovery phrases, in geographically separate locations.



Burn your recovery phrases on fireproof and waterproof metal plates to guarantee their longevity. Never underestimate the importance of these backups: if you lose your computer's `~/.specter` folder AND you lose one of your hardware wallets without a Descriptor backup, all your funds will be irretrievably lost, even with a 2-on-3 configuration. Multi-signature redundancy protects against the loss of a Hardware Wallet, but only if you have correctly backed up your Wallet's Descriptor.



## Advantages and limitations of Specter Desktop



**Benefits**: Optimum confidentiality with complete local validation without third-party servers. Multisignature flexibility for advanced configurations (corporate, family, individual). Extensive Hardware Wallet support with full interoperability (USB and air-gapped).



**Limitations**: Significant learning curve on advanced Bitcoin concepts (UTXOs, descriptors, derivation paths).



## Best practices



Always check addresses and amounts on your Hardware Wallet screen before validation, to protect yourself against malware.



Keep PDF backups separate from your seeds. These public descriptors can be stored in a bank vault or encrypted cloud, facilitating recovery without exposing your private keys.



Test recovery on token amounts before using your portfolios with large funds. Create, test, delete and restore to validate your procedures.



Keep Specter and your firmware up to date. Distribute your multi-signature co-signers geographically (home/office/nearby) to withstand localized disasters. Use descriptive labels to facilitate accounting and tax returns.



## Bonus: Installation on a Bitcoin server (Umbrel, RaspiBlitz, Start9)



If you already own a Bitcoin server such as Umbrel, RaspiBlitz, MyNode or Start9, you can install Specter Desktop directly from their application store. This approach offers several significant advantages: the application automatically configures itself with your local Bitcoin core node, it remains accessible 24/7 via a Interface web from any device on your network, and you can even access it securely remotely via Tor. Your entire Bitcoin infrastructure is centralized on a single dedicated server, simplifying management and strengthening your sovereignty.



### Installation from the Umbrel App Store



From your Umbrel Interface, go to the App Store and search for Specter Desktop. Click on "Install" to launch the installation.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Once installation is complete, open Specter Desktop on your Umbrel. The welcome screen will ask you to choose your connection type. If you're using Specter on your Umbrel, click on "Update settings" to configure the connection.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Select "Remote Specter USB connection" to enable the use of USB hardware wallets connected to your local computer while using Specter on the remote Umbrel server.



![Configuration Remote Specter USB](assets/fr/20.webp)



Follow the instructions displayed to configure the HWI Bridge. You need to access the device bridge settings and add the domain `http://umbrel.local:25441` to the whitelist. Click on "Update" to save the configuration.



![HWI Bridge Settings](assets/fr/21.webp)



If you'd also like to use your USB hardware wallets from your local computer, download the Specter Desktop application to your machine and set it to "Yes, I run Specter remotely". Click on "Save" to finalize the configuration.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Conclusion



Specter Desktop democratizes advanced Bitcoin configurations, making multi-signature accessible without sacrificing sovereignty or confidentiality. For users managing significant amounts of money, it transforms institutional practices into solutions that can be deployed by private individuals.



Although the application requires an initial investment in infrastructure and learning, it offers complete sovereignty: control of the validation infrastructure, physical Ownership of keys, and transactions free from third-party surveillance. Whether you're an individual securing your savings, a family creating a multi-generational safe-deposit box, or a company managing cash flow, Specter Desktop is the reference tool for reconciling maximum security and absolute sovereignty.



## Resources



### Official documentation




- [Specter Desktop official website](https://specter.solutions/desktop/)
- [GitHub source code](https://github.com/cryptoadvance/specter-desktop)
- [Complete documentation](https://docs.specter.solutions/)



### Community and support




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Reddit discussion forum](https://reddit.com/r/specterdesktop/)
- [GitHub bug reports](https://github.com/cryptoadvance/specter-desktop/issues)