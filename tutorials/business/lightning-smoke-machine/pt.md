---
name: Lightning Smoke Machine
description: Accione uma máquina de fumo com um pagamento Lightning através do ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Introdução



Transforma uma máquina de fumo clássica num dispositivo que pode ser pago em Bitcoin através de Lightning Network. Cada pagamento desencadeia automaticamente um jato de fumo!





- Nível: Intermediário
- Tempo estimado: 2-3 horas
- Casos de utilização: Eventos Bitcoin, actuações artísticas, demonstrações relâmpago, efeitos de palco automatizados



## Pré-requisitos



### Conhecimento





 - Eletrónica de base (cablagem, relés)
 - Soldadura (ou utilização de conectores Dupont)
 - Configuração de rede (WiFi, WebSocket)



### Contas necessárias





- Servidor BTCPay: Instância funcional (auto-hospedada ou hospedada)
- Blink Wallet : Conta + acesso API



### Acesso





- Acesso de administrador ao servidor BTCPay
- Ligação WiFi para o ESP32



## Materiais necessários



### Hardware - Componentes electrónicos





- 1 Microcontrolador - ESP32-WROOM-32


*O ESP32-WROOM-32 é um microcontrolador WiFi/Bluetooth compacto e de baixo custo para ligar dispositivos electrónicos à Internet e controlá-los remotamente*



![ESP32](assets/fr/1.webp)





- 1 Módulo de relé - 5V com optoacoplador


*Um relé é como um interrutor que o ESP32 pode acionar para ligar ou desligar a máquina de fumo*



![relay](assets/fr/2.webp)





- ~10 cabos Dupont - Macho/Macho e Macho/Fêmea



![dupont-cables](assets/fr/3.webp)





- 1 Fonte de alimentação para o ESP32 - USB de 5V ou bateria Li-Po



![battery](assets/fr/4.webp)





- 1 cabo micro-USB - ligação entre o ESP32 e a fonte de alimentação



![micro-usb-cables](assets/fr/5.webp)





- 1 máquina de nevoeiro de 220V com controlo remoto a pilhas de 12V



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 garrafa de líquido compatível com a sua máquina de fumo



### Hardware - Ferramentas





- Ferro de soldar + estanho (se estiver a soldar)
- Chave de fendas
- Multímetro (recomendado)



### Software





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Navegador Web compatível com WebSerial (Chrome/Edge/Brave)
- Servidor BTCPay configurado. Para obter mais informações sobre como criar uma instância do servidor BTCPay, visite este tutorial: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Arquitetura do sistema



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **AVISO DE SEGURANÇA - LER ANTES DE CONTINUAR** **⚠️**



Este projeto envolve uma máquina de nevoeiro ligada a uma fonte de alimentação de **220V**. Um funcionamento incorreto pode resultar em **eletrocussão fatal** ou **incêndio**.



**Regras não negociáveis:**



1. **Desligue SEMPRE a máquina de fumo da rede eléctrica** antes de abrir o controlo remoto ou de mexer na cablagem


2. **Retirar a pilha do telecomando** antes de a manusear (risco de curto-circuito e danos nos componentes)


3. **Verifique se todas as suas ligações estão isoladas** antes de voltar a ligar qualquer coisa


4. **Nunca volte a ligar a alimentação de 220V** até que a caixa de controlo remoto tenha sido fechada e fixada



Se não se sentir à vontade com este tipo de manuseamento, leve consigo alguém que esteja.



---

## PARTE 1: Montagem das ferragens



### Passo 1: Preparar o controlo remoto



Objetivo: Ligar o relé ao botão ON/OFF do controlo remoto


1. Abrir o controlo remoto




    - Identificar o botão ON/OFF
    - Desaparafusar a caixa para abrir o controlo remoto


2. Localizar as ligações




 - Localize os terminais + e - do
 - Teste a continuidade com um multímetro (opcional)



![smoke-machine-remote](assets/fr/8.webp)



3. Cablagem do botão (solda ou conectores)




    - Soldar um cabo preto ao terminal - do botão
    - Soldar um cabo vermelho ao terminal comum +



![smoke-machine-remote](assets/fr/9.webp)



### Passo 2: Ligação ao módulo relé



**Lembrete: Terminologia dos relés




| **Terminal**         | **Descrição**           | **Função**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normalmente Aberto)   | Circuito aberto por padrão | Fecha quando o relé é ativado |
| NC (Normalmente Fechado) | Circuito fechado por padrão  | Abre quando o relé é ativado  |
| COM (Comum)         | Terminal central          | Alterna entre NO e NC              |

**Cablagem do controlo remoto para o módulo de relé:**




- Fio preto do botão ON/OFF **→** NO (Normalmente aberto)
- Fio vermelho (comum) **→** COM (comum)



**Lógica:**


Quando o ESP32 ativa o relé, liga COM e NO, o que é exatamente o mesmo que premir o botão do controlo remoto.


