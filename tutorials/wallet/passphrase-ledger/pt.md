---
name: BIP39 Passphrase Ledger
description: Como adicionar uma passphrase à sua carteira Ledger?
---
![cover](assets/cover.webp)

Uma passphrase BIP39 é uma senha opcional que, quando combinada com sua frase mnemônica, fornece uma camada adicional de segurança para carteiras Bitcoin determinísticas e hierárquicas. Neste tutorial, vamos revisar juntos como configurar uma passphrase na sua carteira Bitcoin segura em um Ledger (independentemente do modelo).

Antes de iniciar este tutorial, se você não está familiarizado com o conceito de passphrase, como funciona e suas implicações para sua carteira Bitcoin, eu recomendo fortemente consultar este outro artigo teórico onde explico tudo:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Como a passphrase funciona em um Ledger?

Com os dispositivos Ledger, você tem duas opções diferentes para configurar uma passphrase na sua carteira: a opção "*PIN-vinculado*" e a opção "*temporária*".

Com a opção "*PIN-vinculado*", você associa uma passphrase com um segundo PIN no seu Ledger. Isso significa que você terá 2 PINs: um para acessar sua carteira regular sem uma passphrase, e o outro para acessar sua segunda carteira protegida pela passphrase.

![PASSPHRASE BIP39](assets/notext/03.webp)

Fundamentalmente, mesmo com esta opção de passphrase vinculada ao segundo PIN, sua passphrase permanece sendo sua passphrase. Isso significa que se você perder seu Ledger e desejar recuperar seus bitcoins em outro dispositivo ou software, você precisará absolutamente de sua frase de 24 palavras e sua **passphrase completa**. O PIN associado à passphrase é usado apenas para acessá-la no seu Ledger atual, mas não funciona em outros Ledgers ou outros softwares. Portanto, é importante fazer um backup completo da sua passphrase em um meio físico. **Saber apenas o PIN secundário não é suficiente para recuperar o acesso à sua carteira**; é simplesmente um recurso de conveniência no seu Ledger.

Esta segunda opção de PIN é particularmente interessante para lidar com ataques físicos. Por exemplo, se um atacante forçá-lo a desbloquear seu dispositivo para roubar seus fundos, você pode usar o primeiro PIN para acessar uma carteira isca contendo uma pequena quantidade de bitcoins, enquanto mantém seus fundos principais seguros atrás do segundo PIN.

Além disso, esta opção oferece todos os benefícios de segurança da passphrase BIP39 sem a restrição de ter que inseri-la manualmente toda vez que usar seu dispositivo de assinatura. Isso permite que você use uma passphrase longa e aleatória, fortalecendo assim a proteção contra ataques de força bruta, enquanto evita a dificuldade de ter que digitá-la manualmente cada vez nos pequenos botões do dispositivo.
A opção da "passphrase temporária" não armazena a passphrase no dispositivo. Toda vez que você quiser acessar sua carteira protegida, precisará inserir manualmente a passphrase no Ledger. Isso torna o uso mais trabalhoso, mas também aumenta ligeiramente a segurança por não deixar nenhum rastro da passphrase no dispositivo. Assim que você desligar o dispositivo, ele retorna ao seu estado padrão e requer uma nova entrada da passphrase completa para acessar as contas ocultas. Esta opção de "passphrase temporária" é, portanto, semelhante ao funcionamento de outras carteiras de hardware.
Neste tutorial, usarei o Ledger Flex como exemplo. No entanto, se você estiver usando outro modelo de Ledger, o processo permanece o mesmo. Para o Ledger Stax, a interface é a mesma do Ledger Flex. Quanto aos modelos Nano S, Nano S Plus e Nano X, embora a interface seja diferente, o processo e os nomes dos menus permanecem os mesmos.
**Atenção:** Se você já recebeu bitcoins em sua Ledger antes de ativar a frase-senha, será necessário transferi-los por meio de uma transação Bitcoin. A frase-senha gera um conjunto de novas chaves, criando assim uma carteira completamente independente da sua carteira inicial. Ao adicionar a frase-senha, você terá uma nova carteira que estará vazia. No entanto, isso não exclui sua primeira carteira sem frase-senha. Você ainda pode acessá-la, diretamente pela sua Ledger sem inserir a frase-senha ou através de outro software usando sua frase de 24 palavras.
Antes de iniciar este tutorial, certifique-se de que já inicializou sua Ledger e gerou sua frase mnemônica. Se este não for o caso e sua Ledger for nova, siga o tutorial específico para o seu modelo disponível na PlanB Network. Uma vez concluída esta etapa, você pode retornar a este tutorial.

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4
https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Como configurar uma frase-senha temporária com uma Ledger?

