---
name: Zeus Embedded
description: Jak používat Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS je původně mobilní aplikace pro vzdálenou správu bleskových uzlů, která umožňuje ovládat uzel nainstalovaný na vzdáleném serveru


Aplikace však obsahuje také "vložený uzel".



**Právě tento aspekt aplikace budeme v tomto tutoriálu zkoumat.** Díky tomu může mít kdokoli svůj vlastní bleskový uzel v mobilu, aniž by potřeboval vyhrazený server, stejně jako ACINQ nabízí svůj neuvěřitelný blesk Wallet Phoenix.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Připomeňme, že Lightning je síť, která funguje paralelně s Bitcoin a umožňuje výměnu bitcoinů bez nutnosti systematicky provádět transakce On-Chain. Výsledkem jsou téměř okamžité transakce bez nutnosti čekat 10 minut na ověření bloku. To je užitečné zejména při placení u obchodníků ve fyzickém světě. Lightning navíc poskytuje pozoruhodnou úroveň **důvěrnosti**, kterou síť Bitcoin nativně nedisponuje*.



**Zeus "Integrated "** je určen pro uživatele Bitcoinů, kteří chtějí maximalizovat své soukromí a autonomii.


Stručně řečeno, je to **potenciálně** mobilní telefon Wallet snů cypherpunkerů. I když je stále v plenkách (alfa verze) a trpí několika chybami, jeho funkce jsou početné a není pochyb o tom, že potěší ty nejodvážnější z nás, kteří chtějí maximální kontrolu a volitelnost.



Na druhou stranu si nemyslím, že je v současné době vhodný pro začátečníky, kteří neznají Bitcoin a chtějí jednoduše odesílat/přijímat satoši. I když to se může v budoucnu změnit, protože se pro začátečníky implementuje funkce úschovy přes protokol Cashu (chaumian Ecash)...



## Instalace aplikace



