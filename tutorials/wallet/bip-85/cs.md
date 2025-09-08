---
name: BIP-85
description: Jak mohu použít BIP-85 pro generate s více výsevními frázemi z hlavního seed?
---
![cover](assets/cover.webp)



## 1. Porozumění BIP-85



### 1.1 Co je BIP-85?



BIP-85 je pokročilá funkce, která umožňuje vytvořit několik vedlejších frází **seed** z jedné hlavní fráze **seed**.



Z každé vedlejší věty seed lze vytvořit zcela nezávislé portfolio Bitcoin. Tato portfolia lze použít k různým účelům: Hot Wallet na mobilu, portfolio pro příbuzného, samostatné spořicí portfolio atd.



Všechny vedlejší věty seed jsou **matematicky odvozené**, ale je **nemožné z vedlejší věty vysledovat hlavní větu seed**. Tím je zajištěno úplné oddělení jednotlivých portfolií.



Pokud máte přístup ke své hlavní frázi seed (a související frázi passphrase, pokud ji používáte), můžete přegenerovat jakoukoli vedlejší frázi seed **identickým způsobem**, aniž byste ji museli ukládat zvlášť.



### 1.2 Proč používat BIP-85?



BIP-85 je užitečný, pokud chcete :





- Vytvoření několika nezávislých portfolií Bitcoin bez vícenásobného zálohování
- Spravujte své finanční prostředky podle různých účelů (úspory, výdaje, rodina, projekty)
- Zajištění záruk pro příbuzné (funkce "strýčka Jima")
- Odstranění portfolia bez ztráty přístupu k finančním prostředkům
- Zjednodušte si zabezpečení: stačí jedna klíčová fráze seed k ochraně



### 1.3 Výhody oproti BIP-32



Pomocí protokolu BIP-32 lze jedinou větou seed vytvořit kompletní hierarchii účtů a adres generate pomocí odvozovacích cest (například: `m/44'/0'/0'/0/0`). Každá cesta může představovat samostatný účet, ale **všechny zůstávají spojeny se stejnou větou seed**. Pokud je tedy tato věta seed kompromitována, **všechny odvozené účty se stanou přístupnými**.



Pomocí BIP-85 lze hlavní větu seed použít k několika zcela nezávislým vedlejším větám generate: **pokud je jedna z těchto vedlejších vět kompromitována, útočník se již nikdy nebude moci vrátit k hlavní větě seed nebo získat přístup k ostatním portfoliím**.


To umožňuje rozdělit rizika:





- Pro Hot Wallet nebo dočasné použití můžete použít sekundární seed a akceptovat vyšší expozici.
- I v případě, že dojde ke kompromitaci této jednotky Hot Wallet, vaše ostatní finanční prostředky, chráněné jinými sekundárními semeny nebo uchovávané v režimu offline, **zůstanou v bezpečí**.



Na druhou stranu v případě BIP-32 i BIP-85 platí, že pokud dojde k narušení hlavního seed, jsou zranitelné **všechny fondy**. Je proto nezbytné chránit jej nejvyšší úrovní zabezpečení.



![image](assets/fr/02.webp)


## 2. Praktické případy použití BIP-85



BIP-85 umožňuje vytvořit více portfolií Bitcoin z jediné základní věty seed, z nichž každá má vlastní sekundární větu seed. Zde je pět praktických případů použití pro organizaci a zabezpečení vašich fondů Bitcoin. Každý případ vysvětluje, proč je použití BIP-85 praktičtější než správa více účtů s jedinou frází seed prostřednictvím BIP-32.



### 2.1 Omezení rizika méně bezpečného portfolia





- Scénář**: Hot Wallet" Wallet (nainstalovaný na zařízení připojeném k internetu), pro denní transakce.
- Řešení BIP-85**: Vytvoříte sekundární větu seed určenou pro toto portfolio.
- Výhoda oproti BIP-32**: Nemusíte do telefonu importovat primární frázi seed, čímž se snižuje riziko hackerského útoku. Ohrožena je pouze sekundární fráze seed, která chrání vaše ostatní peněženky. U BIP-32 musíte použít hlavní frázi seed a obchozí cestu, čímž dojde k odhalení všech vašich prostředků.



### 2.2 Vytvoření portfolia pro člena rodiny





