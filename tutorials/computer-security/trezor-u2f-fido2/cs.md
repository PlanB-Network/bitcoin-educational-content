---
name: Trezor U2F a FIDO2
description: Posilte své online zabezpečení pomocí aplikace Trezor
---
![cover](assets/cover.webp)



Zařízení Trezor jsou hardwarové peněženky původně určené k zabezpečení Bitcoin Wallet, ale mají také pokročilé možnosti silného ověřování na webu. Díky kompatibilitě s protokoly **U2F** a **FIDO2** umožňují zabezpečit přístup k online účtům, aniž byste se museli spoléhat pouze na hesla.



Protokol U2F (*Universal 2nd Factor*) představily společnosti Google a Yubico v roce 2014 a poté jej standardizovala aliance FIDO. Umožňuje při přihlašování přidat druhý fyzický ověřovací faktor (2FA). Po aktivaci musí uživatelé kromě klasického hesla schválit každý pokus o připojení ke svému účtu stisknutím tlačítka na zařízení Trezor. V tomto kontextu funguje Trezor podobně jako Yubikey.



Tato metoda je založena na asymetrické kryptografii: nepřenášejí se žádná tajná data, takže phishingové nebo odposlechové útoky jsou neúčinné. U2F nyní podporuje mnoho online služeb.



Kromě U2F, které umožňuje dvoufaktorové ověřování, podporují Trezory také FIDO2 (*Fast IDentity Online 2.0*), což je vývojová verze U2F. Jedná se o standardizovaný ověřovací protokol z roku 2018, který rozšiřuje logiku U2F a má za cíl zcela nahradit hesla. Je založen na dvou složkách: *WebAuthn* (na straně prohlížeče) a *CTAP2* (na straně fyzického klíče). FIDO2 umožňuje ověřování "bez hesla": uživatelé se identifikují výhradně prostřednictvím svého zařízení Trezor, které funguje jako jedinečný kryptografický token, bez dalšího hesla. Tento protokol je nyní kompatibilní s řadou online služeb, zejména těch, které jsou určeny pro podniky.



Kromě funkce "bez hesla*" umožňuje FIDO2 také dvoufaktorové ověřování podobně jako U2F.



FIDO2 také zavádí pojem rezidentních pověření, tj. identifikátorů uložených přímo v Trezoru, které obsahují jak soukromý klíč umožňující připojení, tak identifikační údaje uživatele. Tento mechanismus umožňuje ověřování skutečně bez hesla: stačí připojit zařízení Trezor a potvrdit přístup, aniž by bylo nutné zadávat identifikační údaje nebo heslo. Naproti tomu nerezidentní pověření, která jsou konvenčnější, ukládají v zařízení pouze soukromý klíč; ID uživatele zůstává uloženo na straně serveru, a musí se proto zadávat při každém připojení. Na to, jak je uložit pomocí zařízení Trezor, se podíváme později.



V tomto návodu se dozvíte, jak aktivovat U2F nebo FIDO2 pro dvoufaktorové ověřování a jak nakonfigurovat FIDO2 pro přístup k účtům bez hesla přímo pomocí zařízení Trezor.



**Poznámka:** U2F je kompatibilní se všemi modely Trezor, ale FIDO2 je podporováno pouze u modelů Safe 3, Safe 5 a Model T, nikoli u modelu One.



## Použití U2F/FIDO2 pro 2FA na zařízení Trezor



Než začnete, ujistěte se, že jste v zařízení Trezor nastavili Bitcoin Wallet. Je důležité, abyste správně uložili svůj klíč Mnemonic, protože klíče používané pro U2F a FIDO2 při dvoufaktorovém ověřování jsou odvozeny od tohoto klíče Mnemonic. Pokud zařízení Trezor ztratíte nebo poškodíte, můžete obnovit přístup ke klíčům zadáním fráze Mnemonic na jiném zařízení Trezor (upozorňujeme, že pro pověření FIDO2 v režimu "*bez hesla*" samotný klíč seed nestačí, jak uvidíme v dalších částech).



Připojte zařízení Trezor k počítači a odemkněte jej.



![Image](assets/fr/01.webp)



Získejte přístup k účtu, který chcete zabezpečit pomocí dvoufaktorového ověřování. Já například použiji účet Bitwarden. Možnost 2FA obvykle najdete v nastavení služby na kartách "*authentication*", "*security*", "*login*" nebo "*password*".



![Image](assets/fr/02.webp)



