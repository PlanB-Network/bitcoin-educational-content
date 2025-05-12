---
term: FORMAT IMPORTU Wallet (WIF)
---

Metoda kodowania klucza prywatnego Bitcoin w taki sposób, aby można go było łatwiej importować lub eksportować między różnymi portfelami. WIF opiera się na kodowaniu `Base58Check`, które zawiera informacje o wersji, kompresji odpowiadającego klucza publicznego oraz sumę kontrolną do wykrywania błędów podczas pisania. Klucz prywatny WIF zaczyna się od znaków `5` dla kluczy nieskompresowanych lub `K` i `L` dla kluczy skompresowanych i zawiera wszystkie znaki niezbędne do odtworzenia oryginalnego klucza prywatnego. Format WIF zapewnia znormalizowane środki do przesyłania klucza prywatnego między różnymi programami Wallet.