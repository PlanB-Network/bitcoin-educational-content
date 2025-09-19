---
name: COLDCARD Q - Key Teleport
description: Co je Key Teleport a jak ho používat?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Jakou funkci **Key Teleport** nabízí společnost Coinkite u svého vlajkového zařízení ColdCardQ?



**Teleport klíčů** umožňuje bezpečně přenášet důvěrná data mezi 2 kartami ColdCardQ. Přenosový kanál nemusí být ani šifrovaný a může být veřejný.



To lze použít k přenosu:





- **gW-0 fráze** (Master seed karty ColdCard Q nebo tajemství uložená v trezoru [seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **důvěrné poznámky a hesla**: může to být libovolné tajemství nebo celý adresář [Secure Notes & Passwords] (https://coldcard.com/docs/secure_notes/) na kartě ColdCardQ.
- zálohu celé karty **ColdCardQ**: aby tato záloha fungovala, nesmí mít karta ColdCardQ, která ji přijímá, Master seed.
- gW-3 (**částečně podepsané transakce Bitcoin**) jako součást schématu s více podpisy.



To vyžaduje, abyste aktualizovali [firmware zařízení na verzi v1.3.2Q](https://coldcard.com/docs/upgrade/) nebo vyšší.



## Jak používat teleportování klíčů?



### 1- Přenos jakéhokoli typu dat



Zde se podíváme na přenos vět seed, poznámek, hesel nebo celého přenosu zálohy ColdCardQ. Případem přenosů PSBT pro transakce s více podpisy se budeme zabývat později.



#### Připravte zařízení na příjem tajemství



V nabídce **"Rozšířené / Nástroje**" na kartě ColdCardQ vyberte možnost **"Teleportování pomocí kláves (spuštění) "**.


Na další obrazovce je navrženo osmimístné heslo, zde "20420219". Toto heslo je třeba sdělit odesílateli. K odeslání tohoto hesla použijte například sms zprávu nebo oblíbený systém zabezpečených zpráv, případně i hlasový hovor.



Poté klikněte na tlačítko **"Enter**" na kartě ColdCardQ a přejděte k dalšímu kroku.




![CCQ-key-teleport](assets/fr/01.webp)




Na obrazovce se vygeneruje kód QR. Tento QR kód je opět třeba sdělit "odesílateli" ColdCardQ. Nejjednodušší způsob, jak to provést, je prostřednictvím videohovoru.



**NEODESÍLEJTE TENTO KÓD QR STEJNÝM PŘENOSOVÝM KANÁLEM, KTERÝM BYLO ODESLÁNO PŘEDCHOZÍ OSMIMÍSTNÉ HESLO**.



![CCQ-key-teleport](assets/fr/02.webp)



*Pro ty z vás, které to zajímá, se pokusíme pochopit základní mechanismus, který umožňuje přenášet tajemství nezabezpečenými kanály*



*Ve skutečnosti zde iniciujeme přenos tajemství pomocí Diffie-Hellmanovy metody, kterou se zabývá kurz BTC204, který jsem přiložil níže*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*V současné době máme:*




- vygeneroval pár efemérních klíčů (veřejný/soukromý Ka a ka, přičemž Ka=G.ka, G je bod generátoru ECDH) a osmimístné heslo.
- použil toto heslo k zašifrování veřejného klíče (Ka) pomocí AES-256-CTR a poté toto heslo přenesl komunikačním kanálem A do "odesílající" karty ColdCardQ.
- nakonec jsme odesílateli předali zašifrovaný paket prostřednictvím výše uvedeného QR kódu, přičemž jsme použili druhý komunikační kanál B odlišný od prvního.



#### Připravte zařízení, které bude odesílat tajemství



Na odesílajícím zařízení klikněte na tlačítko **"QR "** a naskenujte kód QR zaslaný přijímajícím zařízením, poté zadejte 8místné heslo, které vám bylo sděleno v předchozím kroku prostřednictvím samostatného kanálu. Nyní jsme připraveni zahájit odesílání dat z "odesílajícího" zařízení.



**Prosím, nezadávejte 8místné heslo nesprávně, protože se nezobrazí žádné chybové hlášení a proces bude pokračovat. Závěrečný přenos dat však selže a budete muset začít znovu**.



![CCQ-key-teleport](assets/fr/03.webp)



*Pro ty zvídavější z vás se ještě jednou podíváme, co máme za lubem v oblasti kryptografie a přenosu tajemství:*




- jsme importovali zašifrovaná data naskenováním kódu QR na přijímacím zařízení.
- pak jsme je dešifrovali pomocí osmimístného hesla, které nám bylo předáno sekundárním kanálem.
- máme tedy k dispozici veřejný klíč (Ka), který původně vygeneroval příjemce.
- Poté na odesílajícím zařízení vytvoříme nový pár efemérních klíčů (Kb/kb, přičemž Kb=G.kb), který použijeme k aplikaci ECDH na Ka. Provedeme tedy operaci kb.Ka=Ks , kde Ks se nazývá **"klíč relace"**.




Nyní budete vyzváni k výběru povahy tajemství, která mají být přenášena mezi dvěma kartami ColdCardQ (důvěrné poznámky, heslo, úplná záloha, semena obsažená v trezoru, hlavní zařízení seed).



![CCQ-key-teleport](assets/fr/04.webp)



Zde bude naším tajemstvím krátká zpráva výběrem možnosti **"Rychlá textová zpráva "**. Napište zprávu (pro nás "PlanB Network rocks") a stiskněte **"ENTER "**.


Zařízení poté vygeneruje nové náhodné heslo nazvané **"Heslo pro teleport "** , v příkladu "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Stiskněte **"ENTER "** a zobrazí se nový QR kód. Nechte jej naskenovat přijímacím zařízením. A na jiném komunikačním kanálu předejte **"Heslo pro teleport "** příjemci.



![CCQ-key-teleport](assets/fr/06.webp)



*Pro zvědavce uvádíme, že v této fázi:*




- po výběru tajemství, která mají být přenášena, vytvoříme nové náhodné heslo s názvem **"Teleportační heslo"**.
- poté zašifrujeme tajemství pomocí AES-256-CTR s použitím **"klíče relace"**, "Ks", vygenerovaného v předchozím kroku
- paket již zašifrovaný pomocí **"Klíče relace "** předřadíme našemu veřejnému klíči Kb a poté přidáme další šifrování Layer AES-256-CTR pomocí **"Hesla teleportu "**. Celá věc je pak zakódována jako kód QR




#### Dokončení přenosu tajemství do přijímacího zařízení



Stisknutím tlačítka **"QR "** naskenujete kód QR, který odesílající zařízení zobrazí prostřednictvím kanálu visio. Budete vyzváni k zadání **"Hesla teleportu "** pro nás "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Data jsou poté dešifrována a srozumitelná přijímacímu zařízení. Přijatá zpráva je skutečně "PlanB Network rocks". To je vše.



![CCQ-key-teleport](assets/fr/08.webp)



*Co se vlastně stalo během této poslední fáze :*?




- dešifrovali jsme data přenášená odesílatelem pomocí **"Teleportačního hesla"**.
- máme tedy veřejný klíč Kb a naši tajnou zprávu zašifrovanou pomocí **"klíče relace "**, "Ks". Jak to ale můžeme udělat, když jako příjemce neznáme Ks, který vytvořil odesílatel?
- Na veřejný klíč Kb.* musíme použít náš soukromý klíč "ka" z úvodního kroku **"Připravte zařízení, které bude přijímat data "**
- Výpočtem ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks zjistíme Ks. Který se nakonec použije k rozluštění tajné zprávy.



### 2 - Převod PSBT do Multisig (pokročilý)



Předpokládá to, že vaše karta Wallet Multisig již byla vytvořena a že vaše zařízení ColdCardQ již bylo přednastaveno tak, aby bylo schopno provádět transakce s více podpisy. Pokud tomu tak není, vysvětlení je k dispozici [zde](https://coldcard.com/docs/Multisig/) na webových stránkách Coinkite.



Krátké připomenutí toho, co je vícepodpisová karta Wallet (Multisig).



K utracení prostředků Wallet je obvykle zapotřebí pouze jeden soukromý klíč k odemčení UTXO přidružených k vašim adresám.


V případě Wallet Multisig může být k utracení prostředků zapotřebí až 15 soukromých klíčů, a tedy 15 podpisů. To je známé jako portfolio "M z N", přičemž N se pohybuje mezi 1 a 15 a M je počet podpisů potřebných k tomu, aby bylo možné prostředky utratit. Například u fondu Wallet Multisig 3 z 5 budou zapotřebí nejméně 3 podpisy z 5 možných.



Úkolem je pak koordinace mezi signatáři, aby postupně podepsali "PSBT" pro "Partially Signed Bitcoin Transaction". V této souvislosti lze k přenosu "PSBT" mezi spolupodepisujícími jednoduchým a důvěrným způsobem použít "**Key Teleport**". K tomu postačí jednoduchý videohovor mezi spolupodepisujícími osobami.



Tady je návod, jak se to dělá na Multisig 3 ze 4.



**Podepisující osoba 1:**



Signatář 1 dováží a podepisuje PSBT. Nakonec klikne na **"T "** a použije **"Klíčový teleport "** pro přenos PSBT signatáři 2.



![CCQ-key-teleport](assets/fr/09.webp)




Po výběru signatáře 2 kliknutím na **"ENTER "** se zobrazí "HESLO TELEPORTU" (zde JJ YC AB 6A), které je třeba signatáři 2 předat jiným komunikačním kanálem. Například SMS nebo hlasový hovor, ale **ne** videohovor.



Znovu stiskněte **"ENTER "** a zobrazí se QR kód představující PSBT podepsaný 1 a následně zašifrovaný "TELEPORT PASSWORD".



![CCQ-key-teleport](assets/fr/10.webp)



**Podepisující osoba 2:**



Signatář 2 naskenuje QR kód, který mu předloží signatář 1. Poté zadá "TELEPORT PASSWORD" přenášený sekundárním komunikačním kanálem, aby dešifroval přenášená data.



Signatář 2 transakci podepíše a poté klikne na **"T "**, aby předal PSBT signatáři 3 prostřednictvím "Key Teleport".


Je zřejmé, že již byly použity 2 podpisy. K platnosti transakce chybí už jen podpis třetího signatáře. Kliknutím na **"ENTER "** vyberte signatáře 3.



![CCQ-key-teleport](assets/fr/11.webp)



A vytvoří se nové "HESLO TELEPORTU", po němž následuje opět kód QR, který kóduje kód PSBT podepsaný čísly 1 a 2 a poté zašifrovaný tímto novým "HESLEM TELEPORTU" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Signatář 3:**



Opakujte stejný krok jako výše.


Signatář 3 naskenuje QR kód, který mu předloží signatář 2. Poté zadá "HESLO TELEPORTU" přenášené sekundárním komunikačním kanálem.



Podepsaná osoba 3 transakci podepíše, a protože tentokrát byly použity 3 ze 4 podpisů, je transakce označena jako dokončená a je připravena k distribuci prostřednictvím různých médií (SD karta, NFC, QR atd.).



![CCQ-key-teleport](assets/fr/13.webp)



Pokud je na kartě ColdCardQ aktivována funkce "Push Tx", jednoduše přiložte kartu ColdCardQ k zadní straně jakéhokoli zařízení připojeného k internetu pomocí technologie NFC (chytrý telefon/tablet), aby se transakce vysílala prostřednictvím sítě Bitcoin.



![CCQ-key-teleport](assets/fr/14.webp)



*Pro přenosy PSBT od jednoho signatáře k druhému se v každé fázi jednoduše používá "teleportace klíče" pomocí "teleportačního hesla", které zašifruje PSBT při přenosu od jednoho signatáře k druhému. Protože přenášená data nemohou být použita k odcizení finančních prostředků, není třeba používat Diffie-Hellmanovu šifru, jako je tomu v případě posílání vysoce důvěrných tajemství (seed, heslo atd...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Zdroj: [Oficiální stránky ColdCard](https://coldcard.com/)*