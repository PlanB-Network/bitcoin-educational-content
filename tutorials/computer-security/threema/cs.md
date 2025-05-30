---
name: Threema
description: Bezpečné a anonymní zasílání rychlých zpráv
---
![cover](assets/cover.webp)



Společnost Threema byla založena v roce 2012 ve Švýcarsku a je to aplikace pro zasílání rychlých zpráv, která zaručuje soukromí a bezpečnost. Na rozdíl od aplikací WhatsApp, Telegram nebo Signal nevyžaduje Threema k vytvoření účtu žádné telefonní číslo ani e-mail Address. Každý uživatel má jedinečný identifikátor, který umožňuje zcela anonymní registraci.



Po technické stránce je komunikace přes systém Threema šifrovaná od konce ke konci. Kód mobilní aplikace je od roku 2020 otevřený, ale serverová infrastruktura zůstává proprietární a centralizovaná. Servery jsou hostovány výhradně ve Švýcarsku (zemi proslulé svým právním rámcem pro ochranu údajů).



![Image](assets/fr/01.webp)



Threema má základní klienty pro Android a iOS. K dispozici je také webová aplikace a software pro Windows, Linux a MacOS. Chcete-li je však používat, musíte se nejprve zaregistrovat v mobilním zařízení.



Aplikace Threema není zdarma. Funguje na modelu jednorázového nákupu: 5,99 EUR za doživotní používání aplikace (nebo 4,99 EUR, pokud si ji koupíte přímo). Abyste mohli aplikaci Threema skutečně anonymně používat, musí být anonymní i platba. Proto si můžete na "*Threema Shop*" koupit aktivační klíč v bitcoinech nebo v hotovosti a aktivovat si tak verzi pro Android. Naopak v systému iOS musí nákup proběhnout přes App Store, a to kvůli omezením společnosti Apple týkajícím se zpeněžení aplikací.



K dispozici je také speciální verze pro firmy s názvem "*Threema Work*". V tomto návodu se zaměříme na verzi pro domácnosti.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| **Threema**          | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end šifrování*



## Instalace aplikace Threema



Threema je k dispozici na všech platformách. Aplikaci si můžete stáhnout přímo z obchodu s aplikacemi v telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



