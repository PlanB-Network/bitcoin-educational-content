---
term: FORÇAR FECHAMENTO
---

Mecanismo de fecho de canal Lightning não cooperativo. Quando dois utilizadores abrem um canal com um Multisig 2/2, cada um pode unilateralmente fechar o canal transmitindo o último Commitment Transaction que já foi assinado, de modo a recuperar os seus bitcoins onchain. Isto é conhecido como "force close".


Este método é geralmente utilizado se um dos participantes já não responde ou se o fecho cooperativo do canal é impossível. Se for possível evitar o encerramento forçado, é preferível, uma vez que demora mais tempo a recuperar os fundos onchain e pode ser muito mais dispendioso em termos de taxas.


Num fecho forçado, um dos dois utilizadores transmite o Commitment Transaction, que reflecte o último estado conhecido do canal Lightning. Há então um bloqueio de tempo antes que os bitcoins possam ser recuperados na cadeia, dando à outra parte tempo para verificar se a transação corresponde ao estado mais recente do canal. Se um utilizador tentar fazer batota ao publicar um Commitment Transaction desatualizado, a outra parte pode utilizar o segredo de revogação para punir o batoteiro e recuperar todos os fundos no canal.