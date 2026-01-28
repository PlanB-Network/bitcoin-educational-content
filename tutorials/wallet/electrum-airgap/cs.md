---
name: Electrum Airgap
description: První krok k bezpečnosti, cold wallet s Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



V tomto návodu vám vysvětlím, jak vytvořit své první zařízení pro podepisování airgap, odpojené od internetu, i když nemáte k dispozici vyhrazený Hardware Wallet. Stačí mít k dispozici dva počítače:




- starého zařízení, kterému bude navždy znemožněno připojení k internetu;
- váš počítač pro každodenní použití.



Tato konfigurace umožňuje vyšší stupeň zabezpečení než klasická konfigurace `Hot Wallet`: starý počítač - bez připojení k síti - je správcem vašich soukromých klíčů, které nejsou nikdy vystaveny na internetu, ale jsou uloženy offline ("airgap" nebo "Cold").



Místo toho si nainstalujete displej Wallet ("watch-only") na svůj denní počítač, který je připojen k síti a pomocí kterého můžete například kontrolovat zůstatky a připravovat transakce na účtenkách.



## Wallet Airgap: Co a jak



Provedením kroků uvedených v této příručce nainstalujeme dva Electrum Software Wallet na dva různé počítače a nakonec vytvoříme dvě peněženky s různými úložišti klíčů: Wallet airgap bude používat celou hierarchii Wallet HD, zatímco Wallet display bude vytvořen s hlavním veřejným klíčem.



Tyto dvě peněženky se od sebe budou ve všech ohledech velmi lišit. Jediné, co budou mít společné, jak uvidíme, jsou adresy:




- gW-13 na počítači airgap se může pouze podepsat, ale po odpojení od sítě nezná rovnováhu a použité adresy;
- gW-12 na denním počítači bude moci pouze připravovat a propagovat transakce, aniž by mohl nakládat s výdaji, protože nemá soukromé klíče.



## Předběžná příprava



Chcete-li si stáhnout Electrum, doporučuji postupovat podle prvních kroků v tomto návodu:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Po stažení vždy před instalací ověřte verzi a poté přejděte ke konfiguraci "One Server", jak najdete v nápovědě v části `Začněte s atrapou Wallet`.



Operace konfigurace "Jeden server" je nutná pouze pro Wallet nainstalovaný v denním počítači, protože druhý počítač bude vždy offline.



Následující operace zahrnují cvičení na dvou různých počítačích (a peněženkách), takže jsem se pro pohodlí a soustředění rozhodl nastavit airgap Wallet se světlým motivem, zatímco displej Wallet má tmavý motiv.



## Wallet Vytvoření vzduchové mezery



Po stažení a ověření stažení programu Electrum si pořiďte kopii spustitelného souboru a přeneste ji do počítače v režimu offline. Poté jej spusťte a nainstalujte Electrum.



Dvojklikem spustíte Electrum: počítač, na kterém budete tento Wallet používat, je offline, ignorujte nastavení sítě a přejděte k vytvoření Wallet, kterému v tomto návodu budeme říkat `airgap`.



![image](assets/en/01.webp)



Vyberte možnost _Standardní peněženka_.



![image](assets/en/02.webp)



A poté vyberte možnost _Create a new seed_ (Vytvořit nové osivo), aby software generate spustil osivo Mnemonic.



![image](assets/en/03.webp)



Přesně přepište 12 slov generate ze systému Electrum na papírovou podložku a pokračujte v kroku ověření, přičemž slova znovu zadejte v pořadí, v jakém si je systém Electrum vyžádá.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Po dokončení vytvoření souboru Wallet nastavte složité heslo (`Strong`) pro zašifrování souboru Wallet v zařízení airgap. Tento krok je velmi choulostivý a důležitý, protože nyní zvolené heslo zabraňuje přístupu k zařízení Wallet, které má dispoziční pravomoc, a může tak utrácet finanční prostředky podepisovat transakce.



![image](assets/en/06.webp)



Kliknutím na tlačítko _Finish_ se definuje Wallet a zobrazí se na obrazovce. Indikátor síťového připojení, tj. barevná tečka v pravém dolním rohu, je samozřejmě červený, protože počítač je odpojen a neumožňuje Wallet vystavit online klávesy.



![image](assets/en/07.webp)



## Vytvoření Wallet vizualizace



Nyní, když má váš Wallet offline soukromé klíče, je třeba nastavit displej Wallet nebo `pouze hlídání`, který vám umožní zobrazit zůstatek a také připravit příjmové transakce, abyste mohli bezpečně pokračovat v akumulaci Sats.



V aplikaci Wallet umístěné v offline zařízení zvolte nabídku _Peněženka_ -> _Informace_



![image](assets/en/08.webp)