Na página inicial da sua Ledger, clique na engrenagem de configurações.

![PASSPHRASE BIP39](assets/notext/04.webp)

Selecione o menu "Avançado", depois "Configurar frase-senha".

![PASSPHRASE BIP39](assets/notext/05.webp)

Este é o passo onde você pode escolher entre a opção "vinculada ao PIN" ou a opção "temporária" sobre a qual falamos na parte anterior. Aqui, explicarei como configurar uma frase-senha temporária, então clique em "Configurar frase-senha temporária".

![PASSPHRASE BIP39](assets/notext/06.webp)
Você será então solicitado a inserir sua frase-senha. Escolha uma frase-senha forte e proceda imediatamente a um backup físico, em um meio como papel ou metal. Neste exemplo, escolhi a frase-senha: `fH3&kL@9mP#2sD5qR!82`. Após inserir sua frase-senha, clique no botão "*Continuar*".
![PASSPHRASE BIP39](assets/notext/07.webp)

Verifique se sua frase-senha corresponde ao que você anotou no seu backup físico, depois clique no botão "*Sim, está correto*" para confirmar.

![PASSPHRASE BIP39](assets/notext/08.webp)

Para finalizar a criação da sua frase-senha, insira o código PIN da sua Ledger. A partir de agora, sempre que quiser acessar sua carteira com uma frase-senha na Ledger, você precisará seguir exatamente os mesmos passos descritos aqui.

![PASSPHRASE BIP39](assets/notext/09.webp)

Agora você pode importar seu conjunto de chaves públicas no Sparrow Wallet para gerenciar sua carteira. No Sparrow, isso corresponderá a uma carteira diferente da sua carteira inicial sem frase-senha.

Abra o Sparrow Wallet. Certifique-se de que o software está conectado a um nó, depois clique na aba "*Arquivo*" e selecione "*Nova Carteira*".

![PASSPHRASE BIP39](assets/notext/10.webp)

Escolha um nome para sua carteira protegida por uma frase-senha. Para este exemplo, optei por um nome que inclui explicitamente o termo "*frase-senha*". No entanto, se preferir manter a discrição desta carteira no seu computador, você pode escolher um nome menos evocativo.

![PASSPHRASE BIP39](assets/notext/11.webp)

Escolha o tipo de script para sua carteira. Aconselho você a escolher "*Taproot*" ou alternativamente "*SegWit Nativo*".

![PASSPHRASE BIP39](assets/notext/12.webp)
Conecte seu Ledger ao computador e clique em "*Connected Hardware Wallet*". Certifique-se de que já inseriu sua passphrase no seu Ledger. Se não, por favor, volte aos passos anteriores para inserir sua passphrase. Antes de prosseguir para a varredura, lembre-se também de abrir a aplicação "*Bitcoin*" no seu Ledger.
![PASSPHRASE BIP39](assets/notext/13.webp)

Clique no botão "*Scan...*".

![PASSPHRASE BIP39](assets/notext/14.webp)

Clique em "*Import Keystore*" ao lado do seu Ledger.

![PASSPHRASE BIP39](assets/notext/15.webp)

Sua carteira protegida pela passphrase agora está criada no Sparrow. Para confirmar, clique no botão "*Apply*".