Přejděte na [webové stránky projektu](https://zeusln.com/) a stáhněte si aplikaci pro operační systém svého chytrého telefonu:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Vytvoření portfolia



Po spuštění aplikace klikněte na tlačítko "Quick Start" a začněte vytvářet Wallet.



![image](assets/fr/03.webp)





Poté se zobrazí řada inicializačních obrazovek. Počkejte několik okamžiků a poté několik minut, dokud nebude uzel 100% synchronizován prostřednictvím Neutrina.



To může trvat několik minut. Pro informaci, neutrino je způsob, jakým mohou mobilní peněženky přistupovat k informacím Blockchain Bitcoin, aniž by bylo nutné spouštět Full node.



![image](assets/fr/04.webp)





Po několika okamžicích můžete vyrazit.



![image](assets/fr/05.webp)




## Nastavení aplikace



Připraven, no, ne tak docela, protože je samozřejmé, že uživatel Zeus hodný tohoto jména ovládá svůj Wallet s noblesou a stylem. Takže budeme muset změnit jeho avatar.



Klikněte na svůj avatar v pravém horním rohu obrazovky:



![image](assets/fr/06.webp)





Klikněte na ozubené kolečko a poté na plus "+" :



![image](assets/fr/07.webp)





Vyberte nejkrásnější fotografii Dia, která bude představovat tuto Wallet, a klikněte na "CHOOSE PICTURE" (vybrat obrázek) v dolní části obrazovky a poté se vraťte zpět kliknutím na šipku vpravo nahoře.



![image](assets/fr/08.webp)





Nakonec přidělíte svému zařízení Wallet přezdívku a kliknete na "SAVE Wallet CONFIG", aby se změna projevila. Nakonec se kliknutím na šipku zpět v levém horním rohu vraťte na domovskou obrazovku.



![image](assets/fr/09.webp)





Tentokrát se můžeme pustit do práce.



![image](assets/fr/10.webp)



### Biometrické údaje



Chcete-li chránit přístup ke službě Wallet, můžete přidat kód PIN/heslo a aktivovat biometrické údaje.



Chcete-li to provést, přejděte do hlavní nabídky Wallet kliknutím na vodorovné pomlčky vlevo nahoře.



![image](assets/fr/11.webp)





Vyberte "Nastavení", poté "Zabezpečení" a nakonec "Nastavit/změnit PIN".



![image](assets/fr/12.webp)





Vytvořte si PIN, potvrďte jej a aktivujte biometrické údaje stisknutím příslušného tlačítka "Biometrické údaje".  Pomocí šipky vlevo nahoře se vraťte do hlavní nabídky.



![image](assets/fr/13.webp)




### Uložit frázi Mnemonic



Jakmile se vrátíte do hlavní nabídky, klikněte na "Zálohovat Wallet" a přečtěte si varovný text, který vás informuje, že ztráta 24 slov, která se chystáte získat, se rovná ztrátě přístupu k vašim prostředkům a že kdokoli, kdo má tato slova kromě vás, může získat přístup k vašim prostředkům. Nikdy je nikomu nepředávejte.



V dolní části obrazovky vyberte možnost "I UNDERSTAND". Poté klikněte na každé z 24 slov, abyste je vyvolali, a pečlivě si je zapište.



Můžete ho napsat na papír nebo třeba pro větší bezpečnost vyrýt na nerezovou ocel, aby byl chráněn před požárem, povodní nebo zřícením. Volba média pro váš Mnemonic bude záviset na vaší bezpečnostní strategii, ale pokud používáte Zeus jako výdajové portfolio obsahující mírné částky, měl by papír stačit.



Pro více informací o správném způsobu ukládání a správy fráze Mnemonic vřele doporučuji tento další návod, zejména pokud jste začátečníci:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Po dokončení klikněte na "I'VE BACKUP MY 24 WORDS" v dolní části obrazovky a jsme zpět na domovské obrazovce, připraveni přijmout naše první bitcoiny.




## Možnost 1 - Příjem bitcoinů On-Chain a otevření kanálu Lightning



**Zeus Embedded** je primárně určen jako vestavěný bleskový uzel, ale lze jej použít i jako Wallet On-Chain.



Chcete-li obdržet bitcoiny On-Chain, klikněte na tlačítko "On-Chain" a poté na "Receive".


Nakonec naskenujte QR kód nebo zkopírujte Bitcoin Address a vložte peníze.



![image](assets/fr/15.webp)





Po potvrzení a připsání prostředků na účet Wallet je můžete použít k otevření **Světelného kanálu**. Váš kanál Lightning je vaší vstupní branou do Lightning Network, která vám umožní mnohem důvěrnější a rychlejší přístup k bitcoinům Exchange.





- Chcete-li tak učinit, klikněte na možnost "PŘESUNOUT FONDY On-Chain DO SVĚTLA"



Na další obrazovce budete vyzváni k otevření kanálu ve spolupráci s **"Olympus by Zeus "**, poskytovatelem služeb Lightning Service Provider, kterého upřednostňuje společnost Wallet.


V tomto výukovém programu zvolíme tuto možnost pro zjednodušení, ale je možné otevřít kanály s libovolným uzlem v síti.


V rámci jedné transakce je možné otevřít i několik kanálů výběrem možnosti "OTEVŘÍT DALŠÍ KANÁL". *Tomu se však budeme věnovat v "pokročilé" verzi výukového programu* **Zeus Embedded**.





- Poté vyberte částku, kterou chcete tomuto kanálu věnovat. V našem případě budou použity všechny naše prostředky On-Chain, proto aktivujeme tlačítko "Použít všechny možné prostředky".





- Nakonec vyberte tlačítko "OPEN CHANNEL" v dolní části obrazovky.



![image](assets/fr/16.webp)





Během několika sekund je kanál vytvořen a my můžeme provádět první transakce Lightning. Na domovské obrazovce vidíme vedle našeho zůstatku Wallet malé hodiny. To proto, že ještě budeme muset počkat na 3 potvrzení On-Chain, než bude kanál skutečně funkční.



![image](assets/fr/17.webp)





Po třech potvrzeních si všimneme, že náš zůstatek je nyní připsán na bleskovou vložku.



![image](assets/fr/18.webp)



Malý detail: když klikneme na nabídku v dolní části obrazovky, abychom si prohlédli stav našich bleskových kanálů, zjistíme, že malá část našeho zůstatku není k dispozici pro utrácení: můžeme utratit pouze 208253 satošů místo 210370, které máme ve skutečnosti. To je normální, protože je to specifické pro protokol blesku.



Na závěr je třeba poznamenat, že náš partner Olympus si vyhrazuje právo uzavřít kanál podle vlastního uvážení, pokud například nebude využíván. Abychom zajistili zachování našeho kanálu, budeme muset platit poskytovateli služeb LSP (Lightning Service Provider), jak uvidíme v dalším odstavci, prostřednictvím 2. způsobu otevření kanálu.





## Odesílání bitcoinů přes Lightning



Nyní, když jsme zprovoznili náš kanál, se podíváme, jak jej můžeme použít k zaplacení blesku Invoice (Invoice).



To provedete kliknutím na tlačítko "Lightning" a poté na "Send".



![image](assets/fr/19.webp)





Na další obrazovce zkopírujte svůj kód Invoice do vyhrazeného pole nebo jej naskenujte kliknutím na ikonu vpravo nahoře. Nakonec posuňte tlačítko "Slide to Pay" doprava a zaplaťte.



![image](assets/fr/20.webp)






Počkejte pár vteřin a Invoice je splacen a vaše satoši cestují rychlostí světla.



![image](assets/fr/21.webp)





Zeus vám pak umožní přidat bankovku, která bude platbu denominovat, nebo zobrazit trasu, kterou vaše satoši urazily, než dosáhly svého cíle (a poplatky účtované všemi mezilehlými uzly). Právě takové funkce se nám na Wallet líbí.



![image](assets/fr/22.webp)



Všimněte si, že na rozdíl od modelu Wallet, jako je [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), se u modelu Zeus trasa vypočítává lokálně a není delegována na třetí stranu (v případě modelu Phoenix na ACINQ). Příjemce platby tedy znáte pouze vy. Ztrácíme trochu efektivity (dokončení platby trvá o něco déle, ale získáváme hodně z hlediska soukromí).





Kliknutím na malou šipku v dolní části domovské obrazovky si také můžete prohlédnout historii plateb. Zde vidíme v položce Green 212 121 satošů Sats přijatých za On-Chain, dále červeně 211 756 satošů Sats použitých na otevření našeho kanálu, respektive 121 212 satošů použitých na zaplacení našeho blesku Invoice.



![image](assets/fr/23.webp)





## Možnost 2 - Příjem bitcoinů přímo na Lightningu



Namísto ručního otevření kanálu, jak jsme si právě ukázali, je možné přijímat prostředky přímo prostřednictvím služby Lightning, a to i bez již existujícího kanálu, pomocí služby Olympus, Zeus LSP.




- To provedete kliknutím na tlačítko "Lightning" na domovské obrazovce a poté na "Receive".
- Poté v poli "Částka" zvolte částku, kterou chcete obdržet, a v dolní části obrazovky vyberte tlačítko "VYTVOŘIT Invoice".



![image](assets/fr/24.webp)





Na další obrazovce se zobrazí částka Invoice, kterou je třeba zaplatit, abyste obdrželi satoši. Dozvídáme se, že LSP zadrží 10 000 Sats, pokud platbu provede Blesk. Později uvidíme, jak jsou tyto poplatky za otevření kanálu odůvodněné.



Zaplaťte částku Invoice nebo ji nechte zaplatit někoho jiného a kanál bude otevřen automaticky, ale s odečtením dohodnutých 10 000 Sats.



![image](assets/fr/25.webp)





Nyní jsme v čele 2 bleskových kanálů, jejichž stav lze zkontrolovat kliknutím na tlačítko označené bílou šipkou v dolní části domovské obrazovky.



Vidíme, že na rozdíl od kanálu otevřeného z naší stupnice On-Chain se u kanálu otevřeného přímo pomocí blesku nezobrazuje žádné varování.


Protože jste za zřízení tohoto kanálu zaplatili, poskytovatel bleskových služeb (LSP) se zavazuje udržovat kanál po dobu 3 měsíců a nabízí vám "příchozí likviditu". Na spodním kanálu vidíte, že kapacita příjmu je 96383 satošů. LSP tedy vázal kapitál, aby vám umožnil přijímat platby přímo po otevření kanálu.



Zaplacené poplatky ve výši 10 000 Satoshi tedy pokrývají: náklady na otevření kanálu (transakce Bitcoin On-Chain, záruku na údržbu kanálu po dobu 3 měsíců a zablokování kapitálu).



![image](assets/fr/26.webp)





Gratulujeme, nyní jste připraveni používat Zeus Embedded, mobilní osvětlovací systém Wallet s nejpokročilejšími funkcemi na trhu.





Chcete-li se dozvědět více o technické obsluze Lightning Network, najdete vynikající bezplatné školení Plan ₿ Academy od Fanise Michalakise:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb