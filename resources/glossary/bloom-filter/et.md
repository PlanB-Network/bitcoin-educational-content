---
term: BLOOM FILTER

---
Tõenäosuslik andmestruktuur, mida kasutatakse selleks, et testida, kas element on osa kogumist. Bloomi filtrid võimaldavad kiiret liikmelisuse kontrollimist ilma kogu andmekogumit testimata. Need on eriti kasulikud kontekstides, kus ruum ja kiirus on kriitilised, kuid kus on vastuvõetav madal ja kontrollitud veamäär. Bloomi filtrid ei tekita valenegatiivseid tulemusi, kuid nad tekitavad teatud hulga valepositiivseid tulemusi. Kui filtrisse lisatakse element, genereerivad mitu hash-funktsiooni positsioonid bittide massiivi. Liikmelisuse kontrollimiseks kasutatakse samu hash-funktsioone. Kui kõik vastavad bitid on seatud, kuulub element tõenäoliselt kogumisse, kuid sellega kaasneb valepositiivsete tulemuste oht. Bloomi filtreid kasutatakse laialdaselt andmebaaside ja võrkude valdkonnas. Eelkõige on teada, et Google kasutab neid oma tihendatud andmebaaside haldussüsteemis *BigTable*. Bitcoini protokollis kasutatakse neid eelkõige SPV rahakottide puhul vastavalt BIP37.

> ► *Kui räägitakse konkreetselt Bloomi filtrite kasutamisest Bitcoini tehingute kontekstis, kasutatakse mõnikord terminit "Transaction Bloom Filtering"