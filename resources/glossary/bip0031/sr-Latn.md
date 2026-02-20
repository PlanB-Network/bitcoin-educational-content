---
term: BIP0031
definition: Uvođenje poruke pong kao odgovora na ping radi provere povezanosti između čvorova u Bitcoin mreži.
---

Predlog usmeren na poboljšanje mehanizama upravljanja mrežom od strane Bitcoin čvorova. Pre BIP31, Bitcoin čvorovi nisu imali direktan način da znaju da li su njihovi vršnjaci još uvek povezani, operativni i nisu preopterećeni. BIP31 je uveo korišćenje `pong` poruke, kao odgovor na `ping` poruku, što omogućava aktivnu proveru povezanosti između čvorova.