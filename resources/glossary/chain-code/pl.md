---
term: KOD ŁAŃCUCHA
---

W kontekście hierarchicznej deterministycznej derywacji (HD) portfeli Bitcoin, kod łańcucha jest 256-bitową kryptograficzną wartością soli używaną do generate kluczy potomnych z klucza nadrzędnego, zgodnie ze standardem BIP32. Kod łańcucha jest używany w połączeniu z kluczem nadrzędnym i indeksem podrzędnym w celu deterministycznego generate nowej pary kluczy (klucza prywatnego i klucza publicznego) bez ujawniania klucza nadrzędnego lub innych pochodnych kluczy podrzędnych.


Dlatego dla każdej pary kluczy istnieje unikalny kod łańcucha. Kod łańcucha uzyskuje się poprzez haszowanie Wallet seed i pobranie prawej połowy bitów. W tym przypadku jest on określany jako główny kod łańcucha, powiązany z głównym kluczem prywatnym. Alternatywnie można go uzyskać przez haszowanie klucza nadrzędnego za pomocą kodu łańcucha nadrzędnego i indeksu, a następnie zachowanie odpowiednich bitów. Jest on następnie określany jako kod łańcucha podrzędnego.


Niemożliwe jest wyprowadzenie kluczy bez znajomości kodu łańcucha powiązanego z każdą parą nadrzędną. Wprowadza pseudolosowe dane do procesu wyprowadzania, aby zapewnić, że generowanie kluczy kryptograficznych pozostaje nieprzewidywalne dla atakujących, a jednocześnie jest deterministyczne dla posiadacza Wallet.


> w języku angielskim "code de chaîne" nazywany jest "chain code", a "code de chaîne maître" - "master chain code"