- Scénář**: Bitcoin Wallet pro někoho blízkého (např. vaši matku), přičemž v případě ztráty jej můžete získat zpět.
- Řešení BIP-85**: Vytvoříte speciální sekundární větu seed a sdílíte pouze tuto větu.
- Výhoda oproti BIP-32**: V případě BIP-32 je při vytváření účtu pro osobu blízkou nutné buď sdílet vaši hlavní frázi seed, čímž riskujete všechny své prostředky a komplikujete správu pro osobu blízkou (správa rozvětvených cest), nebo vytvořit novou frázi seed, kterou uložíte vedle své hlavní fráze seed.



### 2.3 Usnadnění správy oddělených portfolií





- Scénář**: Oddělíte své bitcoiny pro různé účely (např. dlouhodobé úspory, prostředky, které nejsou určeny pro KYC).
- Řešení BIP-85**: Vytvoříte sekundární věty seed věnované každému cíli.
- Výhoda oproti BIP-32**: U BIP-32 mají všechny účty stejnou frázi seed, což komplikuje správu v portfoliích třetích stran, protože je nutné spravovat odvozovací cesty, jako je `m/44'/0'/0'`. Kromě toho není možné přiřadit každému zařízení samostatný účet (např. "spoření na Coldcard", "denní na mobilu", "dovolená na Trezoru"). BIP-85 přiřazuje každému cíli jedinečnou sekundární frázi seed, kterou lze snadno identifikovat a importovat na každé zařízení zvlášť.



### 2.4 Používání dočasného účtu Wallet pro transakce





- Scénář**: Potřebujete dočasné portfolio pro jednorázovou transakci nebo pro zachování důvěrnosti (např.: míchání fondů, interakce s Exchange KYC atd.).
- Řešení BIP-85**: Vytvoříte sekundární větu seed, použijete ji pro transakci a v případě potřeby ji zničíte s vědomím, že ji lze regenerovat.
- Výhoda oproti BIP-32**: V případě BIP-32 je dočasný účet závislý na hlavní větě seed, což v případě kompromitace vystavuje všechny vaše finanční prostředky.





## 3. Než začnete





- Hardware** (volitelné)
 - Karta Coldcard Mk4 nebo Q1
 - Karta MicroSD





- Základní znalosti
 - Porozumění frázím Mnemonic (BIP-39): seznam 12 až 24 slov k uložení portfolia.
 - Vědět, co je Bitcoin Wallet: software nebo zařízení pro správu bitcoinů a jak jej obnovit pomocí fráze Mnemonic.
 - Další zdroje v přílohách.





- Kompatibilní** software
 - Sparrow wallet (počítač, pouze pro hlídání nebo pokročilou správu)
 - Nunchuck (mobilní, pro více podpisů)
 - BlueWallet (mobilní)
 - ...





- 3.4 Konfigurace karty Coldcard**
 - Inicializujte větu seed o 24 slovech na kartě Coldcard.
 - Volitelně: Přidejte passphrase pro zabezpečení přístupu k pobočkám BIP-85.
 - Aktivujte užitečné možnosti: NFC (pro export), zakázat USB na baterii (zabezpečení).




## 4. Návod krok za krokem



Při vytváření, používání a načítání sekundární karty Mnemonic s BIP-85 na kartě Coldcard postupujte podle následujících kroků.



### 4.1 generate a seed vedlejší věta



Z hlavní věty seed vytvoříte vedlejší větu seed.


Zapněte kartu Coldcard a zadejte kód PIN.





- 1. Pokud jste na svůj hlavní model seed použili model passphrase:**
 - Na domovské obrazovce přejděte na `passphrase`.
    - Vyberte možnost `Přidat slovo` a zadejte heslo.
    - Stiskněte tlačítko `Použít`.
    - Zkontrolujte identitu Wallet: Přejděte na `Rozšířené > Zobrazit identitu` a zaznamenejte otisk prstu Wallet.





- 2. Přejděte do nabídky BIP-85**
 - Na domovské obrazovce přejděte na `Rozšířené > Odvození seed B85`
 - Přečtěte si upozornění a potvrďte.



Karta ColdCard vás informuje, že generovaná semena jsou matematicky odvozena od vašeho hlavního kódu seed, ale kryptograficky jsou zcela nezávislá.


![image](assets/fr/03.webp)





- 3. Výběr formátu


Vyberte formát fráze seed: vyberte 12, 18 nebo 24 slov. Zaškrtněte počet slov, který akceptuje model Wallet, do něhož chcete frázi seed importovat.