Quando o ESP32 corta o relé, COM e NO separam-se, o que equivale a soltar o botão.



![remote-relay](assets/fr/10.webp)



### Passo 3: Ligar o ESP32 ao módulo relé



**Diagrama de cablagem




| **ESP32** | **→** | **Módulo de Relé** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Entrada)        |

**Verificação: **




- VCC e GND bem ligados (polaridade)
- GPIO 21 utilizado para sinal de controlo
- Sem curto-circuito visível



![relay-esp32](assets/fr/11.webp)



**Hardware de ponto de controlo


Antes de mudar para o software, verifique :




- Controlo remoto com cablagem correta
- Módulo de relé ligado ao ESP32
- Não há fios desencapados a tocar noutros componentes
- 220V sempre desligado



![relay-esp32](assets/fr/12.webp)





---


## PARTE 2: Configuração do software



Utilizaremos *Blink* como exemplo, mas *BTCPay Server* também oferece *Strike, Breez e Boltz* se preferir outra opção.



### Passo 1: Plugins, Instalação *BitcoinSwitch* + *Blink



1 - Aceda à sua instância *BTCPay Server* com uma conta de administrador



2 - Crie a sua primeira cortina



3 - No lado esquerdo do *BTCPay Server*, desloque-se para o fundo e vá para *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Vamos instalar os plugins *BitcoinSwitch* e *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Percorrer a lista de plugins e clicar em *"Install "* : *BitcoinSwitch e Blink* (ou o wallet disponível à sua escolha)



![btcpay-plugins](assets/fr/15.webp)



6 - Uma vez concluída a instalação, reinicie o *BTCPay Server* e aguarde 1 minuto para que a instância seja reiniciada



![btcpay-plugins](assets/fr/16.webp)



7 - Quando regressar a *"Manage plugins "*, verifique se ambos os plugins foram instalados



![btcpay-plugins](assets/fr/17.webp)



### Passo 2: Backend: *BTCPay Server + Blink* configuração



**1 - Criar um wallet *Blink***




- Visite https://www.blink.sv
- Criar a sua conta. Consulte o tutorial :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Gerar uma chave API *Blink***




- Aceder à interface do API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** e iniciar sessão com a mesma conta que utilizou para criar o seu wallet *Blink*



![blink-api](assets/fr/18.webp)





   - Uma vez ligado, aceda ao separador *API Keys* (Chaves API)



![blink-api](assets/fr/19.webp)





   - Clique em *" + "* no canto superior direito para aceder à configuração da sua chave API



![blink-api](assets/fr/20.webp)





   - Dê um nome à sua chave API e deixe as configurações padrão. Depois, no terceiro passo, anote a sua chave API - só a verá uma vez: `blink_mZ5KxxxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Uma vez criada, deverá aparecer na sua lista de chaves API activas.



![blink-api](assets/fr/22.webp)



**3 - Ligar *Blink* ao servidor *BTCPay***




- Abra o seu *BTCPay Server*
- Navegar para : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Clique em *Utilizar um nó personalizado*
- Colar a seguinte cadeia de ligação:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Importante** :




- Não modificar a primeira parte: `type=blink;server=https://api.blink.sv/graphql`;
- Substituir apenas :
    - api-key= *pela sua chave API Blink
    - wallet-id= *pelo seu wallet Blink* ID
- Em seguida, clique em *Testar ligação* e depois em *Guardar*



![btcpay-server](assets/fr/24.webp)





 - Verificar se a ligação está estabelecida (estado verde)



![btcpay-server](assets/fr/25.webp)



**4 - Criar um ponto de venda (PoS)




- Em BTCPay Server, aceda ao separador *Plugins* e clique em *Point of sale*



![btcpay-server](assets/fr/26.webp)





- Dê um nome ao seu PdS e clique em *Criar*



![btcpay-server](assets/fr/27.webp)





- Configuração do PoS :
    - Selecionar um estilo de ponto de venda = *Visor para impressão*
    - Moeda = *SATS*
    - Clique em *SAVE*



![btcpay-server](assets/fr/28.webp)





- Configuração do produto :
    - Eliminar todos os produtos predefinidos
    - Em seguida, clique em *adicionar item*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Configurar o produto:
    - Título : *máquina de fumo*
    - Preço : *10 sats*
    - Interruptor GPIO Bitcoin : 21
    - Duração da comutação do Bitcoin (em milissegundos) : 5000
    - Clique em *Fechar* e depois em *Guardar* para guardar o novo produto



![btcpay-server](assets/fr/31.webp)



### Passo 3: Firmware: Atualização do ESP32



**1 - Ir para o sítio flash




- Ir para : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash o firmware do BitcoinSwitch**




