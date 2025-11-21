---
term: KOD PŁATNOŚCI WIELOKROTNEGO UŻYTKU
---

W BIP47 kod płatności wielokrotnego użytku jest statycznym identyfikatorem generowanym z Bitcoin Wallet, który umożliwia transakcję powiadomienia i wyprowadzenie unikalnych adresów. Pozwala to uniknąć ponownego wykorzystania adresów, co prowadzi do utraty prywatności, bez konieczności ręcznego uzyskiwania i przesyłania nowych, nieużywanych adresów dla każdej płatności. W BIP47 kody płatności wielokrotnego użytku są skonstruowane w następujący sposób:


- Bajt 0 odpowiada wersji;
- Bajt 1 to pole bitowe służące do dodawania informacji w przypadku konkretnego użycia;
- Bajt 2 wskazuje parzystość `y` klucza publicznego;
- Od bajtu 3 do bajtu 34 znajduje się wartość `x` klucza publicznego;
- Od bajtu 35 do bajtu 66 znajduje się kod łańcucha powiązany z kluczem publicznym;
- Od bajtu 67 do bajtu 79 występuje zerowe wypełnienie.


Część czytelna dla człowieka (HRP) jest zwykle dodawana na początku kodu płatności, a suma kontrolna na końcu, a następnie jest kodowana w base58. Konstrukcja kodu płatności jest więc dość podobna do konstrukcji klucza rozszerzonego. Oto na przykład mój własny kod płatności BIP47 w base58:


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


W implementacji BIP47 PayNym, kody płatności mogą być również wyrażone w formie identyfikatorów powiązanych z wizerunkiem robota. Oto na przykład mój:


```text
+throbbingpond8B1
```


Korzystanie z kodów płatniczych z implementacją PayNym jest obecnie dostępne na Sparrow Wallet na PC i Samourai Wallet na urządzenia mobilne.