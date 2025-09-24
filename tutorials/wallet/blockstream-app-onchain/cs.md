---
name: Blockstream App - Onchain
description: Nastavení aplikace Blockstream v mobilu a správa onchain transakcí
---
![cover](assets/cover.webp)


## 1. Úvod


### 1.1 Cíl výuky





- Tento návod vysvětluje, jak používat mobilní aplikaci **Blockstream App** ke správě Bitcoin **onchain** Wallet, tj. transakcí zaznamenaných přímo na hlavním Blockchain Bitcoin.
- Zahrnuje instalaci, počáteční konfiguraci, vytvoření účtu Software Wallet a operace pro příjem a odesílání bitcoinů.
- Poznámka: Další výukové programy v dodatcích se týkají Liquid, Watch-Only a verze pro stolní počítače.



![image](assets/fr/01.webp)



### 1.2 Cílová skupina





- **Začátečníci**: Uživatelé, kteří chtějí spravovat své bitcoiny pomocí intuitivní mobilní aplikace.
- **Středně pokročilí uživatelé**: Lidé, kteří chtějí porozumět funkcím onchainu a možnostem ochrany soukromí, jako je Tor nebo SPV.



### 1.3. Připomínky k peněženkám Hot





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: všechny názvy pro aplikaci nainstalovanou v chytrém telefonu, počítači nebo jakémkoli zařízení připojeném k internetu, která umožňuje správu a zabezpečení soukromých klíčů z Bitcoin Wallet.
- Na rozdíl od **hardwarových peněženek**, známých také jako **Cold peněženky**, které izolují klíče offline, softwarové peněženky fungují v propojeném prostředí, což je činí zranitelnějšími vůči kybernetickým útokům.





- **Doporučené použití**:
    - Ideální pro správu středně velkého množství Bitcoin, zejména pro každodenní transakce.
    - Vhodné pro začátečníky nebo uživatele s omezeným majetkem, pro které se může zdát Hardware Wallet zbytečný.





- **Omezení**: Méně bezpečné pro ukládání velkých finančních prostředků nebo dlouhodobých úspor. V takovém případě zvolte raději Hardware Wallet.




## 2. Představujeme aplikaci Blockstream





