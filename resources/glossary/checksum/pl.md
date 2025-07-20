---
term: CHECKSUM
---

Suma kontrolna to wartość obliczana na podstawie zestawu danych, używana do weryfikacji integralności i ważności tych danych podczas transmisji lub przechowywania. Algorytmy sum kontrolnych są przeznaczone do wykrywania przypadkowych błędów lub niezamierzonych zmian danych, takich jak błędy transmisji lub uszkodzenie pliku. Istnieją różne rodzaje algorytmów sum kontrolnych, takie jak kontrole parzystości, modułowe sumy kontrolne, kryptograficzne funkcje Hash lub kody BCH (*Bose, Ray-Chaudhuri i Hocquenghem*).


W Bitcoin sumy kontrolne są używane na poziomie aplikacji w celu zapewnienia integralności adresów odbiorczych. Suma kontrolna jest obliczana na podstawie ładunku Address użytkownika, a następnie dodawana do tego Address w celu wykrycia wszelkich błędów w jego danych wejściowych. Suma kontrolna jest również obecna we frazach odzyskiwania (mnemonikach).


> ogólnie przyjęte jest używanie angielskiego terminu "suma kontrolna" bezpośrednio w języku francuskim