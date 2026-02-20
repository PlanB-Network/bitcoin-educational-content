---
term: Invoice lightning
definition: Žádost o platbu Lightning obsahující všechny informace potřebné k provedení transakce.
---

Blesková žádost o platbu vygenerovaná příjemcem, která obsahuje všechny informace potřebné k dokončení transakce.


Blesk Invoice obsahuje cíl platby v podobě veřejného klíče uzlu příjemce, ale také prefix `LN`, částku, čas do vypršení platnosti, tajenku Hash používanou v HTLC a další metadata, z nichž některá jsou nepovinná, například možnosti směrování. Tyto faktury jsou definovány standardem BOLT11. Po zaplacení nelze blesk Invoice znovu použít.


