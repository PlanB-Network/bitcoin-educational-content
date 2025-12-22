---
name: BIP47 - PayNym
description: Utilizar um código de pagamento reutilizável na Ashigaru
---
![cover](assets/cover.webp)



O pior erro de privacidade que se pode cometer no Bitcoin é a reutilização de endereços. Sempre que o mesmo endereço recebe vários pagamentos, estas transacções são ligadas entre si, fornecendo ao mundo um mapa das suas transacções. Por conseguinte, recomenda-se vivamente que utilize sempre no generate um endereço único para cada recibo. Mas para algumas aplicações Bitcoin, isto não é simples.



O BIP47, proposto por Justus Ranvier em 2015, dá uma resposta elegante a este problema. Introduz o conceito de um **código de pagamento reutilizável**: um identificador único que permite receber um número virtualmente ilimitado de pagamentos de bitcoin na cadeia, sem nunca reutilizar um endereço. Graças a um mecanismo criptográfico baseado numa troca ECDH (*Diffie-Hellman em curvas elípticas*), cada pagamento para o mesmo código resulta num endereço em branco, específico da relação entre o remetente e o destinatário.



![Image](assets/fr/01.webp)



Este princípio BIP47 é implementado em particular pelo **PayNym**, o sistema originalmente desenvolvido pelo Samourai Wallet e agora retomado pela Ashigaru. Neste tutorial, veremos como ativar o seu PayNym, trocar códigos de pagamento com um correspondente e efetuar transacções sem reutilizar um endereço.



Não vou entrar aqui em pormenores sobre o funcionamento do BIP47. Se quiser aprofundar o assunto, consulte o capítulo 6.6 do meu curso de formação BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Pré-requisitos



Para seguir este tutorial, só precisa de um wallet na aplicação Ashigaru. Se não sabe como descarregar, verificar, instalar a aplicação ou criar um wallet, recomendo que consulte primeiro este tutorial:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Solicitar PayNym



O primeiro passo é reclamar o seu PayNym. Esta operação só tem de ser efectuada uma vez por wallet. Ela associa o seu código de pagamento BIP47 derivado do seu seed (`PM...`) a um identificador único específico da implementação do PayNym. Este identificador mais curto e mais legível pode então ser transmitido aos seus correspondentes para facilitar as trocas, sem ter de partilhar o código BIP47 longo e completo.



Para o fazer, clique na sua imagem PayNym no canto superior esquerdo da interface, depois no seu código de pagamento `PM...`.



![Image](assets/fr/02.webp)



Em seguida, clique nos três pequenos pontos no canto superior direito e selecione `Claim PayNym`.



![Image](assets/fr/03.webp)



Confirmar clicando no botão "RECLAMAR O SEU PAYNYM".



![Image](assets/fr/04.webp)



Actualize a página: o seu ID PayNym é agora apresentado por baixo da sua imagem, mesmo por cima do seu código de pagamento BIP47.



![Image](assets/fr/05.webp)



O seu PayNym está agora ativo e pronto a ser utilizado para as suas primeiras transacções BIP47.



## Ligar a um contacto



Existem dois tipos de ligação entre PayNym: **follow** e **connect**. A operação `follow` é completamente gratuita. Estabelece uma ligação entre dois PayNym através do Soroban, um protocolo de comunicação encriptado baseado no Tor, desenvolvido pela equipa Samourai e adotado pela Ashigaru. Esta ligação permite que dois utilizadores que se seguem troquem informações de forma privada, em particular para coordenar transacções colaborativas como Stowaway ou StonewallX2, que veremos num outro tutorial. Esta etapa é específica do PayNym e não faz parte do protocolo BIP47.



![Image](assets/fr/06.webp)



