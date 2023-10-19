---
name: Tails

description: Instalar o Tails em um pendrive
---

_**Guia proposto por Hari Seldon como parte do Agora256**_

![image](assets/cover.jpeg)

Um sistema operacional portátil e amnésico que protege você contra vigilância e censura.

## Por que ter um pendrive com o Tails instalado?

O Tails (https://tails.boum.org/) é a maneira mais fácil de ter um computador seguro sempre à sua disposição, que não deixará rastros no computador em que você o utiliza.

Para usar o Tails, desligue o computador disponível (na casa dos seus pais, na casa dos seus amigos, em um café com internet...) e inicialize-o a partir do seu pendrive Tails, em vez do Windows, macOS ou Linux.

Depois disso, você terá um espaço de trabalho e comunicação independente do sistema operacional habitual e que nunca utiliza o disco rígido.

O Tails nunca escreve no disco rígido e usa apenas a memória RAM do computador para funcionar. Essa memória é completamente apagada quando o Tails é desligado, eliminando assim todas as possíveis evidências.

## Alguns casos concretos de uso

Para lhe dar ideias concretas sobre a importância de ter sempre um pendrive com o Tails, aqui está uma pequena lista não exaustiva compilada pela equipe do Agora256:

- Conectar-se à internet e ao Tor de forma não censurada e anônima para acessar sites sem deixar rastros;
- Abrir um PDF de um site suspeito;
- Testar o backup da sua chave privada de Bitcoin com a carteira Electrum;
- Usar uma suíte de escritório (LibreOffice) e trabalhar em um computador que não é seu;
- Dar os primeiros passos em um ambiente Linux para aprender a sair do mundo da Microsoft e da Apple.

## Como confiar no Tails?

Sempre há uma dose de confiança no uso de software, mas essa confiança não precisa ser cega. Uma ferramenta como o Tails deve tentar fornecer aos seus usuários meios de ser confiável. Para o Tails, isso significa:

- um código-fonte público: https://gitlab.tails.boum.org/;
- um projeto baseado em projetos renomados: Tor e Debian;
- downloads verificáveis e reproduzíveis;
- recomendações de várias pessoas e organizações.

## Guia de instalação e uso

Este guia de instalação tem como objetivo orientá-lo em cada etapa da instalação. Não descreveremos mais do que o guia oficial as ações a serem realizadas, mas apontaremos você na direção certa, fornecendo dicas e truques.

Por razões de experiência prática, essas dicas serão focadas nas plataformas macOS e Linux.
🛠️
Antes de iniciar este procedimento, certifique-se de ter um pen drive com velocidade de leitura de pelo menos 150 MB/s e capacidade de pelo menos 8 GB, idealmente do tipo USB 3.0.

Pré-requisitos

- 1 pen drive, apenas para o Tails, com pelo menos 8 GB
- Um computador conectado à internet com Linux, macOS (ou Windows)
- Aproximadamente uma hora disponível, dependendo da velocidade da sua conexão com a internet, sendo ½ hora para a instalação (arquivo para download de 1,3 GB)

## Passo 1: Baixar o Tails para o seu computador

![image](assets/1.jpeg)

> 🔗 Seção oficial do Tails: https://tails.boum.org/install/linux/index.fr.html#download

O download do arquivo de instalação com a extensão .img pode levar algum tempo, dependendo da velocidade da sua conexão de download, então planeje com antecedência. Com uma linha moderna e rápida, isso levará menos de 5 minutos.

Salve o arquivo em uma pasta conhecida, como "Downloads", pois isso será necessário para prosseguir para o próximo passo.

## Passo 2: Verificar o seu download

![image](assets/2.jpeg)

> 🔗 Seção oficial do Tails: https://tails.boum.org/install/linux/index.fr.html#verify

Verificar o download garante que ele tenha sido emitido pelos desenvolvedores do Tails e que não tenha sido corrompido ou interceptado durante o download.

É possível verificar manualmente se o arquivo que você acabou de baixar é o esperado usando PGP, mas sem conhecimento avançado, essa verificação oferece o mesmo nível de segurança que a verificação JavaScript na página de download, embora seja muito mais complicada e propensa a erros.

Portanto, use o botão "Selecionar seu download..." oferecido na seção oficial para verificar o arquivo!

## Passo 3: Instalar o Tails no seu pen drive

![image](assets/3.jpeg)

> 🔗 Seção oficial do Tails:
>
> - Linux: https://tails.boum.org/install/linux/index.fr.html#install
> - macOS: https://tails.boum.org/install/mac/index.fr.html#etcher e https://tails.boum.org/install/mac/index.fr.html#install

Esta etapa de instalação do Tails no seu pen drive é a mais difícil de todo o guia, especialmente se você nunca fez isso antes. O ponto mais importante é escolher corretamente o procedimento na seção oficial para o seu sistema operacional: Linux ou macOS.

Em seguida, uma vez que as ferramentas estejam instaladas e preparadas conforme recomendado, o arquivo com a extensão .img poderá ser copiado para o seu pen drive (apagando todos os dados existentes) para que ele seja inicializável independentemente.

Boa sorte! E vamos para o passo 4.

## Passo 4: Reinicie com o Tails no seu pen drive

![image](assets/4.jpeg)

> 🔗 Secção oficial do Tails: https://tails.boum.org/install/linux/index.fr.html#restart
> É hora de iniciar um dos seus computadores usando a sua nova pen USB. Insira-a numa das portas USB e reinicie!

> 💡 A maioria dos computadores não inicia automaticamente a partir da pen USB Tails, mas você pode pressionar a tecla do menu de arranque para exibir uma lista de dispositivos possíveis para iniciar a partir.

Descubra qual tecla você precisa pressionar para garantir que você tenha o menu de arranque que permite selecionar a pen USB em vez do seu disco rígido habitual, aqui está uma lista não exaustiva por fabricante:

| Fabricante | Tecla            |
| ---------- | ---------------- |
| Acer       | F12, F9, F2, Esc |
| Apple      | Option           |
| Asus       | Esc              |
| Clevo      | F7               |
| Dell       | F12              |
| Fujitsu    | F12, Esc         |
| HP         | F9               |
| Huawei     | F12              |
| Intel      | F10              |
| Lenovo     | F12              |
| MSI        | F11              |
| Samsung    | Esc, F12, F2     |
| Sony       | F11, Esc, F10    |
| Toshiba    | F12              |
| outros...  | F12, Esc         |

Depois de selecionar a pen USB, você deverá ver esta nova tela de arranque, é um bom sinal, então deixe o computador continuar a iniciar...

![imagem](assets/5.jpeg)

## Passo 5: Bem-vindo ao Tails!

![imagem](assets/6.jpeg)

> 🔗 Secção oficial do Tails: https://tails.boum.org/install/linux/index.fr.html#tails

Um ou dois minutos após o carregador de inicialização e a tela de carregamento, a Tela de boas-vindas aparece.

![imagem](assets/7.jpeg)

Na Tela de boas-vindas, selecione o seu idioma e layout de teclado na seção Idioma e Região. Clique em Iniciar o Tails.

![imagem](assets/8.jpeg)

Se o seu computador não estiver conectado à rede com fios, consulte as instruções oficiais do Tails para ajudá-lo a conectar-se à rede sem fio (seção "Teste a sua rede sem fio").

Depois de conectado à rede local, o Assistente de Conexão ao Tor aparece para ajudá-lo a se conectar à rede Tor.

![imagem](assets/9.jpeg)

Você pode começar a navegar anonimamente, explorar as opções e os softwares incluídos no Tails. Divirta-se, você tem total liberdade para cometer erros, pois nada é alterado na pen USB... O próximo reinício esquecerá todas as suas experiências!

## Num próximo guia...

Depois de ter experimentado um pouco mais com a sua própria pen USB Tails, exploraremos outros tópicos mais avançados num outro artigo, como:

> Atualizar uma chave com a versão mais recente do Tails; Configurar e usar armazenamento persistente; Instalar software adicional.
> Até lá, como sempre, se você tiver alguma dúvida, não hesite em compartilhá-la com a comunidade Agora256, estamos aprendendo juntos, para sermos melhores amanhã do que somos hoje!

> _**Guia proposto por Hari Seldon como parte do Agora256; post original: https://agora256.com/installer-tails-usb/**_
