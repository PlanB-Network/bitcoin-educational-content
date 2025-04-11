---
name: Ledger Nano S

description: Como configurar o seu dispositivo Ledger Nano S
---

![image](assets/cover.webp)

Carteira física fria - €60 - Iniciante - Para proteger de €2.000 a €50.000

A Ledger é a solução francesa para proteger bitcoins de maneira simples.

Neste tutorial, também discutiremos a seção de frases de segurança, uma solução avançada para armazenar grandes quantias: 20.000€ - 100.000€.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Conectar o Ledger à carteira de Bitcoin Sparrow (guia de escrita)

Certifique-se de ler primeiro a outra parte "Usando Carteiras de Hardware Bitcoin". Vou passar rapidamente por algumas etapas e focar principalmente no que é específico para o Ledger aqui.

## Configurando o dispositivo

O Ledger vem com seu próprio cabo USB. Certifique-se de usar esse cabo e não apenas qualquer cabo antigo. Alguns cabos USB são apenas para energia. Este transmite dados E energia. Quando usei o dispositivo com um cabo USB de carregamento de telefone que estava por perto, o dispositivo não conseguiu se conectar.

Conecte-o ao seu computador e o dispositivo será ligado.

![image](assets/1.webp)

Navegue pelas opções. Você verá

1. Configurar como novo dispositivo
2. Restaurar a partir da frase de recuperação

Basicamente, está perguntando se você deseja que o dispositivo crie uma semente para você ou se você já tem uma que gostaria de usar. É uma prática recomendada fazer sua própria semente, mas fazer isso com segurança é muito avançado e está fora do escopo deste artigo. Escolha "Configurar como novo dispositivo"

Em seguida, você será solicitado a escolher um PIN. Isso não faz parte da sua semente de Bitcoin e é específico apenas para este dispositivo. Ele bloqueia o dispositivo.

Em seguida, ele apresentará a você 24 palavras que você precisa navegar e anotar.

Curiosamente, quando você chegar ao final, ele diz "pressione para a esquerda para verificar suas palavras". Isso não descreve como você confirma para prosseguir, apenas significa que você pode voltar e olhar as palavras novamente. Em vez disso, pressione para a direita e confirme pressionando simultaneamente para a esquerda e para a direita.

A próxima parte é super irritante. Ele mistura as 24 palavras e você precisa confirmar cada uma, de 1 a 24, navegando por todas as palavras para cada seleção. Depois de terminar, ele permite que você confirme com uma pressão de dois botões e continue.

![image](assets/2.webp)

Você verá no seu painel que você tem um botão de configurações e um botão de sinal de mais que permite instalar aplicativos. Mas você precisa se conectar ao Ledger Live primeiro. Faremos isso a seguir...

## Baixe o Ledger Live

Você pode baixar o Ledger Live em sua página da web, mas é melhor obtê-lo no GitHub, onde o código-fonte é mantido.

Pesquise no Google "ledger live GitHub" ou clique neste link https://github.com/LedgerHQ/ledger-live-desktop

![image](assets/3.webp)

Role para baixo até ver o título "Downloads"...

![image](assets/4.webp)

