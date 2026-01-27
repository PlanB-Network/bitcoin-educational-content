---
name: COLDCARD - Co-Sign
description: Objevte funkci Co-Sign a použijte ji na své kartě COLDCARD
---

![cover](assets/cover.webp)


*Upozornění: Tento návod je určen lidem, kteří již mají nějaké zkušenosti s peněženkami s více podpisy, zařízeními Coinkite a softwarem, jako je Sparrow wallet nebo Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Proč ColdCard Co-Sign?



Tato funkce umožňuje přidat **výdajové podmínky** do zařízení ColdCard (Q nebo Mk4) na způsob hardwarového bezpečnostního modulu (HSM) a chránit tak své finanční prostředky při zachování značné flexibility a kontroly nad nimi.



Výdajové podmínky mohou být například:





- Omezení velikosti**: omezení množství bitcoinů, které můžete utratit v rámci jedné transakce.
- Omezení rychlosti:** rozhodněte, kolik transakcí můžete provést za jednotku času (za hodinu, den, týden atd.), přičemž mezi nimi musíte mít minimální počet bloků.
- Předem schválené adresy:** Bitcoiny lze posílat pouze na předem schválené adresy.
- Dvoufaktorové ověřování:** Vyžaduje potvrzení mobilní aplikací 2FA třetí strany (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) na chytrém telefonu/tabletu s přístupem k internetu a podporou NFC.



**Jak to funguje



Přidáním druhého klíče seed k zařízení ColdCard Mk4 nebo Q, který se nazývá "Spending Policy Key" a který budeme v tomto návodu označovat jako "C Key".


Kromě tohoto dodatečného klíče seed budete vyzváni k zadání alespoň jednoho dalšího klíče Supply (XPUB), který budeme nazývat "záložní klíč", abyste mohli vytvořit klíč Wallet Multisig 2-on-N.



Stručně řečeno, vytvoříme Wallet Multisig a vaše zařízení ColdCard bude obsahovat 2 soukromé klíče potřebné k utrácení prostředků, hlavní klíč seed zařízení a "klíč zásad utrácení".



Pokaždé, když je klíč "C" požádán o podpis, uplatní se zadané podmínky pro čerpání a karta ColdCard se podepíše pouze tehdy, pokud je transakce v souladu s těmito podmínkami.



Pokud si přejete od těchto podmínek výdajů upustit, můžete tak učinit:




- podpisem jedním ze záložních klíčů a rukou seed nebo 2 záložními klíči v závislosti na velikosti Multisig.
- zadáním klíče "Spending Policy Key" nebo "C Key" v nabídce "Co-Sign". **Druhý z nich nelze zadat přímo v zařízení, jinak by mohl kdokoli zrušit nastavené podmínky výdajů**




## Konfigurace spolupodpisu karty ColdCard



