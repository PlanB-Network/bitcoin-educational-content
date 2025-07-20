---
term: IP_ASN.MAP
---

Plik używany w Bitcoin Core do przechowywania ASMAP, który usprawnia grupowanie (tj. grupowanie) adresów IP, opierając się na numerach systemów autonomicznych (ASN). Zamiast grupowania połączeń wychodzących według prefiksów sieci IP (/16), plik ten pozwala na dywersyfikację połączeń poprzez ustanowienie mapy adresowania IP do ASN, które są unikalnymi identyfikatorami dla każdej sieci w Internecie. Pomysł polega na poprawie bezpieczeństwa i topologii sieci Bitcoin poprzez dywersyfikację połączeń w celu ochrony przed niektórymi atakami (zwłaszcza atakiem Erebus).