![PASSPHRASE BIP39](assets/notext/16.webp)
Escolha uma senha forte para garantir o acesso ao Sparrow Wallet. Esta senha assegurará a segurança do acesso aos dados da sua carteira no Sparrow, o que ajuda a proteger suas chaves públicas, endereços, etiquetas e histórico de transações contra qualquer acesso não autorizado.
Aconselho que você salve esta senha em um gerenciador de senhas para não esquecê-la.

![PASSPHRASE BIP39](assets/notext/17.webp)

E pronto, sua carteira está agora criada! No menu "*Settings*", o Sparrow fornecerá o seu "*Master fingerprint*". Isso representa a impressão digital da sua chave mestre, usada como base para derivar sua carteira. Eu recomendo fortemente manter uma cópia dessa impressão digital. No meu exemplo, ela corresponde a: `281ee33a`.

![PASSPHRASE BIP39](assets/notext/18.webp)

Lembre-se do que mencionamos nas partes anteriores: um erro, mesmo que pequeno, ao inserir sua passphrase gerará uma carteira totalmente nova com chaves diferentes. Sempre que precisar garantir que está acessando a carteira certa com a passphrase correta, verifique se a impressão digital da sua chave mestre corresponde à que você anotou. Esta informação, por si só, não representa risco à segurança dos seus fundos ou à sua privacidade.

Antes de usar sua carteira com uma passphrase, aconselho fortemente que você faça um teste de recuperação a seco. Anote uma informação de referência como seu xpub ou a impressão digital da sua chave mestre, depois resete seu Ledger enquanto a carteira ainda estiver vazia. Em seguida, tente restaurar sua carteira no Ledger usando seus backups em papel da frase de 24 palavras e da passphrase. Verifique se a informação gerada após a restauração corresponde ao que você inicialmente anotou. Se for o caso, você pode ter certeza de que seus backups em papel são confiáveis.

## Como configurar uma passphrase vinculada a um PIN com um Ledger?

Na página inicial do seu Ledger, clique na roda de configurações.

![PASSPHRASE BIP39](assets/notext/19.webp)

Selecione o menu "*Advanced*", depois "*Set passphrase*".

![PASSPHRASE BIP39](assets/notext/20.webp)

Este é o passo onde você pode escolher entre a opção "*linked to PIN*" ou "*temporary*" que falamos na parte anterior. Aqui, explicarei como configurar uma passphrase anexada a um novo PIN, então clique em "*Set passphrase and attach it to a new PIN*".

![PASSPHRASE BIP39](assets/notext/21.webp)
Você deve então escolher o código PIN que será associado à sua passphrase. Assim como com o código PIN principal, é recomendado escolher um código PIN de 8 dígitos, o mais aleatório possível. Além disso, certifique-se de salvar este código em um local diferente de onde seu Ledger Flex é guardado.
No meu caso, o código PIN principal é `58293647` e eu escolhi `71425839` como o código PIN secundário associado à frase-secreta.
![PASSPHRASE BIP39](assets/notext/22.webp)

Você será então solicitado a inserir sua frase-secreta. Escolha uma frase-secreta forte e prossiga imediatamente para um backup físico, em um meio como papel ou metal. Neste exemplo, eu escolhi a frase-secreta: `fH3&kL@9mP#2sD5qR!82`. Após inserir sua frase-secreta, clique no botão "*Continue*".

![PASSPHRASE BIP39](assets/notext/23.webp)

Verifique se sua frase-secreta corresponde ao que você anotou no seu backup físico, então clique no botão "*Yes, it's correct*" para confirmar.

![PASSPHRASE BIP39](assets/notext/24.webp)

Para finalizar a criação da sua frase-secreta, insira o código PIN principal do seu Ledger (não o associado à frase-secreta).

![PASSPHRASE BIP39](assets/notext/25.webp)

A partir de agora, sempre que você quiser acessar sua carteira com uma frase-secreta no Ledger, precisará inserir não o código PIN principal, mas o código PIN secundário:
- Código PIN principal (`58293647`) > carteira sem frase-secreta.
- Código PIN secundário (`71425839`) > carteira com frase-secreta.

