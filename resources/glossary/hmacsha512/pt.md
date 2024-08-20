---
termo: HMAC-SHA512
---

`HMAC-SHA512` significa "Código de Autenticação de Mensagem Baseado em Hash - Algoritmo de Hash Seguro 512". É um algoritmo criptográfico usado para verificar a integridade e autenticidade de mensagens trocadas entre duas partes. Ele combina a função de hash criptográfico `SHA512` com uma chave secreta compartilhada para gerar um Código de Autenticação de Mensagem (MAC) único para cada mensagem.

No contexto do Bitcoin, o uso natural do `HMAC-SHA512` é ligeiramente derivado. Este algoritmo é usado no processo de derivação determinística e hierárquica da árvore de chave criptográfica de uma carteira. `HMAC-SHA512` é notavelmente usado para ir da semente à chave mestra, e então para cada derivação de um par pai para pares filhos. Este algoritmo também é encontrado dentro de outro algoritmo de derivação chamado `PBKDF2`, usado para ir da frase de recuperação e senha para a semente.