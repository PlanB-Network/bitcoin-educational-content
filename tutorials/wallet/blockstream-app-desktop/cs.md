---
name: Blockstream App - Desktop
description: Jak používat aplikaci Hardware Wallet s aplikací Blockstream v počítači?
---
![cover](assets/cover.webp)



## 1. Úvod



### 1.1 Cíl výuky





- Tento návod vysvětluje, jak pomocí aplikace **Blockstream** v počítači spravovat **řetězový** Bitcoin Wallet s **Hardware Wallet**, což umožňuje bezpečné transakce zaznamenané na hlavním Blockchain Bitcoin.
- Zahrnuje instalaci, počáteční konfiguraci, připojení Hardware Wallet a přijímání a odesílání bitcoinů v řetězci.
- Poznámka: Další výukové programy v přílohách se týkají Liquid, Watch-Only a mobilní aplikace.



### 1.2 Cílová skupina





- **Začátečníci**: Uživatelé, kteří chtějí spravovat své bitcoiny pomocí zabezpečeného softwaru pro stolní počítače a Hardware Wallet.
- **Středně pokročilí uživatelé**: Lidé, kteří chtějí pochopit, jak používat Hardware Wallet pro onchain transakce a možnosti ochrany soukromí, jako je Tor nebo SPV.



### 1.3. Základní informace o hardwarových peněženkách





- **Hardware Wallet**, **Cold Wallet**: Na rozdíl od peněženek **Hot** (softwarové peněženky v připojených zařízeních) se jedná o fyzické zařízení, které uchovává soukromé klíče v režimu offline a nabízí vysokou úroveň zabezpečení proti kybernetickým útokům.
- **Doporučené použití**:
    - Ideální pro zajištění velkých částek nebo dlouhodobých úspor.
    - Vhodné pro uživatele, kteří se zaměřují na bezpečnost a chtějí chránit své finanční prostředky před riziky spojenými s připojenými zařízeními.
- **Omezení**: Pro zobrazení zůstatků, adres generate a vysílání transakcí podepsaných Hardware Wallet je nutný software, například aplikace Blockstream.



## 2. Představujeme aplikaci Blockstream





- **Blockstream App** je mobilní (iOS, Android) a desktopová aplikace pro správu peněženek Bitcoin a aktiv na Liquid Network. Společnost Blockstream ji získala v roce 2016, jmenovala se *GreenAddress*, byla přejmenována na *Blockstream Green* (2019) a nyní se jmenuje *Blockstream app* (2025).
- **Klíčové vlastnosti**:
- **Onchain** transakce na Blockchain Bitcoin.
    - Transakce v síti **Liquid** (Sidechain pro rychlé a důvěrné výměny).
- Pouze **sledovaná portfolia** pro sledování fondů bez přístupu ke klíčům.
    - Možnosti ochrany osobních údajů: připojení přes **Tor**, připojení k **osobnímu uzlu** přes Electrum nebo ověření **SPV** pro snížení závislosti na uzlech třetích stran.
    - Funkce **Replace-by-fee (RBF)** pro urychlení nepotvrzených transakcí.
- **Kompatibilita**: Integruje hardwarové peněženky, jako je **Blockstream Jade**.
- **Interface**: Intuitivní pro začátečníky, s pokročilými možnostmi pro experty.
- **Poznámka**: Tato příručka se zaměřuje na použití v řetězci s Hardware Wallet ve verzi pro stolní počítače. Další návody uvedené jako přílohy se týkají použití v mobilní aplikaci, pro onchain, Liquid a funkce Watch-Only.



## 3. Instalace a nastavení aplikace Blockstream Desktop



### 3.1. stáhnout





