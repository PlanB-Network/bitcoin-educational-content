---
name: Aplikace Blockstream - pouze pro sledování
description: Jak nakonfigurovat Watch-only wallet v aplikaci Blockstream?
---

![cover](assets/cover.webp)


## 1. Úvod


### 1.1 Cíl výuky





- Tento návod vysvětluje, jak nastavit a používat funkci **Watch-Only** mobilní aplikace **Blockstream App** ke sledování zařízení Bitcoin Wallet bez přístupu k jeho soukromým klíčům.
- Zahrnuje instalaci, počáteční konfiguraci, import rozšířeného veřejného klíče a jeho použití ke sledování zůstatků a přijímacích adres generate.
- Poznámka: Další výukové programy, uvedené v příloze, se týkají systémů Onchain, Liquid a verze pro stolní počítače.



### 1.2. Cílová skupina





- Začátečníci**: Uživatelé, kteří chtějí sledovat portfolio Bitcoin (často spojené s Hardware Wallet) prostřednictvím intuitivní mobilní aplikace.
- Středně pokročilí uživatelé**: Lidé, kteří chtějí spravovat portfolia pouze pro čtení a zároveň využívat možnosti ochrany soukromí, jako je Tor nebo SPV.
- Majitelé Hardware Wallet**: Majitelé generate mohou zkontrolovat své zůstatky a adresy generate bez připojení zařízení.
- Podniky a obchody** :
 - Sledujte své transakce pro účely účetnictví, aniž byste museli odhalit své soukromé klíče.
 - Ověřování přijatých transakcí bez zadávání soukromých klíčů v online platebních systémech.
 - Umožnit zaměstnancům generate nové přijímací adresy bez přístupu k soukromým klíčům.
- Organizace a crowdfunding**: Zobrazte dárcům transparentně zůstatek, aniž byste jim umožnili přístup k finančním prostředkům.



### 1.3. Představení funkce Watch-Only



**Watch-Only** Wallet umožňuje sledovat transakce a zůstatek Bitcoin Wallet bez přístupu k soukromým klíčům. Na rozdíl od běžného Wallet uchovává pouze veřejná data, například **rozšířený **veřejný klíč** (z něhož vznikl "**xpub**", dále "zpub", "ypub" atd.), což mu umožňuje získávat adresy příjemců a sledovat historii transakcí na Blockchain Bitcoin. Absence soukromých klíčů znemožňuje vyplacení finančních prostředků z aplikace, což zaručuje zvýšenou bezpečnost.



![image](assets/fr/10.webp)



**Proč používat Watch-only wallet?





- Bezpečnost**: Ideální pro monitorování portfolia zabezpečeného pomocí **Hardware Wallet** bez odhalení soukromých klíčů na připojeném zařízení.
- Pohodlí**: Umožňuje zkontrolovat zůstatek a nové adresy příjemců generate bez připojení Hardware Wallet.
- Důvěrnost**: Kompatibilní s možnostmi jako **Tor** nebo **SPV** pro omezení závislosti na serverech třetích stran.
- Případy použití**: Sledování finančních prostředků na cestách, generování adres pro příjem plateb nebo ověřování transakcí bez rizika soukromých klíčů.



![image](assets/fr/01.webp)



### 1.4. Rozšířené veřejné klíče



**Rozšířený veřejný klíč** (xpub, ypub, zpub atd.) je část dat odvozená od Bitcoin Wallet, která generuje všechny podřízené veřejné klíče a jejich přidružené adresy pro příjem, aniž by umožňovala přístup k soukromým klíčům.





- Jak to funguje** : Rozšířený veřejný klíč je generován z fráze seed deterministickým procesem (BIP-32). Vytváří hierarchický strom podřízených veřejných klíčů, z nichž každý lze převést na přijímací Address. Pomocí stejné odvozovací cesty (např. `m/44'/0'/0'`) jako sledovaný Wallet generuje Watch-only wallet stejné adresy, což umožňuje sledování prostředků a vytváření nových adres pro příjem.



![image](assets/fr/11.webp)





- Rozšířené typy veřejných klíčů
 - xpub**: Používá se pro starší portfolia (adresy začínající na "1", BIP-44) a portfolia Taproot (adresy začínající na "bc1p", BIP-86).
 - ypub**: Určeno pro kompatibilní peněženky SegWit (adresy začínající na "3", BIP-49).
 - zpub**: (adresy začínající na "bc1q", BIP-84).
 - Ostatní (tpub, upub, vpub atd.)**: Používá se pro alternativní sítě (např. Testnet) nebo specifické standardy. Například tpub je určen pro síť Testnet.





- Vyznamenání** : Volba mezi xpub, ypub nebo zpub závisí na typu Address (legacy, SegWit, Taproot nebo vnořený SegWit) a na standardu BIP používaném Wallet. Zkontrolujte formát požadovaný vaším zdrojovým portfoliem, abyste zajistili kompatibilitu s aplikací Blockstream.





- Bezpečnost a důvěrnost** : Rozšířený veřejný klíč není z hlediska bezpečnosti citlivý, protože neumožňuje utrácení finančních prostředků (nemá přístup k soukromým klíčům). Je však citlivý z hlediska důvěrnosti, protože odhaluje všechny veřejné adresy a související transakční historii.



**Doporučení**: Chraňte svůj rozšířený veřejný klíč jako citlivou informaci.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet připomínka





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: všechny názvy pro aplikaci nainstalovanou v chytrém telefonu, počítači nebo jakémkoli zařízení připojeném k internetu, která umožňuje správu a zabezpečení soukromých klíčů z Bitcoin Wallet.
- Na rozdíl od **hardwarových peněženek**, známých také jako **Cold peněženky**, které izolují klíče offline, softwarové peněženky fungují v propojeném prostředí, což je činí zranitelnějšími vůči kybernetickým útokům.





- Doporučené použití** :
    - Ideální pro správu středně velkého množství Bitcoin, zejména pro každodenní transakce.
    - Vhodné pro začátečníky nebo uživatele s omezeným majetkem, pro které se může zdát Hardware Wallet zbytečný.





- Omezení**: Méně bezpečné pro ukládání velkých finančních prostředků nebo dlouhodobých úspor. V takovém případě zvolte raději Hardware Wallet.




## 2. Představujeme aplikaci Blockstream





