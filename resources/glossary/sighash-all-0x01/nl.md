---
term: SIGHASH_ALL
definition: SigHash-vlag die aangeeft dat de handtekening alle inputs en outputs van de transactie dekt.
---

Type SigHash Flag gebruikt in Bitcoin transactiehandtekeningen om aan te geven dat de handtekening geldt voor alle onderdelen van de transactie. Door `SIGHASH_ALL` te gebruiken, dekt de ondertekenaar alle ingangen en alle uitgangen. Dit betekent dat noch de inputs, noch de outputs gewijzigd kunnen worden na de handtekening zonder deze ongeldig te maken. Dit type SigHash Flag komt het meest voor bij Bitcoin transacties, omdat het volledige finaliteit en integriteit van de transactie garandeert.