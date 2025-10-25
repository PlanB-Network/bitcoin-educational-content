---
name: Blockstream App - Liquid
description: Jak nakonfigurovat aplikaci Blockstream a používat Liquid Network
---
![cover](assets/cover.webp)


## 1. Úvod


### 1.1 Cíl výuky





- Tento návod vysvětluje, jak používat mobilní aplikaci **Blockstream App** ke správě portfolia **Bitcoin Liquid**, tj. transakcí zaznamenaných přímo v postranním řetězci Bitcoin "Liquid".
- Zahrnuje instalaci, počáteční konfiguraci, vytvoření Software Wallet a operace pro příjem a odesílání bitcoinů na Liquid.
- Poznámka: Další výukové programy v dodatcích se týkají verzí Onchain, Watch-Only a verze pro stolní počítače.



### 1.2 Cílová skupina





- **Začátečníci**: Uživatelé, kteří chtějí spravovat své bitcoiny pomocí intuitivní mobilní aplikace integrující Liquid Network.
- **Středně pokročilí uživatelé**: Lidé, kteří chtějí porozumět funkcím onchainu a možnostem ochrany soukromí, jako je Tor nebo SPV.



### 1.3 Představujeme Liquid



**Liquid** je **Sidechain** Bitcoin, vyvinutý společností **[Blockstream](https://blockstream.com/Liquid/)**, navržený tak, aby nabízel rychlejší a pokročilejší funkce Confidential Transactions a zároveň zůstal napojený na hlavní Blockchain Bitcoin.



Sidechain je nezávislý Blockchain, který pracuje paralelně s Bitcoin pomocí mechanismu známého jako **oboustranný kolík**. Tento systém uzamyká bitcoiny na hlavní Blockchain a vytváří **Liquid-Bitcoiny (L-BTC)**, tokeny, které obíhají na Liquid Network, přičemž si zachovávají paritu hodnoty s původními bitcoiny. Prostředky lze kdykoli vrátit na Blockchain Bitcoin.



![image](assets/fr/17.webp)






- (1) **Peg-in**: Bitcoiny (BTC) jsou uzamčeny na hlavní Blockchain federací Liquid. Na oplátku je na Blockchain Liquid vydáno ekvivalentní množství bitcoinů Liquid (L-BTC), které zajišťuje paritu mezi oběma řetězci, a je zasláno uživateli.





- (2) **Nezávislé transakce**: Transakce mohou probíhat současně a nezávisle na hlavní jednotce Blockchain (BTC) a Sidechain Liquid (L-BTC) v závislosti na požadavcích uživatele.





- (3) **Peg-out**: Uživatel pošle Liquid-Bitcoins (L-BTC) zpět do federace Liquid. Federace poté odemkne ekvivalentní množství bitcoinů (BTC) na hlavním Blockchain a převede je uživateli.



Liquid se spoléhá na **federaci** důvěryhodných účastníků (burzy, uznané společnosti Bitcoin), kteří řídí ověřování bloků a dvoustranné ukotvení. Na rozdíl od Blockchain Bitcoin, která je decentralizovaná a spoléhá na těžaře, je Liquid **federovaná** síť, což znamená, že její bezpečnost a správa závisí na těchto účastnících. To sice znamená kompromis v oblasti decentralizace, ale umožňuje to optimalizovat výkon a pokročilé funkce.



![image](assets/fr/18.webp)



##### Proč používat Liquid?





- **Rychlost**: Díky blokům generovaným každou minutu federací validátorů jsou transakce na Liquid potvrzeny přibližně za **1 minutu** ve srovnání s 10 minutami a více u transakcí na řetězci.
- **Zvýšená důvěrnost**: Liquid používá **Confidential Transactions**, který skrývá částku a typ převáděného majetku, čímž se transakce stávají soukromějšími (ačkoli adresy zůstávají viditelné).
- **Nízké poplatky**: Transakce na Liquid jsou obecně levnější, takže jsou ideální pro časté převody nebo malé částky.
- **Více aktiv**: Kromě L-BTC podporuje Liquid vydávání dalších digitálních aktiv, jako jsou stablecoiny nebo tokeny, pro použití ve specifických aplikacích.
- **Případy použití**: Liquid je vhodný zejména pro výměnu mezi platformami, rychlé platby nebo aplikace vyžadující inteligentní smlouvy, přičemž zůstává spojen s bezpečností Bitcoin.



**Poznámka: Tento návod se zaměřuje na používání Liquid prostřednictvím aplikace Blockstream. Podrobné informace o Liquid Network naleznete v příloze.**



### 1.4. Hot Wallet připomínka





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: všechny názvy pro aplikaci nainstalovanou v chytrém telefonu, počítači nebo jakémkoli zařízení připojeném k internetu, která umožňuje správu a zabezpečení soukromých klíčů z Bitcoin Wallet.
- Na rozdíl od **hardwarových peněženek**, známých také jako **Cold peněženky**, které izolují klíče offline, softwarové peněženky fungují v propojeném prostředí, což je činí zranitelnějšími vůči kybernetickým útokům.





- **Doporučené použití**:
    - Ideální pro správu středně velkého množství Bitcoin, zejména pro každodenní transakce.
    - Vhodné pro začátečníky nebo uživatele s omezeným majetkem, pro které se může zdát Hardware Wallet zbytečný.





- **Omezení**: Méně bezpečné pro ukládání velkých finančních prostředků nebo dlouhodobých úspor. V takovém případě zvolte raději Hardware Wallet.




## 2. Představujeme aplikaci Blockstream





- **Blockstream App** je mobilní (iOS, Android) a desktopová aplikace pro správu peněženek Bitcoin a aktiv na Liquid Network. V roce 2016 ji koupila společnost [Blockstream](https://blockstream.com/), dříve se jmenovala *Green Address* a poté *Blockstream Green*.
- **Klíčové vlastnosti**:
- **Onchain** transakce na Blockchain Bitcoin.
    - Transakce v síti **Liquid** (Sidechain pro rychlé a důvěrné výměny).
- Pouze **sledovaná portfolia** pro sledování fondů bez přístupu ke klíčům.
    - Možnosti ochrany osobních údajů: připojení přes **Tor**, připojení k **osobnímu uzlu** přes Electrum nebo ověření **SPV** pro snížení závislosti na uzlech třetích stran.
    - Funkce **Replace-by-fee (RBF)** pro urychlení nepotvrzených transakcí.
- **Kompatibilita**: Integruje hardwarové peněženky, jako je **Blockstream Jade**.
- **Interface**: Intuitivní pro začátečníky, s pokročilými možnostmi pro experty.
- **Poznámka**: Tato příručka se zaměřuje na použití na řetězu. Další návody v dodatcích se týkají onchainu, Watch-Only a verze pro stolní počítače.




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





- **Funkce**: Připojuje aplikaci k vlastnímu **kompletnímu uzlu Bitcoin** prostřednictvím **serveru Electrum**.
- **Proč?**: Poskytuje úplnou kontrolu nad daty Blockchain a eliminuje závislost na serverech Blockstream.
- **Předpoklad**: Předpoklad: nakonfigurovaný uzel Bitcoin.
- **Doporučení**: Pokročilí uživatelé, kteří chtějí maximální suverenitu.



#### 3.2.4. Ověřování SPV





- **Funkce**: Funkce **Zjednodušené ověření platby (SPV)** slouží k přímému ověření určitých údajů Blockchain bez nutnosti stahování celého řetězce.
- **Proč?**: Snižuje závislost na výchozím uzlu Blockstream a zároveň zůstává nenáročný na mobilní zařízení.
- **Nevýhoda**: Je méně bezpečná než Full node, protože některé informace získává z uzlů třetích stran.
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






- (1) **"Nastavení mobilního zařízení Wallet"** : Vytvoření nového mobilního telefonu Hot Wallet (Hot Wallet).
- (2) **"Obnovit ze zálohy "**: Import stávajícího portfolia pomocí fráze Mnemonic (12 nebo 24 slov). Upozornění: Neimportujte frázi z Cold Wallet, protože bude vystavena na připojeném zařízení, čímž se zruší její zabezpečení.
- (3) **"Pouze pro sledování "**: Pro zobrazení zůstatku (např. vašeho Cold Wallet) bez vystavení věty Mnemonic importujte existující portfolio pouze pro čtení. Viz návod "Watch Only" v příloze.



**V tomto výukovém programu**: Klepnutím na **"Nastavení mobilního Wallet"** vytvoříte Hot Wallet.


Váš Wallet se automaticky vytvoří a zobrazí se domovská stránka Wallet, zde nazvaná "Můj Wallet 5":



![image](assets/fr/07.webp)



**Důležité**: Aplikace Blockstream zjednodušila vytváření Wallet tím, že nezobrazuje automaticky 12slovnou větu seed. *I když se nyní portfolio vytvoří jedním kliknutím, hrozí, že pokud si frázi seed* neuložíte, ztratíte přístup ke svým prostředkům.



### 4.2. Uložit větu seed





- Na domovské obrazovce Wallet klikněte na kartu "Zabezpečení" a poté na výzvu "Zálohovat" nebo na nabídku "Fráze pro obnovení":



![image](assets/fr/08.webp)



Zobrazí se 12slovná fráze seed, kterou můžete uložit.





- S maximální pečlivostí si zapište frázi o zotavení. Zapište si ji na papír nebo na kov a uložte ji na bezpečném místě (na bezpečném, offline místě). Tato fráze je vaším jediným prostředkem pro přístup k bitcoinům v případě ztráty zařízení nebo vymazání aplikace.
- Je také důležité si uvědomit, že kdokoli s touto frází může ukrást všechny vaše bitcoiny. Nikdy je neukládejte digitálně:
 - Žádný snímek obrazovky
 - Žádné zálohování do cloudu, e-mailu nebo zpráv
 - Žádné kopírování/vkládání (riziko uložení do schránky)



**! Tento bod je rozhodující**. Další informace o zálohování :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Zkontrolujte větu seed



Před odesláním finančních prostředků na účet Address spojený s touto frází seed musíte otestovat zálohování svých 12 slov.


Za tímto účelem zapíšeme odkaz, odstraníme soubor Wallet, obnovíme jej pomocí zálohy a zkontrolujeme, zda se odkaz nezměnil.





- Na domovské obrazovce Wallet klikněte na kartu "Nastavení", poté na "Podrobnosti o Wallet" a zkopírujte zPub ([rozšířený veřejný klíč](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Poznámka: zpub Address lze importovat do aplikace Blockstream pro funkci "Watch Only" (viz Dodatek).





- Odstraňte aplikaci, poté obnovte Wallet pomocí **"Obnovit ze zálohy "** zadáním věty Mnemonic a zkontrolujte, zda se zpub nezměnil. Pokud ano, pak je vaše záloha správná a můžete odeslat prostředky do Wallet.





- Chcete-li se dozvědět více o tom, jak provést test obnovení, naleznete zde speciální výukový program :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Zabezpečení přístupu k aplikaci



Uzamkněte přístup k aplikaci pomocí silného kódu PIN:




- Na domovské obrazovce Wallet přejděte na **"Zabezpečení "** a poté klikněte na **"PIN "**
- Zadejte a potvrďte **náhodný šestimístný kód PIN**.



**Biometrická volba**: Pro větší pohodlí je k dispozici, ale je méně bezpečná než robustní PIN kód (riziko neoprávněného přístupu, např. otisk prstu nebo sken obličeje během spánku).



**Poznámka**: PIN zabezpečuje zařízení, ale k obnovení prostředků lze použít pouze frázi seed.





## 5. Použití Liquid Wallet



### 5.1. Přijímání bitcoinů "L-BTC"



Pro příjem Liquid-Bitcoins (L-BTC) je k dispozici několik možností. Můžete někoho požádat, aby vám nějaké poslal přímo sdílením Liquid přijímajícího Address, což je podrobně popsáno níže.



Případně můžete své bitcoiny Exchange získat v řetězci nebo prostřednictvím Lightning Network pro L-BTC pomocí [můstku, jako je Boltz](https://boltz.Exchange/): zadejte svůj Liquid přijímající Address, proveďte platbu podle svých preferencí a obdržte své L-BTC.





- Na domovské obrazovce portfolia klikněte na možnost "**Transakce**" a poté na možnost **"Přijmout "**.



![image](assets/fr/19.webp)





- Ve výchozím nastavení aplikace zobrazí prázdnou **příjemku Address, onchain** (formát SegWit v0, začínající `bc1q...`). Klepnutím na "Bitcoin" vyberte **Liquid Bitcoin** :



![image](assets/fr/20.webp)





- **Možnosti**:
 - (1) Klepnutím na šipky vyberte další novou větu Address spojenou s touto větou seed.
    - (2) Můžete si také vybrat Address z již použitých/zobrazených, a to kliknutím na tři tečky vpravo nahoře a poté na "Seznam adres"
    - (3) Chcete-li požádat o konkrétní částku, klikněte na tři tečky vpravo nahoře, vyberte možnost "Request amount" a zadejte požadovanou částku. QR bude aktualizován a místo Address bude zadán platební URI Bitcoin.



![image](assets/fr/21.webp)





- Sdílejte Address/URI kliknutím na "**Sdílet**", zkopírováním textu nebo naskenováním QR kódu.
- **Ověřování**: Address sdíleného s příjemcem, aby se předešlo chybám nebo útokům (např. malwaru modifikujícímu schránku).



### 5.2. poslat bitcoiny





- Na domovské obrazovce portfolia klikněte na "**Transakce**" a poté na **"Odeslat "** :



![image](assets/fr/22.webp)





- **Zadejte údaje**:
    - (1) Zadejte **Address příjemce** nalepením nebo naskenováním QR kódu.
    - (2) Zkontrolujte majetek a účet, ze kterého jsou prostředky zasílány.
    - (3) Uveďte **částku**, která má být zaslána. Můžete zvolit jednotku: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- **Zkontrolujte**:
    - Na souhrnné obrazovce zkontrolujte kód Address, částku a poplatky.
    - Chyba Address může mít za následek nevratnou ztrátu finančních prostředků. Pozor na škodlivý software, který modifikuje schránku.



![image](assets/fr/24.webp)





- **Potvrzení**: Posunutím tlačítka "Odeslat" transakci podepíšete a rozesíláte.
- **Následná opatření**: V záložce Wallet "Transakce" se transakce zobrazí jako "Nepotvrzená", poté jako "Potvrzená" a následně jako "Dokončená":



![image](assets/fr/25.webp)





- Doba mezi dvěma bloky je u Liquid 1 minuta, takže transakce je rychle potvrzena a dokončena.




## Přílohy



### A1. Další výukové programy aplikace Blockstream



Používání sítě Onchain



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Import a sledování modelu Wallet v režimu "Pouze sledování"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Verze pro stolní počítače



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Osvědčené postupy



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
 - Chcete-li dosáhnout maximální důvěrnosti, připojte svůj Wallet k vlastnímu uzlu Bitcoin prostřednictvím serveru Electrum namísto použití veřejného uzlu





- Vyberte si síť, která nejlépe vyhovuje vašim potřebám:
- **Onchain**: V případě dlouhodobé úschovy nebo transakcí s velkou hodnotou (poplatky jsou v poměru k částce zanedbatelné).
- **Liquid**: Použijte pro rychlé a levné přenosy se zvýšenou důvěrností.
- **Blesk**: Vyberte si okamžité a levné převody malých částek.





- Vždy zkontrolujte dodací adresy:
 - Před odesláním finančních prostředků pečlivě zkontrolujte Address. Finanční prostředky zaslané na nesprávný účet Address jsou navždy ztraceny. Používejte kopírování/vkládání nebo skenování QR kódu, nikdy nekopírujte/neupravujte Address ručně.





- **Optimalizace nákladů**:
 - Pro transakce v řetězci zvolte vhodné poplatky (pomalé, střední, rychlé) podle naléhavosti a přetížení sítě.
 - Pro malá množství použijte Liquid nebo Lightning.





- Aktualizujte aplikaci




### A3. Další zdroje





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