- Aplikace Blockstream** je mobilní (iOS, Android) a desktopová aplikace pro správu portfolia Bitcoin a aktiv na Liquid Network. Aplikace, kterou společnost [Blockstream](https://blockstream.com/) získala v roce 2016, se dříve jmenovala *Green Address* a poté *Blockstream Green*.
- Klíčové vlastnosti** :
    - Onchain** transakce na Blockchain Bitcoin.
    - Transakce v síti **Liquid** (Sidechain pro rychlé a důvěrné výměny).
    - Pouze sledovaná** portfolia pro sledování fondů bez přístupu ke klíčům.
    - Možnosti ochrany osobních údajů: připojení přes **Tor**, připojení k **osobnímu uzlu** přes Electrum nebo ověření **SPV** pro snížení závislosti na uzlech třetích stran.
    - Funkce **Replace-by-fee (RBF)** pro urychlení nepotvrzených transakcí.
- Kompatibilita**: Integruje hardwarové peněženky, jako je **Blockstream Jade**.
- Interface**: Intuitivní pro začátečníky, s pokročilými možnostmi pro experty.
- Poznámka**: Tato příručka se zaměřuje na použití na řetězu. Další návody v dodatcích se týkají onchainu, Watch-Only a verze pro stolní počítače.




## 3. Instalace a konfigurace aplikace Blockstream



### 3.1. stáhnout





- Pro Android** :
    - Stáhněte si [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) z obchodu Google Play.
    - Alternativa: Nainstalujte si soubor APK, který je k dispozici na [oficiálním GitHubu společnosti Blockstream](https://github.com/Blockstream/green_android).
- Pro iOS** :
    - Stáhněte si aplikaci [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) z App Store.
- Poznámka**: Ujistěte se, že stahujete z oficiálních zdrojů, abyste se vyhnuli podvodným aplikacím.



### 3.2. počáteční konfigurace





- Domovská obrazovka**: Při prvním otevření aplikace se zobrazí obrazovka bez nakonfigurovaného Wallet. Vytvořená nebo importovaná portfolia se zde zobrazí později.



![image](assets/fr/02.webp)





- Přizpůsobení nastavení**: Klikněte na "Nastavení aplikace", upravte níže uvedené možnosti, klikněte na "Uložit", restartujte aplikaci a vytvořte své portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Vylepšená ochrana soukromí (pouze Android)





- Funkce**: Funkce: Zakáže snímky obrazovky, skryje náhledy aplikací ve správci úloh a uzamkne přístup, když je telefon zamčený.
- Proč?** : Chrání vaše data před neoprávněným fyzickým přístupem nebo malwarem zachycujícím obrazovku.



#### 3.2.2. Připojení přes Tor





- Funkce**: Funkce: Směřujte síťový provoz přes **Tor**, anonymní síť, která šifruje vaše připojení.
- Proč?**: Skryjte svou IP adresu Address a chraňte své soukromí, což je ideální, pokud nedůvěřujete své síti (například veřejné Wi-Fi).
- Nevýhoda**: Nevýhoda: Může zpomalit aplikaci kvůli šifrování.
- Doporučení**: Pokud je pro vás důvěrnost prioritou, aktivujte Tor, ale otestujte rychlost připojení.



#### 3.2.3. Připojení k osobnímu uzlu





- Funkce**: Připojuje aplikaci k vlastnímu **kompletnímu uzlu Bitcoin** prostřednictvím **Electrum serveru**.
- Proč?**: Poskytuje úplnou kontrolu nad daty Blockchain a odstraňuje závislost na serverech Blockstream.
- Předpoklad**: Předpoklad: nakonfigurovaný uzel Bitcoin.
- Doporučení**: Doporučení: Pokročilí uživatelé, kteří chtějí maximální suverenitu.



#### 3.2.4. Ověřování SPV





- Funkce**: Funkce **Zjednodušené ověření platby (SPV)** slouží k přímému ověření určitých údajů Blockchain bez nutnosti stahování celého řetězce.
- Proč?**: Snižuje závislost na výchozím uzlu Blockstream a zároveň zůstává nenáročný na mobilní zařízení.
- Nevýhoda**: Je méně bezpečná než Full node, protože některé informace získává z uzlů třetích stran.
- Doporučení**: Pokud nemůžete použít osobní uzel, ale pro optimální zabezpečení dáváte přednost Full node, aktivujte SPV.





## 4. Vytvoření portfolia Bitcoin "pouze pro sledování"



### 4.1. Obnovení rozšířeného veřejného klíče



Chcete-li nastavit Watch-only wallet, musíte nejprve získat rozšířený veřejný klíč (xpub, ypub, zpub atd.) sledovaného Wallet. Tyto informace jsou obvykle k dispozici v nastavení nebo v části "Informace o Wallet" vašeho softwaru nebo Hardware Wallet.





- Příklad s aplikací Blockstream: Na domovské obrazovce Wallet přejděte do "Nastavení", poté do "Podrobnosti o Wallet" a zkopírujte zpub :



![image](assets/fr/09.webp)





- Alternativa 1: generate kód QR obsahující rozšířený veřejný klíč pro naskenování v dalším kroku.
- Alternativa 2: Použijte output descriptor, pokud jej váš Wallet poskytuje.



### 4.2. import Wallet Watch-only





- Upozornění**: Nastavte své portfolio v soukromí, bez kamer a pozorovatelů.
- Na domovské obrazovce klikněte na "Nastavit nové portfolio" a poté na "Začít" :



![image](assets/fr/04.webp)





- Zobrazí se další obrazovka:



![image](assets/fr/06.webp)






- (1) **"Nastavení mobilního zařízení Wallet"** : Vytvoření nového mobilního telefonu Hot Wallet. Viz návod "Blockstream App - Onchain" v příloze.
- (2) **"Obnovit ze zálohy "**: Import stávajícího portfolia pomocí fráze Mnemonic (12 nebo 24 slov). Pozor: Neimportujte frázi z Cold Wallet, protože bude vystavena na připojeném zařízení, čímž se zruší její zabezpečení.
- (3) **"Pouze pro sledování "**: možnost, která nás zajímá v tomto výukovém programu.





- Poté vyberte možnost "**Jediný podpis**" a síť "**Bitcoin**":



![image](assets/fr/12.webp)





- Vložte rozšířený veřejný klíč (xpub, ypub, zpub atd.), naskenujte příslušný kód QR nebo zadejte kód output descriptor. I když je v aplikaci uvedeno "xpub", jsou autorizovány i klíče ypub, zpub atd. Poté klikněte na tlačítko "Připojit":



![image](assets/fr/13.webp)




### 4.3. Používání pouze hodinek Wallet



Po importu zobrazí Watch-only wallet celkový zůstatek a transakční historii adres odvozených z rozšířeného veřejného klíče. Viditelné jsou pouze transakce v řetězci (transakce Liquid jsou ignorovány). Chcete-li sledovat Liquid Wallet, zopakujte import výběrem "Liquid" v předchozím kroku.





- Zobrazení zůstatku a historie**: na domovské obrazovce můžete zobrazit celkový zůstatek a historii transakcí v řetězci:



![image](assets/fr/14.webp)





- generate a příjem Address**: Klepnutím na "Transact" a poté na "Receive" vytvoříte nový řetězový Address. Sdílejte jej prostřednictvím QR kódu nebo jej zkopírujte, abyste mohli přijímat finanční prostředky:



![image](assets/fr/15.webp)





- Odeslat finanční prostředky**: Klikněte na **"Transakce "** a poté na **"Odeslat "**. Můžete zadat :
 - Address příjemce.
 - Částka transakce.
 - Transakční poplatky.



Protože však Watch-only wallet nedrží soukromé klíče, nemůžete posílat finanční prostředky přímo. Chcete-li transakci podepsat, připojte PSBT Hardware Wallet nebo Exchange naskenováním QR kódů (možnost dostupná například na kartě Coldcard Q).



![image](assets/fr/16.webp)





- Poznámka**: Vždy zkontrolujte údaje o přijímajícím Address a transakci, abyste se vyhnuli chybám. Prostředky zaslané na nesprávný Address nelze získat zpět.




## Přílohy



### A1. Další výukové programy aplikace Blockstream





- Použití sítě Onchain :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Použití přístroje Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Verze pro stolní počítače :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Rozšířené veřejné klíče





- Slovníček pojmů :
 - [Rozšířené veřejné klíče](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kurz :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Osvědčené postupy



Chcete-li aplikaci **Blockstream** používat bezpečně a efektivně, dodržujte následující doporučení. Pomohou vám ochránit vaše finanční prostředky, optimalizovat transakce a zachovat důvěrnost v sítích **Bitcoin (onchain)**, **Liquid** a **Lightning**.





- Zajistěte si frázi pro obnovení** :
 - Výukový program: Uložení fráze Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Použijte zabezpečené ověřování** :
 - Aktivujte **silný kód PIN** nebo **biometrické ověření** (otisk prstu nebo rozpoznání obličeje) pro ochranu přístupu k aplikaci.
 - Nikdy nesdělujte svůj PIN nebo biometrické údaje.





- Chraňte své soukromí** :
 - generate nový Address pro každý příjem v řetězci nebo Liquid pro omezení sledování na Blockchain.
 - Aktivujte funkce "Enhanced Privacy", "Tor" a "SPV".
 - Pro dosažení maximální důvěrnosti připojte svůj Wallet k vlastnímu uzlu Bitcoin prostřednictvím serveru Electrum namísto použití veřejného uzlu





- Vyberte si síť, která nejlépe vyhovuje vašim potřebám** :
 - Onchain**: V případě dlouhodobé úschovy nebo transakcí s velkou hodnotou (poplatky jsou v poměru k částce zanedbatelné).
 - Liquid**: Použijte pro rychlé a levné přenosy se zvýšenou důvěrností.
 - Blesk**: Vyberte si okamžité a levné převody malých částek.





- Vždy zkontrolujte dodací adresy** :
 - Před odesláním finančních prostředků pečlivě zkontrolujte Address. Finanční prostředky zaslané na nesprávný účet Address jsou navždy ztraceny. Používejte kopírování/vkládání nebo skenování QR kódu, nikdy nekopírujte/neupravujte Address ručně.





- Optimalizace nákladů** :
 - Pro transakce v řetězci zvolte vhodné poplatky (pomalé, střední, rychlé) podle naléhavosti a přetížení sítě.
 - Pro malá množství použijte Liquid nebo Lightning.





- Aktualizujte aplikaci




### A4. Další zdroje





- Oficiální odkazy na Blockstream:**
 - [Oficiální webové stránky](https://blockstream.com/)**
 - [Podpora pro mobilní aplikaci](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentace a chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Block Explorers :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blesk: **[1ML (Lightning Network)](https://1ml.com/)**





 - Výuka a výukové programy:** **[Plan ₿ Network](https://planb.network/)** :
  - Zajištění fráze pro obnovení



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Slovník pojmů](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Slovník pojmů](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
