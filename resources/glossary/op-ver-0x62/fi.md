---
term: OP_VER (0X62)

definition: Käytöstä poistettu opcode, joka lisäsi asiakasversion, muutettu OP_SUCCESS-opcodemiksi.
---
Sallii asiakasversion työntämisen pinoon. Tämä opkoodi poistettiin käytöstä, koska jos sitä olisi käytetty, jokainen päivitys olisi johtanut kovaan haarautumiseen. BIP342 muutti tämän opkoodin muotoon `OP_SUCCESS`.