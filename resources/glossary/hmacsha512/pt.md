---
term: HMAC-SHA512

---
a sigla `HMAC-SHA512` significa "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Trata-se de um algoritmo criptográfico utilizado para verificar a integridade e a autenticidade das mensagens trocadas entre duas partes. Combina a função hash criptográfica `SHA512` com uma chave secreta partilhada para gerar um código de autenticação de mensagem (MAC) único para cada mensagem.

No contexto do Bitcoin, o uso natural do `HMAC-SHA512` é ligeiramente derivado. Este algoritmo é utilizado no processo de derivação determinística e hierárquica da árvore de chaves criptográficas de uma carteira. o `HMAC-SHA512` é usado principalmente para ir da semente para a chave mestra e, em seguida, para cada derivação de um par pai para pares filhos. Este algoritmo é também encontrado noutro algoritmo de derivação chamado `PBKDF2`, utilizado para ir da frase de recuperação e da frase-chave para a semente.