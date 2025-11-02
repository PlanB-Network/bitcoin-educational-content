---
name: BIP-39 passphrase SeedSigner
description: Como é que adiciono um passphrase à minha carteira SeedSigner?
---

![cover](assets/cover.webp)



Um passphrase BIP39 é uma senha opcional que, combinada com a frase Mnemonic, fornece um Layer adicional de segurança para carteiras Bitcoin determinísticas e hierárquicas. Neste tutorial, vamos descobrir juntos como configurar um passphrase no seu Bitcoin Wallet usado com um SeedSigner.



![Image](assets/fr/01.webp)



## Pré-requisitos antes de adicionar um passphrase



Antes de começar este tutorial, se não estiveres familiarizado com o conceito de passphrase, como funciona e as suas implicações para o teu Bitcoin Wallet, recomendo-te vivamente que consultes este outro artigo teórico onde explico tudo (isto é muito importante, pois usar um passphrase sem perceber bem como funciona pode colocar os teus bitcoins em risco) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Antes de iniciar este tutorial, certifique-se também de que já inicializou o seu SeedSigner e gerou a sua frase Mnemonic. Se não o tiver feito e o seu SeedSigner for novo, siga o tutorial na Plan ₿ Academy. Quando tiver concluído esta etapa, pode voltar a este tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Como é que adiciono um passphrase ao SeedSigner?



Adicionar um passphrase ao seu portefólio gerido através do SeedSigner cria um portefólio completamente novo, gerando um conjunto de chaves totalmente separado. Consequentemente, se já tiver uma carteira que contenha Satss, deixará de poder aceder-lhe com o passphrase, uma vez que este gera uma carteira completamente diferente.



Para aplicar um passphrase ao seu SeedSigner, ligue o dispositivo e digitalize o seu SeedQR como habitualmente. O SeedSigner apresentará então a impressão digital do seu Wallet atual, correspondente ao Wallet **sem passphrase**. O Wallet com o passphrase terá uma impressão digital diferente.



Clicar no botão `BIP-39 passphrase`.



![Image](assets/fr/02.webp)



Em seguida, introduza o passphrase da sua escolha no campo fornecido, utilizando o teclado no ecrã. Certifica-te de que fazes uma ou mais cópias de segurança físicas (papel ou metal): a perda deste passphrase resultará na perda permanente do acesso aos teus bitcoins. **Para restaurar um Wallet, tanto o Mnemonic quanto o passphrase são essenciais ** Se qualquer um deles for perdido, seus bitcoins serão irremediavelmente bloqueados.



Quando tiveres completado a tua entrada, valida-a premindo o botão `KEY3` no canto inferior direito do SeedSigner.



![Image](assets/fr/03.webp)



*Neste exemplo, utilizei o passphrase `pba`. No entanto, no seu caso, certifique-se de que escolhe um passphrase robusto. Para saber como definir um passphrase ótimo, consulte este outro artigo:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

O SeedSigner apresenta então a nova impressão digital do seu passphrase Wallet. Faça várias cópias desta impressão digital: é importante quando utiliza um Wallet com o passphrase, pois permite-lhe verificar, de cada vez que introduz o passphrase, se não cometeu nenhum erro de digitação e se está a aceder ao Wallet correto.



Por exemplo, se, no meu caso, ao iniciar o SeedSigner, escrever por engano o passphrase `Pba` em vez de `pba`, esta simples mudança de minúsculas para maiúsculas resultará na criação de uma carteira completamente diferente daquela a que pretendo aceder.



Esta impressão digital não representa qualquer risco para a segurança ou confidencialidade do seu Wallet. Não revela qualquer informação, pública ou privada, sobre as suas chaves. Ao contrário do Mnemonic e do passphrase, pode guardar a impressão digital num suporte digital. Recomendo que guarde uma cópia em vários locais: em papel, num gestor de senhas, etc.



Depois de ter guardado a sua impressão digital, clique em "Concluído".



![Image](assets/fr/04.webp)



Tem então acesso a todas as funções da sua carteira, tal como num SeedSigner clássico.



![Image](assets/fr/05.webp)



Agora pode importar o keystore para o Sparrow wallet e usar o seu Wallet normalmente. De cada vez que reiniciar, terá de analisar o seu SeedQR e voltar a introduzir o seu passphrase utilizando o teclado, como fizemos aqui.



Antes de utilizar efetivamente o seu Wallet com o passphrase, recomendo vivamente que efectue um teste de recuperação totalmente vazio. Isto permitir-lhe-á confirmar que a frase do Mnemonic e as cópias de segurança do passphrase são válidas. Para saber como efetuar esta verificação, consulte o seguinte tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895