---
name: Configurando um BitAxe
Description: Como configurar um BitAxe?
---

### Introdução

BitAxe é um projeto de código aberto criado por Skot e [disponível no GitHub](https://github.com/skot/bitaxe) que permite a experimentação de mineração de forma custo-efetiva.

Ele desvendou o funcionamento do famoso Antminer S19 da Bitmain, líder de mercado em ASICs, as máquinas especializadas para mineração de bitcoin. Agora, é possível usar esses poderosos chips em novos projetos de código aberto. Diferentemente do Nerdminer, o BitAxe possui poder computacional suficiente para ser conectado a um pool de mineração, o que permitirá que você ganhe regularmente alguns satoshis. O Nerdminer, por outro lado, só pode ser conectado ao que é chamado de solopool, que funciona como um bilhete de loteria: você tem uma pequena chance de ganhar a recompensa completa do bloco.

Existem várias versões do BitAxe, com diferentes chips e desempenhos:

| Série do Modelo Bitaxe   | Chip ASIC | Usado Em                    | Taxa de Hash Esperada       | Ideal Para                                                                                                 |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Série 100)   | 1 x BM1397| Série Antminer 17           | 400 GH/s (até 450 GH/s)     | Iniciantes em mineração de Bitcoin, oferecendo uma taxa de hash sólida com consumo de energia moderado.    |
| Bitaxe Ultra (Série 200) | 1 x BM1366| Antminer S19 XP e S19k Pro  | 500 GH/s (até 550 GH/s)     | Mineradores sérios visando equilibrar eficiência e taxa de hash mais alta.                                 |
| Bitaxe Hex (Série 300)   | 6 x BM1366| Antminer S19k Pro e S19 XP  | 3.0 TH/s (até 3.3 TH/s)     | Mineradores buscando escalabilidade e alto desempenho sem sacrificar a eficiência.                         |
| Bitaxe Supra (Série 400) | 1 x BM1368| Antminer S21                | 600 GH/s (até 700 GH/s)     | Entusiastas sérios buscando as maiores taxas de hash e eficiência.                                         |

Neste tutorial, estaremos usando um BitAxe Ultra 204 equipado com um chip BM1366, usado para o Antminer S19XP. Este já vem montado e com o firmware instalado pelo vendedor.

### [A lista de vendedores está disponível nesta página](https://bitaxe.org/legit.html)

![signup](assets/2.webp)

Geralmente, a fonte de alimentação é vendida com ele. Caso contrário, você precisará comprar uma fonte de alimentação com um cabo jack de 5V e pelo menos 4A.

![signup](assets/1.webp)

### Configuração
Quando você conectar seu BitAxe pela primeira vez, ele tentará se conectar a uma rede Wi-Fi por padrão. Após cinco tentativas, ele exibirá o nome de sua própria rede Wi-Fi para que você possa se conectar a ela e configurá-la.
Para fazer isso, você pode usar qualquer computador ou smartphone. Vá para as configurações de Wi-Fi, procure por novas redes e você verá uma Wi-Fi chamada Bitaxe_XXXX. Aqui, é `Bitaxe_A859`. Conecte-se a esta rede Wi-Fi, e uma janela será automaticamente aberta.

![signup](assets/3.webp)

Nesta janela, clique nas três pequenas barras horizontais no canto superior esquerdo, depois em `Settings`.

![signup](assets/4.webp)

Você precisará inserir manualmente as informações da sua rede Wi-Fi, pois não há um sistema de descoberta automática.
![signup](assets/5.webp)
Portanto, indique o SSID do Wi-Fi, ou seja, o nome da sua rede, a senha, bem como as informações da pool de mineração que você escolheu. Tenha cuidado, aqui a URL da pool não é apresentada da mesma maneira. Por exemplo, para a Braiins, a URL da pool fornecida é: `stratum+tcp://eu.stratum.braiins.com:3333`.

![signup](assets/6.webp)

Como você pode ver na tela, você precisa remover as partes `stratum+tcp://` e `:3333`, deixando apenas `eu.stratum.braiins.com`. Então, no campo `Port`, insira os 4 dígitos no final da URL fornecida pela pool, mas sem o `:`. Aqui, portanto, é `3333`.

