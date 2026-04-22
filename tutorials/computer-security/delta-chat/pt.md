---
name: Delta Chat
description: Guia prático para uma ferramenta de mensagens descentralizada
---

![image](assets/cover.webp)




## Introdução - Controlo da conversação e privacidade



Nos últimos anos, tem-se falado cada vez mais do Chat Control, uma proposta de regulamentação que visa introduzir o controlo automático das mensagens privadas nas principais plataformas de comunicação. O objetivo declarado é combater os conteúdos ilegais, mas o problema é que este mecanismo implicaria, de facto, uma vigilância em massa, pondo em causa a encriptação de ponta a ponta e, consequentemente, a privacidade de todos os utilizadores, e não apenas dos infractores.



O verdadeiro risco é que os chats se tornem ambientes controlados, onde cada mensagem, imagem ou anexo pode ser analisado antes mesmo de chegar ao destinatário. E é aqui que entra uma possível solução: afastar-se das plataformas centralizadas e optar por sistemas de mensagens descentralizados, que não dependem de um único fornecedor e não podem ser facilmente sujeitos a este tipo de escrutínio.



Uma dessas soluções será apresentada neste tutorial: Delta Chat. Uma ferramenta madura e já utilizável.




## Porquê o Delta Chat e como funciona



O Delta Chat é uma solução de mensagens já muito boa para utilização quotidiana: muito útil para falar com amigos, familiares e outras pessoas, tal como um verdadeiro equivalente do WhatsApp.



É um sistema de mensagens descentralizado baseado inteiramente no correio eletrónico. Basicamente, aproveita a infraestrutura do correio eletrónico tradicional, mas constrói uma interface e uma experiência modernas de mensagens instantâneas em cima dela. À primeira vista, isto pode parecer um pouco improvisado, mas na verdade funciona muito bem e é surpreendentemente robusto. Pode utilizar servidores de correio dedicados chamados ChatMail, mas também pode funcionar sem problemas com servidores de correio normais. Isto significa que pode iniciar sessão com uma conta existente, se quiser, sem ter de criar nada de novo.



Outro destaque é o suporte para WebXDCs, que são pequenas aplicações Web que podem ser utilizadas diretamente nos chats, à semelhança das mini-aplicações do Telegram. A diferença importante é que estas aplicações não têm acesso à Internet, pelo que não podem seguir o utilizador ou enviar dados para o exterior.



Do ponto de vista da segurança, o Delta Chat utiliza encriptação verificada de ponta a ponta, baseada no PGP mas com extensões modernas que o tornam comparável em termos de nível de proteção ao Signal. A única falta atual é o Perfect Forward Secrecy, mas esse é um aspeto em evolução.



Como se baseia apenas no correio eletrónico, o Delta Chat evita-o completamente:




- números de telefone obrigatórios
- IDs centralizados
- registos ligados a um único serviço



E é isso que torna esta ferramenta muito resistente a regulamentos invasivos como o Chat Control.




## Instalação



A partir do site oficial do [Delta Chat] (https://delta.chat/download) pode ir para a secção Download. No Linux está convenientemente disponível através do Flathub, mas também existem pacotes para Arch, NixOS, Snap e versões autónomas.



![image](assets/it/01.webp)



Também está disponível para:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store] (https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- e outras lojas...



Se está à procura de um guia para instalar o F-Droid, este tutorial pode ajudá-lo:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Um aspeto muito importante: as versões para computador não requerem um telemóvel. Ao contrário do WhatsApp ou do SimpleX Chat, não é necessário registar-se primeiro no telemóvel. Pode criar o seu perfil diretamente no PC ou transferi-lo de outro dispositivo.




## Criação de perfil



Quando a aplicação é aberta, o Delta Chat pergunta se pretende criar um novo perfil ou utilizar um já existente.



![image](assets/it/02.webp)



Ao criar um novo perfil, pode introduzir:




- um nome
- uma imagem (opcional)



Um servidor ChatMail é proposto por defeito, mas é possível:




- escolher outro servidor ChatMail
- utilizar uma conta de correio eletrónico clássica
- configurar manualmente o IMAP e o SMTP
- registar-se utilizando o código de convite de outro utilizador



Após alguns segundos, o perfil está pronto e pode começar a utilizar a aplicação.



![image](assets/it/03.webp)




## Interface e chat



A interface é muito simples e direta:




- Mensagens do dispositivo, que são comunicações locais
- Mensagens guardadas, semelhantes às do Telegram e sincronizáveis entre dispositivos



![image](assets/it/04.webp)



Para adicionar um contacto, basta:




- Mostrar o seu código QR
- Verificar o telemóvel da outra pessoa
- Convidar através de uma ligação (partilhar a ligação do convite).



![image](assets/it/05.webp)



Quando a ligação é estabelecida, a encriptação de ponta a ponta é automaticamente configurada. A interface de utilizador do chat é muito semelhante à do WhatsApp:




- mensagens de texto e de voz
- fotografias, vídeos e ficheiros
- respostas às mensagens
- reacções
- mensagens pop-up
- notificações personalizáveis.



![image](assets/it/06.webp)



## WebXDC: aplicações em chats:



O Delta Chat permite a utilização de WebXDC, ou seja, pequenas aplicações incorporadas nas conversas. Segue-se uma pequena lista das mais úteis identificadas:




- inquéritos
- pranchetas de desenho
- conversas privadas temporárias
- jogos com pontuações de conversação partilhadas



Também é possível iniciar jogos mais complexos, o que demonstra a flexibilidade desta ferramenta.



![image](assets/it/07.webp)



## Grupos, canais e funcionalidades avançadas



É possível criar grupos, utilizar autocolantes (especialmente nos computadores de secretária) e, activando as opções experimentais, até canais, semelhantes aos do Telegram.



Nas definições avançadas, pode ativar:




- chamadas de voz (ainda experimental)
- gestão avançada de perfis de correio eletrónico
- cópias de segurança completas.



![image](assets/it/08.webp)



## Multidispositivo e cópia de segurança



O Delta Chat é totalmente compatível com vários dispositivos:




- pode adicionar um segundo dispositivo através do código QR
- pode efetuar uma transferência completa através da cópia de segurança.



Em segundos, encontrará novamente as suas conversas, grupos e histórico completo, sem depender de um servidor central.



![image](assets/it/09.webp)




## Conclusão



Numa altura em que se fala cada vez mais do controlo das comunicações privadas, Delta Chat representa uma resposta concreta: mensagens descentralizadas e encriptadas que podem ser verdadeiramente utilizadas todos os dias.



É a solução que, de todas as que experimentei, mais me convenceu pela simplicidade, privacidade e liberdade. Se quiser, pode também contactar-me no Delta Chat através do seguinte [link de convite](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Se gostou deste guia, pode apoiar-me fazendo um donativo e deixando um polegar para cima. E lembre-se: somente usando e explorando o Delta Chat tanto no celular quanto no computador é que você realmente descobrirá toda a sua funcionalidade.



Até à próxima vez.