A operação de ligação (`connect`), por outro lado, exige uma transação on-chain. Consiste em efetuar uma transação de notificação tal como definida na BIP47. Esta transação Bitcoin contém metadados num output `OP_RETURN`, que estabelece um canal de comunicação encriptado entre o pagador e o destinatário. A partir deste canal, o pagador poderá generate endereços de receção únicos para cada pagamento, e o destinatário será notificado destes pagamentos e poderá generate as chaves privadas associadas aos endereços para gastar estes fundos mais tarde.



Esta transação de notificação tem um custo: a taxa mining e o 546 sats enviado para o endereço de notificação do destinatário para assinalar a ligação. Uma vez estabelecida a ligação, pode ser efectuado um número quase infinito de pagamentos via BIP47.



Em poucas palavras:




- follow": gratuito, estabelece comunicação encriptada via Soroban, útil para as ferramentas de colaboração do Ashigaru;
- `Connect`: a pagar, efectua a operação de notificação BIP47 para ativar o canal entre o pagador e o destinatário.



Para interagir com um PayNym, é necessário primeiro *segui-lo*. Esta é a primeira etapa antes de estabelecer uma ligação BIP47. Digamos que pretende enviar pagamentos recorrentes para a PayNym `+instinctiveoffer10`.



Vai à tua página PayNym no Ashigaru, depois clica no botão `+` no canto inferior direito da interface.



![Image](assets/fr/07.webp)



Pode então colar o código de pagamento completo do destinatário ou ler o seu código QR.



![Image](assets/fr/08.webp)



Se só tiver o seu ID PayNym, vá a [Paynym.rs](https://paynym.rs/) para encontrar o código QR associado ao seu código de pagamento.



![Image](assets/fr/09.webp)



Depois de ter digitalizado o código QR, clique no botão "SEGUIR" para seguir o PayNym.



![Image](assets/fr/10.webp)



A ação `FOLLOW` é suficiente para as transacções de colaboração (*cahoots*). No entanto, para enviar pagamentos BIP47, é necessário estabelecer uma ligação: clique em `CONNECT` para efetuar a transação de notificação.



![Image](assets/fr/11.webp)



A transação de notificação é então difundida na rede. Aguarde até que haja pelo menos uma confirmação antes de efetuar o seu primeiro pagamento.



![Image](assets/fr/12.webp)



## Efetuar um pagamento BIP47



Está agora ligado ao destinatário e pode enviar um pagamento para um endereço único, gerado automaticamente utilizando o protocolo BIP47, sem qualquer troca prévia com o destinatário.



Na página principal do PayNym, clique no contacto a quem pretende enviar um pagamento.



![Image](assets/fr/13.webp)



No canto superior direito da interface, clique no ícone de seta.



![Image](assets/fr/14.webp)



Introduzir o montante a enviar. Não é necessário introduzir um endereço de receção: este será automaticamente obtido através do protocolo BIP47.



![Image](assets/fr/15.webp)



Verifique cuidadosamente os detalhes da transação, incluindo as taxas, e depois arraste a seta verde na parte inferior do ecrã para assinar e transmitir a transação.



![Image](assets/fr/16.webp)



A transação foi enviada.



![Image](assets/fr/17.webp)



Neste exemplo, o pagamento foi efectuado para outra das minhas carteiras PayNym. Por conseguinte, posso ver que chegou à minha outra Ashigaru wallet, sem que tenha sido trocado qualquer endereço manualmente: apenas foi utilizado o identificador PayNym.



![Image](assets/fr/18.webp)



Já sabe como utilizar os códigos de pagamento reutilizáveis BIP47 graças à implementação PayNym na aplicação Ashigaru. Pode agora partilhar este código de pagamento com qualquer pessoa que queira enviar-lhe pagamentos (especialmente pagamentos recorrentes). Pode também publicar o seu ID PayNym no seu sítio Web ou nas redes sociais para receber donativos.



Para aprofundar os seus conhecimentos sobre este protocolo, compreender em pormenor o seu funcionamento e as suas implicações em termos de confidencialidade, recomendo vivamente que frequente o meu curso BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c