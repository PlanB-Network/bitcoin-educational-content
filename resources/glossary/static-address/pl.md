---
term: STATIC Address
---

W kontekście Silent Payments odnosi się do unikalnego identyfikatora, który umożliwia otrzymywanie płatności bez ponownego użycia Address, bez interakcji i bez widocznego powiązania On-Chain między różnymi płatnościami a statycznym Address. Technika ta eliminuje potrzebę generate nowych, nieużywanych adresów odbiorczych dla każdej transakcji, unikając w ten sposób zwykłych interakcji w Bitcoin, w których odbiorca musi dostarczyć płatnikowi nowy Address. Jest to w pewnym sensie odpowiednik kodu płatności wielokrotnego użytku w kontekście BIP47.


Ten Address składa się z dwóch kluczy publicznych: $B_{\text{scan}}$ do skanowania i $B_{\text{spend}}$ do wydawania, połączonych w statyczny Address $B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$. Odbiorca publikuje ten Address, umożliwiając nadawcom uzyskanie unikalnych adresów płatności bez dalszej interakcji z odbiorcą. Aby zarządzać wieloma różnymi źródłami płatności, do $B_{\text{spend}}$ można dodać etykietę, tworząc w ten sposób kilka oznaczonych adresów statycznych z $B_1$, $B_2$ itd. Pozwala to na segregację płatności przy użyciu pojedynczej bazy Address, zmniejszając tym samym obciążenie skanowania Blockchain. Jednak wszystkie statyczne adresy podmiotu można łatwo powiązać ze względu na powszechne użycie $B_{\text{scan}}$.