- Aplikace **Blockstream** je mobilní (iOS, Android) a desktopová aplikace pro správu portfolia Bitcoin a aktiv na Liquid Network. Aplikace, kterou společnost [Blockstream](https://blockstream.com/) získala v roce 2016, se dříve jmenovala *Green Address* a poté *Blockstream Green*.
- **Klíčové vlastnosti**:
- **Onchain** transakce na Blockchain Bitcoin.
    - Síťové transakce **Liquid** (Sidechain pro rychlé a důvěrné výměny).
- Pouze **sledovaná portfolia** pro sledování fondů bez přístupu ke klíčům.
    - Možnosti ochrany osobních údajů: připojení přes **Tor**, připojení k **osobnímu uzlu** přes Electrum nebo ověření **SPV** pro snížení závislosti na uzlech třetích stran.
    - Funkce **Replace-by-fee (RBF)** pro urychlení nepotvrzených transakcí.
- **Kompatibilita**: Integruje hardwarové peněženky, jako je **Blockstream Jade**.
- **Interface**: Intuitivní pro začátečníky, s pokročilými možnostmi pro experty.
- **Poznámka**: Tato příručka se zaměřuje na použití na řetězu. Další návody v dodatcích se týkají Liquid, Watch-Only a verze pro stolní počítače.



## 3. Instalace a konfigurace aplikace Blockstream



### 3.1. stáhnout





- **Pro Android**:
    - Stáhněte si [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) z obchodu Google Play.
    - Alternativa: Nainstalujte si soubor APK, který je k dispozici na [oficiálním GitHubu společnosti Blockstream](https://github.com/Blockstream/green_android).
- **Pro iOS**:
    - Stáhněte si aplikaci [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) z App Store.
- **Poznámka**: Ujistěte se, že stahujete z oficiálních zdrojů, abyste se vyhnuli podvodným aplikacím.



### 3.2. počáteční konfigurace





- **Domovská obrazovka**: Při prvním otevření aplikace se zobrazí obrazovka bez nakonfigurovaného Wallet. Vytvořená nebo importovaná portfolia se zde zobrazí později.



![image](assets/fr/02.webp)





- **Přizpůsobení nastavení**: Klikněte na "Nastavení aplikace", upravte níže uvedené možnosti, klikněte na "Uložit", restartujte aplikaci a vytvořte své portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Vylepšená ochrana soukromí (pouze Android)





- **Funkce**: Zakáže snímky obrazovky, skryje náhledy aplikací ve správci úloh a uzamkne přístup, když je telefon zamčený.
- **Proč?**: Chrání vaše data před neoprávněným fyzickým přístupem nebo malwarem zachycujícím obrazovku.


#### 3.2.2. Připojení přes Tor





- **Funkce**: Směřujte síťový provoz přes **Tor**, anonymní síť, která šifruje vaše připojení.
- **Proč?**: Skryjte svou IP adresu Address a chraňte své soukromí, což je ideální, pokud nedůvěřujete své síti (například veřejné Wi-Fi).
- **Nevýhoda**: Může zpomalit aplikaci kvůli šifrování.
- **Doporučení**: Pokud je pro vás důvěrnost prioritou, aktivujte Tor, ale otestujte rychlost připojení.


#### 3.2.3. Připojení k osobnímu uzlu





- **Funkce**: Připojí aplikaci k vlastnímu **kompletnímu uzlu Bitcoin** prostřednictvím serveru **Electrum**.
- **Proč?**: Poskytuje úplnou kontrolu nad daty Blockchain a eliminuje závislost na serverech Blockstream.
- **Předpoklad**: Předpoklad: nakonfigurovaný uzel Bitcoin.
- **Doporučení**: Pokročilým uživatelům, kteří hledají maximální suverenitu.


#### 3.2.4. Ověřování SPV





- **Funkce**: Funkce **Zjednodušené ověření platby (SPV)** slouží k přímému ověření určitých údajů Blockchain, aniž by bylo nutné stahovat celý řetězec.
- **Proč?**: Snižuje závislost na výchozím uzlu Blockstream a zároveň zůstává nenáročný na mobilní zařízení.
- **Nevýhoda**: Méně bezpečný než Full node, protože se v některých informacích spoléhá na uzly třetích stran.
- **Doporučení**: Pokud nemůžete používat osobní uzel, ale pro optimální zabezpečení dáváte přednost uzlu Full node, aktivujte SPV.





## 4. Vytvoření portfolia onchain Bitcoin



### 4.1. Zahájení tvorby





- **Upozornění**: Nastavte své portfolio v soukromí, bez kamer a pozorovatelů.
- Na domovské obrazovce klikněte na možnost "Začít" :



![image](assets/fr/04.webp)





- Pokud chcete spravovat **Cold Wallet** (offline Wallet): klikněte na **"Connect Jade "** a použijte Hardware Wallet Blockstream Jade nebo jiné kompatibilní peněženky Cold.



![image](assets/fr/05.webp)





- Zobrazí se další obrazovka:



![image](assets/fr/06.webp)





- (1) **"Nastavení mobilního zařízení Wallet"** : Vytvořte nový mobilní telefon Hot Wallet (Hot Wallet).
- (2) **"Obnovit ze zálohy "**: Import stávajícího portfolia pomocí fráze Mnemonic (12 nebo 24 slov). Upozornění: Neimportujte frázi Cold Wallet, protože bude vystavena v připojeném zařízení, čímž se zruší její zabezpečení.
- (3) **"Pouze pro sledování "**: Pro zobrazení zůstatku (např. vašeho Cold Wallet) bez vystavení věty Mnemonic importujte existující portfolio pouze pro čtení. Viz návod Watch Only v příloze.



**V tomto výukovém programu**: Klepnutím na **"Nastavení mobilního Wallet"** vytvoříte Hot Wallet.


Automaticky se vytvoří váš Wallet a zobrazí se domovská stránka Wallet, zde nazvaná "Můj Wallet 5":



![image](assets/fr/07.webp)



**Důležité**: Aplikace Blockstream zjednodušila vytváření Wallet tím, že nezobrazuje automaticky 12slovnou větu seed. *Přestože se nyní portfolio vytvoří jedním kliknutím, hrozí, že pokud si neuložíte frázi seed*, ztratíte přístup ke svým prostředkům.



### 4.2. Uložit větu seed





- Na domovské obrazovce Wallet klikněte na kartu "Zabezpečení" a poté na výzvu "Zálohovat" nebo na nabídku "Fráze pro obnovení":



![image](assets/fr/08.webp)



Zobrazí se 12slovná věta seed, kterou můžete uložit.





- S maximální pečlivostí si zapište frázi o zotavení. Zapište si ji na papír nebo na kov a uložte ji na bezpečném místě (na bezpečném, offline místě). Tato fráze je vaším jediným prostředkem pro přístup k bitcoinům v případě ztráty zařízení nebo vymazání aplikace.
- Je také důležité si uvědomit, že kdokoli s touto frází může ukrást všechny vaše bitcoiny. Nikdy je neukládejte digitálně:
 - Žádný snímek obrazovky
 - Žádné zálohování do cloudu, e-mailu nebo zpráv
 - Žádné kopírování/vkládání (riziko uložení do schránky)



**! Tento bod je rozhodující**. Další informace o zálohování :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Potvrzení věty seed



Před odesláním finančních prostředků na účet Address spojený s touto větou seed musíte otestovat zálohování svých 12 slov.



Za tímto účelem zapíšeme odkaz, odstraníme soubor Wallet, obnovíme jej pomocí zálohy a zkontrolujeme, zda se odkaz nezměnil.





- Na domovské obrazovce Wallet klikněte na kartu "Nastavení", poté na "Podrobnosti o Wallet" a zkopírujte zPub ([rozšířený veřejný klíč](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Poznámka: zpub Address lze importovat do aplikace Blockstream pro funkci "Watch Only" (viz Dodatek).





- Odstraňte aplikaci, poté obnovte Wallet pomocí **"Obnovit ze zálohy "** zadáním fráze Mnemonic a zkontrolujte, zda se zpub nezměnil. Pokud ano, pak je vaše záloha správná a můžete odeslat prostředky do Wallet.





- Chcete-li se dozvědět více o tom, jak provést test obnovení, naleznete zde speciální výukový program :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Zabezpečení přístupu k aplikaci



Uzamkněte přístup k aplikaci pomocí silného kódu PIN:




- Na domovské obrazovce Wallet přejděte na **"Zabezpečení "** a poté klikněte na **"PIN "**
- Zadejte a potvrďte **náhodný šestimístný kód PIN**.



**Biometrická volba**: Pro větší pohodlí je k dispozici, ale je méně bezpečná než robustní PIN kód (riziko neoprávněného přístupu, např. otisk prstu nebo sken obličeje během spánku).



**Poznámka**: PIN zabezpečuje zařízení, ale k získání prostředků lze použít pouze frázi seed.





## 5. Použití řetězce Wallet



### 5.1. Přijímání bitcoinů





- Na domovské obrazovce portfolia klikněte na možnost "**Transakce**" a poté na možnost **"Přijmout "**.



![image](assets/fr/10.webp)





- Aplikace zobrazí **prázdný příjem Address** (formát SegWit v0, začínající na `bc1q...`). Použití nového Address při každém příjmu Bitcoin zvyšuje důvěrnost.





- **Možnosti**:
    - (1) "Bitcoin": kliknutím vyberte zásilku onchain nebo Liquid a vyberte aktivum.
    - (2) Klepnutím na šipky vyberte další novou větu Address spojenou s touto větou seed.
    - (3) Můžete si také vybrat Address z již použitých/zobrazených adres kliknutím na tři tečky vpravo nahoře a poté na "Seznam adres"
    - (4) Chcete-li požádat o konkrétní částku, klikněte na tři tečky vpravo nahoře, vyberte možnost "Request amount" a zadejte požadovanou částku. QR bude aktualizován a místo Address bude uveden platební URI Bitcoin.




![image](assets/fr/11.webp)





- Sdílejte Address/URI kliknutím na "**Sdílet**", zkopírováním textu nebo naskenováním QR kódu.
- **Ověřování**: Address sdíleného s příjemcem, aby se předešlo chybám nebo útokům (např. malwaru modifikujícímu schránku).



### 5.2. poslat bitcoiny





- Na domovské obrazovce portfolia klikněte na "**Transakce**" a poté na **"Odeslat "** :



![image](assets/fr/12.webp)





- **Zadejte údaje**:
    - (1) Zadejte **Address příjemce** nalepením nebo naskenováním QR kódu.
    - (2) Zkontrolujte majetek a účet, ze kterého jsou prostředky zasílány.
    - (3) Uveďte **částku**, která má být zaslána. Můžete zvolit jednotku: BTC, satoshis, USD, ...


Minimální částka (dush limit) k 8. 3. 2025 je 546 Sats.




    - (4) Vyberte možnost **transakční poplatky** :
        - V závislosti na naléhavosti vyberte jednu z nabízených možností (např. rychlý, střední, pomalý) a zobrazí se přibližná doba přenosu.
        - V případě vlastních poplatků ručně upravte počet Satoshi za vbytes (tržní sazby viz [Mempool.space](https://Mempool.space/)).




![image](assets/fr/13.webp)





- **Zkontrolujte**:
    - Na souhrnné obrazovce zkontrolujte číslo Address, částku a poplatky.
    - Chyba v Address může mít za následek nevratnou ztrátu finančních prostředků. Pozor na škodlivý software, který modifikuje schránku.



![image](assets/fr/14.webp)





- **Potvrzení**: Posunutím tlačítka "Odeslat" transakci podepíšete a rozesíláte.
- **Následná opatření**: Na kartě Wallet "Transakce" se transakce zobrazí jako "čekající" až do potvrzení (1 až 6 potvrzení):



![image](assets/fr/15.webp)





- Dokud není transakce potvrzena, umožňuje funkce "Replace by fee" (viz příloha) urychlit její vyřízení zvýšením transakčních poplatků:



![image](assets/fr/16.webp)




## Přílohy



### A1. Další výukové programy Blockstream



Používání Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Import a sledování modelu Wallet v režimu "Pouze sledování"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Verze pro stolní počítače



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Vysvětlení Replace-by-fee (RBF)



**Definice**: Replace-by-fee (RBF) je funkce sítě Bitcoin, která umožňuje odesílateli urychlit potvrzení **onchain** transakce tím, že souhlasí se zaplacením vyššího poplatku.



**Omezení** :




- RBF není k dispozici pro transakce Liquid nebo Lightning.
- Počáteční transakce musí být při svém vytvoření označena jako kompatibilní s RBF, což aplikace Blockstream provede automaticky.



**Další informace:**




- [Slovníček pojmů](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Osvědčené postupy



Chcete-li aplikaci **Blockstream** používat bezpečně a efektivně, dodržujte následující doporučení. Pomohou vám ochránit vaše finanční prostředky, optimalizovat transakce a zachovat důvěrnost v sítích **Bitcoin (onchain)**, **Liquid** a **Lightning**.





- Zajistěte si frázi pro **obnovení**:
 - Výukový program: Uložení věty Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Použijte **zabezpečené ověřování**:
 - Aktivujte **silný kód PIN** nebo **biometrické ověření** (otisk prstu nebo rozpoznání obličeje) pro ochranu přístupu k aplikaci.
 - Nikdy nesdělujte svůj PIN nebo biometrické údaje.





- **Chraňte své soukromí**:
 - generate nový Address pro každý příjem v řetězci nebo Liquid pro omezení sledování na Blockchain.
 - Aktivujte funkce "Enhanced Privacy", "Tor" a "SPV".
 - Pro dosažení maximální důvěrnosti připojte svůj Wallet k vlastnímu uzlu Bitcoin prostřednictvím serveru Electrum namísto použití veřejného uzlu





- Vyberte si síť, která nejlépe vyhovuje vašim potřebám:
- **Onchain**: V případě dlouhodobé úschovy nebo transakcí s velkou hodnotou (poplatky jsou v poměru k částce zanedbatelné).
- **Liquid**: Použijte pro rychlé a levné přenosy se zvýšenou důvěrností.
- **Blesk**: Vyberte si okamžité a levné převody malých částek.





- Vždy zkontrolujte dodací adresy:
 - Před odesláním finančních prostředků si Address pečlivě zkontrolujte. Finanční prostředky zaslané na nesprávný účet Address jsou navždy ztraceny. Používejte kopírování/vkládání nebo skenování QR kódu, nikdy nekopírujte/neupravujte Address ručně.





- **Optimalizace nákladů**:
 - Pro transakce v řetězci zvolte vhodné poplatky (pomalé, střední, rychlé) podle naléhavosti a přetížení sítě.
 - Pro malá množství použijte Liquid nebo Lightning.





- Aktualizujte aplikaci




### A4. Další zdroje





- **Oficiální odkazy:**
- [Oficiální webové stránky](https://blockstream.com/)
- [Podpora pro mobilní aplikaci](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentace a chat
- [GitHub](https://github.com/Blockstream/green_android)





- **Block Explorers:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blesk: **[1ML (Lightning Network)](https://1ml.com/)**





- **Výuka a výukové programy:** **[Plan ₿ Network](https://planb.network/)**
 - Zajištění fráze pro obnovení



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Slovník pojmů](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Slovník pojmů](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb