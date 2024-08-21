---
termi: OP_HASH256 (0XAA)
---

Ottaa pinon päällimmäisen alkion ja korvaa sen sen hash-arvolla käyttämällä `SHA256`-funktiota kahdesti. Syöte hashataan ensin `SHA256`:lla, ja sitten saatu tiiviste hashataan toisen kerran `SHA256`:lla. Tämä kaksivaiheinen prosessi tuottaa 256-bittisen sormenjäljen.