- Ligue o ESP32 ao seu computador com o seu cabo USB/Micro-USB
- Em seguida, clique em *Connect to Device* (Ligar ao dispositivo)
- Abre-se uma janela, selecione a porta USB do seu ESP32 e clique em *Connect* (Ligar)



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Quando o ESP32 estiver ligado, vamos fazer o flash do firmware do BitcoinSwitch. Na secção *T-Display*, clica em *Upload Firmware* para obteres a última versão disponível (atualmente: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Aguarde o carregamento, o processo estará concluído quando os registos mostrarem *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Desligue o ESP32



**3 - Verificar a instalação do firmware do BitcoinSwitch




- Recarregar a página: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Volte a ligar o ESP32 ao seu computador com o cabo USB/Micro-USB
- Em seguida, clique em *Ligar ao dispositivo
- Selecione a porta USB no seu ESP32 e clique em *Connect* (Ligar) como descrito acima
- Uma vez ligado, prima o botão **RESET** no ESP32
- Verifique nos registos se as últimas linhas mostram :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Isto é normal, significa que ainda não existe uma configuração, mas que o firmware foi instalado)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Gerar URL LNURL** do WebSocket



Formato final previsto :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Etapas de geração :




- Abra a sua instância do servidorBTCPay e, em seguida, vá para o PoS que criámos mais tarde.
- Em seguida, clique em "Ver" para abrir o seu PdS no browser



![btcpay-server-https](assets/fr/37.webp)





- Copie o URL da página, por exemplo :



![btcpay-server-https](assets/fr/38.webp)



Vamos desvendar este URL:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → o domínio da sua instância do servidor BTCPay
- `46XXXXXXXXXXXXXXXXXXXXwFB` → o seu identificador único do PdS
- `/pos` → indica um ponto de venda



Transformá-lo:




- Substituir `https://` por `wss://`
- Adicione `/bitcoinswitch` no final



Resultado:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Guarde este URL para configuração futura, pois ele permitirá que seu ESP32 se comunique em tempo real com o servidor BTCPay. O protocolo WebSocket (`wss://`) estabelece uma conexão permanente entre os dois: assim que um pagamento Lightning é confirmado em seu PoS, BTCPay envia instantaneamente a informação para o ESP32, que pode então acionar sua máquina de fumaça.



**5 - Configuração de WiFi e WebSocket




- Regressar à página: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) com o ESP32 ligado
- Ir para *Configurar dispositivo* → *Definições de Wi-Fi*



Informar :




- SSID WiFi: o nome da sua rede WiFi
- Palavra-passe WiFi: a sua palavra-passe WiFi



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Na secção *LNbits Device URL* (URL do dispositivo LNbits), cole o URL WebSocket criado no passo anterior
- Clique em *Upload config*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Aguarde que o carregamento seja concluído; os registos devem apresentar os parâmetros que acabou de introduzir (SSID, palavra-passe e URL WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Aguarde enquanto o ESP32 estabelece a ligação WebSocket. Deverá ver :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Pode agora desligar o ESP32



---
## Software Checkpoint



Antes do teste final, verificar :





- Blink ligado ao BTCPay
- PdV criado com pelo menos 1 item
- ESP32 flashed com BitcoinSwitch
- WiFi configurado no ESP32
- URL WebSocket correto
- Registos ESP32 sem erros



---

## Testes e depuração



### Completar o teste final



1. Ligar a máquina de fumos (220V) e ligá-la


2. Alimentar o ESP32 (bateria ou USB)


3. Abra o seu BTCPay PoS no seu navegador


4. Verificar o item "máquina de fumo


5. Pagar com um wallet Lightning (Blink ou outro wallet)


6. Observar:




 - O relé faz um clique (som audível e o LED do relé acende-se)
 - A máquina de fumo é activada
 - Fumo gerado!



### Problemas e soluções de equidade




| **Problema**                        | **Causa provável**              | **Solução**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 não se conecta            | Driver USB ausente             | Instale [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relé não clica                | Cabeamento GPIO incorreto            | Verifique GPIO 21 → IN                                                                        |
| Máquina de fumaça não responde         | Controle remoto mal cabeado         | Verifique NO/NC/COM                                                                           |
| Tempo limite do WebSocket                   | URL incorreta                  | Verifique wss:// e /bitcoinswitch                                                            |
| WiFi não se conecta             | SSID/Senha incorreto            | Reflash da config WiFi                                                                    |
| Pagamento recebido, mas nada acontece | ESP32 não conectado ao WebSocket | Verifique logs RESET                                                                      |

## Recursos



### Ligações úteis





- Firmware do BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Documentos do servidor BTCPay : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- Pinagem do ESP32 : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Comunidade e apoio





- Servidor BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Mattermost oficial
- Servidor BTCPay Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Telegram oficial, comunidade ativa
- BitcoinSwitch (erros de firmware)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Código fonte





- Código fonte do firmware do BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Empilhar sats, fazer fumo, divertir-se, manter-se humilde! **⚡**