V systému Android je také možné [instalovat přes APK](https://shop.threema.ch/en/download).



Existují také [počítačové verze](https://threema.ch/download) (MacOS, Linux a Windows). Tento návod vám ukáže, jak je synchronizovat.



## Koupit licenci Threema



Pokud jste aplikaci nainstalovali přímo přes obchod s aplikacemi, zaplatili jste již za licenci a měli byste k ní mít okamžitý přístup. Pokud jste šli přes F-Droid nebo APK, musíte nyní zakoupit licenci na oficiálních webových stránkách.



[Přejděte na stránku "*Threema Shop*"(https://shop.threema.ch/) a klikněte na tlačítko "*Koupit Threema pro Android*".



![Image](assets/fr/02.webp)



Zvolte počet licencí, které chcete zakoupit (pokud je to jen pro vás, stačí jedna), vyberte měnu a způsob dodání licence. Můžete si vybrat, zda chcete licenci obdržet e-mailem, nebo přímo na webu, pokud si přejete zůstat v anonymitě. Poté klikněte na tlačítko "*Přejít k platbě*".



![Image](assets/fr/03.webp)



Zvolte si způsob platby. V mém případě budu platit bitcoiny, což doporučuji i vám, protože vám to umožní zůstat v anonymitě (za předpokladu, že vhodně používáte Bitcoin) a je to mnohem pohodlnější než platba na dálku v hotovosti. Poté klikněte na tlačítko "*Další*".



![Image](assets/fr/04.webp)



Pokud Invoice nepotřebujete, klikněte znovu na tlačítko "*Další*", aniž byste zadávali osobní údaje.



Poté potvrďte nákup kliknutím na "*Potvrdit platbu*".



![Image](assets/fr/05.webp)



Poté je třeba odeslat uvedenou částku na poskytnutý účet Bitcoin Address (bohužel blesk zatím není podporován). Po potvrzení transakce na Blockchain klikněte na tlačítko "*Zavřít*" vedle Invoice.



Poté získáte přístup ke svému licenčnímu klíči. Upozornění: pokud jste nezadali e-mail Address, zobrazí se tento klíč pouze zde. Nezapomeňte si uložit adresu URL této stránky, abyste se k ní mohli v případě potřeby dostat později.



![Image](assets/fr/06.webp)



## Vytvoření účtu na platformě Threema



Nyní, když máte licenční klíč, můžete aplikaci konečně spustit. Pokud jste si aplikaci Threema nezakoupili prostřednictvím obchodu s aplikacemi, budete při prvním spuštění vyzváni k zadání licenčního klíče, který jste si zakoupili na webu.



![Image](assets/fr/07.webp)



Poté klikněte na tlačítko "*Nastavit nyní*".



![Image](assets/fr/08.webp)



Pohybem prstu po obrazovce získáte zdroj entropie generate, který je potřebný k vytvoření vašeho "*Threema ID*".



![Image](assets/fr/09.webp)



Poté se zobrazí vaše "*Threema ID*". To vám umožní kontaktovat ostatní uživatele. Klikněte na "*Další*".



![Image](assets/fr/10.webp)



Zvolte heslo. To vám v případě potřeby umožní obnovit přístup k účtu. Heslo si vytvořte co nejdelší a náhodné a jeho kopii si bezpečně uložte, například do správce hesel.



![Image](assets/fr/11.webp)



Poté si zvolte uživatelské jméno, které může být buď vaše skutečné jméno, nebo pseudonym.



![Image](assets/fr/12.webp)



ID Threema pak můžete propojit se svým telefonním číslem. To vám usnadní vyhledávání v kontaktech, ale pokud používáte Threema, je to také kvůli zachování vaší anonymity: proto je lepší ho nepropojovat. Klikněte na tlačítko "*Další*".



![Image](assets/fr/13.webp)



Po dokončení tohoto kroku klikněte na tlačítko "*Dokončit*".



![Image](assets/fr/14.webp)



Nyní jste připojeni ke společnosti Threema a můžete začít komunikovat.



![Image](assets/fr/15.webp)



## Nastavení systému Threema



Nejdříve přejděte do nastavení kliknutím na tři malé tečky v pravém horním rohu a poté vyberte možnost "*Nastavení*".



![Image](assets/fr/16.webp)



Na kartě "*Soukromí*" najdete několik možností, které můžete přizpůsobit svým potřebám:




- Synchronizace kontaktů v telefonu ;
- Přijímání zpráv od neznámých osob;
- Indikátor zápisu při zadávání dat ;
- Oznámení o přijetí zpráv..



![Image](assets/fr/17.webp)



Na kartě "*Zabezpečení*" doporučuji aktivovat možnost "*Zamykací mechanismus*", abyste ochránili přístup k aplikaci. Doporučuje se také aktivovat možnost passphrase pro zabezpečení místních záloh.



![Image](assets/fr/18.webp)



Neváhejte prozkoumat další části nastavení a přizpůsobit aplikaci svým preferencím.



![Image](assets/fr/19.webp)



## Zálohování účtu Threema



Než začnete vyměňovat zprávy, je důležité naplánovat způsob obnovení účtu, zejména v případě výměny nebo ztráty telefonu. Za tímto účelem klikněte na tři tečky v pravém horním rohu okna Interface a poté přejděte do nabídky "*Zálohy*".



![Image](assets/fr/20.webp)



Zde najdete dvě možnosti zálohování dat:




- "*Threema Safe*";
- "*Zálohování dat*".



"Threema Safe* ukládá všechny informace o vašem účtu, kromě konverzací, na serverech společnosti Threema. Tyto údaje jsou zašifrovány heslem, které jste si zvolili při vytváření účtu, čímž je zajištěno, že k nim společnost Threema nemá přístup. Zálohování se provádí automaticky a pravidelně.



Chcete-li obnovit svůj účet v novém zařízení, stačí pomocí aplikace "*Threema Safe*" zadat své "*Threema ID*" a heslo. Pokud některý z těchto dvou údajů chybí, nebude možné účet obnovit.



Tato možnost umožňuje načíst pouze vaše ID, profil, kontakty, skupiny a některá nastavení, ale **ne historii konverzací**.



Chcete-li aktivovat funkci "*Threema Safe*", jednoduše zaškrtněte tuto možnost v nabídce "*Zálohování*".



![Image](assets/fr/21.webp)



Pokud chcete také zálohovat a obnovit historii konverzací, musíte použít možnost "*Zálohování dat*". Ta vytvoří úplnou zálohu vašeho účtu uloženou lokálně v telefonu. Tuto zálohu budete muset přenést do nového zařízení a pomocí hesla (a případně passphrase) obnovit celý účet.



Protože je tato záloha pouze místní, je třeba ji pravidelně kopírovat na externí médium. V opačném případě bude obnova v případě ztráty zařízení nemožná. Tato metoda se proto hodí spíše pro plánované přenášení z jednoho zařízení do druhého než pro nouzové situace.



Upozornění: "*Zálohování dat*" funguje pouze v případě, že používáte stejný operační systém. Nebudete ji moci použít například k přechodu z telefonu Samsung na iPhone.



## Přizpůsobení profilu Threema



V levém horním rohu aplikace Interface klikněte na svůj profilový obrázek a poté vyberte možnost "*Můj profil*".



![Image](assets/fr/22.webp)



Zde si můžete přizpůsobit svůj profil: přidat fotografii, zvolit, kdo jej může vidět, nebo zobrazit své přihlášení do systému Threema.



![Image](assets/fr/23.webp)



## Synchronizace softwaru počítače



Pokud chcete mít přístup ke svým konverzacím na počítači, můžete svůj účet Threema synchronizovat pomocí specializovaného softwaru. Stáhněte si software pro svůj operační systém [z oficiálních webových stránek](https://threema.ch/en/download).



![Image](assets/fr/24.webp)



V telefonu klikněte na tři tečky vpravo nahoře a otevřete nabídku "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Klikněte na "*Přidat zařízení*" a poté pomocí telefonu naskenujte kód QR zobrazený softwarem v počítači.



![Image](assets/fr/26.webp)



Synchronizaci potvrdíte kliknutím na skupinu emoji zobrazenou v softwaru.



![Image](assets/fr/27.webp)



V počítači se přihlaste pomocí hesla.



![Image](assets/fr/28.webp)



Kromě mobilní aplikace můžete nyní přistupovat ke svému účtu Threema přímo z počítače.



![Image](assets/fr/29.webp)



## Odesílání zpráv pomocí systému Threema



Nyní, když je vše správně nastaveno, můžete začít komunikovat. Klikněte na tlačítko "*Spustit chat*".



![Image](assets/fr/30.webp)



Vyberte možnost "*Nový kontakt*".



![Image](assets/fr/31.webp)



Zadejte nebo naskenujte "*Threema ID*" svého korespondenta.



![Image](assets/fr/32.webp)



Klikněte na ikonu zprávy.



![Image](assets/fr/33.webp)



Pošlete první zprávu svému korespondentovi.



![Image](assets/fr/34.webp)



Jakmile váš korespondent odpoví, spojení se naváže a vy uvidíte jeho jméno a profilovou fotografii. Poté můžete odesílat zprávy Exchange, multimediální soubory a dokonce i volat.



![Image](assets/fr/35.webp)



Gratulujeme, nyní jste se seznámili s používáním aplikace Threema messaging, která je skvělou alternativou k aplikaci WathsApp! Pokud se vám tento návod zdál užitečný, budu vám velmi vděčný, když mi níže zanecháte palec Green. Neváhejte tento návod sdílet na svých sociálních sítích. Moc vám děkuji!



Doporučuji také tento další tutoriál, ve kterém vám představím Proton Mail, alternativu Gmailu, která je mnohem šetrnější k soukromí:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2