Zobrazí se okno se všemi informacemi o Wallet, kde můžete zaškrtnout `derivační cestu` a `otisk hlavního prstu`, například je označit vedle slov ve větě Mnemonic (důrazně doporučujeme).



![image](assets/en/09.webp)



Nezapomeňte, že tato data získáváte z nepřipojeného počítače, takže budete muset zkopírovat/vložit `zpub` do textového souboru a uložit jej na USB disk.



Nyní se můžete přesunout k počítači připojenému k internetu, spustit Electrum a vytvořit novou službu Wallet.



V nabídce _File_ vyberte možnost _New/Restore_.



![image](assets/en/10.webp)



Nová verze Wallet je určena pouze k prohlížení, takže ji v tomto návodu budeme nazývat `pouze k prohlížení`.



![image](assets/en/12.webp)



Na další obrazovce vyberte možnost _Standardní peněženka_ a pokračujte kliknutím na tlačítko _Další_.



![image](assets/en/13.webp)



Při volbě `Skladiště klíčů` buďte opatrní: pro vytvoření zobrazení Wallet vyberte možnost _Použít hlavní klíč_. Poté pokračujte příkazem _Další_.



![image](assets/en/14.webp)



Vložte sem soubor `zpub` zkopírovaný z Wallet offline, který jste přenesli do tohoto počítače prostřednictvím média USB.



![image](assets/en/15.webp)



Na závěr nastavte silné heslo i pro tento kód Wallet, případně jiné než pro odpovídající kód Cold.



Na displeji se zobrazí Wallet s varováním. Toto hlášení vás upozorní, že se jedná pouze o displej Wallet a že s ním nemůžete utratit související finanční prostředky.



**Poznámka Dobře**: **Proto budete muset vždy vlastnit soukromé klíče, abyste mohli disponovat UTXO tohoto Wallet**. S dobrým zálohovacím systémem pro vás nebude obtížné zůstat v plném vlastnictví svých bitcoinů.



![image](assets/en/16.webp)



Toto upozornění se zobrazí při každém otevření tohoto programu Wallet. Klikněte na tlačítko _Ok_ a přejděte k ověřovacímu kroku.



## Ověření dvou Wallet



Jak jsme se dozvěděli na začátku této příručky, airgap Wallet a jeho displej Wallet jsou dvě portfolia, která mají různé funkce, ale **sdílejí stejné adresy**.



Pokud se podíváme na obě peněženky vedle sebe, vizuálně si všimneme, že ve vzduchové mezeře Wallet je symbol "seed", zatímco v hodinkách pouze pro hodinky není. I tento detail vám pomůže zapamatovat si, že displej Wallet Wallet nemá soukromé klíče.



![image](assets/en/17.webp)



Chcete-li však provést přesnou první kontrolu, vyberte v obou peněženkách nabídku `Adresy`: protože mají stejné adresy, měl by být seznam adres pro obě peněženky stejný.



![image](assets/en/18.webp)



⚠️ **POZOR**: **neexistuje žádná střední cesta, adresy musí být stejné. V případě, že se liší, je nutné smazat veškerou dosavadní práci a začít znovu**.



Nyní můžete provést dvě různé kontroly. Nejprve zkuste obě peněženky odstranit a obnovit je od začátku, každou v příslušném počítači. V případě, že přistoupíte k tomuto ověření, jsou postupy pro zobrazení Wallet totožné s výše uvedenými.



V případě vzduchové mezery Wallet však budete muset na obrazovce `skladiště` zvolit možnost _Již mám osivo_ a zadat slova zkopírováním z papírové zálohy.



Po skončení zkušebního období "bez zatížení" můžete zkusit provést transakci s malou částkou a okamžitě ji utratit.



## Přijímání a utrácení transakcí



Chcete-li začít používat airgap Electrum, můžete provést transakci s účtenkou s malou částkou a poté ji utratit za vlastní Address. Poté se můžete seznámit s postupem a ověřit si, že máte finanční prostředky plně pod kontrolou.



**Poznámka**: Nedoporučuji, abyste na Wallet vkládali velké množství finančních prostředků, dokud si nebudete jisti, že můžete všechny operace provádět bez problémů.



Níže popsané kroky se mohou na první pohled zdát složité. Nenechte se tím však vyvést z míry: až je poprvé vyzkoušíte, zjistíte, že jejich provedení zabere jen několik minut.



