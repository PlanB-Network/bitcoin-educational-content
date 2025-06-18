---
term: P2P TRANSPORT V2
---

Nova verzija Bitcoin P2P transportnog protokola koja uključuje oportunističku enkripciju radi poboljšanja privatnosti i sigurnosti komunikacija između čvorova. Ovo poboljšanje ima za cilj da Address nekoliko problema sa osnovnom verzijom P2P protokola, posebno tako što čini razmenjene podatke neprepoznatljivim pasivnom posmatraču (kao što je internet provajder), čime se smanjuju rizici od cenzure i napada kroz detekciju specifičnih obrazaca u paketima podataka.


Implementirana enkripcija ne uključuje autentifikaciju kako bi se izbeglo dodavanje nepotrebne složenosti i kako se ne bi ugrozila priroda mrežne veze bez dozvola. Ipak, ovaj novi P2P transportni protokol nudi bolju sigurnost protiv pasivnih napada i čini aktivne napade značajno skupljim i lakše uočljivim (posebno MITM napade). Uvođenje pseudo-slučajnog toka podataka otežava zadatak napadačima koji žele da cenzurišu ili manipulišu komunikacijama.


P2P Transport V2 je uključen kao opcija (onemogućena po defaultu) u verziji 26.0 Bitcoin Core, implementiranoj u decembru 2023. Može se aktivirati sa opcijom `v2transport=1` u konfiguracionoj datoteci.