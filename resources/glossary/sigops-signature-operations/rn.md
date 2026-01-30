---
term: Sigops (signature operations)
definition: Ibikorwa vy'umukono wa gihanga bikenewe kugira bemeze ama transactions ya Bitcoin.
---

Yerekeza ku bikorwa vy’umukono wa digitale bikenewe kugira ngo umuntu yemeze amafaranga. Igikorwa kimwekimwe cose ca Bitcoin gishobora kubamwo ibintu vyinshi vyinjizwa, kimwe cose muri vyo gishobora gusaba umukono umwe canke myinshi kugira ngo kibonwe ko gifise akamaro. Igenzura ry'izo sinya rikorwa biciye mu gukoresha amakode yihariye yitwa "sigops". By'umwihariko, ibi birimwo `OP_GUSUZUMA`, `OP_GUSUZUMA GUSUZUMA`, `OP_GUSUZUMA VYINSHI`, na `OP_GUSUZUMA VYINSHI`. Ivyo bikorwa bishiraho umuzigo w’akazi ku nzira z’uruja n’uruza zitegerezwa kubigenzura. Kugira ngo hatagira ibitero vya DoS biciye mu gutera imbere kw’umubare w’ama sigops, iyo porotokole rero ishiraho umupaka ku mubare w’ama sigops yemerewe ku bubiko, kugira ngo umuzigo wo kwemeza ugume ushobora gutunganirizwa neza ku bihimba. Ubu uwo mupaka ushizwe ku rugero rwo hejuru rw’ama sigops 80.000 ku bubiko. Kugira ngo ubare, amanode akurikiza aya mategeko:


Mu `urufunguzo rw'inyandiko`, `OP_GUSUZUMA` na `OP_GUSUZUMA GUSUZUMA` biharurwa nk'ama sigops 4. Amakode y'ibikorwa `OP_SUZUMA VYINSHI` na `OP_SUZUMA VYINSHI GUSUZUMA` biharura 80 sigops. Nkako, mu gihe co guharura, ivyo bikorwa bigwizwa na 4 iyo bitari mu gice c’inyungu ya SegWit (ku P2WPKH, igitigiri c’ama sigops rero kizoba 1);


Mu `redeemscript`, amakode y'ibikorwa `OP_SUZUMA` na `OP_SUZUMA GUSUZUMA` navyo biharurwa nk'ibice 4, `OP_SUZUMA VYINSHI` na `OP_SUZUMA VYINSHI GUSUZUMA` biharurwa nk'`4n` iyo bibanjirije si`se;


Ku `Inyandiko y'Icabona`, `OP_GUSUZUMA` na `OP_GUSUZUMA GUSUZUMA` bifise agaciro ka sigop 1, `OP_GUSUZUMA VYINSHI` na `OP_GUSUZUMA VYINSHI` biharurwa nka `n` iyo vyashizweho na `other si;0nse,


Mu nyandiko za Taproot, sigops zifatwa mu buryo butandukanye ugereranije n’inyandiko za kera. Aho guharura ata guca ku ruhande igikorwa cose c’umukono, Taproot itanga ingengo y’imari ya sigops ku bijanye n’inyungu yose y’ugucuruza, ikaba ihuye n’ubunini bw’iyo nsiguro. Iyi budget ni 50 sigops hamwe n’ubunini bwa byte bw’icabona c’injiza. Buri gikorwa co gusinya kigabanya iyo ngengo y’imari na 50. Iyo ugushirwa mu ngiro kw’igikorwa co gusinya kugabanya ingengo y’imari munsi ya zero, inyandiko ntigira akamaro. Ubu buryo buratuma habaho uguhinduranya cane mu nyandiko za Taproot, mu gihe umuntu aguma afise uburinzi ku bikorwa bibi bishobora gushika bifitaniye isano n’ama sigops, mu kubihuza ata guca ku ruhande n’uburemere bw’ivyo yinjije. Gutyo, inyandiko za Taproot ntiziri mu rugero rw’ama sigops 80.000 ku giciro c’ibarabara.