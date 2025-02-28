---
term: HASHCASH

---
HashCash je systém proof-of-work, který v roce 1997 navrhl Adam Back pro boj proti spamu a útokům DoS. Je založen na principu, že odesílatel musí provést výpočetní úlohu (konkrétně najít částečnou kolizi na kryptografické hashovací funkci), aby dokázal svou práci. Tato úloha je pro odesílatele časově a energeticky nákladná, ale ověření výsledku příjemcem je rychlé a jednoduché. Tento protokol se ukázal jako zvláště vhodný pro boj proti spamu v e-mailové komunikaci, protože je minimálně zatěžující pro legitimní uživatele a zároveň představuje významnou překážku pro spammery. Odeslání jednoho e-mailu totiž vyžaduje několik vteřin výpočtu, ale opakování této operace milionkrát se stává energeticky a časově nesmírně nákladným, což často popírá ekonomický zájem na spamových kampaních, ať už marketingových, nebo záškodnických. Navíc umožňuje zachovat anonymitu odesílatele.

HashCash si rychle osvojili cypherpunkeři, kteří chtěli vyvinout anonymní systém elektronické měny bez prostředníků. Inovace Adama Backa skutečně poprvé zavedla koncept nedostatku v digitálním světě. Koncept proof of work pak najdeme v několika elektronických měnových systémech předcházejících Bitcoinu, mj:


- b-money od Wei Daie vydaný v roce 1998;
- R-POW od Hala Finneyho vydaná v roce 2004;
- BitGold od Nicka Szaba vydaný v roce 2005.

Princip HashCash se nachází také v protokolu Bitcoin, kde se používá jako ochranný mechanismus proti útokům Sybil.