Neste tutorial, estamos usando a pool de mineração Braiins, mas você é livre para escolher outra. Você pode encontrar nossos tutoriais sobre pools de mineração [no site da Rede PlanB](https://planb.network/en/tutorials/mining).

Em seguida, em `User`, insira seu identificador e depois a `Password`, geralmente, é `"x"` ou `"Anything123"`.

A configuração de `Core Voltage` deve ser deixada em `1200` por padrão, e para `Frequency`, também deixe o valor padrão inicialmente. Será possível ajustar essa configuração mais tarde para obter mais poder de computação. No entanto, é importante garantir que a temperatura do chip não exceda 65-70°C, pois o BitAxe não possui um sistema para reduzir o desempenho em caso de superaquecimento. Se a temperatura exceder muito os 65°C, isso poderia danificar seu BitAxe.

![signup](assets/7.webp)

Uma vez que você tenha inserido corretamente todas as configurações, clique no botão `Save` na parte inferior, depois reinicie seu BitAxe simplesmente desplugando-o e plugando-o novamente.
Se você inseriu suas informações corretamente, o dispositivo deve se conectar rapidamente ao seu Wi-Fi, depois à pool de mineração, e começar a exibir algumas informações em sua pequena tela. Provavelmente levará alguns minutos para que ele apareça no painel de controle da pool de mineração.
### Painel de Controle e Tela

Três diferentes exibições passarão. Na terceira página, você verá a informação de `IP`, que é o endereço IP que permite você se conectar ao painel de controle. Aqui, o endereço é `192.168.1.19`.

![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)

Para acessar o painel de controle, simplesmente insira este endereço no seu navegador de internet.

No painel de controle, você encontrará todas as informações exibidas na pequena tela, as quais vamos agora examinar em detalhes.

![signup](assets/11.webp)

| Tela do BitAxe | Painel de Controle                          | Descrição                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh             | Hashrate                                    | A potência de computação atual, expressa em GigaHash/s                                                                                                                                                                      |
| W/THs          | Eficiência                                  | Esta é a eficiência do seu BitAxe expressa em W/THs. É a relação entre a potência elétrica consumida e a potência de computação produzida.                                                                                  |
| A/R            | Shares                                      | Quantidade de `Shares` enviadas pelo seu BitAxe para a pool, representando a quantidade de trabalho fornecido.                                                                                                             |
| UT             | Tempo de Atividade                          | Tempo desde que seu BitAxe está operando sem interrupção (disponível no menu à esquerda em `Logs`).                                                                                                                        |
| BD            | Maior Dificuldade                           | Máxima dificuldade alcançada desde o último reinício. Para comparação, a dificuldade atual da rede é de cerca de 85T.                                                                                                     |
| FAN           | FAN na caixa `Calor`                        | Velocidade de rotação do ventilador, expressa em rotações por minuto.                                                                                                                                                     |
| Temp          | Temperatura do ASIC na caixa `Calor`        | Temperatura do chip, que não deve exceder 65°C.                                                                                                                                                                           |
| Pwr           | Potência                                    | Potência em watts consumida. No entanto, esta informação não leva em conta a tela, o ventilador ou a fonte de alimentação. Por exemplo, quando exibe 11.7W, o consumo total é na realidade 15.8W.                       |
| mV mA         | Tensão de Entrada Corrente de Entrada       | Tensão e corrente consumidas pela máquina. A potência em watts é igual à tensão multiplicada pela corrente.                                                                                                               |
| FH            | Memória Livre (menu esquerdo -> `Logs`)     | A memória disponível.                                                                                                                                                                                                    |
| vCore         | Tensão do ASIC (na caixa de Desempenho)     | Tensão medida no chip ASIC.                                                                                                                                                                                               |
| IP            | NA                                          | Endereço IP.                                                                                                                                                                                                              |
| V2.1.0        | Versão (menu esquerdo -> `Logs`)            | Versão do firmware.                                                                                                                                                                                                       |
Você pode alterar as configurações de Wi-Fi ou de pool a qualquer momento sem nenhum problema.  
Dependendo da ventilação e da temperatura do seu ambiente, você pode precisar aumentar ou talvez diminuir o desempenho para que a temperatura não exceda 65°C. Se você aumentar o desempenho, ganhará mais satoshis, mas seu BitAxe também consumirá mais eletricidade!