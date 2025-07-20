---
term: LNURL
---

Protokół komunikacyjny, który określa zestaw funkcji zaprojektowanych w celu uproszczenia interakcji między węzłami Lightning i klientami, a także aplikacjami innych firm. Protokół ten opiera się na protokole HTTP i umożliwia tworzenie linków do różnych operacji, takich jak żądanie płatności, żądanie wypłaty lub inne funkcje, które poprawiają komfort użytkowania. Każdy LNURL to adres URL zakodowany w bech32 z przedrostkiem `lnurl`, który po zeskanowaniu uruchamia serię automatycznych działań na Lightning Wallet.


Na przykład LNURL-withdraw (LUD-03) pozwala wypłacić środki z usługi poprzez zeskanowanie kodu QR, bez konieczności ręcznego generate i Invoice. Lub LNURL-auth (LUD-04) pozwala łączyć się z usługami online za pomocą klucza prywatnego na Lightning Wallet zamiast hasła.