Pro příjem finančních prostředků musíte nutně použít displej Wallet umístěný v počítači připojeném k internetu. V nabídce `Přijmout` klikněte na `Vytvořit žádost_, aby Electrum generate první dostupný Address a pomocí něj nám poslal několik sátů.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Jakmile se transakce rozšíří, můžete si již všimnout, že - jak je přirozené - je viditelná pouze na displeji Wallet a nikoli na vzduchové mezeře Wallet.



![image](assets/en/21.webp)



Poté, co vaše transakce obdrží určité potvrzení, můžete připravit výdaj a vyzkoušet si tak postup podepisování od společnosti Wallet mimo síť. Poté připravte transakci pouze na hodinkách a stisknutím tlačítka _Preview_ ji zkontrolujte



![image](assets/en/22.webp)



Zobrazí se okno pokročilých transakcí, ve kterém je to vidět:




- transakce není podepsaná (`Status: Unsigned);
- příkazy `Sign` a `Broadcast` jsou blokovány.



Jediné, co můžete udělat, je exportovat transakci tak, jak je, přenést ji do airgapu Wallet a podepsat ji.



Vložte do počítače jednotku USB flash a v nabídce vlevo dole vyberte možnost _Sdílet_.



![image](assets/en/23.webp)



Poté vyberte možnost _Uložit do souboru_.



![image](assets/en/24.webp)



Uložení transakce na paměťovou kartu USB.



Všimněte si, že Electrum dává souboru název s prvními číslicemi transaction ID a příponou souboru je `.PSBT`, což znamená `Partially Signed Bitcoin Transaction`.



Rozbalte médium se souborem `.PSBT` a připojte jej k počítači v režimu offline.



V okně Wallet airgap nyní zvolte nabídku _Tools_, poté _Load transaction_ a následující From file_.



![image](assets/en/25.webp)



Ve správci souborů vyberte z jeho umístění soubor `.PSBT`.



![image](assets/en/29.webp)



Software počítače mimo síť automaticky otevře okno pokročilé transakce, které je zcela identické s oknem na displeji Wallet. Stav je `Nepodepsáno`, ale rozdíl je v tom, že příkaz `Podepsat` je zde aktivní. A právě ten budete muset provést.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Nyní, když je transakce podepsána, nezapomeňte, že váš počítač Wallet je v režimu offline. Proto - i když vidíte aktivní příkaz `Broadcast` - váš Wallet nebude schopen šířit transakci do sítě Bitcoin.



Nyní je třeba zopakovat operaci exportu podepsané transakce na USB flash disk, abyste ji mohli importovat do počítače připojeného k internetu a propagovat ji.



V levém dolním menu opět vyberte možnost _Sdílet_ a poté možnost _Uložit do souboru_.



![image](assets/en/28.webp)



Nyní má soubor jinou příponu: **PSBT` má nyní transakce příponu `.txn`. Od této chvíle vám Electrum umožní rozpoznat podepsané transakce od nepodepsaných**.



![image](assets/en/30.webp)



Pro finální propagaci transakce vyjměte USB flash disk z off-line počítače a vložte jej do počítače připojeného k internetu.



V okně pouze pro sledování zopakujte postup importu, tj. v nabídce _Nástroje_ vyberte _Načíst transakci_ a nakonec _Ze souboru_.



![image](assets/en/31.webp)



Electrum vám otevře okno transakce, které se výrazně liší od okna zobrazeného dříve na tomto webu Wallet. Nyní je transakce podepsaná (`Status: Signed`) a příkaz `Broadcast` je přístupný.



Poslední operace, kterou je třeba provést, je právě tato:



![image](assets/en/32.webp)



## Závěry



Vaše testy jsou nyní dokončeny. Pokud jste postupovali podle návodu a dosáhli stejných výsledků, vytvořili jste pomocí Electrumu na dvou různých počítačích Wallet Cold, které můžete použít v režimu airgap k ukládání bitcoinů.



Jediné věci, kterým musíte věnovat zvýšenou pozornost, jsou dvě:


1) **nikdy nepoužívejte vzduchovou mezeru Wallet k přijímacím adresám generate**. Protože je offline, vždy vám nabídne první Address, který se shoduje s tím, který jste právě použili k provedení testovací transakce;



![image](assets/en/33.webp)



_Jak je vidět na obrázku výše, offline Wallet nezná svou vlastní historii Address. V tomto ohledu je zcela slepý. **Jediným úkolem, který pro vás může udělat, je ukládat vaše offline klíče a podepisovat vaše transakce**_.



2) Použijte USB flash disk určený pouze pro tento účel, **nepoužívejte médium, které používáte často**. U každodenních nástrojů je větší pravděpodobnost kybernetického útoku a neúmyslně můžete napadnout i počítač, který máte odpojený od sítě. Paměť USB, kterou používáte pouze k tomuto účelu, má velmi málo příležitostí navázat kontakt s vaším počítačem online, zejména pokud jste hodler, který nemusí utrácet, čímž se snižuje pravděpodobnost přijetí a následného přenosu virů, malwaru apod.