V části věnované dvoufaktorovému ověřování vyberte možnost "*Passkey*" (termín se může lišit v závislosti na používaném webu).



![Image](assets/fr/03.webp)



Často budete požádáni o potvrzení aktuálního hesla.



![Image](assets/fr/04.webp)



Bezpečnostní klíč pojmenujte pro snadnější rozpoznání a klikněte na "*Přečíst klíč*".



![Image](assets/fr/05.webp)



Na obrazovce Trezor se zobrazí údaje o vašem účtu. Dotkněte se obrazovky nebo stiskněte tlačítko pro potvrzení. Budete také požádáni o potvrzení kódu PIN.



![Image](assets/fr/06.webp)



Zaregistrujte tento bezpečnostní klíč.



![Image](assets/fr/07.webp)



Když se budete chtít připojit ke svému účtu, budete od nynějška kromě obvyklého hesla požádáni o připojení zařízení Trezor.



![Image](assets/fr/08.webp)



Poté můžete stisknutím obrazovky zařízení Trezor potvrdit ověření.



![Image](assets/fr/09.webp)



Výhodou použití zařízení Trezor Hardware Wallet pro dvoufaktorové ověřování je, že díky frázi Mnemonic můžete snadno obnovit své klíče. Kromě této základní zálohy můžete použít také nouzový kód poskytovaný každou službou, u které máte aktivované 2FA. Tento nouzový kód vám umožní připojit se k účtu, pokud ztratíte bezpečnostní klíč. V případě potřeby tedy nahrazuje 2FA pro připojení.



Například v systému Bitwarden se k tomuto kódu dostanete kliknutím na "*Zobrazit kód pro obnovení*".



![Image](assets/fr/10.webp)



Doporučuji, abyste tento kód uchovávali na jiném místě než hlavní heslo, abyste zabránili jejich společné krádeži. Pokud máte heslo uloženo například ve správci hesel, uchovávejte nouzový kód 2FA odděleně na papíře.



Tento přístup nabízí dvě úrovně zálohování pro případ ztráty zařízení Trezor pro ověřování 2FA: první zálohu s použitím fráze Mnemonic pro všechny účty a druhou zálohu specifickou pro každý účet s nouzovými kódy. Je však důležité **nezaměňovat úlohu fráze Mnemonic s úlohou nouzového kódu** :




- Fráze Mnemonic o 12 nebo 24 slovech vám umožní přístup nejen ke klíčům používaným pro 2FA na všech vašich účtech, ale také k bitcoinům zabezpečeným pomocí zařízení Trezor;
- Nouzový kód umožňuje dočasně obejít požadavek 2FA pouze na daném účtu (v tomto příkladu pouze na Bitwarden).



## Používání FIDO2 v zařízení Trezor



Kromě dvoufaktorového ověřování umožňuje FIDO2 také ověřování "bez hesla", tj. bez nutnosti zadávat heslo při přihlašování na web. Pro přístup k zabezpečenému účtu tímto způsobem stačí připojit zařízení Trezor k počítači. Zde naleznete návod, jak tuto funkci nakonfigurovat.



Než začnete, ujistěte se, že jste na zařízení Trezor nastavili Bitcoin Wallet. Je důležité uložit Mnemonic, protože identifikátory FIDO2 "*bez hesla*" jsou zašifrovány vaším seed (jak tyto identifikátory správně uložit, zjistíme v následující části).



Připojte zařízení Trezor k počítači a odemkněte jej.



![Image](assets/fr/01.webp)



Přistupte k účtu, který chcete zabezpečit, v režimu "*bez hesla*". Jako příklad použiji účet Bitwarden. Tuto možnost obvykle najdete v nastavení služby, často na kartě "*autentizace*", "*zabezpečení*" nebo "*heslo*".



Například v systému Bitwarden se tato možnost nachází na kartě "*Master password*". Kliknutím na "*Zapnout*" aktivujete ověřování prostřednictvím FIDO2.



![Image](assets/fr/11.webp)



Často budete vyzváni k potvrzení hesla.



![Image](assets/fr/12.webp)



Na obrazovce Trezor se zobrazí údaje o vašem účtu. Dotkněte se obrazovky nebo stiskněte tlačítko pro potvrzení. Budete také muset potvrdit kód PIN.



![Image](assets/fr/13.webp)



Na webu přidejte jméno, abyste si zapamatovali bezpečnostní klíč, a klikněte na "*Zapnout*".



