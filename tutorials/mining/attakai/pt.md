---
name: Attakaï

description: transformação de um S9 em aquecimento residencial
---

![capa](assets/cover.png)

# Attakai - a mineração em casa tornada possível e acessível!

A iniciativa "Attakaï" explora a mineração de Bitcoin utilizando o calor gerado. O guia propõe soluções para tornar os mineradores adequados para uso como radiadores em residências, oferecendo assim mais conforto e economia de energia. O Bitcoin ajusta automaticamente a dificuldade da mineração e recompensa os mineradores pelo seu trabalho. No entanto, a concentração da taxa de hash pode representar riscos para a neutralidade da rede. "Attakaï" oferece um guia prático para retrofitar os mineradores de forma econômica, permitindo que os participantes reduzam sua conta de eletricidade e sejam recompensados com sats sem KYC.

## Introdução

"Attakaï", que significa "a temperatura ideal" em japonês, é o nome da iniciativa que visa descobrir a mineração de bitcoin através da reutilização do calor lançado por @ajelexBTC e @BlobOnChain com o Découvre Bitcoin. Este guia de retrofitting de um ASIC servirá como base para aprender mais sobre a mineração, seu funcionamento, sua história recente e a economia subjacente.

### Por que reutilizar o calor de um ASIC?

É importante entender a relação entre energia e produção de calor em um sistema elétrico.

Para um investimento de 1 kW de energia elétrica, um radiador elétrico produz 1 kW de calor, nem mais nem menos. Os novos radiadores não são mais eficientes do que os radiadores tradicionais. Sua vantagem está em sua capacidade de difundir o calor de forma contínua e homogênea em um ambiente, proporcionando assim mais conforto em comparação com os radiadores tradicionais, que alternam entre alta potência de aquecimento e ausência de aquecimento, gerando variações regulares de temperatura e desconforto.

Um computador, ou mais amplamente uma placa eletrônica, não consome energia para realizar cálculos, ele apenas precisa que a energia circule em seus componentes para funcionar. O consumo de energia é devido à resistência elétrica dos componentes, que gera perdas e, portanto, calor, é o que chamamos de efeito Joule.
Certaines empresas tiveram a ideia de compartilhar as necessidades de potência de cálculo e aquecimento por meio de radiadores/servidores. A ideia é distribuir os servidores de uma empresa em pequenas unidades que podem ser colocadas em residências ou escritórios. No entanto, essa ideia enfrenta vários problemas. A necessidade dos servidores não está relacionada à necessidade de aquecimento e as empresas não podem usar as capacidades de cálculo de seus servidores de forma flexível. Também existem limites para a largura de banda que os indivíduos podem ter. Todas essas restrições impedem que a empresa rentabilize essas instalações caras ou forneça um serviço de servidor online estável sem ter centros de dados capazes de assumir quando não há necessidade de aquecimento.

> "O calor do seu computador não é desperdiçado se você precisar aquecer sua casa. Se você usa um aquecedor elétrico onde mora, então o calor do seu computador não é um desperdício. É o mesmo preço se você gerar esse calor com seu computador. Se você tiver um sistema de aquecimento mais barato do que o elétrico, então o desperdício está apenas na diferença de custo. Se for verão e você estiver usando o ar condicionado, então é o dobro.
> A mineração de bitcoins deve ocorrer onde é mais barata. Talvez seja onde o clima é frio e onde o aquecimento é elétrico, onde minerar se tornaria gratuito."
> Satoshi Nakamoto - 8 de agosto de 2010

O Bitcoin e sua prova de trabalho se destacam porque ajustam automaticamente a dificuldade da mineração com base na quantidade de cálculos realizados por toda a rede, essa quantidade é chamada de hashrate e é expressa em hash/segundo. Atualmente, estima-se que seja de 280 Exahash/segundo, ou seja, 280 trilhões de trilhões de hash/segundo. Esse hashrate representa trabalho e, portanto, uma quantidade de energia gasta. Quanto maior o hashrate, maior a dificuldade aumenta e vice-versa. Assim, é possível ativar ou desativar um minerador de Bitcoin a qualquer momento sem impacto na rede, ao contrário dos radiadores/servidores que precisariam permanecer estáveis para oferecer seu serviço. O minerador é recompensado pelo trabalho realizado em relação ao trabalho dos outros, por menor que seja essa participação.

Resumindo, um radiador elétrico e um minerador de Bitcoin produzem ambos 1 kW de calor para 1 kW de eletricidade gasta. No entanto, o minerador também recebe bitcoins como recompensa. Independentemente do preço da eletricidade, do preço do bitcoin ou da concorrência da atividade de mineração na rede Bitcoin, é economicamente mais vantajoso aquecer-se com um minerador do que com um radiador elétrico.