- Přejděte na [oficiální webové stránky](https://blockstream.com/app/) a klikněte na "_Download Now_". Stáhněte si verzi odpovídající vašemu operačnímu systému (Windows, macOS, Linux).
- **Poznámka**: Ujistěte se, že stahujete z oficiálního zdroje, abyste se vyhnuli podvodnému softwaru.



### 3.2. počáteční konfigurace





- **Domovská obrazovka**: Při prvním otevření aplikace se zobrazí obrazovka bez nakonfigurovaného Wallet. Vytvořená nebo importovaná portfolia se zde zobrazí později.



![image](assets/fr/02.webp)





- **Přizpůsobení nastavení**: Klepněte na ikonu nastavení vlevo dole, upravte níže uvedené možnosti a poté opusťte Interface a pokračujte.



![image](assets/fr/03.webp)



#### 3.2.1. Obecné parametry





- V nabídce Nastavení klikněte na možnost "**Obecné**".
- **Funkce**: V případě potřeby změňte jazyk softwaru a aktivujte experimentální funkce.



![image](assets/fr/04.webp)



#### 3.2.2. Připojení přes Tor





- V nabídce Nastavení klikněte na položku "**Síť**".
- **Funkce**: Směřujte síťový provoz přes **Tor**, anonymní síť, která šifruje vaše připojení.
- **Proč?**: Skryjte svou IP adresu Address a chraňte své soukromí, což je ideální, pokud nedůvěřujete své síti (například veřejné Wi-Fi).
- **Nevýhoda**: Může zpomalit aplikaci kvůli šifrování.
- **Doporučení**: Pokud je pro vás důvěrnost prioritou, aktivujte Tor, ale otestujte rychlost připojení.



![image](assets/fr/05.webp)



#### 3.2.3. Připojení k osobnímu uzlu





- V nabídce Nastavení klikněte na možnost "**Vlastní servery a ověřování**".
- **Funkce**: Připojuje aplikaci k vlastnímu **kompletnímu uzlu Bitcoin** prostřednictvím **serveru Electrum**.
- **Proč?**: Poskytuje úplnou kontrolu nad daty Blockchain a eliminuje závislost na serverech Blockstream.
- **Předpoklad**: Předpoklad: nakonfigurovaný uzel Bitcoin.
- **Doporučení**: Pokročilí uživatelé, kteří chtějí maximální suverenitu.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Ověřování SPV





- V nabídce Nastavení klikněte na možnost "**Vlastní servery a ověřování**".
- **Funkce**: Používá **Zjednodušené ověření plateb (SPV)**, které stahuje hlavičky bloků a ověřuje vaše transakce pomocí důkazu o zařazení (Merkle), aniž by ukládalo kompletní Blockchain.
- **Proč?**: Snižuje závislost na výchozím uzlu Blockstream a zároveň je pro zařízení nenáročný.
- **Nevýhoda**: V porovnání s Full node je méně bezpečná, protože některé informace získává z uzlů třetích stran.
- **Doporučení**: Pokud nemůžete používat osobní uzel, ale pro optimální zabezpečení dáváte přednost uzlu Full node, aktivujte SPV.



![image](assets/fr/07.webp)



## 4. Připojení zařízení Hardware Wallet k aplikaci Blockstream



### 4.1. Předběžné úvahy



#### 4.1.1. Pro uživatele Ledger





- Blockstream Green podporuje pouze aplikaci **Bitcoin Legacy** na zařízeních Ledger (Nano S, Nano X).
- Kroky, které je třeba provést v aplikaci **Ledger Live** před připojením zařízení :


1. Přejděte do **"Nastavení "** → **"Experimentální funkce "** a aktivujte **vývojářský režim**.


2. Přejděte na **"My Ledger"** → **"App Catalogue "** a nainstalujte aplikaci **Bitcoin Legacy**


3. Před spuštěním Blockstream Green otevřete na Ledger aplikaci **Bitcoin Legacy** a navažte spojení.




- **Poznámka**: Při připojování se ujistěte, že je Ledger odblokován pomocí PIN kódu a že je aktivní aplikace Bitcoin Legacy.



#### 4.1.2 Inicializace zařízení Hardware Wallet





- Pokud nebyl váš Hardware Wallet (Ledger, Trezor nebo Blockstream Jade) nikdy používán (buď s Blockstream Green, nebo s jiným softwarem, jako je Ledger Live), musíte jej nejprve inicializovat. Tento krok zahrnuje v bezpečném prostředí, bez kamer a pozorovatelů:


1. **seed phrase generation / Mnemonic phrase** (12, 18 nebo 24 slov): Napište si ji pečlivě na kus papíru.


2. **Ověření fráze seed**: Ověřte import Wallet z uvedených slov, např. ověřením rozšířeného veřejného klíče. Provádí se před odesláním prostředků do Wallet a trvalým zajištěním fráze seed.


3. **Zabezpečení fráze seed**: Frázi uložte na fyzickém nosiči (papír nebo kov) a na bezpečném místě. Nikdy ji neukládejte digitálně (žádné snímky obrazovky, cloud ani e-mail).




- **Důležité**: Fráze seed je jediným prostředkem, jak získat zpět své finanční prostředky v případě ztráty nebo poruchy zařízení. Kdokoli s přístupem může vaše bitcoiny ukrást.
- **Zdroje** pro zálohování a kontrolu věty seed :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfigurace pro tento výukový program :





- Předpokládáme, že zařízení Hardware Wallet již bylo inicializováno pomocí fráze seed a uzamykacího kódu PIN.
- Předpokládáme, že zařízení Hardware Wallet nebylo nikdy připojeno k aplikaci Blockstream, což vyžaduje vytvoření nového účtu. Pokud již bylo zařízení Hardware Wallet s aplikací Blockstream App používáno, účet se automaticky zobrazí při otevření aplikace.



### 4.2. Spuštění připojení





- Na domovské obrazovce klikněte na "**Nastavení nového Wallet**", poté potvrďte podmínky a klikněte na "**Začít**" :



![image](assets/fr/08.webp)





- Vyberte možnost "**On Hardware Wallet**":



![image](assets/fr/09.webp)





- Pokud používáte **Blockstream Jade**, klikněte na příslušné tlačítko. V opačném případě vyberte možnost "**Připojit jiné hardwarové zařízení**" :



![image](assets/fr/10.webp)





- Připojte zařízení Hardware Wallet k počítači prostřednictvím rozhraní USB a vyberte jej v aplikaci Blockstream :



![image](assets/fr/22.webp)





- Počkejte prosím, než aplikace Blockstream importuje informace o vašem portfoliu:



![image](assets/fr/23.webp)



### 4.3. Vytvoření účtu





- Pokud již byl váš účet Hardware Wallet používán s aplikací Blockstream, váš účet se po importu automaticky zobrazí v účtu Interface. V opačném případě si vytvořte účet kliknutím na "**Vytvořit účet**" :



![image](assets/fr/24.webp)





- Chcete-li nakonfigurovat klasické portfolio Bitcoin, zvolte možnost "**Standard**":



![image](assets/fr/25.webp)





- Po vytvoření účtu máte přístup k hlavnímu portfoliu Interface:



![image](assets/fr/26.webp)





## 5. Použití řetězce Wallet s Hardware Wallet



### 5.1. Přijímání bitcoinů





- Na hlavní obrazovce portfolia klikněte na "**Přijmout**" :



![image](assets/fr/27.webp)





- Aplikace zobrazí **prázdný příjem Address**. Používání nového Address pro každou recepci zvyšuje důvěrnost. Klepnutím na "**Kopírovat Address**" zkopírujete Address nebo necháte odesílatele naskenovat zobrazený QR kód:



![image](assets/fr/12.webp)



**Možnosti** :




- (1) Kliknutím na šipky vytvoříte nový generate propojený s vaším portfoliem.
- (2) Chcete-li požádat o konkrétní částku, klikněte na "**Další možnosti**" a poté na "**Požádat o částku**". QR bude aktualizován a místo Address bude uveden platební URI Bitcoin, např: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Chcete-li znovu použít předchozí položku Address, klikněte na "**Další možnosti**" a poté na "**Seznam adres**" :



![image](assets/fr/14.webp)





- **Ověřování**: Pečlivě zkontrolujte sdílenou schránku Address, abyste předešli chybám nebo útokům (např. malwaru modifikujícímu schránku).
- Jakmile je transakce odvysílána v síti, objeví se ve vašem účtu Wallet. Vyčkejte 1 až 6 potvrzení, abyste transakci považovali za nezměnitelnou.



![image](assets/fr/28.webp)



### 5.2. poslat bitcoiny





- Na hlavní obrazovce portfolia klikněte na "**Odeslat**".



![image](assets/fr/29.webp)





- **Zadejte údaje**:
    - (1) Zkontrolujte, zda je vybráno aktivum **Bitcoin** (onchain).
    - (2) Zadejte **Address příjemce** vložením nebo naskenováním QR kódu pomocí webové kamery.
    - (3) Uveďte **částku**, která má být zaslána (v BTC, satoších nebo jiných jednotkách).




![image](assets/fr/16.webp)





- Vyberte **transakční poplatky** (nepovinné) :
 - Vyberte si z nabízených možností (rychlá, střední, pomalá) podle naléhavosti s odhadovanou dobou potvrzení.
 - Pro vlastní poplatky ručně upravte počet satoshis na vbyte. Ty se zobrazují na domovské obrazovce. Viz také [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Ruční výběr UTXO** (volitelné): Kliknutím na "**Ruční výběr Coin**" vyberete konkrétní UTXO, které se mají v transakci použít.



![image](assets/fr/18.webp)





- **Předběžné ověření**: Poté klikněte na "**Potvrdit transakci**". Ve skutečnosti bude transakce uvolněna do sítě až poté, co ji podepíšete svým Hardware Wallet, který jediný má tajné klíče spojené s adresami, z nichž budou strženy UTXO (satoši).



![image](assets/fr/19.webp)





- **Závěrečná kontrola a podpis**: Zkontrolujte, zda jsou všechny parametry transakce správné **na obrazovce Hardware Wallet**, a poté transakci podepište. Chyba v Address může mít za následek nevratnou ztrátu finančních prostředků.





- **Vysílání**: Po podpisu aplikace Blockstream automaticky odvysílá transakci v síti Bitcoin.



![image](assets/fr/20.webp)





- **Následná opatření**:
 - Transakce se na domovské obrazovce Wallet zobrazí jako "čekající", dokud nebude potvrzena.
 - Dokud není transakce potvrzena, lze použít funkci **Replace-by-fee (RBF)** k urychlení potvrzení zvýšením poplatku (viz příloha).



![image](assets/fr/21.webp)



## Přílohy



### A1. Další výukové programy Blockstream





- Používání přístroje Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Import a sledování portfolia v režimu "Pouze pro sledování" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Používání aplikace Blockstream v mobilních telefonech (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Vysvětlení Replace-by-fee (RBF)





- **Definice**: Replace-by-fee (RBF) je funkce sítě Bitcoin, která umožňuje odesílateli urychlit potvrzení **onchain** transakce zvýšením poplatku.
- **Limity** :
    - RBF není k dispozici pro transakce Liquid nebo Lightning.
    - Počáteční transakce musí být označena jako kompatibilní s RBF, což aplikace Blockstream provede automaticky.
- Další informace naleznete v [našem slovníku pojmů](https://planb.network/resources/glossary/RBF-replacebyfee).



### A3. Osvědčené postupy





- Zajistěte si frázi pro **obnovení**:
    - Uložte větu Hardware Wallet's Mnemonic na fyzický nosič (papír, kov) na bezpečném místě.
    - Nikdy je neukládejte digitálně (cloud, e-mail, snímek obrazovky).
    - Výukový program : Uložení věty Mnemonic :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Chraňte své soukromí**:





    - generate nový Address pro každý příjem v řetězci.
    - Aktivujte funkci **Tor** nebo **SPV** pro omezení sledování.
    - Připojte se k vlastnímu uzlu Bitcoin prostřednictvím služby Electrum a získejte maximální suverenitu.
- Vždy zkontrolujte dodací adresy:





    - Před podpisem zkontrolujte Address na obrazovce Hardware Wallet.
    - Abyste se vyhnuli ručním chybám, použijte funkci kopírování/vkládání nebo QR kód.
- **Optimalizace nákladů**:





    - Úprava poplatků podle naléhavosti a přetížení sítě (viz [Mempool.space](https://Mempool.space/)).
    - Pro rychlé a levné transakce, které nevyžadují zabezpečení v řetězci, použijte Liquid nebo Lightning.
- **Aktualizace softwaru**:





    - Udržujte aplikaci Blockstream a firmware Hardware Wallet v aktuálním stavu s nejnovějšími funkcemi a bezpečnostními záplatami.



### A4. Další zdroje





- **Oficiální odkazy**:
    - [Oficiální webové stránky](https://blockstream.com/)
    - [Podpora pro aplikaci Blockstream](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentace a chat
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Blokoví průzkumníci**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - Blesk : [1ML (Lightning Network)](https://1ml.com/)





- **Zajištění fráze pro obnovení:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Slovníček pojmů](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Slovníček pojmů](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb