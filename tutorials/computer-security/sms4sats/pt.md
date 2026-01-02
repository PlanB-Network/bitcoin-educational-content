---
name: SMS4Sats
description: Receber e enviar SMS de forma anónima pagando em Bitcoin Lightning
---

![cover](assets/cover.webp)



A verificação por SMS tornou-se uma necessidade para muitos serviços em linha. Quer seja para criar uma conta numa plataforma, validar um registo ou confirmar uma identidade, os sítios Web exigem quase sistematicamente um número de telefone. Esta prática generalizada coloca um grande problema para quem deseja preservar a sua privacidade: o seu número pessoal torna-se um identificador permanente, ligando as suas várias actividades digitais à sua identidade real e abrindo a porta a solicitações comerciais indesejadas.



*o *SMS4Sats** responde a este problema oferecendo números de telefone temporários para receber e enviar mensagens SMS. O serviço distingue-se pelo seu modelo sem registo e pelo pagamento exclusivo do Bitcoin através do Lightning Network. Por alguns satoshis, o utilizador obtém um número descartável que lhe permite validar um registo sem nunca revelar o seu número pessoal.



Este tutorial guia-o através das três funcionalidades do SMS4Sats: receber um SMS de verificação, enviar um SMS anónimo e alugar um número temporário durante várias horas.



## O que é o SMS4Sats?



O SMS4Sats é um serviço em linha, acessível em [sms4sats.com](https://sms4sats.com), que permite a gestão anónima de SMS mediante pagamento em Bitcoin Lightning. O serviço oferece três funcionalidades distintas: a receção de códigos de verificação de utilização única, o envio de SMS para qualquer número e o aluguer de números temporários durante várias horas.



### Filosofia e modelo de funcionamento



O projeto foi concebido para garantir a máxima confidencialidade e soberania financeira. Ao não exigir a criação de uma conta e ao aceitar apenas pagamentos Bitcoin Lightning, o SMS4Sats elimina completamente a necessidade de fornecer dados pessoais. Não é necessário nenhum endereço de correio eletrónico, nenhum cartão de crédito, nenhuma informação pessoal. Apenas o pagamento Lightning é necessário para aceder aos serviços.



O serviço suporta mais de 400 sítios e aplicações em cerca de 120 países, cobrindo a maioria das necessidades comuns de verificação. Esta vasta cobertura geográfica permite a validação de registos numa variedade de plataformas, desde redes sociais a serviços de mensagens.



### Modelo de pagamento condicional



O SMS4Sats utiliza facturas relâmpago condicionais (facturas hodl) para a sua funcionalidade de receção de SMS. Este mecanismo garante que só é cobrado se o SMS for efetivamente recebido. Se nenhuma mensagem chegar dentro do tempo previsto (20 minutos no máximo), o pagamento é automaticamente anulado e os satoshis são devolvidos ao seu wallet. Esta garantia não se aplica às funcionalidades de envio e de aluguer, que não são reembolsáveis.



## As três caraterísticas do SMS4Sats



A interface do SMS4Sats está organizada em torno de três separadores que correspondem a três utilizações distintas: **RECEBER** para receber códigos de verificação, **ENVIAR** para enviar SMS anónimos e **ALUGAR** para alugar um número temporário.



### Receber um SMS



A principal caraterística permite-lhe obter um número temporário para receber um código de verificação único. Depois de o código ter sido recebido e utilizado, o número é desativado permanentemente.



### Enviar um SMS



Esta funcionalidade permite-lhe enviar um SMS para qualquer número de telefone sem revelar a sua identidade. O destinatário receberá a mensagem de um número anónimo.



### Alugar um ato



Para os utilizadores que necessitam de receber várias mensagens SMS num único número, a SMS4Sats oferece uma opção de aluguer temporário. Esta opção permite-lhe receber e enviar várias mensagens durante o período de aluguer.



**Nota sobre os preços** : Os preços apresentados neste tutorial são indicativos. Variam consoante o país do número, o serviço de destino e a procura atual. Por exemplo, um SMS para Telegram França pode custar entre 1.500 e 5.000 satoshis, consoante as condições. Verifique sempre o montante exato da fatura Lightning antes de efetuar o pagamento.



## Receber um SMS de verificação



Vejamos em pormenor como utilizar o SMS4Sats para receber um código de verificação, ilustrado pela criação de uma conta Telegram.



### Passo 1: Selecionar o país e o serviço



Aceder a [sms4sats.com] (https://sms4sats.com) e permanecer no separador **RECEIVE**. Selecione o país do número pretendido no menu pendente. Se o serviço alvo da sua assinatura estiver listado, selecione-o para otimizar as hipóteses de receção.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



Neste exemplo, seleccionamos França como o país e Telegram como o serviço de destino. Clique em **NEXT** para avançar para o passo seguinte.



### Passo 2: Pagar a fatura Lightning



É apresentada uma fatura relâmpago sob a forma de um código QR. O valor varia de acordo com o país e o serviço selecionado. Digitalize o código QR com seu Lightning wallet ou copie a fatura para pagar manualmente.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Repare na mensagem importante: "Sem código SMS = Sem pagamento". Se não receber um SMS, o seu pagamento será automaticamente anulado e reembolsado num prazo máximo de 20 minutos.



### Passo 3: Obter o número temporário



Após a confirmação do pagamento, o número de telefone temporário é imediatamente apresentado. Um contador indica o tempo que falta para receber o SMS.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Copie este número (aqui +33 7 74 70 09 66) para o utilizar no serviço em que pretende inscrever-se.



### Passo 4: Utilizar o número no serviço de destino



Introduza o número temporário na aplicação ou no sítio Web onde criou a sua conta. No nosso exemplo Telegram, introduza o número, confirme-o e aguarde pelo código de verificação.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



O processo é idêntico ao do registo convencional: introduz-se o número, o Telegram envia um código de verificação por SMS e, em seguida, finaliza-se a criação da conta.



### Passo 5: Recuperar o código de verificação



Regressar à interface SMS4Sats. Assim que o SMS for recebido, o código de ativação é automaticamente apresentado. Clique em **COPY CODE** para o copiar facilmente.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Introduza este código no serviço de destino para finalizar o seu registo. O número temporário é então desativado de forma permanente.



## Enviar um SMS anónimo



O SMS4Sats também lhe permite enviar mensagens SMS para qualquer número sem revelar a sua identidade.



### Passo 1: Escrever a mensagem



Clique no separador **ENVIAR**. Introduza o número de telefone de destino com o respetivo código de marcação internacional e escreva a sua mensagem (máximo de 1600 caracteres).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Clique em **NEXT** para proceder ao pagamento.



### Passo 2: Pagar e enviar



Pagar a fatura relâmpago apresentada. Uma vez confirmado o pagamento, o SMS é enviado imediatamente para o destinatário.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



É apresentado um código de confirmação para confirmar que a mensagem foi enviada. O destinatário receberá o SMS de um número anónimo.



## Alugar um número temporário



Para utilizações que exijam várias mensagens SMS no mesmo número, a função ALUGAR permite-lhe alugar um número durante várias horas.



### Configuração do aluguer



Clique no separador **RENT**. Selecione o país e a duração.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Pontos importantes a ter em conta




- Os preços variam consoante o país e a duração da estadia
- Os alugueres não são reembolsáveis**, ao contrário das mensagens SMS de utilização única
- Os números alugados geralmente não funcionam com o Telegram
- Esta opção é adequada para a subscrição de vários serviços em sucessão



Depois de ter clicado em **SEGUINTE** e pago a fatura Lightning, receberá um número que poderá utilizar durante o período de aluguer para receber e enviar mensagens SMS.



## Vantagens e limitações



### Destaques



**Não são necessários dados pessoais**: O modelo de não registo garante que não são recolhidas informações pessoais.



**Três funções adicionais**: Receber, enviar e alugar cobrem a maioria das necessidades.



**Pagamento apenas em Bitcoin** : O Lightning Network permite transacções instantâneas e pseudónimas.



**Reembolso automático**: Ao receber mensagens SMS, o sistema de facturas hodl garante que só paga se a SMS chegar.



### Restrições a considerar



**Segurança relativa do canal SMS**: Os códigos SMS não são um método de autenticação robusto e não devem ser utilizados para contas sensíveis.



**Compatibilidade variável**: Muitos sítios detectam e bloqueiam números virtuais. Podem ser necessárias várias tentativas.



**Números não reutilizáveis**: Após uma única utilização, o número é reciclado e não pode ser recuperado.



**Alugueres não reembolsáveis**: Ao contrário das mensagens SMS únicas, os alugueres não têm garantia de devolução do dinheiro.



## Melhores práticas



### Utilize o Tor para obter mais privacidade



O SMS4Sats é acessível via [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Esta configuração oculta o seu endereço IP quando acede ao serviço.



### Evitar contas críticas



Nunca utilize um número descartável para as suas contas importantes (banco, correio eletrónico principal). Se estas plataformas exigirem a revalidação do seu número numa data posterior, perderá o acesso à conta.



### Separe as suas identidades digitais



Para contas pseudónimas, combine o número temporário com um endereço de correio eletrónico descartável e um browser isolado da sua utilização habitual.



### Escolha um 2FA robusto



Uma vez criada a sua conta, active soluções de autenticação mais fortes: Aplicação TOTP (Aegis, Ente Auth) ou chave de segurança física FIDO2.



## Conclusão



O SMS4Sats é uma solução completa para a gestão de SMS confidenciais. Quer pretenda receber um código de verificação, enviar uma mensagem anónima ou alugar um número temporário, o serviço responde a uma vasta gama de necessidades de confidencialidade, graças ao pagamento em Bitcoin Lightning.



No entanto, é preciso ter em conta as suas limitações: o serviço não garante o anonimato absoluto e não é adequado para contas sensíveis ou de longa duração. Utilizado de forma sensata e consciente das suas limitações, o SMS4Sats é uma ferramenta prática para recuperar o controlo sobre as suas comunicações telefónicas.



## Recursos





- [Sítio Web oficial do SMS4Sats](https://sms4sats.com)
- [FAQ do serviço] (https://sms4sats.com/faq)
- [Endereço do Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)