Agora você pode importar seu conjunto de chaves públicas no Sparrow Wallet para gerenciar sua carteira. No Sparrow, isso corresponderá a uma carteira diferente da sua carteira inicial sem frase-secreta.

Abra o Sparrow Wallet. Certifique-se de que o software está conectado a um nó, então clique na aba "*File*" e selecione "*New Wallet*".

![PASSPHRASE BIP39](assets/notext/26.webp)

Escolha um nome para sua carteira protegida por uma frase-secreta. Para este exemplo, optei por um nome que inclui explicitamente o termo "*passphrase*". No entanto, se preferir manter a discrição desta carteira no seu computador, você pode escolher um nome menos evocativo.

![PASSPHRASE BIP39](assets/notext/27.webp)

Escolha o tipo de script para sua carteira. Aconselho você a escolher "*Taproot*" ou, na falta disso, "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/28.webp)
Conecte seu Ledger ao seu computador, então clique em "*Connected Hardware Wallet*". Certifique-se de que já tem sua frase-secreta no seu Ledger desbloqueando-o com o código PIN secundário. Se não, reinicie seu Ledger e insira o código PIN associado à frase-secreta. Antes de prosseguir para a varredura, lembre-se também de abrir a aplicação "*Bitcoin*" no seu Ledger.

![PASSPHRASE BIP39](assets/notext/29.webp)

Clique no botão "*Scan...*".

![PASSPHRASE BIP39](assets/notext/30.webp)

Clique em "*Import Keystore*".

![PASSPHRASE BIP39](assets/notext/31.webp)

Sua carteira protegida pela frase-secreta agora está criada no Sparrow. Para confirmar, clique no botão "*Apply*".

![PASSPHRASE BIP39](assets/notext/32.webp)

Escolha uma senha forte para garantir o acesso ao Sparrow Wallet. Esta senha garantirá a segurança do acesso aos dados da sua carteira no Sparrow, o que ajuda a proteger suas chaves públicas, endereços, etiquetas e histórico de transações contra qualquer acesso não autorizado.

Aconselho você a salvar esta senha em um gerenciador de senhas para não esquecê-la.
![PASSPHRASE BIP39](assets/notext/33.webp)
E aí está, sua carteira agora está criada! No menu "*Configurações*", o Sparrow fornecerá a você sua "*Impressão digital mestre*". Isso representa a impressão digital da sua chave mestra, usada na base da derivação da sua carteira. Eu recomendo fortemente que você guarde uma cópia dessa impressão digital. No meu exemplo, ela corresponde a: `281ee33a`.

![PASSPHRASE BIP39](assets/notext/34.webp)

Lembre-se do que mencionamos nas partes anteriores: um erro, mesmo que pequeno, ao inserir sua frase-senha gerará uma carteira completamente nova com chaves diferentes. Sempre que precisar garantir acesso à carteira correta com a frase-senha certa, verifique se a impressão digital da sua chave mestra corresponde à que você anotou. Esta informação, por si só, não representa risco algum para a segurança dos seus fundos ou sua privacidade.
Antes de usar sua carteira com uma frase-senha, eu aconselho fortemente que você faça um teste de recuperação a seco. Anote uma informação de referência como seu xpub ou a impressão digital da sua chave mestra, depois resete seu Ledger enquanto a carteira ainda estiver vazia. Em seguida, tente restaurar sua carteira no Ledger usando seus backups em papel da frase de 24 palavras e da frase-senha. Verifique se a informação gerada após a restauração corresponde ao que você inicialmente anotou. Se for o caso, você pode ter certeza de que seus backups em papel são confiáveis.

Parabéns, sua carteira Bitcoin agora está segura com uma frase-senha! Se você achou este tutorial útil, eu apreciaria se você pudesse deixar um joinha abaixo. Sinta-se à vontade para compartilhar este artigo em suas redes sociais. Muito obrigado!

Eu também recomendo que você confira este outro tutorial completo sobre como usar seu Ledger Flex:

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a