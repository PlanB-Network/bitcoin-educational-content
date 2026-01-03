---
name: SMS4Sats
description: Přijímejte a odesílejte SMS anonymně platbou v Bitcoin Lightning
---

![cover](assets/cover.webp)



Ověřování pomocí SMS se stalo nezbytnou součástí mnoha online služeb. Ať už jde o vytvoření účtu na platformě, ověření registrace nebo potvrzení totožnosti, webové stránky téměř systematicky vyžadují telefonní číslo. Tato rozšířená praxe představuje velký problém pro každého, kdo si chce zachovat soukromí: vaše osobní číslo se stává trvalým identifikátorem, který spojuje vaše různé digitální aktivity s vaší skutečnou identitou a otevírá dveře nežádoucím komerčním nabídkám.



**SMS4Sats** na tento problém reaguje nabídkou dočasných telefonních čísel pro příjem a odesílání SMS zpráv. Služba se vyznačuje modelem bez registrace a exkluzivní platbou Bitcoin prostřednictvím Lightning Network. Za několik satošů získáte jednorázové číslo, které vám umožní potvrdit registraci, aniž byste kdy odhalili své osobní číslo.



Tento návod vás provede třemi funkcemi SMS4Sats: přijímání ověřovacích SMS, odesílání anonymních SMS a pronájem dočasného čísla na několik hodin.



## Co je SMS4Sats?