Na parte inferior, você verá o link: Instruções para verificar o hash e as assinaturas dos pacotes de instalação estão disponíveis nesta página. Clique nesse link. (https://live.ledger.tools/lld-signatures)

![image](assets/5.webp)

No topo, há opções de links para o pacote de software que você precisa, dependendo do seu sistema operacional. Clique no apropriado para fazer o download.

Em seguida, queremos verificar o hash do download, para segurança adicional.
'Ledger publica o hash de cada um dos arquivos disponíveis nesta página. Agora vamos fazer o hash do download e comparar o resultado. Ele precisa ser idêntico para garantir que o arquivo não tenha sido adulterado.
Abra o terminal em um Mac ou CMD no Windows. Siga estes comandos...

cd Downloads

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Para Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Para Windows
```

<Enter>

Espero que seja óbvio que os comandos começam após as setas. Certifique-se de que, se este artigo estiver desatualizado, você altere o nome do arquivo nos comandos para exatamente o nome do arquivo que você baixou. Você precisa pressionar a tecla <Enter> após cada comando. Os comandos como vistos aqui podem não caber em uma linha no seu navegador da web. Observe que tudo é digitado em uma linha.

Observe a saída do hash e verifique se é idêntica àquela publicada no GitHub.

Idealmente, você deseja se certificar de que os hashes publicados não sejam falsos. Fazemos isso com assinaturas gpg, mas está fora do escopo deste artigo. Se você quiser aprender sobre isso (e sugiro que eventualmente faça), leia este artigo.

## Conecte-se ao Ledger Live

Antes de executar o Ledger Live, é útil ativar uma VPN para garantir um pouco mais de privacidade. O Ledger ainda terá todos os seus endereços, mas não saberá seu endereço IP, que revela seu endereço residencial. O Mullvad VPN é um excelente serviço de VPN e não é muito caro (não estou fazendo propaganda, é apenas o que eu uso).

Instale o software em seu computador e execute-o.

![image](assets/6.webp)

Selecione seu dispositivo e escolha "Primeira vez usando..."

![image](assets/7.webp)

Você será guiado por um assistente, mas já fizemos todos esses passos, então você pode apenas avançar.

![image](assets/8.webp)

Após muitas etapas e um questionário, ele verificará se o dispositivo é genuíno. Você precisa garantir que esteja conectado e tenha inserido o PIN e, em seguida, ele perguntará no dispositivo se você permite que o Ledger Live se conecte. Você precisa confirmar isso, é claro.

![image](assets/9.webp)

Havia algum anúncio de shitcoin disfarçado de "notas de lançamento" na próxima janela pop-up. Dispense-o e você deverá chegar a esta tela.

![image](assets/10.webp)

Você precisa clicar em "Adicionar conta" para obter uma carteira de Bitcoin.

![image](assets/11.webp)

Certifique-se de escolher Bitcoin e não Bitcoin Cash ou qualquer outra shitcoin. Ele verificará o dispositivo e você precisará confirmar para prosseguir NO DISPOSITIVO. Ele calculará os endereços por alguns minutos. Em seguida, clique em CONCLUÍDO.

![image](assets/12.webp)
![image](assets/13.webp)

Ótimo. Agora você tem um gerenciador de carteira de shitcoin contendo uma carteira de Bitcoin em seu computador. Na verdade, você não precisa mais disso e pode se livrar dele. O verdadeiro objetivo era obter o aplicativo Bitcoin no próprio dispositivo, e esta era a única maneira, exceto por realizar algumas técnicas extremas de engenharia de software.

Lembre-se de que anteriormente, no dispositivo, tínhamos um botão de configurações e um botão de sinal de mais. Agora temos um botão extra - o botão do aplicativo Bitcoin.

Agora você pode fechar o Ledger Live.

## Adicionar uma senha'

Agora que temos o aplicativo Bitcoin, podemos adicionar uma frase de acesso à nossa frase de semente. Antes, quando a semente foi criada pela primeira vez, não podíamos fazer isso porque, no início, não tínhamos o aplicativo Bitcoin e precisávamos nos conectar ao Ledger Live para obtê-lo.
Vá para o menu "configurações" dentro do dispositivo, em seguida, o submenu "segurança". Em seguida, selecione a frase de acesso. Você verá "Recurso avançado". Clique no botão direito, você verá "ler manual..." e depois de um clique no botão direito, você verá "voltar". Mas isso não é o fim. Intuitivamente, você pensaria isso, mas clique no botão direito novamente. Você verá "configurar frase de acesso".

Você pode decidir "anexar ao PIN" ou "definir temporariamente". Eu recomendo "anexar ao PIN". Dessa forma, você pode acessar diferentes carteiras dependendo do PIN que você digitar quando ligar o dispositivo pela primeira vez. Se você "definir temporariamente", precisará digitar a frase de acesso sempre que quiser acessar essa carteira, mas sempre será a partir do PIN padrão.

Digite a frase de acesso e confirme.

Será solicitado o "PIN atual". Este não é o PIN que você está associando à nova frase de acesso. É o PIN que você digitou quando ligou o dispositivo para esta sessão.

Agora você pode sair para o menu principal selecionando a opção voltar algumas vezes.

## Observando a Carteira

Em artigos anteriores, expliquei como baixar e verificar a carteira Sparrow e como conectá-la ao seu próprio nó ou a um nó público. Você deve seguir esses guias:

- Instale o Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Instale a Carteira Bitcoin Sparrow (https://armantheparman.com/download-sparrow/)

- Conecte a Carteira Bitcoin Sparrow ao Bitcoin Core (https://armantheparman.com/sparrowcore/)

Uma alternativa ao uso da Carteira Bitcoin Sparrow é a Carteira Desktop Electrum, mas prosseguirei explicando a Carteira Bitcoin Sparrow, pois considero que seja a melhor para a maioria das pessoas. Usuários avançados podem preferir usar o Electrum como alternativa.

Agora vamos carregá-la e conectar o Ledger, com a carteira contendo a frase de acesso. Esta carteira nunca foi exposta ao Ledger Live porque foi criada DEPOIS de conectarmos o dispositivo ao Ledger Live. Certifique-se de nunca mais conectá-la ao Ledger Live para não expor sua nova carteira privada.

Crie uma Nova Carteira:

![image](assets/14.webp)

Dê um nome bonito a ela

![image](assets/15.webp)

Observe a caixa de seleção "Tem transação existente". Se esta é uma carteira que você já usou antes, marque esta opção, caso contrário, seu saldo será exibido incorretamente como zero. Marcar esta caixa solicita ao Sparrow que examine o banco de dados do Bitcoin Core (o blockchain) em busca de transações anteriores. Para este guia, estamos usando uma carteira completamente nova, então você pode deixar a caixa desmarcada.

![image](assets/16.webp)

Clique em "Carteira de Hardware Conectada" e verifique se o dispositivo está realmente conectado, ligado, PIN inserido e se você inseriu o aplicativo Bitcoin.

![image](assets/17.webp)

Clique em "Digitalizar" e depois em "Importar Keystore" na próxima tela.

![image](assets/18.webp)

Não há nada para editar na próxima tela, o Ledger preencheu para você. Clique em "Aplicar"

![image](assets/19.webp)

A próxima tela permite que você adicione uma senha. Não confunda isso com "frase de acesso"; muitas pessoas fazem isso. A nomenclatura é infeliz. A senha permite que você bloqueie esta carteira em seu computador. É específica para este software neste computador. Não faz parte da sua chave privada do Bitcoin.

'![image](assets/20.webp)

Após uma pausa, enquanto o computador pensa, você verá os botões à esquerda mudarem de cinza para azul. Parabéns, sua carteira está pronta para uso. Faça e envie transações à vontade.

![image](assets/21.webp)

## Recebendo

Para receber alguns bitcoins, vá para a guia "Endereços" à esquerda e escolha um dos endereços para receber. Basta clicar com o botão direito no endereço desejado e selecionar "copiar endereço". Em seguida, vá para sua exchange de onde o dinheiro está sendo enviado e cole-o lá. Ou você pode fornecer o endereço a um cliente que possa usá-lo para pagar você.

Quando você usa a carteira pela primeira vez, você deve receber uma quantia muito pequena, pratique gastando-a para outro endereço, seja dentro da carteira ou de volta para a exchange, para provar que a carteira está funcionando conforme o esperado.

Depois de fazer isso, você deve fazer backup das palavras que você anotou. Uma única cópia não é suficiente. Tenha pelo menos duas cópias em papel (metal é melhor) e mantenha-as em dois locais diferentes e bem seguros. Isso reduz o risco de um desastre natural destruir sua HWW e o backup em papel em um único incidente. Veja "Usando Carteiras de Hardware Bitcoin" para uma discussão completa sobre isso.

## Enviando

![image](assets/22.webp)

Ao fazer um pagamento, você precisa colar o endereço para o qual está pagando no campo "Pagar para". Na verdade, você não pode deixar o campo "Rótulo" em branco, é apenas para os registros de suas próprias carteiras, mas o Sparrow não permite isso - apenas insira algo (apenas você verá). Insira o valor e você também pode ajustar manualmente a taxa desejada.

A carteira não pode assinar a transação a menos que a HWW esteja conectada. Essa é a função da HWW - receber a transação, assiná-la e devolvê-la, assinada. Certifique-se de que, ao assinar no dispositivo, você inspecione visualmente se o endereço para o qual está pagando é o mesmo no dispositivo e na tela do computador, e a fatura que você recebe (por exemplo, você pode ter recebido um e-mail para pagar um determinado endereço).

Também preste atenção que, se você escolher usar uma moeda que seja maior que o valor do pagamento, o restante será enviado de volta para um dos endereços de troco de suas carteiras. Algumas pessoas não sabiam disso e procuraram sua transação em uma blockchain pública e pensaram que alguns bitcoins foram enviados para o endereço de um atacante, mas na verdade era o próprio endereço de troco delas.

## Firmware

Para atualizar o firmware, você precisa se conectar ao Ledger Live. Se você quiser fazer isso, deve limpar o dispositivo primeiro e garantir que tenha suas palavras de backup e frase de acesso disponíveis para restaurar o dispositivo. A razão pela qual prefiro limpar o dispositivo primeiro é que você precisa conectar seu dispositivo ao Ledger Live para atualizar o firmware, e prefiro não expor sua nova carteira (aquela com a frase de acesso) ao Ledger Live, nunca. Eu simplesmente não confio que a Ledger não esteja extraindo minhas informações de chave pública do dispositivo quando me conecto ao Ledger Live. Eles afirmam que não, mas não posso verificar isso a menos que leia o código e entenda o hardware interno também.

## Conclusão

Este artigo mostrou como usar uma HWW Ledger de maneira mais segura e privada do que o anunciado - mas este artigo sozinho não é suficiente. Como eu disse no início, você deve combiná-lo com as informações fornecidas em "Usando Carteiras de Hardware Bitcoin".
Dicas:

Endereço Estático do Lightning: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/'


Para aprofundar este tema e reforçar a segurança da sua carteira num Ledger Nano com uma passphrase BIP39, convido-o a consultar este tutorial completo:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

