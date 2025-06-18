---
term: ATAK PYŁOWY
---

Dusting Attack polega na wysyłaniu niewielkich ilości bitcoinów na dużą liczbę adresów odbiorczych. Celem atakującego jest zmuszenie odbiorców do konsolidacji tych kwot z innymi UTXO. Następnie atakujący śledzi przyszłe ruchy tych niewielkich ilości bitcoinów, dążąc do utworzenia klastrów adresów, czyli ustalenia, czy wiele adresów należy do tego samego podmiotu. Korelując informacje zebrane podczas ataku dusting z innymi danymi i heurystykami wykorzystywanymi w analizie łańcucha, atakujący może zidentyfikować określone podmioty i powiązane z nimi adresy. Metoda ta stanowi zagrożenie jedynie dla prywatności użytkowników, ale nie wpływa na bezpieczeństwo ich środków.


> niektórzy bitcoinerzy sugerują, aby nie używać już terminu "atak dustingowy", ponieważ może on wprowadzać w błąd. W rzeczywistości termin "Dust" opisuje coś bardzo specyficznego w Bitcoin Core. Gdyby atak typu dusting faktycznie wykorzystywał Dust zgodnie z opisem w Core, atak byłby nieskuteczny. Dlatego niektórzy sugerują użycie terminu "wymuszone ponowne użycie Address", aby dokładniej opisać ten atak *