![image](assets/fr/04.webp)





- 4. Vybrat index
 - Zadejte index v rozmezí 0 až 9999.
 - Tento index je rozhodující pro pozdější regeneraci sekundárního seed. Pečlivě jej uschovejte a opatřete štítkem, např: "Index 1 = Wallet mobile", "Index 2 = rodinný projekt", "Index 4 = testovací směs", ...
 - Pokud ji ztratíte, neztratíte přístup ke svým prostředkům, ale budete muset vyzkoušet kombinace od 0 do 9999, abyste je našli.


![image](assets/fr/05.webp)





- 5. Poznámka nebo export vedlejší věty seed**


Karta ColdCard nyní zobrazuje novou vedlejší větu seed. Můžete :




 - Ruční **poznámka**.
 - Tisk :
     - 1` pro uložení na kartu SD
     - `2` pro **přechod do režimu "použít tento seed"** na kartě ColdCard (užitečné pro export nebo podepisování transakce)
     - 3` pro zobrazení **QR kódu** (ke skenování pomocí mobilní aplikace, jako je BlueWallet nebo Nunchuck)
     - 4` pro odeslání pomocí **NFC**



💡 V tuto chvíli máte nezávislou větu seed, kterou lze použít v jakémkoli BIP39 Wallet (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Použití sekundárního seed



Nyní můžete tento odvozený kód seed použít k vytvoření nového portfolia v :




- mobilní aplikace
- další Hardware Wallet
- portfolio Multisig



### 4.3 Obnovení ztracené sekundární věty seed



Chcete-li kdykoli načíst sekundární jednotku seed, postup opakujte:


1. Restartujte kartu ColdCard


2. Zadejte svůj kód PIN


3. Zadejte svůj kód passphrase, je-li definován


4. Přejděte na `Rozšířené > Odvodit seed B85`


5. Zvolte formát (12/18/24 slov)


6. Zadejte stejný index (např. `1`)


7. Získáte přesně stejný sekundární seed




## 5. Limity, rizika a osvědčené postupy



### 5.1 Závislost na hlavní větě seed + passphrase



Použití BIP85 se zcela opírá o 24slovnou hlavní větu seed a také o passphrase, pokud jste ji použili.




- Z těchto dvou Elements lze regenerovat všechny sekundární věty seed.
- Bez jednoho z těchto 2 Elements ztratíte přístup ke všem derivátovým portfoliím.



### 5.2 Rizika při konfiguraci s více podpisy



Důrazně nedoporučujeme používat v konfiguraci multi-sig sekundární fráze seed vygenerované ze stejné primární fráze seed: pokud dojde ke kompromitaci zařízení nebo primární fráze seed, může útočník přegenerovat všechny klíče multi-sig.



### 5.3 Kompatibilita softwaru



Ne všechny aplikace přímo podporují odvození BIP85. Semena generovaná pomocí BIP85 jsou však standardními semeny BIP39 (12, 18 nebo 24 slov), a lze je proto použít v jakémkoli portfoliu kompatibilním s BIP39.



### 5.4 Registr účtů BIP85



Doporučuje se vést si aktualizovaný osobní rejstřík sekundárních frází seed.




- Umožňuje rychle zjistit, který index BIP85 odpovídá kterému portfoliu, aniž byste museli udržovat sekundární fráze seed.
- Tento rejstřík by měl zůstat minimalistický, bez výslovné zmínky o Bitcoin, a měl by být uložen odděleně od hlavního seed. Nezapomeňte se o něm zmínit v plánu dědictví.



Rejstřík může obsahovat :




- použitý index bIP85 (číslo od 0 do 9999)
- název použití nebo referenční název (např. Hot Wallet, osobní úspory, Wallet od maminky)
- v případě potřeby otisk prstu Wallet pro ověření v aplikaci ColdCard



### 5.5 Zálohování



Zálohy musí obsahovat :




- hlavního systému seed
- gW-76 (pokud se používá)



Nikdy je neskladujte společně:




- hlavního systému seed a passphrase
- hlavní registr seed a registr účtů BIP85



Další zdroje v přílohách.




## PŘÍLOHY



## A.1 Slovníček pojmů





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed phrase](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Uložte frázi pro obnovení



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Porozumění protokolu passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Jak fungují portfolia Bitcoin



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f