![Video apresentação](https://youtu.be/gKoh44UCSnE)

### O valor agregado para o Bitcoin

Nous não entraremos em detalhes sobre o funcionamento da mineração aqui (recursos disponíveis na academia, se necessário). O que é importante entender é como a mineração contribui para a descentralização do Bitcoin. Várias tecnologias já existentes foram combinadas de forma engenhosa para dar vida ao consenso de Nakamoto. Esse consenso permite recompensar economicamente os atores honestos por sua participação na operação da rede Bitcoin, ao mesmo tempo em que desencoraja os atores desonestos. Esse é um dos pontos-chave que permite a existência sustentável da rede.

Os atores honestos, aqueles que realizam a mineração de acordo com as regras, competem entre si para obter a maior parte possível da recompensa pela produção de novos blocos. Esse incentivo econômico naturalmente leva a uma forma de centralização, pois as empresas optam por se especializar nessa atividade lucrativa, reduzindo seus custos por meio de economias de escala. Esses atores industriais têm uma posição vantajosa para a compra, manutenção de máquinas e também para a negociação de tarifas de eletricidade em grande escala.

> "No início, a maioria dos usuários executaria nós de rede, mas à medida que a rede se expandisse além de um certo ponto, ela seria cada vez mais deixada para especialistas com fazendas de servidores de hardware especializado. Uma bateria de servidores precisaria apenas de um único nó na rede e o restante da LAN se conectaria a esse nó." - Satoshi Nakamoto - 2 de novembro de 2008

Algumas entidades possuem uma porcentagem considerável da taxa de hash total em grandes fazendas de mineração. Podemos observar a recente onda de frio nos Estados Unidos, onde uma parte significativa da taxa de hash foi desligada para permitir que a energia fosse redirecionada para residências com necessidades excepcionais de eletricidade. Durante vários dias, os mineradores foram incentivados economicamente a desligar suas fazendas e, portanto, podemos ver esse clima excepcional na curva da taxa de hash do Bitcoin.

Esse assunto pode se tornar problemático e trazer um risco significativo para a neutralidade da rede. Um ator que possua mais de 51% da taxa de hash poderia facilmente censurar transações, se assim o desejasse. Portanto, é importante distribuir a taxa de hash entre vários atores, em vez de entidades centralizadas que poderiam ser facilmente apreendidas por um governo, por exemplo.

**Se os mineradores estiverem distribuídos em milhares, ou até mesmo milhões, de residências ao redor do mundo, torna-se muito complicado para um Estado assumir o controle.**

À sa sortie d'usine, um minerador não é adequado para ser usado como um radiador em uma residência, devido a dois problemas principais: ruído excessivo e falta de ajuste. No entanto, esses problemas podem ser facilmente resolvidos por meio de modificações simples no hardware e software, permitindo obter um minerador muito mais silencioso e que pode ser configurado e automatizado como os aquecedores elétricos modernos.

**Attakaï é uma iniciativa educacional que ensina como fazer uma adaptação do Antminer S9 da maneira mais econômica possível.**

Esta é uma excelente oportunidade para aprender praticando. Além de reduzir sua conta de eletricidade, você é recompensado por sua participação com sats KYC gratuitos.

## Capítulo 1: Guia de compra para um ASIC usado

Nesta seção, veremos as melhores práticas para comprar um Bitmain Antminer S9 usado, a máquina na qual este tutorial de adaptação em radiador será baseado. Este guia também funciona para outros modelos de ASIC, pois é um guia geral de compra de hardware de mineração usado.

O Antminer S9 é um dispositivo oferecido pela Bitmain desde maio de 2016. Ele consome 1323W de eletricidade e produz 13,5 TH/s. Embora seja considerado antigo, ainda é uma excelente opção para começar a mineração. Como foi produzido em grande quantidade, é fácil encontrar peças sobressalentes em abundância em muitas regiões do mundo. Geralmente, pode ser adquirido de forma peer-to-peer em sites como o Ebay ou LeBonCoin, pois os revendedores voltados para profissionais não o oferecem mais devido à sua menor competitividade em comparação com máquinas mais recentes. É menos eficiente do que ASICs como o Antminer S19, lançado em março de 2020, mas isso o torna um hardware usado acessível e mais adequado para as modificações que faremos.

O Antminer S9 existe em várias variantes (i, j) que trazem pequenas modificações ao hardware de primeira geração. Não acreditamos que esse elemento deva influenciar sua decisão de compra e este guia funcionará para todas essas variantes.

O preço dos ASICs varia de acordo com vários fatores, como o preço do bitcoin, a dificuldade da rede, a eficiência da máquina e o custo da eletricidade. Portanto, é difícil dar uma estimativa precisa para a compra de uma máquina usada. Em fevereiro de 2023, o preço esperado na França geralmente varia entre 100€ e 200€, mas esses preços podem mudar rapidamente.

![imagem](assets/guide-achat/1.jpeg)

O Antminer S9 é composto pelas seguintes partes:

- 3 placas de hash onde estão os chips que produzem o hash

![imagem](assets/guide-achat/2.jpeg)'

- Uma placa de controle que inclui um slot para um cartão SD, uma porta Ethernet e conectores para as hashboards e os ventiladores. É o cérebro do seu ASIC.

![image](assets/guide-achat/3.jpeg)

- 3 cabos de dados que conectam as hashboards à placa de controle

![image](assets/guide-achat/4.jpeg)

- A fonte de alimentação que funciona em 220V e pode ser conectada como um eletrodoméstico comum

![image](assets/guide-achat/5.jpeg)

- 2 ventiladores de 120mm

![image](assets/guide-achat/6.jpeg)

- Um cabo macho C13

![image](assets/guide-achat/7.jpeg)

Ao comprar uma máquina usada, é importante verificar se todas as peças estão incluídas e funcionais. Durante a troca, você deve pedir ao vendedor para ligar a máquina e verificar se ela está funcionando corretamente. É importante verificar se o aparelho liga corretamente e, em seguida, verificar a conectividade com a internet conectando um cabo Ethernet e acessando a interface de conexão da Bitmain por meio de um navegador de internet na mesma rede local. Você pode encontrar este endereço IP conectando-se à interface do seu roteador de internet e procurando os dispositivos conectados. Este endereço deve ter o seguinte formato: 192.168.x.x

![image](assets/guide-achat/8.gif)

Também verifique se as credenciais padrão funcionam (nome de usuário: root, senha: root). Se as credenciais padrão não funcionarem, será necessário fazer um reset da máquina.

![image](assets/guide-achat/9.jpeg)

Depois de conectado, você deve ser capaz de ver o estado de cada hashboard no painel de controle. Se o minerador estiver conectado a um pool, você deve ver todas as hashboards funcionando. É importante observar que os mineradores fazem muito barulho, isso é normal. Certifique-se também de que os ventiladores estão funcionando corretamente.

Você pode então remover o pool de mineração do antigo proprietário para configurar o seu próprio posteriormente. Se desejar, você também pode inspecionar as hashboards desmontando a máquina. No entanto, esta etapa é mais complexa e requer mais tempo e algumas ferramentas. Se você deseja realizar esse desmonte, pode consultar a próxima parte deste tutorial que detalha como fazê-lo. É importante observar que os mineradores acumulam muita poeira e requerem manutenção regular. É essa acumulação de poeira e a qualidade da manutenção que você poderá observar desmontando a máquina.
Depois de revisar todos esses pontos, você pode comprar sua máquina com um alto grau de confiança. Em caso de dúvida, consulte a comunidade e se precisar de equipamentos para realizar este tutorial, não hesite em nos enviar uma mensagem.

Para sintetizar este guia em uma frase: **"Não confie, verifique"**.

## Capítulo 2: Guia de compra de peças para modificações

![image](assets/piece/1.jpeg)

### Como transformar o seu Antminer S9 em um aquecedor silencioso e conectado?

Se você é proprietário de um Antminer S9, provavelmente sabe o quão barulhento e volumoso esse equipamento pode ser. No entanto, é possível transformá-lo em um aquecedor silencioso e conectado seguindo alguns passos simples. Neste artigo, apresentaremos os equipamentos necessários para realizar as modificações, enquanto um artigo posterior explicará em detalhes os passos a serem seguidos para realizar essas mudanças.

### 1. Substituir os ventiladores

Os ventiladores originais do Antminer S9 são muito barulhentos para usar o seu Antminer como aquecedor. A solução é substituí-los por ventiladores mais silenciosos. Nossa equipe testou vários modelos da marca Noctua e selecionou o Noctua NF-A14 iPPC-2000 PWM como a melhor opção, certifique-se de escolher a versão de 12V dos ventiladores. Este ventilador de 140mm pode produzir até 1300W de aquecimento, mantendo um nível teórico de ruído de 31 dB. Para poder instalar esses ventiladores de 140mm, você precisará usar um adaptador de 140mm para 120mm, que pode ser encontrado na loja DécouvreBitcoin. E também adicionaremos grades de proteção de 140mm.

![image](assets/piece/1.jpeg)
![image](assets/piece/2.jpeg)
![image](assets/piece/3.jpeg)

O ventilador da fonte de alimentação também é bastante barulhento e precisa ser substituído. Recomendamos o Noctua NF-A6x25 PWM. Observe que os conectores dos ventiladores Noctua não são os mesmos que os originais, portanto, você precisará de um adaptador para conectá-los, 2 serão suficientes. Tome cuidado também para escolher a versão de 12V do ventilador.

![image](assets/piece/4.jpeg)
![image](assets/piece/5.jpeg)

### 2. Adicionar um bridge WIFI/Ethernet

Em vez de usar um cabo Ethernet, você pode conectar o seu Antminer via WIFI adicionando um bridge WIFI/Ethernet. Selecionamos o vonets vap11g-300, pois ele permite facilmente captar o sinal WIFI do seu roteador e transmiti-lo para o seu Antminer via Ethernet sem criar uma sub-rede. Se você tiver habilidades elétricas, poderá alimentá-lo diretamente com a fonte de alimentação do Antminer, sem precisar adicionar um carregador USB, para isso você precisará de uma tomada fêmea de 5,5mmx2,1mm.

![image](assets/piece/6.jpeg)
![image](assets/piece/7.jpeg)

### 3. Opcional: adicionar uma tomada conectada

'Se você quiser ligar/desligar seu Antminer do seu smartphone e monitorar seu consumo de energia, você pode adicionar uma tomada inteligente. Testamos a tomada ANTELA na versão 16A compatível com o aplicativo smartlife. Esta tomada inteligente permite consultar o consumo diário e mensal e se conecta diretamente ao seu roteador Wi-Fi.

![image](assets/piece/8.jpeg)

> Lista de equipamentos e links
>
> - 2X adaptador 3D de peça 140mm para 120mm
> - 2X NF-A14 iPPC-2000 PWM [link](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - 2X Grades de ventiladores 140mm [link](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - Noctua NF-A6x25 PWM [link](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
> - Conector elétrico 2,5mm2 [link](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)'
> - Vonets vap11g-300 [link](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1> - Optionnel prise connectée ANTELA [link](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

## Chapitre 3 - TUTORIEL : Como transformar um minerador em um aquecedor?

![image](assets/hardware/0.jpeg)

Se você é um bricoleiro experiente e está procurando transformar um minerador em um aquecedor, este tutorial é para você. Gostaríamos de alertar que fazer modificações em um dispositivo eletrônico pode apresentar riscos elétricos e de incêndio. Portanto, é essencial tomar todas as precauções necessárias para evitar danos ou lesões.
De fábrica, um minerador não é realmente utilizável como um radiador em uma residência, pois é muito barulhento e não é ajustável. No entanto, é possível fazer modificações simples para resolver esses problemas.

> ATENÇÃO: É essencial ter instalado previamente o Braiins OS+ em seu minerador, ou qualquer outro software capaz de reduzir o desempenho de sua máquina. Essa medida é crucial, pois, com o objetivo de reduzir o ruído, iremos instalar ventiladores menos potentes, que poderão dissipar menos calor.

### Materiais necessários

- 2 adaptadores 3D de 140mm para 120mm
- 2 ventiladores Noctua NF-A14 iPPC-2000 PWM
- 2 grades de ventiladores de 140mm
- 1 ventilador Noctua NF-A6x25 PWM
- Fio elétrico de 2,5mm2
- Vonets VAP11G-300
- Opcional: tomada conectada ANTELA

### Substituição dos ventiladores

Vamos começar substituindo o ventilador da fonte de alimentação.

> ATENÇÃO: Antes de tudo, certifique-se de ter desconectado seu minerador para evitar qualquer risco de choque elétrico.

![image](assets/hardware/1.jpeg)

Vamos começar substituindo o ventilador da fonte de alimentação.

Primeiro, remova os 6 parafusos na lateral do gabinete que o mantêm fechado. Depois de remover os parafusos, abra cuidadosamente o gabinete para remover a proteção de plástico que cobre os componentes.

![image](assets/hardware/2.jpeg)
![image](assets/hardware/3.jpeg)'

En seguida, é hora de remover o ventilador original, tendo cuidado para não danificar os outros componentes. Para fazer isso, remova os parafusos que o seguram no lugar e delicadamente descole a cola branca que envolve o conector. É importante proceder com delicadeza para evitar danificar os fios ou conectores.

![image](assets/hardware/4.jpeg)

Uma vez removido o ventilador original, você notará que os conectores do novo ventilador Noctua não correspondem aos do ventilador original. Na verdade, o novo ventilador possui 3 fios, incluindo um fio amarelo que permite controlar a velocidade. No entanto, esse fio não será usado neste caso específico. Para conectar o novo ventilador, é recomendado usar um adaptador especial. No entanto, é importante observar que esse adaptador às vezes pode ser difícil de encontrar.

![image](assets/hardware/5.jpeg)

Se você não tiver esse adaptador, ainda poderá conectar o novo ventilador usando um conector de fio elétrico. Para isso, você precisará cortar os cabos do antigo e do novo ventilador.

![image](assets/hardware/6.jpeg)
![image](assets/hardware/7.jpeg)

No novo ventilador, use um cortador e corte cuidadosamente os contornos da capa principal a 1cm sem cortar as capas dos cabos abaixo.

![image](assets/hardware/8.jpeg)

Em seguida, puxando a capa principal para baixo, corte as capas dos cabos vermelho e preto da mesma maneira que antes. E corte o cabo amarelo rente.

![image](assets/hardware/9.jpeg)

No antigo ventilador, é mais delicado cortar a capa principal sem danificar as capas dos cabos vermelho e preto. Para isso, usamos uma agulha que deslizamos entre a capa principal e os fios vermelhos e pretos.

![image](assets/hardware/10.jpeg)
![image](assets/hardware/11.jpeg)

Uma vez que os fios vermelhos e pretos estejam livres, corte as capas sempre com cuidado para não danificar os fios elétricos.

![image](assets/hardware/12.jpeg)

Em seguida, conecte os cabos com um conector, o fio preto com o preto e o fio vermelho com o vermelho. Você também pode adicionar fita isolante.

![image](assets/hardware/13.jpeg)
![image](assets/hardware/14.jpeg)

Uma vez que a conexão esteja feita, é hora de colocar o novo ventilador Noctua com a grade e os parafusos antigos, os novos parafusos que estão na caixa serão reutilizados posteriormente. Certifique-se de colocá-lo na orientação correta. Você notará uma seta em um dos lados do ventilador, que indica a direção do fluxo de ar. É importante colocar o ventilador de forma que essa seta aponte para dentro do gabinete. Em seguida, reconecte o ventilador.
'![image](assets/hardware/15.jpeg)![image](assets/hardware/16.jpeg)

> Opcional: Se você tiver conhecimentos em eletricidade, pode adicionar diretamente na saída de alimentação de 12V um conector jack fêmea de 5,5 mm que permitirá alimentar diretamente a ponte Wi-Fi Vonet. No entanto, se você não tiver certeza de suas habilidades em eletricidade, é melhor usar o conector USB com um carregador de smartphone para evitar qualquer risco de curto-circuito ou dano elétrico.

![image](assets/hardware/17.jpeg)

Depois de fazer as conexões, coloque a tampa de plástico sobre a caixa de plástico e não dentro dela.

![image](assets/hardware/18.jpeg)

Por fim, recoloque a tampa da caixa no lugar e aperte os 6 parafusos nas laterais para fixar tudo no lugar. E pronto, sua caixa de alimentação agora está equipada com um novo ventilador.

### Substituição dos 2 ventiladores principais

1.  Primeiro, desconecte os ventiladores e desparafuse-os.
2.  ![image](assets/hardware/19.jpeg)

3.  Os conectores dos novos ventiladores Noctua não correspondem aos originais, mas não se preocupe! Pegue seu estilete e corte cuidadosamente as pequenas abas de plástico para que os conectores se encaixem perfeitamente no seu minerador.

![image](assets/hardware/20.jpeg)
![image](assets/hardware/21.jpeg)

3. É hora de instalar as peças 3D!
   Fixe-as em ambos os lados do minerador usando os parafusos que você removeu dos ventiladores. Aperte até que a cabeça do parafuso esteja embutida na peça 3D e que ela esteja bem fixada no lugar. Cuidado para não apertar demais, você pode deformar a peça e um dos parafusos pode tocar em um capacitor! Em seguida, corte cuidadosamente as pequenas abas de plástico para que os conectores se encaixem perfeitamente no seu minerador.

![image](assets/hardware/22.jpeg)

4. Agora vamos para os ventiladores.
   Fixe-os nas peças 3D usando os parafusos fornecidos na caixa. Preste atenção na direção do fluxo de ar, as setas nas laterais dos ventiladores indicarão a direção a seguir. Vá do lado da porta Ethernet para o outro lado. Veja a foto abaixo.

![image](assets/hardware/23.jpeg)
![image](assets/hardware/24.jpeg)
![image](assets/hardware/25.jpeg)

5. Última etapa: conecte os ventiladores e fixe as grades por cima com os parafusos que não foram usados na caixa do ventilador de alimentação. Você só tem 4, mas 2 por grade em ângulos opostos serão suficientes. Se necessário, você também pode procurar por outros parafusos semelhantes em uma loja de ferragens.

![image](assets/hardware/26.jpeg)'
'![image](assets/hardware/27.jpeg)
Enquanto espera poder oferecer uma caixa mais elegante para o seu novo aquecedor, pode prender a caixa e a fonte de alimentação juntas com abraçadeiras de eletricista.

![image](assets/hardware/28.jpeg)

E para o toque final, ligue a ponte Vonet à porta Ethernet à sua fonte de alimentação. Se ainda não o fez, pode seguir este tutorial para configurar a sua ponte.

![image](assets/hardware/29.jpeg)

E pronto, parabéns! Acabou de substituir toda a parte mecânica do seu minerador. Agora deverá ouvir muito menos ruído.

## Capítulo 4 - Modificação do software - Redefinir um Antminer S9

**Série de artigos proposta por BlobOnChain & Ajelex - 15/02/2023**

### Redefinir através do botão "Reset"

Este método pode ser aplicado nos primeiros 10 minutos após o arranque do minerador.

Após ligar o minerador durante 2 minutos, pressione o botão "Reset" durante 5 segundos e depois solte-o. O minerador será restaurado para as configurações de fábrica em 4 minutos e reiniciará automaticamente (não é necessário desligá-lo).

![image](assets/software/1.jpeg)

Restaurar através do lado web

Faça login na interface do utilizador do seu minerador, clique em "Upgrade" >> "Realizar uma redefinição" e depois clique em "OK" na janela pop-up.

### Sistema operativo original

Para esta parte, vamos assumir que a máquina está a funcionar, está ligada e tem o seu sistema operativo original instalado. Vamos dar uma breve vista de olhos na interface do sistema operativo original proposto pela Bitmain.

Primeiro, ligue-se à sua máquina através da sua rede local:

![image](assets/software/2.gif)

Uma vez na página de login, terá de fazer login no ASIC utilizando as credenciais padrão:

- nome de utilizador: root
- senha: root

(Como redefinir se a senha padrão não funcionar?)

O sistema operativo principal é relativamente básico. Com as 4 abas: Sistema, Configuração do Minerador, Estado do Minerador, Rede. Na aba Configuração do Minerador, pode configurar até 3 pools de mineração.

![image](assets/software/3.jpeg)

Na aba Estado do Minerador, poderá observar várias informações sobre o funcionamento do ASIC em tempo real. A taxa de hash expressa em GH/s, informações mais detalhadas sobre o pool, bem como detalhes sobre o estado de cada placa de hash e a velocidade dos ventiladores em rotações por minuto.

![image](assets/software/4.jpeg)

### Braiins OS+'

Vediamo ora il software Braiins OS+ ASIC (https://braiins.com/os/plus). Il software è sviluppato da Braiins (https://braiins.com/), la società madre di Braiins Pool (https://braiins.com/pool). Al momento in cui scriviamo, questo pool di mining detiene il 4,39% dell'hashrate globale (https://mempool.space/fr/mining/pool/slushpool). La società con sede a Praga era precedentemente nota come Slushpool ed è stata la prima mining pool a essere lanciata nel novembre 2010. Oggi l'azienda, che ha un'ampia gamma di attività, offre strumenti di studio della redditività per il mining (https://insights.braiins.com/en), soluzioni per la gestione delle farm di mining insieme all'attività del pool e software di ottimizzazione per gli ASIC. Offre inoltre il mining con il nuovo protocollo Stratum V2 (https://braiins.com/bitcoin-mining-stack-upgrade).

Vediamo quindi da vicino come funzionano i dispositivi di Bitmain, che attualmente sono gli unici modelli compatibili:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e e S9 [i, j]

Il software Braiins OS può essere installato in modo semplice su tutte le macchine sopra elencate. Offre un controllo più preciso sulla macchina, consentendo di overcloccarla per overcloccarla o di sottocloccarla per sottocloccarla. Inoltre, consente di regolare con precisione la frequenza di ciascun chip grazie a una funzione di ottimizzazione automatica chiamata autotuning. Poiché ogni chip hash è leggermente diverso a causa del processo di produzione, il software verifica la frequenza ottimale per ciascuno di essi per ottenere la massima efficienza (W/TH). Il software sostiene che le prestazioni possono essere superiori fino al 25% rispetto all'originale. Secondo le nostre misurazioni, è possibile raggiungere queste cifre.

## Installazione di Braiins OS+

Esistono diversi modi per installare Braiins OS+ su un ASIC. Si può fare riferimento a questa guida, ma anche alla documentazione ufficiale di Braiins e ai video tutorial.
Installazione di Braiins OS+ direttamente sulla memoria dell'Antminer

Scoprite come installare facilmente Braiins OS+ direttamente sulla memoria del vostro Antminer con BOS toolbox, sostituendo così il sistema operativo originale, utilizzando i passaggi descritti di seguito. Se si desidera mantenere il sistema operativo originale in parallelo, è possibile installare Braiins OS+ su una scheda SD.

1. Accendere l'Antimner e collegarlo al box Internet.
2. Scaricare BOS toolbox Windows / Linux
3. Descompacte o arquivo baixado e abra o arquivo bos-toolbox.bat, escolha o idioma e, após alguns instantes, você verá esta janela:
   ![image](assets/software/5.jpeg)

4. A Bos toolbox permitirá que você encontre facilmente o endereço IP do seu Antminer e instale o Braiins OS+. Se você já conhece o endereço IP da sua máquina, pode pular para a etapa 8. Caso contrário, vá para a guia de escaneamento.

![image](assets/software/6.jpeg)

5. Normalmente, em redes domésticas, a faixa de endereços IP está entre 192.168.1.1 e 192.168.1.255, então coloque "192.168.1.0/24" no campo de faixa de IP. Se a sua rede for diferente, altere esses endereços. Em seguida, clique em "Start".

6. Atenção, se o Antminer tiver uma senha, a detecção não funcionará. Se for o caso, a maneira mais simples é fazer um Reset factory.

7. Você deverá ver todos os Antminers na sua rede, aqui o endereço IP é 192.168.1.37.

![image](assets/software/7.jpeg)

8. Clique em "Back" e depois na guia "install", insira o endereço IP encontrado anteriormente no campo "Miner(s)" e "admin" (ou "root") no campo "Password", que é a senha padrão, e clique em "Start".
   Se a instalação não funcionar, nem com "admin" ou "root" como senha, pode ser necessário fazer um reset factory e tentar novamente.

![image](assets/software/8.jpeg)

9. Após alguns instantes, o seu Antminer será reiniciado e você poderá acessar a interface do Braiins OS+ no endereço IP em questão, aqui é 192.168.1.37, digitando-o diretamente na barra de endereço do seu navegador. O nome de usuário padrão é "root" e não há senha padrão.
   Instalação do Braiins OS+ em um cartão SD

![image](assets/software/9.jpeg)

![image](assets/software/10.jpeg)

O segundo método utiliza a interface original do seu Antminer. Este método funciona para máquinas com um sistema operacional anterior a 2019.

### Interface Antminer

1. Baixe o novo sistema operacional a ser instalado aqui.
2. Como na seção anterior, conecte-se à sua máquina através da sua rede local.
3. Vá para a guia "System" e depois "Upgrade".
4. Carregue o arquivo que você baixou e faça o flash da imagem.

![image](assets/software/11.jpeg)

### Cartão micro SD

Um segundo método permite que você use um cartão micro SD. Este método funciona apenas para máquinas com um sistema operacional posterior a 2019.

1. Baixe o novo sistema operacional a ser instalado aqui.

2. Faça o flash da imagem baixada em um cartão micro SD. Para isso, você pode usar o Etcher. Simplesmente copiar o arquivo para o cartão micro SD não funcionará.
3. Se você possui um Antminer S9 e suas variantes (S9i, S9j), você precisará ajustar os "jumpers" para forçar o seu ASIC a inicializar a partir do arquivo contido no cartão micro SD em vez da NAND. Se você tiver outro modelo, você pode pular para a parte 4. Os jumpers estão localizados na placa de controle na parte superior do ASIC, próximo à porta Ethernet. Você precisará removê-la deslizando-a para trás. Depois de alterar a posição do jumper como nas imagens abaixo BOOT FROM SD, você pode reinserir a placa de controle e reconectar o S9.

![image](assets/software/12.jpeg)

![image](assets/software/13.jpeg)

4. Insira o cartão micro SD no ASIC.
5. Inicie o ASIC. Se a versão de instalação automática foi usada, o novo sistema operacional será instalado automaticamente. A instalação estará concluída quando os dois LEDs acenderem ao mesmo tempo. Você pode reiniciar o ASIC e remover o cartão micro SD. Se a outra versão foi baixada, você precisará deixar o cartão micro SD dentro do ASIC.

Para obter mais informações sobre a instalação, você pode visitar esta seção do site da Braiins.

## A interface

Você precisará se conectar ao seu ASIC de forma semelhante. Usando o endereço IP local do seu dispositivo na sua rede através de um navegador.

As credenciais padrão são as mesmas do sistema operacional original.

- nome de usuário: root
- senha: root

Você será recebido pelo painel de controle do Brains OS+

### Painel de controle

![image](assets/software/14.jpeg)

Nesta primeira página, você poderá observar o desempenho da sua máquina em tempo real.

- Três gráficos em tempo real que mostram a temperatura, a taxa de hash e o status geral da sua máquina.
- À direita, a taxa de hash real, a temperatura média dos chips, a eficiência estimada em W/THs e o consumo de energia.
- Abaixo, a velocidade de rotação dos ventiladores em porcentagem da velocidade máxima e o número de rotações por minuto.

![image](assets/software/15.jpeg)

- Mais abaixo, você encontrará uma visualização detalhada de cada placa de hash. A temperatura média da placa e dos chips que a compõem, a tensão e a frequência.
- Detalhes sobre os pools de mineração ativos em Pools.
- O status do autotuning em Tuner Status.
- À direita, detalhes sobre as partes transmitidas para o pool.

### Configuração

![image](assets/software/16.jpeg)

### Sistema

![image](assets/software/17.jpeg)

### Ações rápidas

![image](assets/software/18.jpeg)

Configuração de um pool
Un pool minerario può essere considerato come una cooperativa agricola. Gli agricoltori mettono in comune la loro produzione per ridurre la varianza della domanda e dell'offerta e ottenere così un reddito più stabile per la loro azienda agricola. Un mining pool funziona allo stesso modo, ma le materie prime messe in comune sono gli hash. La scoperta di un singolo hash valido consente di creare un blocco e di ottenere la ricompensa di 6,25 BTC più le commissioni di transazione incluse nel blocco. Se si effettua il mining da soli, si viene ricompensati solo quando si trova un blocco. Competendo contro tutti gli altri minatori del pianeta, avreste pochissime possibilità di vincere questa grande lotteria e dovreste comunque pagare le commissioni associate all'utilizzo del vostro miner, senza alcuna garanzia di successo. I pool di mining risolvono questo problema mettendo in comune la potenza di calcolo di diversi (migliaia) minatori e dividendo le ricompense tra loro in base alla percentuale di hashrate del pool che viene raggiunta quando viene trovato un blocco. È possibile utilizzare questo strumento per vedere le proprie possibilità di estrarre un singolo blocco. Se si inseriscono le informazioni per un Antminer S9, si può vedere che le probabilità di trovare un hash che consenta la creazione di un blocco sono 1/24.777.849 per ogni blocco, o 1/ 172.068 al giorno. In media (con un hashrate e una difficoltà costanti) ci vorrebbero 471 anni per trovare un blocco.

Tuttavia, poiché il Bitcoin è una questione di probabilità, i minatori solitari sono talvolta ricompensati per aver corso questo rischio: Solo Bitcoin Miner risolve il blocco con un tasso di hash di soli 10 TH/s, battendo probabilità estremamente improbabili - Decrypt

Se vi piace il gioco d'azzardo, potete provarci, ma la nostra guida non andrà in quella direzione. Ci concentreremo invece sul pool di mining più adatto alle nostre esigenze per creare un sistema di riscaldamento.

As considerações a ter ao escolher um pool de mineração são o funcionamento das recompensas do pool, que podem ser diferentes, bem como o valor mínimo antes de poder retirar as recompensas para um endereço. Por exemplo, a Braiins, que oferece o software que estamos discutindo aqui, também oferece um pool. Este pool tem um sistema de recompensa chamado "Score" que incentiva os mineradores a minerar por longos períodos. A participação inclui um fator de tempo de atividade que é expresso com uma "taxa de hash de pontuação". No nosso caso, em que desejamos um sistema de aquecimento que possa ser ligado apenas por alguns minutos, este não é o sistema de recompensa ideal. Preferimos um sistema de recompensa que nos dê uma recompensa igual para cada participação. Além disso, o valor mínimo de retirada para o Braiins Pool é de 100.000 sats e On-Chain. Portanto, perdemos alguns sats em taxas de transação e parte da nossa recompensa pode ser bloqueada se não minerarmos o suficiente durante o inverno.

O modelo de recompensa que nos interessa é o PPS, que significa "pagamento por ação". Isso significa que o minerador receberá uma recompensa por cada ação válida. Também existe uma variante desse sistema, o FPPS (Pagamento Completo por Ação), que divide não apenas a recompensa da coinbase, mas também as taxas de transação incluídas no bloco. Os pools de mineração que recomendamos para conectar sua mineração/aquecimento são o Linecoin Pool (FPPS) e o Nicehash (PPS).

- Nicehash: A vantagem do Nicehash é que a retirada pode ser feita usando o Lightning com taxas mínimas. Além disso, o valor mínimo de retirada é de 2000 sats. A desvantagem é que o Nicehash usa sua taxa de hash para a blockchain mais lucrativa, sem realmente dar controle ao usuário, e portanto, não necessariamente participa da taxa de hash do Bitcoin.

- Lincoin: A vantagem do Linecoin é o número de recursos oferecidos, como um painel detalhado, a possibilidade de fazer retiradas com um Paynym (BIP 47) para uma melhor proteção da privacidade, e a integração de um bot do Telegram, bem como automações diretamente configuráveis no aplicativo móvel. Este pool minera apenas blocos de Bitcoin, mas o valor mínimo para retirada ainda é alto, de 100.000 sats. Vamos examinar mais detalhadamente a interface de um desses pools em um próximo artigo.

Para configurar um pool no Braiins 0S+, você precisará criar uma conta em um dos pools de sua escolha. Aqui vamos usar o exemplo do Lincoin:

![image](assets/software/19.jpeg)

Depois de criar sua conta, clique em Conectar ao Pool

Em seguida, copie o endereço Stratum e seu nome de usuário:

![image](assets/software/20.jpeg)

Agora você pode voltar para a interface do Braiins OS+ para inserir essas credenciais. Para a senha, você pode deixar o campo em branco.

![image](assets/software/21.jpeg)

### Overclocking e Underclocking

O overclocking e o underclocking consistem em ajustar as frequências nas placas de mineração para melhorar o desempenho do ASIC. A diferença entre os dois está na complexidade dessas configurações de frequência.

O **overclocking** é um ajuste simples que envolve aumentar a frequência nas placas de mineração para aumentar a taxa de hash da máquina. O underclocking, por outro lado, envolve diminuir a frequência do relógio de um circuito integrado abaixo de sua frequência nominal. Ao reduzir a frequência do relógio de um ASIC por meio do underclocking, também reduzimos o calor gerado pelo hardware. Isso permite diminuir a velocidade dos ventiladores necessários para resfriar o ASIC, pois eles não precisam trabalhar tão duro para manter uma temperatura adequada. Ao reduzir a velocidade dos ventiladores, também reduzimos o ruído gerado pelo ASIC. Isso pode ser especialmente útil para usuários que utilizam ASICs em casa e desejam minimizar as perturbações sonoras causadas pelo equipamento de mineração.

É importante observar que o underclocking pode resultar em uma redução no desempenho do ASIC, portanto é importante encontrar um bom equilíbrio entre desempenho e ruído.

O Braiins OS+ suporta overclocking, underclocking de ASICs e autotuning. Ele permite que os usuários ajustem a frequência do relógio de seu hardware de forma flexível para maximizar o desempenho ou economizar energia de acordo com suas preferências.

### Autotuning

Antes de 2018, os mineradores tinham duas maneiras de obter vantagem em suas atividades: encontrar eletricidade a um custo razoável e comprar hardware mais eficiente. No entanto, em 2018, uma nova descoberta foi feita no campo de software e firmware de mineração, chamada AsicBoost. Essa técnica permite que os mineradores reduzam seus custos em cerca de 13% ao modificar o firmware executado em seus dispositivos.
'Aujourd'hui, existe um novo avanço no setor de software e firmware de mineração chamado de autorregulação (ou autotuning) que oferece uma vantagem ainda maior do que o AsicBoost. Os ASICs são compostos por muitos pequenos chips de computador que realizam o hashing. Esses chips são feitos de silício, o mesmo elemento amplamente utilizado em semicondutores e outros componentes microeletrônicos. A compreensão chave aqui é que nem todos os chips de silício são idênticos - cada um pode variar ligeiramente em suas propriedades elétricas. Os fabricantes de hardware sabem disso e publicam as especificações de desempenho de suas máquinas de mineração com base no limite inferior de suas tolerâncias. Em outras palavras, os fabricantes conhecem a frequência que funciona melhor para os chips médios e usam essa frequência de forma uniforme para todos os chips da máquina.

Isso impõe um limite superior à taxa de hashing que uma máquina pode ter. A autorregulação é um processo no qual algoritmos avaliam as frequências ideais para o hashing chip por chip, em vez de tratar toda a máquina como uma única unidade. Isso significa que um chip de melhor qualidade, que pode realizar mais hashings por segundo, obterá uma frequência mais alta, e um chip de qualidade inferior, que pode realizar relativamente menos, obterá uma frequência mais baixa. A autorregulação por chip é essencialmente uma maneira de otimizar o desempenho de um ASIC por meio do software e firmware que são executados nele.

O resultado final é uma taxa de hashing mais alta por watt de eletricidade, o que significa margens de lucro maiores para os mineradores. A razão pela qual as máquinas não são distribuídas com esse tipo de software é que a variação por máquina não é desejável, pois os clientes querem saber exatamente o que estão obtendo, e, portanto, é uma má ideia para os fabricantes venderem um produto que não tenha desempenho consistente e previsível de uma máquina para outra. Além disso, a autorregulação por chip requer recursos de desenvolvimento consideráveis, pois é complexa de ser implementada. Os fabricantes já gastam muitos recursos no desenvolvimento de seus próprios firmwares. Existem soluções de software que permitem a implementação do autotuning, como o Braiins OS+. Além de melhorar o desempenho do ASIC em até 20%.

> Guia criado por DecouvreBitcoin, mais informações sobre MINAGE 201 - crédito Jim e Ajelex'