![Image](assets/fr/14.webp)



Poté budete vyzváni k identifikaci, aby bylo možné zkontrolovat, zda klíč správně funguje.



![Image](assets/fr/15.webp)



Od této chvíle již nebude nutné při přihlašování k účtu zadávat e-mail Address ani přihlašovací jméno. Stačí kliknout na tlačítko a ověřit se fyzickým klíčem na přihlašovacím formuláři.



![Image](assets/fr/16.webp)



Potvrďte připojení k zařízení Trezor zadáním kódu PIN Hardware Wallet.



![Image](assets/fr/17.webp)



Budete připojeni ke svému účtu, aniž byste museli zadávat heslo.



![Image](assets/fr/18.webp)



**Vezměte prosím na vědomí, že i když na zařízení Trezor aktivujete ověřování "*bez hesla*" prostřednictvím FIDO2, hlavní heslo pro váš online účet bude stále platné pro účely přihlášení**



## Uložení pověření FIDO2 (obyvatelé pověření)



Pokud používáte FIDO2 nebo U2F pro dvoufaktorové ověřování, tj. pro přihlašování k účtům, které kromě ověření 2FA prostřednictvím zařízení Trezor vyžadují také heslo, získáte přístup ke klíčům pouze pomocí fráze Mnemonic. Pokud však používáte FIDO2 v režimu "*bez hesla*", jak je popsáno v předchozí části, bude nutné kromě zálohování fráze Mnemonic, která tyto přihlašovací údaje šifruje, vytvořit také kopii přihlašovacích údajů FIDO.



K tomu budete potřebovat počítač s nainstalovaným jazykem Python. Otevřete terminál a spusťte následující příkaz pro instalaci potřebného softwaru Trezor:



```shell
pip3 install --upgrade trezor
```



Připojte zařízení Trezor k počítači prostřednictvím rozhraní USB a odemkněte jej pomocí kódu PIN.



![Image](assets/fr/01.webp)



Chcete-li načíst seznam identifikátorů FIDO2 uložených v zařízení Trezor, spusťte následující příkaz:



```shell
trezorctl fido credentials list
```



Potvrďte export na zařízení Trezor.



![Image](assets/fr/19.webp)



Na terminálu se zobrazí přihlašovací údaje FIDO2. Například pro můj účet Bitwarden jsem dostal tyto informace:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Všechny tyto informace zkopírujte a uložte do textového souboru. S touto zálohou není spojeno žádné významné riziko kromě toho, že odhalíte, že tyto služby používáte s FIDO2. "*Identita pověření*" je zašifrována pomocí vašeho Wallet's seed, což znamená, že útočník, který by tuto zálohu získal, by se nemohl připojit k vašim účtům, ale pouze by si všiml, že tyto účty používáte. K dešifrování těchto ID je třeba mít v zařízení Wallet nainstalován modul seed.



Můžete proto vytvořit několik kopií tohoto textového souboru a uložit je na různých místech, například lokálně v počítači, ve službě hostingu souborů a na externím médiu, například na USB flash disku. Mějte však na paměti, že tato záloha není automaticky aktualizována, takže ji budete muset obnovit pokaždé, když nastavíte nové "*bezheslové*" spojení se zařízením Trezor.



Nyní si představme, že jste rozbili svůj Trezor. Chcete-li získat zpět své pověření FIDO2, musíte nejprve obnovit svůj Wallet pomocí fráze Mnemonic na novém zařízení Trezor kompatibilním s FIDO2.



Po dokončení obnovení importujte své identifikátory FIDO2 do nového zařízení tak, že v terminálu spustíte následující příkaz:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Jednoduše nahraďte `<CREDENTIAL_ID>` jedním z vašich identifikátorů. Například v mém případě by to dalo :



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Zařízení Trezor vás vyzve k importu identifikátoru FIDO2. Potvrďte stisknutím tlačítka na obrazovce.



![Image](assets/fr/20.webp)



Přihlášení FIDO2 je nyní na zařízení Trezor funkční. Tento postup opakujte pro každý ze svých identifikátorů.



Gratulujeme, nyní jste připraveni na používání zařízení Trezor s U2F a FIDO2! Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte palec Green. Neváhejte tento návod sdílet na svých sociálních sítích. Děkuji vám mnohokrát!



Doporučuji také tento další tutoriál, ve kterém se podíváme na jiné řešení pro ověřování U2F a FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e