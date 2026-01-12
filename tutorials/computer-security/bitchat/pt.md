---
name: Bitchat
description: Mensagens descentralizadas e sem Internet para uma comunicação livre
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Este tutorial em vídeo da BTC Sessions orienta-o no processo de configuração e utilização do Bitchat!


O Bitchat surgiu de um esforço de prototipagem rápida em que [@jack](https://primal.net/jack) desenvolveu o conceito inicial durante uma sessão de programação de fim de semana. [@calle](https://primal.net/calle) juntou-se ao projeto pouco tempo depois para co-desenvolver a implementação Android. Atualmente, Jack lidera o desenvolvimento da versão iOS, enquanto Calle supervisiona a versão Android com o apoio de muitos outros colaboradores.


## Introdução: Conversar livremente, sem a grelha


Imagine enviar mensagens quando a internet cai, durante um desastre natural ou em lugares onde a comunicação é restrita. O Bitchat torna isso possível. É uma aplicação de mensagens descentralizada e peer-to-peer que ignora os servidores centrais, permitindo que os dispositivos falem diretamente uns com os outros, totalmente offline, utilizando Bluetooth e redes em malha. Projetado com privacidade e resiliência em mente, o Bitchat é ideal para uso em áreas onde a conetividade tradicional não é confiável ou não está disponível - como durante cenários de desastre, em locais remotos ou para aqueles que procuram evitar a vigilância. Em sua essência, o Bitchat usa criptografia para garantir que cada mensagem seja criptografada de ponta a ponta, verificada e à prova de adulteração.


Neste tutorial, vamos mostrar como o Bitchat funciona e como pode utilizá-lo para uma comunicação verdadeiramente privada e pronta para ser utilizada offline.


## 🚀 Caraterísticas principais


O Bitchat permite o envio de mensagens offline através destas [funcionalidades](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Compatível com várias plataformas**: Compatibilidade total de protocolo entre iOS e Android.
- Rede em malha descentralizada**: Descoberta automática de pares e retransmissão de mensagens multi-hop através de Bluetooth Low Energy (BLE)
- Encriptação de ponta a ponta**: Troca de chaves X25519 + AES-256-GCM para mensagens privadas
- Chats baseados em canais**: Mensagens de grupo baseadas em tópicos com proteção opcional por palavra-passe
- Armazenar e encaminhar**: Mensagens armazenadas em cache para pares offline e entregues quando eles se reconectam
- Privacidade em primeiro lugar**: Sem contas, sem números de telefone, sem identificadores persistentes
- Comandos no estilo IRC: Interface familiar no estilo `/join, /msg, /who`.
- Retenção de mensagens**: Memorização opcional de mensagens em todo o canal controlada pelos proprietários do canal
- Limpeza de emergência**: Toque três vezes no logótipo para apagar instantaneamente todos os dados
- Interface de utilizador moderna para Android**: Jetpack Compose com Material Design 3
- Temas claros/escuros**: Estética inspirada no terminal que corresponde à versão iOS
- Otimização da bateria**: Varrimento adaptativo e gestão de energia


## 1️⃣ Como funciona o Bitchat - simplesmente


O Bitchat permite-lhe enviar mensagens para telefones próximos diretamente através de Bluetooth (`BLE` como se segue), sem necessidade de Internet ou sinal de telemóvel. Quando inicia uma conversa, os telefones executam um aperto de mão seguro para criar uma chave de encriptação única e temporária para a sua conversa. Todas as mensagens são protegidas com encriptação de ponta a ponta e é utilizada uma nova chave para cada uma delas, de modo a garantir que as mensagens anteriores permanecem seguras, mesmo que o telemóvel seja comprometido mais tarde. Por fim, a aplicação divide as mensagens em pequenos pedaços e mistura-os com dados fictícios aleatórios para ocultar a sua atividade de envio de mensagens. Para conversas diretas entre dispositivos, só funciona num raio de alcance de até ~100 m. É como passar notas encriptadas numa sala cheia de gente - os dispositivos sussurram diretamente uns aos outros, destruindo as chaves após cada mensagem.


O Bitchat também permite que você entre em salas de bate-papo baseadas em localização usando o protocolo Nostr e `#geohashes`. Um geohash é um código curto, como `#u33d`, que representa uma área geográfica específica, de um único bairro, até uma cidade ou região inteira. Você pode se `teleportar` para qualquer sala de bate-papo geohash ao redor do mundo simplesmente digitando sua tag. As suas mensagens são enviadas através de uma rede descentralizada de retransmissores, que protege a sua localização exacta. Além disso, cada vez que se junta a uma sala de geohash, é-lhe atribuída uma nova identidade temporária, acrescentando uma camada extra de privacidade às suas conversas baseadas na localização.


Para obter pormenores técnicos mais precisos, consulte o [Livro Branco oficial](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Instalação e configuração


### Onde comprar Bitchat


Pode instalar o Bitchat através de:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (para dispositivos iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (para dispositivos Android)


Os utilizadores do Android também têm opções alternativas:



- Baixe o APK diretamente da página [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) ou
- Instalar através da [Zapstore] compatível com Nostr (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Nota**: _Este tutorial centra-se principalmente na implementação do Android. A versão iOS pode ser diferente


### Processo de configuração


Após a instalação, abra o Bitchat para ver esta tela de permissões iniciais. Veja o que você precisa fazer:


1. **Conceder estas permissões necessárias:**


   - Acesso Bluetooth** (para descobrir utilizadores Bitchat próximos)
   - Localização exacta** (o Android requer isto para a funcionalidade Bluetooth)
   - Notificações** (para receber alertas de mensagens privadas)

2. **Desativar a otimização da bateria**:


   - Isso permite que o Bitchat seja executado em segundo plano
   - Mantém continuamente as ligações da rede em malha


Toque em `Grant Permissions` , siga as `prompts` e `Disable Battery Optimization` para passar ao ecrã seguinte.


![image](assets/en/02.webp)


Bem-vindo ao ecrã principal do Bitchat. Vamos orientar-nos:


### Definições


Primeiro as coisas mais importantes. O menu de definições pode ser aberto tocando no logótipo `Bitchat`.  Estão disponíveis as seguintes opções:



- Definir a `aparência` (sistema/claro/escuro).
- ativar `Proof of work` para geohash para dissuasão de spam (opcional)
- Ativar `Tor` para aumentar a privacidade.


![image](assets/en/16.webp)


### Definir a sua identidade


Toque no campo `bitchat/anonXXXX` na parte superior para escolher o seu nome de utilizador. É assim que os outros o verão nos modos Bluetooth e Internet. Por exemplo, podes alterar "anon2022" para um nome de utilizador à tua escolha.


![image](assets/en/03.webp)


### Selecionar canais de rede


Utilize o menu `#canais de localização` (à direita do nome de utilizador) para alternar entre os tipos de ligação:



- Malha BLE***: Modo Bluetooth predefinido (sem Internet, de 10 a 50 metros de alcance)
- #geohashes**: Comunidades geográficas activadas pela Internet utilizando o [protocolo Nostr](https://nostr.com/)


Quando você seleciona o modo `#geohashes`, o Bitchat integra-se com o protocolo Nostr para habilitar comunidades geográficas. Suas mensagens são publicadas para "retransmissores Nostr descentralizados" ao invés da rede peer-to-peer do Bitchat, permitindo conversas mais amplas, mas filtradas por localização. Crucialmente, suas chaves de identidade Bitchat assinam criptograficamente todos os eventos Nostr para manter a autenticação, enquanto tags geohash (como `#u4pruyd` para um bairro) filtram as mensagens para o nível de precisão escolhido. Isso significa que você pode participar de discussões locais sem revelar coordenadas exatas, embora seja necessário acesso à internet.


![image](assets/en/04.webp)


### Monitorizar os pares

licença: CC-BY-SA-V4

O contador de pares mostra os utilizadores:



- Nas proximidades (malha BLE) ou
- Na sua zona geohash (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Chat global e mensagens privadas


O Bitchat oferece dois modos de comunicação distintos para atender a diferentes necessidades:



- Canais públicos:** Para conversas abertas com outras pessoas. Pode ligar-se através da rede de malha BLE local para utilizadores próximos ou através de um #geohash global para comunidades com acesso à Internet e baseadas na localização.
- Mensagens privadas:** Para conversas seguras e individuais. Estas estabelecem uma ligação direta e encriptada para manter as suas trocas confidenciais.


A compreensão de ambos os modos ajudá-lo-á a navegar nas suas conversas.


### Canais públicos: O Centro Comunitário


O menu `#canais de localização` (canto superior direito) controla a sua visibilidade pública. A seleção de `mesh` liga-o a todos os utilizadores próximos através da malha BLE, normalmente dispositivos num raio de 10-50 metros. Isto cria um fórum aberto onde as mensagens são transmitidas a todos os que estão ao alcance, ideal para anúncios de eventos ou alertas locais.


Para um alcance geográfico mais alargado, escolha qualquer etiqueta `#geohash` para se juntar a comunidades com acesso à Internet filtradas por localização. Estes canais utilizam relés de protocolo Nostr, permitindo a comunicação entre cidades ou regiões, mantendo a relevância baseada na localização. As suas mensagens aparecem em direto para os outros no mesmo canal, com os novos participantes a verem automaticamente o histórico de mensagens recentes ao aderirem.


![image](assets/en/06.webp)


### Conversas privadas: Seguro e encriptado


Para iniciar uma conversa privada, toque uma vez diretamente em qualquer `nome de utilizador` apresentado em `Visão geral dos utilizadores`. Também pode tocar no `ícone de estrela` para marcar esse utilizador como favorito, o que o manterá visível na sua lista de contactos, mesmo quando estiver offline.


![image](assets/en/07.webp)


O Bitchat inicia automaticamente o seu "aperto de mão de segurança" quando se inicia uma conversa privada. Os dispositivos trocam chaves efémeras para criar um túnel encriptado especificamente para a sua conversa. Este processo garante que todas as suas mensagens e arquivos compartilhados permaneçam confidenciais graças à criptografia contínua de ponta a ponta. As mensagens privadas permitem a partilha de texto e de ficheiros.


![image](assets/en/08.webp)


## 4️⃣ Caraterísticas adicionais


Você pode acessar o painel de ações instantaneamente digitando `/` em qualquer lugar no Bitchat. Isto revela um menu de comandos para ações rápidas.



- Gerir ligações**: `Bloquear utilizadores` ou `Desbloquear pares`
- Controlos de canais**: `Mostrar canais` ou `Entrar/criar canal`
- Interações sociais**: `Mandar um abraço caloroso` ou `dar uma palmada com a truta` 🎣
- Manutenção do chat**: `Limpar mensagens do chat`
- Ferramentas de privacidade**: `Ver quem está online` ou `Enviar mensagem privada`


Os comandos são executados imediatamente - como `/block Satoshi` para silenciar os críticos ou `/hug Hal` para espalhar positividade 🫂.


![image](assets/en/09.webp)


## 5️⃣ Criar um canal


Os canais no Bitchat permitem a comunicação organizada em torno de tópicos, locais ou comunidades. Para criar o seu próprio canal, siga este fluxo de trabalho:


### Passo 1: Criar um canal


Para criar um canal, digite `/j` ou `/join` seguido do `nome do canal` em qualquer chat (por exemplo, `/j <nome do canal>`). Após a criação, um novo `ícone ⧉` aparece indicando o novo canal. Outros usuários podem entrar digitando o mesmo comando (por exemplo, `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Passo 2: Configurar as definições


Para além dos comandos predefinidos, estão disponíveis as seguintes definições num canal:



- `/save` para guardar mensagens localmente
- `/transfer` para transferir a propriedade do canal e
- `/pass` para alterar a palavra-passe do canal.


Para comunidades privadas, este comando ativa a proteção por palavra-passe, exigindo que os membros aprovados introduzam uma palavra-passe personalizada antes de aderirem.


## 6️⃣ Modo de pânico


Agora, vamos falar sobre o "modo de pânico": tocar três vezes no "logótipo Bitchat" inicia uma limpeza completa de todas as mensagens e dados locais dentro da aplicação. Esta é a tua derradeira salvaguarda de privacidade, perfeita para situações que exijam discrição imediata.


**Lembrete importante:** _O modo Pânico é permanente. Uma vez ativado, os dados não podem ser recuperados. Utilizar com precaução


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Os canais Geohash permitem conversas direcionadas com base em "localizações geográficas" em vez de ligações de rede tradicionais. Esta caraterística transforma o bitchat numa ferramenta de comunicação com conhecimento de localização, ideal para coordenação local, construção de comunidades e discussões específicas de localização.


### Como funcionam os `#geohashes


O sistema divide o mundo em quadrados de grelha utilizando o [sistema Geohash](https://en.wikipedia.org/wiki/Geohash), em que cada carácter no hash representa uma maior precisão:



- Nível 4** (por exemplo, `u33d`): Cobre aproximadamente 25km × 25km - ideal para discussões em toda a cidade
- Nível 6** (por exemplo, `u33d8z`): Cobre cerca de 1,2 km × 1,2 km - precisão de vizinhança
- Nível 8** (por exemplo, `u33d8z1k`): Cobre cerca de 150 m × 150 m - precisão do segmento de rua


A seleção de precisão equilibra a privacidade com a utilidade: níveis mais elevados criam zonas mais exclusivas, mas revelam a sua localização com maior precisão.


### Juntar-se a canais `#geohash


1. Aceder ao menu `#canais de localização`.

2. Selecione o nível de precisão pretendido e introduza o `#geohash` (por exemplo, #u33d)

3. Toque no botão `Teleportar` para se juntar ao `#canal de localização`.


![image](assets/en/12.webp)


Em alternativa, pode tocar no `ícone de mapa` para utilizar a vista de mapa para determinar o nível de precisão e tocar em `selecionar` para entrar no `canal de localização`.


![image](assets/en/13.webp)


**Lembrete importante**: a funcionalidade _#geohash requer uma ligação ativa à Internet - ao contrário da malha BLE que funciona offline através de Bluetooth


## 8️⃣ Heatmaps


Os mapas de calor são uma forma interessante de descobrir eventos e canais do Bitchat em todo o mundo. o [Bitmap](https://bitmap.lat/) visualiza e rastreia mensagens anónimas e baseadas na localização através da rede Nostr, apresentando eventos efémeros da Nostr. Dá uma vista de olhos e junta-te a canais e chats específicos do local.


![image](assets/en/15.webp)


## 🎯 Conclusão


O Bitchat permite uma comunicação segura e descentralizada para cenários onde as mensagens tradicionais falham. É capaz de operar sem infraestrutura de internet usando a rede de malha BLE, tornando-a adequada para protestos, zonas de desastre e áreas remotas onde a conetividade é limitada ou censurada. A aplicação garante a privacidade através de encriptação de chave efémera, canais de localização baseados em geohash e um apagamento de dados em modo de pânico.


A aplicação ainda está na fase inicial de desenvolvimento, mas já se mostra promissora. Os utilizadores devem esperar bugs ocasionais e reportar problemas através do [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Estão previstas melhorias, incluindo a integração do `ecash` para transacções privadas na aplicação utilizando o protocolo Cashu.


![image](assets/en/14.webp)


## 📚 Recursos Bitchat


[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)