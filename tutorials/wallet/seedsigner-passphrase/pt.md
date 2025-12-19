---
name: BIP-39 Passphrase SeedSigner
description: Como é que adiciono um passphrase à minha carteira SeedSigner?
---

![cover](assets/cover.webp)



Um passphrase BIP39 é uma senha opcional que, combinada com a frase mnemónica, fornece uma camada adicional de segurança para carteiras Bitcoin determinísticas e hierárquicas. Neste tutorial, vamos descobrir juntos como configurar um passphrase no seu Bitcoin wallet usado com um SeedSigner.



![Image](assets/fr/01.webp)



## Pré-requisitos antes de adicionar uma frase-chave



Antes de começar este tutorial, se não estiveres familiarizado com o conceito de passphrase, como funciona e as suas implicações para o teu Bitcoin wallet, recomendo-te vivamente que consultes este outro artigo teórico onde explico tudo (isto é muito importante, pois usar um passphrase sem perceber bem como funciona pode colocar os teus bitcoins em risco) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Antes de iniciar este tutorial, certifique-se também de que já inicializou o seu SeedSigner e gerou a sua frase mnemónica. Se não o fez e o seu SeedSigner é novo, siga o tutorial na Plan ₿ Academy. Quando tiver concluído esta etapa, pode voltar a este tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Como é que adiciono um passphrase ao SeedSigner?



Adicionar um passphrase ao seu portefólio gerido através do SeedSigner cria um portefólio completamente novo, gerando um conjunto de chaves completamente separado. Por conseguinte, se já tiver uma carteira que contenha satss, deixará de poder aceder-lhe com o passphrase, uma vez que este gera uma carteira completamente diferente.



Para aplicar um passphrase ao seu SeedSigner, ligue o dispositivo e digitalize o seu SeedQR como habitualmente. O SeedSigner mostrará então a impressão digital do seu wallet atual, correspondente ao **sem passphrase**. O wallet com passphrase terá uma impressão digital diferente.



Clique no botão `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Em seguida, introduza o passphrase da sua escolha no campo fornecido, utilizando o teclado no ecrã. Certifique-se de que faz um ou mais backups físicos (papel ou metal): a perda deste passphrase resultará na perda permanente do acesso aos seus bitcoins. **Para restaurar um wallet, tanto a mnemónica como o passphrase são essenciais ** Se qualquer um deles for perdido, os seus bitcoins serão irremediavelmente bloqueados.



Quando tiveres completado a tua entrada, valida-a premindo o botão `KEY3` no canto inferior direito do SeedSigner.



![Image](assets/fr/03.webp)



*Neste exemplo, utilizei o passphrase `pba`. No entanto, no seu caso, certifique-se de que escolhe um passphrase robusto. Para saber como definir um passphrase ótimo, consulte este outro artigo:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

O SeedSigner apresenta então a nova impressão digital do seu passphrase wallet. Faça várias cópias desta impressão digital: é importante quando se utiliza um wallet com o passphrase, pois permite-lhe verificar, de cada vez que introduz o passphrase, se não cometeu nenhum erro de digitação e se está a aceder ao wallet correto.



Por exemplo, se, no meu caso, ao iniciar o SeedSigner, escrever por engano o passphrase `Pba` em vez de `pba`, esta simples mudança de minúsculas para maiúsculas resultará na criação de uma carteira completamente diferente daquela a que pretendo aceder.



Esta impressão digital não representa qualquer risco para a segurança ou confidencialidade do seu wallet. Não revela qualquer informação, pública ou privada, sobre as suas chaves. Assim, ao contrário da mnemónica e do passphrase, pode guardar a impressão digital num suporte digital. Recomendo que guarde uma cópia em vários locais: numa folha de papel, num gestor de palavras-passe, etc.



Depois de ter guardado a sua impressão digital, clique em "Concluído".



![Image](assets/fr/04.webp)



Tem então acesso a todas as funções da sua carteira, tal como num SeedSigner clássico.



![Image](assets/fr/05.webp)



Agora podes importar o keystore para o Sparrow Wallet e usar o teu wallet normalmente. De cada vez que reiniciar, terá de analisar o seu SeedQR e voltar a introduzir o seu passphrase utilizando o teclado, como fizemos aqui.



Antes de utilizar efetivamente o seu wallet com o passphrase, recomendo vivamente que efectue um teste de recuperação totalmente vazio. Isto permitir-lhe-á confirmar que as suas cópias de segurança da frase mnemónica e do passphrase são válidas. Para saber como efetuar esta verificação, consulte o seguinte tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895