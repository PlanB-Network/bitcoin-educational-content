---
term: HASHCASH
---

HashCash je systém proof-of-work navržený Adamem Backem v roce 1997 za účelem boje proti spamu a DoS útokům. Je založen na principu, že odesílatel musí provést výpočetní úkol (konkrétně nalezení částečné kolize na kryptografické hašovací funkci), aby prokázal svou práci. Tento úkol je pro odesílatele nákladný z hlediska času a energie, ale ověření výsledku příjemcem je rychlé a jednoduché. Tento protokol se ukázal jako obzvláště vhodný pro boj proti spamu v emailové komunikaci, protože je pro legitimní uživatele minimálně zatěžující, zatímco pro spammery představuje významnou překážku. Skutečně, odeslání jednoho emailu vyžaduje několik sekund výpočtu, ale replikace této operace milionkrát se stává extrémně nákladnou z hlediska energie a času, což často neguje ekonomický zájem spamových kampaní, ať už jsou pro marketingové účely nebo škodlivé. Navíc umožňuje zachování anonymity odesílatele.

HashCash byl rychle přijat cypherpunky, kteří hledali vývoj anonymního elektronického měnového systému bez zprostředkovatelů. Skutečně, Adam Backova inovace poprvé představila koncept vzácnosti v digitálním světě. Koncept proof of work je pak nalezen v několika systémech elektronické měny předcházejících Bitcoin, včetně:
* b-money od Wei Dai publikované v roce 1998;
* R-POW od Hal Finney publikované v roce 2004;
* BitGold od Nick Szabo publikované v roce 2005.

Princip HashCash je také nalezen v protokolu Bitcoin, kde je používán jako ochranný mechanismus proti Sybil útokům.