---
term: MASTER SCHLÜSSEL

---
Im Zusammenhang mit HD-Wallets (Hierarchical Deterministic) ist der private Hauptschlüssel ein eindeutiger privater Schlüssel, der aus dem Seed der Wallet abgeleitet wird. Um den Hauptschlüssel zu erhalten, wird die Funktion `HMAC-SHA512` auf den Seed angewendet, wobei die Worte "*Bitcoin Seed*" wörtlich als Schlüssel verwendet werden. Das Ergebnis dieser Operation ist eine 512-Bit-Ausgabe, wobei die ersten 256 Bits den Hauptschlüssel und die restlichen 256 Bits den Hauptkettencode bilden. Der Hauptschlüssel und der Hauptkettencode dienen als Ausgangspunkt für die Ableitung aller untergeordneten privaten und öffentlichen Schlüssel in der Baumstruktur der HD-Wallet. Daher befindet sich der private Hauptschlüssel in der Tiefe 0 der Ableitung.

![](../../dictionnaire/assets/19.webp)