![video](https://youtu.be/MjMPDUWWegw)



### 1 - Aktivace funkcí



Nejprve se ujistěte, že je v zařízení nainstalována alespoň nejnovější verze firmwaru:




- Mk4: v5.4.2
- Q: v1.3.2Q




Na kartě Mk4 nebo ColdCardQ přejděte na *Rozšířené nástroje > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*V následujícím návodu budou snímky obrazovky pořízeny na kartě ColdCardQ, ale kroky a nabídky jsou pro Mk4 a Q stejné.*



Zobrazí se souhrn funkcí.


Pro označení klíčů se používá následující terminologie, kterou budeme používat i při vytváření víceznakového systému Wallet 2 na 3, který se chystáme vytvořit:



Klíč A = hlavní karta Coldcard seed


Klíč B = záložní klíč


Klíč C = Klíč výdajové politiky



Klikněte na **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



V dalším kroku je třeba rozhodnout, který soukromý klíč bude sloužit jako "klíč výdajové politiky" nebo "klíč C".



Vidíme, že máme k dispozici několik možností:





- Nebo stisknutím tlačítka **"ENTER "** vytvoříte novou větu generate o 12 slovech.





- Buď klikněte na **"(1) "** pro import stávajícího 12slovného seed, nebo vyberte **"(2) "** pro import stávajícího 24slovného seed.





- Nebo stiskněte **"(6) "** pro importování seed z trezoru vašeho zařízení.



Pro účely tohoto návodu jsme se rozhodli importovat existující 12slovný soubor seed stisknutím tlačítka **"(1) "**. Může se jednat o libovolný kód seed BIP39, který již vlastníte a pro který máte samozřejmě zálohu.



Pomocí klávesnice zadejte 12 slov seed. Pro tento příklad zvolíme platnou frázi seed beef x 12. Poté stiskněte **"ENTER "**.


*Upozornění: pokud nemáte zálohu tohoto dokumentu seed, nebudete již moci upravit nastavení "Co-Sign" ve svém zařízení, abyste mohli změnit podmínky pro utrácení*



V zařízení je nyní aktivována funkce "Co-Sign". Dále budeme muset zvolit naše výdajové podmínky a poté dokončit vytvoření vícepodpisu Wallet.



![Co-Sign](assets/fr/03.webp)



### 2 - Zvolte podmínky výdajů nebo "*výdajové politiky*"



Zde určíme podmínky výdajů, které musí být splněny, když **"Klíč C "** nebo **"Klíč zásad výdajů**" podepíše transakci.



V nabídce **"Spoluúčast na podpisu "** klikněte na **"Zásady výdajů**".



Poté můžete zvolit maximální velikost, tj. maximální počet satošů, které lze utratit v rámci jedné transakce.



Pro tento příklad zvolíme maximální velikost **21212** satoší. Potvrďte kliknutím na **"ENTER "**.




![Co-Sign](assets/fr/04.webp)



Poté se rozhodneme nastavit maximální rychlost, tj. počet transakcí, které bude zařízení schopno podepsat za jednotku času. Pro tento návod zvolíme neomezenou rychlost, tj. bez omezení počtu transakcí.




![Co-Sign](assets/fr/05.webp)



### 3 - Vytvořit Wallet Multisig 2-on-N



Kromě **hlavního klíče seed** (klíč A) a **klíče "Spending Policy Key "** (klíč C) musíme ještě zvolit třetí klíč pro náš Wallet Multisig, tj. **"Záložní klíč "** (klíč B).



Náš klíč "B" bude muset být importován buď prostřednictvím karty SD, nebo v případě aplikace ColdCardQ prostřednictvím kódu QR.


K tomu budeme potřebovat druhé zařízení ColdCard Mk4 nebo Q, na kterém je použit náš klíč B.



Na tomto druhém zařízení obsahujícím váš **"Záložní klíč "**, v tomto případě například na kartě ColdCard Mk4, přejděte z hlavní nabídky na **"Nastavení "**, poté na **"Multisig Wallet"** a nakonec na **"Export Xpub "**.


(Pokud je vaším druhým zařízením ColdCardQ, budete mít samozřejmě možnost exportovat svůj Xpub prostřednictvím kódu QR).





![Co-Sign](assets/fr/06.webp)





Na další obrazovce vložte kartu SD a klikněte na tlačítko **"validate "** vpravo dole. Poté klikněte na **"(1) "** pro uložení souboru na kartu SD.



Soubor bude ve svém názvu obsahovat otisk veřejného klíče (*fingerprint*) a bude mít tvar `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Poté vložte kartu SD do "počáteční" aplikace ColdCardQ a importujte náš "záložní klíč" (klíč B).


V nabídce "ColdCard Co-Signing" vyberte "Build 2-of-N", na další obrazovce klikněte na **"ENTER "** a poté znovu na **"ENTER "** pro import "Backup Key" z karty SD.



![Co-Sign](assets/fr/08.webp)



Na další obrazovce nechte položku "Číslo účtu" prázdnou (pokud přesně nevíte, co děláte) a znovu klikněte na **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Konečně jsme připraveni používat náš nový model Wallet Multisig 2-sur-3 v následujícím složení:



Klíč A= Studená karta Q master seed


Klíč B= záložní klíč (právě importovaný z druhého zařízení Coldcard)


Klíč C= Klíč výdajové politiky (pokud je použit k podpisu, ukládá předem definované podmínky pro čerpání)



## Spolupodpis s Sparrow wallet



V případě potřeby si přečtěte níže uvedené výukové programy, abyste se seznámili se softwarem Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Export Wallet Multisig 2-sur-3 do Sparrow wallet



Nyní potřebujeme exportovat naše Wallet Multisig do Sparrow, abychom tam mohli umístit naše první satoši.



V hlavní nabídce aplikace ColdCardQ vyberte možnost **"Nastavení "** a poté **"Multisig Peněženky "**.


Nyní se zobrazí sada peněženek Multisig známá kartě ColdCard s počtem klíčů "2/3" (2-sur3). Vyberte právě vytvořenou peněženku Multisig **"ColdCard Co-Sign "** a klikněte na **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Nakonec vyberte metodu, která vám umožní exportovat Wallet do Sparrow. V našem případě zvolíme SD kartu, a proto po vložení SD karty do slotu A zařízení klikněte na **"(1) "**.



![Co-Sign](assets/fr/11.webp)



Poté v okně Sparrow wallet vyberte možnost "Importovat Wallet".



![Co-Sign](assets/fr/12.webp)



Poté klikněte na **"Importovat soubor "**. Poté vyberte soubor **"export-Coldcard_Co-sign.txt "** na vaší SD kartě.



![Co-Sign](assets/fr/13.webp)



Zadejte název Wallet tak, jak se bude zobrazovat v Sparrow, a zvolte heslo pro zašifrování Wallet (nebo ne).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Nyní jsme připraveni obdržet první saturace a otestovat podmínky výdajů, které jsme aplikovali na náš Wallet.



![Co-Sign](assets/fr/16.webp)



### 2 - Testování předem definovaných výdajových politik



Připomínáme, že jsme se rozhodli pro maximální magnitudu našeho Wallet Multisig 21212 satoši. To znamenalo, že pokaždé, když klíč Spending Policiy (klíč C) podepíše transakci, bude tato platná pouze v případě, že vynaložená částka bude menší nebo rovna 21212 satoši.



Vyzkoušejme to.


Nejprve klikneme na kartu "Receive" (Přijmout) v okně Sparrow a na kartu Wallet, kterou budeme používat v celém tomto výukovém programu, přeneseme několik datových souborů.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Pak zkusme utratit více než povolených 21212 satošů simulací transakce za 50 000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Po naskenování kódu QR představujícího *nepodepsanou* transakci pomocí našeho nástroje ColdCardQ pro import transakce se na obrazovce zobrazí toto. Výstražná zpráva nám oznamuje, že nebyly splněny podmínky pro čerpání. Pokud transakci přesto podepíšeme, pak se podepíše pouze jeden ze dvou klíčů (hlavní klíč seed v zařízení, ale ne "klíč C").




![Co-Sign](assets/fr/23.webp)



Zde vidíme, že po importu naší transakce do systému Sparrow byl na transakci použit pouze jeden z podpisů.



![Co-Sign](assets/fr/24.webp)




Nyní experiment zopakujme, ale pro transakci o velikosti 21 000 satoši, tj. menší než maximální velikost (21212 Sats), kterou jsme stanovili pro tento Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Zkusme tuto transakci podepsat pomocí naší karty ColdCardQ.



Tentokrát se žádný problém neobjevil, nezobrazilo se žádné varování, a když jsme podepsanou transakci importovali do Sparrow wallet, byly tentokrát použity dva podpisy, takže transakce byla platná a připravená k distribuci.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Podepisování pomocí nástroje Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1 - Web 2FA a adresy na bílé listině



V tomto odstavci použijeme náš Wallet Multisig Co-Sign s Nunchukem a využijeme příležitosti použít nové podmínky pro výdaje, abychom zjistili, jak to jde.



Přejděte na *Rozšířené nástroje > ColdCard Co-Signing*.


Jsme požádáni o zadání klíče "Spending Policy Key", abychom se dostali do nabídky, která nám umožní změnit podmínky výdajů. V našem případě zadáme 12 x "beef".



Z praktických důvodů souvisejících s tímto návodem jsme se rozhodli zachovat velikost 21212 Sats a maximální "mezní rychlost". Na druhou stranu budeme pomocí nabídky **"Whitelist Addresses "** vnucovat adresy, na které mohou být naše prostředky vynaloženy.




![Co-Sign](assets/fr/31.webp)




Naskenujte kódy QR přiřazené k adresám (vybereme 2), které chcete přidat do bílého seznamu, a klikněte na **"ENTER "**. Po ověření adres postupným stisknutím tlačítka **"ENTER "** vidíme, že byly uplatněny limity na adresy Magnitude a příjemce.



![Co-Sign](assets/fr/32.webp)



Abychom získali úplnou představu o možnostech, které funkce "Co-Sign" nabízí, aktivujme možnost "Web 2FA".


Tato funkce umožňuje použít aplikaci kompatibilní s protokolem TOTP RFC-6238, například Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / nebo Aegis Authenticator, a přidat tak další zabezpečení Layer.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Konkrétně před podpisem transakce je třeba přiblížit zařízení s podporou NFC a připojením k internetu ke kartě Coldcard. Tím se automaticky dostanete na webovou stránku coldcard.com, kde budete vyzváni k zadání šestimístného kódu pro vaši žádost. Pokud zadáte správný kód, zobrazí se na webové stránce buď QR kód, který je třeba naskenovat pro kartu ColdCardQ, nebo 8místný kód, který je třeba zadat na zařízení Mk4 a autorizovat tak zařízení k podpisu.





![Co-Sign](assets/fr/33.webp)



Po naskenování QR kódu zobrazeného v aplikaci duálního ověřování a přidání účtu ColdCard Co-Sign (CCC) budete vyzváni k ověření, zda je vše v pořádku, zadáním kódu 2FA.



Zadejte svou kartu ColdCard do zadní části zařízení NFC.



![Co-Sign](assets/fr/34.webp)



Na otevřené webové stránce zadejte kód 2FA své oblíbené aplikace. Poté naskenujte QR kód zobrazený na kartě ColdCardQ (nebo zadejte 8místný kód zobrazený na kartě Mk4).



![Co-Sign](assets/fr/35.webp)




Nyní jsme zavedli omezení velikosti (21212 Sats), cílových adres a dvojího ověřování.



![Co-Sign](assets/fr/36.webp)



### 2- Export Wallet Multisig 2-na-3 do Nunchuku



Tentokrát exportujeme Wallet Multisig 2-on-3 do Nunchuku, stejně jako jsme to udělali dříve s Sparrow.


Přejděte do *Nastavení > Peněženky Multisig > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Tentokrát vyberte možnost NFC pro export kliknutím na stejnojmenné tlačítko ColdcardQ **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Pokud aplikaci Nunchuk otevíráte poprvé, klikněte na **"Obnovit stávající Wallet"**.



![Co-Sign](assets/fr/38.webp)



Pokud již máte v aplikaci Wallet, klikněte na **"+"** vpravo nahoře a poté na **"Obnovit stávající Wallet"**.



![Co-Sign](assets/fr/39.webp)




Poté zvolte **"Obnovit Wallet z karty COLDCARD "** a poté **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Nakonec klepněte zadní stranou smartphonu na obrazovku zařízení ColdCardQ a importujte zařízení Wallet prostřednictvím technologie NFC.



![Co-Sign](assets/fr/41.webp)



Náš účet a satoši, které byly dříve uloženy prostřednictvím Sparrow wallet, jsou zpět.



![Co-Sign](assets/fr/42.webp)



### 3 - Testování předem definovaných výdajových politik



Nyní se pokusíme provést transakci, která porušuje 2 podmínky výdajů, které jsme nastavili. **Zkusíme utratit více než 21212 Sats na neschválený účet Address.** Zkusíme poslat 22 222 Sats na náhodný účet Address.



![Co-Sign](assets/fr/43.webp)



Po vytvoření transakce klikněte na 3 malé tečky v pravém horním rohu a exportujte ji na kartu ColdCard.



![Co-Sign](assets/fr/44.webp)



Poté vyberte možnost **"Exportovat přes BBQR "** a naskenujte QR kód zobrazený pomocí aplikace ColdCardQ.



![Co-Sign](assets/fr/45.webp)



Aplikace ColdcardQ poté zobrazí varování, které po posunutí na spodní část obrazovky objasní, že transakce podle očekávání porušuje podmínky výdajů.



**Všimněte si, že zařízení neuvádí, o jaké podmínky výdajů se jedná, aby se případný útočník nemohl pokusit omezení obejít.**




![Co-Sign](assets/fr/46.webp)



Pokud ještě potvrdíte stisknutím tlačítka **"ENTER "**, zobrazí se QR kód představující podepsanou transakci. Pokud jej importujete na Nunchuk, uvidíte, že byl použit pouze jeden podpis.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Proveďme přesně stejnou operaci, ale tentokrát s transakcí, která respektuje limit velikosti (21212 Sats), a odešle satoši na jednu ze dvou adres, které jsme předem nakonfigurovali.



Nunchuk 12121 Sats zasíláme na jednu z našich 2 adres. Poté vyexportujeme transakci do naší karty ColdCard, jak jsme již dříve provedli.



![Co-Sign](assets/fr/49.webp)




Po importu nepodepsané transakce do naší aplikace ColdCardQ se podívejme, co se nám tentokrát zobrazí.



Upozornění se objevuje vždy, ale tentokrát po přejití na spodní část obrazovky vidíme, že jde o ověření transakce pomocí 2FA. Zařízení nás vyzve, abychom kartu ColdcardQ přiblížili k terminálu NFC připojenému k internetu (chytrý telefon nebo tablet), což uděláme.



![Co-Sign](assets/fr/50.webp)



Na chytrém telefonu se otevře webová stránka s výzvou k zadání kódu 2FA, což díky aplikaci Proton Authenticator učiníme.



![Co-Sign](assets/fr/51.webp)





Poté naskenujte QR kód, který se zobrazí na webové stránce, a autorizujte svou kartu ColdCard k podpisu transakce.


Transakce je nyní podepsána dvěma klíči, a je tedy platná.



Pokud je na kartě ColdCardQ povolena funkce "Push Tx", můžete transakci vysílat přímo do sítě jednoduchým klepnutím na zadní stranu smartphonu.



![Co-Sign](assets/fr/52.webp)




Pokud nemáte aktivovanou funkci "Push tx", stiskněte tlačítko "QR" na kartě ColdCardQ, aby se podepsaná transakce zobrazila jako kód QR, a importujte ji do aplikace Nunchuk stejným způsobem jako v předchozím příkladu.



![Co-Sign](assets/fr/53.webp)



Tentokrát si všimneme, že byly použity 2 podpisy, takže transakce je připravena k vysílání v síti Bitcoin.



![Co-Sign](assets/fr/54.webp)




Dostali jsme se na konec tohoto návodu, který vám poskytne přehled o možnostech, které nabízí funkce Co-Sign integrovaná do zařízení ColdCardQ a Mk4 od společnosti Coinkite, a také o jejím využití prostřednictvím peněženek, jako jsou Sparrow a Nunchuk.