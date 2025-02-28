---
term: KETTAKOOD

---
Bitcoini rahakottide hierarhilise deterministliku (HD) tuletamise kontekstis on ahelakood 256-bitine krüptograafiline soolaväärtus, mida kasutatakse vanemvõtmest alamvõtmete genereerimiseks vastavalt BIP32 standardile. Ahelakoodi kasutatakse koos vanemvõtme ja lapsvõtme indeksiga, et luua deterministlikult uus võtmepaar (isiklik ja avalik võti) ilma vanemvõtme või teiste tuletatud lastvõtmete paljastamiseta.

Seetõttu on iga võtmepaari jaoks olemas unikaalne ahelakood. Kettakood saadakse kas rahakoti seemne hashimise teel ja võttes bitide parempoolse poole. Sellisel juhul nimetatakse seda master-kettakoodiks, mis on seotud master-privaatvõtmega. Teise võimalusena saab selle ka vanemvõtme hashimise teel koos selle vanemahelakoodiga ja indeksiga, säilitades seejärel parempoolsed bitid. Sellisel juhul nimetatakse seda lapse ahelakoodiks.

Võtmeid on võimatu tuletada ilma iga vanempaariga seotud ahelakoodi teadmata. See lisab tuletamisprotsessi pseudosrandomandmeid, et tagada, et krüptograafiliste võtmete genereerimine jääb ründajate jaoks ettearvamatuks, kuid on rahakoti omaniku jaoks deterministlik.

> ► *Inglise keeles nimetatakse "code de chaîne" "ahelakoodiks" ja "code de chaîne maître" "master chain code".*