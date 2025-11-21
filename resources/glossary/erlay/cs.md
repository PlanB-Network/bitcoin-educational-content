---
term: ERLAY
---

Navrhovaný síťový protokol pro zlepšení účinnosti předávání nepotvrzených transakcí mezi uzly Bitcoin.


V současné době se každá transakce šíří prostřednictvím systému, v němž každý uzel vysílá transakci, o níž ví, všem svým kolegům. Problémem je, že to vede k velké redundanci a využití šířky pásma pro duplicity. Mnoho vysílání transakcí je zbytečných, protože příjemce o těchto transakcích již ví a každý uzel se o každé transakci musí dozvědět pouze jednou. Erlay navrhuje omezit ve výchozím nastavení počet vrstevníků, kterým uzel přímo posílá transakce, o nichž ví, na 8 a poté použít proces sesouhlasení založený na knihovně minisketch pro efektivnější sdílení chybějících transakcí.


Erlay by snížil spotřebu šířky pásma přibližně o 40 %, což by zpřístupnilo provoz Full node uživatelům s omezeným připojením k internetu, a podpořilo tak lepší decentralizaci sítě. Tento protokol by také udržoval téměř konstantní spotřebu šířky pásma s rostoucím počtem připojení. To znamená, že pro provozovatele uzlů by bylo mnohem jednodušší přijímat velmi velký počet připojení od svých kolegů, což by zvýšilo bezpečnost sítě Bitcoin snížením rizika rozdělení, ať už úmyslného, nebo náhodného. Erlay by navíc ztížil určení uzlu, z něhož transakce pochází, čímž by se zvýšila důvěrnost pro uživatele uzlů, které nepracují pod sítí Tor.


Erlay je navržen v BIP330.