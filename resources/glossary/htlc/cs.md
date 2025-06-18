---
term: HTLC
---

Znamená "*Hashed Timelock Contract*". Jedná se o mechanismus Smart contract, který se používá hlavně u blesků. Někdy se vyskytuje také v atomických výměnách. V podstatě HTLC podmiňuje převod peněz odhalením tajemství a zahrnuje také časovou podmínku, která chrání peníze odesílatele v případě neúspěšné transakce.


V systému Lightning umožňuje HTLC posílat bitcoiny do uzlu, s nímž nemáte přímý kanál, a to prostřednictvím několika kanálů, aniž by bylo nutné po cestě důvěřovat. Platba mezi jednotlivými uzly je podmíněna poskytnutím předobrazu (tajemství, které po zaheslování odpovídá dohodnuté hodnotě). Pokud konečný příjemce poskytne tento předobraz, může si nárokovat prostředky a nutně umožní každému zprostředkujícímu uzlu kaskádovitě si nárokovat prostředky.


Například pokud chce Alice poslat 1 BTC Davidovi, ale nemá s ním přímý kanál, musí jít přes Boba a Carol, kteří mezi sebou mají platební kanály. Zde je popsán průběh transakce:




- David daruje Alici blesk Invoice. Ten obsahuje Hash $h$ tajného $s$ (předobrazu), který zná pouze David. Máme tedy: $h = \text{Hash}(s)$ ;
- Alice vytvoří HTLC s Bobem, který jí nabídne zaslání 1 BTC pod podmínkou, že jí Bob poskytne tajemství $s$ (předobraz), které odpovídá Hash $h$ ;
- Bob vytvoří HTLC s Carol, která mu nabídne poslat 1 BTC pod podmínkou, že mu poskytne stejné tajemství $s$ ;
- Carol vytvoří HTLC s Davidem, který nabídne další 1 BTC, pokud odhalí předobraz $s$;
- David prozradí Carol $s$ (což věděl jen on) a získá 1 BTC. Carol nyní může použít $s$ k získání BTC od Boba. A Bob, který nyní zná $s$, udělá totéž s Alicí.


Nakonec Alice poslala 1 BTC Davidovi prostřednictvím Boba a Carol (neutrální akce pro Carol), aniž by si kdokoli musel důvěřovat, protože vše je kaskádově zajištěno podmínkami HTLC.


HTLC tak umožňují takzvané "atomické" výměny: buď je převod zcela úspěšný, nebo se nezdaří a prostředky se vrátí. Tím je zaručena bezpečnost transakcí, a to i mezi více účastníky bez nutnosti důvěry.