SMS4Sats je online služba dostupná na adrese [sms4sats.com](https://sms4sats.com), která umožňuje anonymní správu SMS prostřednictvím platby v Bitcoin Lightning. Služba nabízí tři různé funkce: příjem jednorázových ověřovacích kódů, odesílání SMS na libovolné číslo a pronájem dočasných čísel na několik hodin.



### Filozofie a provozní model



Projekt je navržen tak, aby byla zajištěna maximální důvěrnost a finanční suverenita. Tím, že SMS4Sats nevyžaduje založení účtu a přijímá pouze platby Bitcoin Lightning, zcela eliminuje nutnost poskytovat osobní údaje. Není vyžadována žádná e-mailová adresa, žádná kreditní karta, žádné osobní údaje. Pro přístup ke službám je vyžadována pouze platba Lightning.



Služba podporuje více než 400 webů a aplikací v přibližně 120 zemích a pokrývá většinu běžných ověřovacích potřeb. Toto rozsáhlé geografické pokrytí umožňuje ověřování registrací na různých platformách, od sociálních sítí po služby zasílání zpráv.



### Model podmíněné platby



SMS4Sats používá pro svou funkci příjmu SMS podmíněné faktury Lightning (hodl faktury). Tento mechanismus zajišťuje, že vám bude účtována pouze tehdy, pokud je SMS skutečně přijata. Pokud do stanovené doby (maximálně 20 minut) žádná zpráva nedorazí, platba se automaticky zruší a satoši se vrátí na váš účet wallet. Tato záruka se nevztahuje na funkce odesílání a pronájmu, které jsou nevratné.



## Tři funkce SMS4Sats



Rozhraní SMS4Sats je uspořádáno do tří záložek, které odpovídají třem různým způsobům použití: **RECEIVE** pro příjem ověřovacích kódů, **SEND** pro odesílání anonymních SMS a **RENT** pro pronájem dočasného čísla.



### Přijmout SMS



Hlavní funkce umožňuje získat dočasné číslo pro získání jedinečného ověřovacího kódu. Po obdržení a použití kódu je číslo trvale deaktivováno.



### Odeslání SMS



Tato funkce umožňuje odeslat SMS na libovolné telefonní číslo, aniž byste odhalili svou totožnost. Příjemce obdrží zprávu z anonymního čísla.



### Pronájem představení



Pro uživatele, kteří potřebují přijímat více SMS zpráv na jednom čísle, nabízí SMS4Sats možnost dočasného pronájmu. Tato možnost umožňuje přijímat a odesílat několik zpráv během doby pronájmu.



**Poznámka k cenám** : Ceny uvedené v tomto návodu jsou orientační. Liší se podle země čísla, cílové služby a aktuální poptávky. Například SMS na číslo Telegram Francie může stát v závislosti na podmínkách 1 500 až 5 000 satošů. Před zaplacením si vždy ověřte přesnou částku na faktuře Blesku.



## Přijmout ověřovací SMS



Podívejme se podrobněji na to, jak pomocí SMS4Sats získat ověřovací kód, na příkladu vytvoření účtu Telegram.



### Krok 1: Výběr země a služby



Přejděte na stránku [sms4sats.com](https://sms4sats.com) a zůstaňte na kartě **RECEIVE**. V rozbalovací nabídce vyberte zemi požadovaného čísla. Pokud je v seznamu uvedena cílová služba vašeho předplatného, vyberte ji, abyste optimalizovali šance na příjem.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



V tomto příkladu vybereme jako zemi Francii a jako cílovou službu Telegram. Kliknutím na tlačítko **NEXT** přejdete k dalšímu kroku.



### Krok 2: Zaplaťte fakturu Lightning



Blesková faktura se zobrazí ve formě kódu QR. Částka se liší podle země a zvolené služby. Naskenujte kód QR pomocí zařízení Lightning wallet nebo si fakturu zkopírujte a zaplaťte ji ručně.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Všimněte si důležitého sdělení: "Žádný SMS kód = žádná platba". Pokud neobdržíte SMS, bude vaše platba automaticky zrušena a vrácena nejpozději do 20 minut.



### Krok 3: Získání dočasného čísla



Po potvrzení platby se okamžitě zobrazí dočasné telefonní číslo. Počítadlo ukazuje čas zbývající do přijetí SMS.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Zkopírujte si toto číslo (zde +33 7 74 70 09 66) a použijte ho u služby, kterou chcete zaregistrovat.



### Krok 4: Použití čísla v cílové službě



Dočasné číslo zadejte v aplikaci nebo na webové stránce, kde si vytváříte účet. V našem příkladu Telegram zadejte číslo, potvrďte jej a počkejte na ověřovací kód.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Postup je stejný jako při běžné registraci: zadáte číslo, společnost Telegram zašle ověřovací kód prostřednictvím SMS a poté dokončíte vytvoření účtu.



### Krok 5: Získání ověřovacího kódu



Návrat do rozhraní SMS4Sats. Jakmile je SMS přijata, automaticky se zobrazí aktivační kód. Klikněte na **KOPÍROVAT KÓD** a snadno si jej zkopírujte.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Zadáním tohoto kódu v cílové službě registraci dokončíte. Dočasné číslo je poté trvale deaktivováno.



## Odeslání anonymní SMS



SMS4Sats vám také umožňuje posílat SMS zprávy na libovolné číslo bez odhalení vaší identity.



### Krok 1: Napsání zprávy



Klikněte na kartu **Odeslat**. Zadejte cílové telefonní číslo s mezinárodní předvolbou a napište zprávu (maximálně 1600 znaků).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Kliknutím na tlačítko **NEXT** přejdete k platbě.



### Krok 2: Zaplaťte a odešlete



Zaplaťte zobrazenou fakturu Lightning. Po potvrzení platby je SMS okamžitě odeslána příjemci.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Zobrazí se potvrzovací kód, který potvrdí, že zpráva byla odeslána. Příjemce obdrží SMS z anonymního čísla.



## Pronájem dočasného čísla



Pro použití, které vyžaduje několik zpráv SMS na stejném čísle, umožňuje funkce RENT pronajmout si číslo na několik hodin.



### Konfigurace pronájmu



Klikněte na kartu **RENT**. Vyberte zemi a dobu trvání.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Důležité body, které je třeba vzít na vědomí:**




- Ceny se liší podle země a délky pobytu
- Na rozdíl od jednorázových SMS zpráv jsou pronájmy nevratné**
- Pronajatá čísla obecně nefungují s Telegram
- Tato možnost je vhodná pro předplatné několika služeb za sebou



Po kliknutí na tlačítko **NEXT** a zaplacení faktury Lightning získáte číslo, které můžete po dobu pronájmu používat k přijímání a odesílání zpráv SMS.



## Výhody a omezení



### Nejdůležitější informace



**Nevyžaduje se zadávání osobních údajů**: Model bez registrace zaručuje, že nejsou shromažďovány žádné osobní údaje.



**Tři další funkce**: Přijímání, odesílání a pronájem pokrývají většinu potřeb.



**Platba pouze v Bitcoin** : Lightning Network umožňuje okamžité a pseudonymní transakce.



**Automatická úhrada**: Systém faktur hodl zaručuje, že při příjmu SMS zpráv zaplatíte pouze v případě, že SMS dorazí.



### Omezení, která je třeba zvážit



**Relativní zabezpečení kanálu SMS**: SMS kódy nejsou spolehlivou metodou ověřování a neměly by se používat pro citlivé účty.



**Kompatibilita proměnných**: Mnoho webů virtuální čísla detekuje a blokuje. Může být nutné provést několik pokusů.



**Nepoužitelná čísla**: Po jednorázovém použití se číslo recykluje a nelze jej obnovit.



**Nezávratné pronájmy**: Na rozdíl od jednorázových SMS zpráv se na pronájem nevztahuje záruka vrácení peněz.



## Osvědčené postupy



### Používání Toru pro větší soukromí



SMS4Sats je přístupný přes [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Tato konfigurace maskuje vaši IP adresu při přístupu ke službě.



### Vyhněte se kritickým účtům



Pro důležité účty (banka, hlavní e-mail) nikdy nepoužívejte jednorázové číslo. Pokud tyto platformy vyžadují, abyste číslo později znovu ověřili, ztratíte k účtu přístup.



### Oddělte své digitální identity



V případě pseudonymních účtů kombinujte dočasné číslo s jednorázovou e-mailovou adresou a prohlížečem, který nepoužíváte obvykle.



### Výběr robustního systému 2FA



Po vytvoření účtu aktivujte silnější řešení ověřování: (Aegis, Ente Auth) nebo fyzický bezpečnostní klíč FIDO2.



## Závěr



SMS4Sats je kompletní řešení pro správu důvěrných SMS. Ať už chcete získat ověřovací kód, poslat anonymní zprávu nebo si pronajmout dočasné číslo, služba splňuje širokou škálu požadavků na důvěrnost díky platbě v Bitcoin Lightning.



Mějte však na paměti její omezení: služba nezaručuje absolutní anonymitu a není vhodná pro citlivé nebo dlouhodobé účty. Při rozumném používání a s vědomím svých omezení je SMS4Sats praktickým nástrojem, jak získat zpět kontrolu nad svou telefonickou komunikací.



## Zdroje





- [oficiální stránky SMS4Sats](https://sms4sats.com)
- [Často kladené dotazy k službám](https://sms4sats.com/faq)
- [adresa Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)