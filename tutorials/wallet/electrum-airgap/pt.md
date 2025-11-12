---
name: Electrum Airgap
description: Um primeiro passo para a segurança, uma cold wallet com Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



Neste tutorial vou explicar como fazer o seu primeiro dispositivo de assinatura airgap, desconectado da Internet, mesmo sem ter um Hardware Wallet dedicado. Tudo o que precisa é de ter dois computadores disponíveis:




- um dispositivo antigo seja impedido para sempre de se ligar à Internet;
- o seu computador de uso diário.



Esta configuração permite um maior grau de segurança do que o clássico `Hot Wallet`: o computador antigo - sem ligação à rede - é o guardião das suas chaves privadas, que nunca são expostas na Internet, mas armazenadas offline ("airgap" ou "Cold").



Em vez disso, instalará um ecrã Wallet ("watch-only") no seu computador diário, que está ligado à rede e com o qual pode, por exemplo, verificar saldos e preparar transacções de recibos.



## Wallet Airgap: O quê e como



Ao seguir os passos deste guia, instalaremos dois Software Wallet Electrum em dois computadores diferentes e, finalmente, criaremos duas carteiras com armazenamentos de chaves diferentes: o Wallet airgap utilizará toda a hierarquia do Wallet HD, enquanto o Wallet display será gerado com a chave pública mestra.



Estas duas carteiras serão, em todos os aspectos, muito diferentes uma da outra. A única coisa que terão em comum, como veremos, são os endereços:




- o gW-13 no computador airgap só pode assinar mas, desligado da rede, não conhece o saldo e os endereços utilizados;
- o Wallet no computador diário só poderá preparar e propagar transacções, sem poder dispor das despesas, na ausência das chaves privadas.



## Preparação preliminar



Para descarregar o Electrum, recomendo que siga os primeiros passos deste tutorial:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Depois de fazer o download, verifique sempre a versão antes de a instalar e, em seguida, proceda à configuração "One Server", tal como se encontra na secção de ajuda, em `Start with a Dummy Wallet`.



A operação de configuração "One Server" só é necessária para o Wallet instalado no computador diário, uma vez que o outro computador estará sempre offline.



As operações seguintes envolvem a prática em dois computadores (e carteiras) diferentes, por isso - por conveniência e concentração - optei por definir o airgap do Wallet com o tema claro, enquanto o ecrã do Wallet tem o tema escuro.



## Wallet Criação de um Airgap



Depois de descarregar e verificar a transferência de Electrum, tire uma cópia do executável e coloque-a no seu computador offline. Em seguida, inicie-o e instale Electrum.



Faça duplo clique para iniciar o Electrum: o computador onde vai utilizar este Wallet está offline, ignore as definições de rede e vá para a criação do Wallet que, neste guia, chamaremos de `airgap`.



![image](assets/en/01.webp)



Selecionar _Carteira normalizada_.



![image](assets/en/02.webp)



E, em seguida, selecione _Criar uma nova semente_ para que o software generate o Mnemonic.



![image](assets/en/03.webp)



Transcrever com exatidão as 12 palavras generate do Electrum para um suporte de papel e prosseguir com a etapa de verificação, reintroduzindo as palavras por ordem quando o Electrum o solicitar.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Após a conclusão da criação do Wallet, defina uma senha complexa (`Strong`) para criptografar o arquivo Wallet no dispositivo airgap. Este passo é muito delicado e importante, pois a senha escolhida agora, impede o acesso ao Wallet que tem poder dispositivo, podendo gastar fundos assinar transações.



![image](assets/en/06.webp)



Ao clicar em _Finish_, o Wallet é definido e aparece no ecrã. Naturalmente, o indicador de ligação à rede, ou seja, o ponto colorido no canto inferior direito, está vermelho, pois o computador está desligado e não permite que o Wallet exponha as teclas online.



![image](assets/en/07.webp)



## Criação Wallet de Visualização



Agora que o seu Wallet tem chaves privadas offline, é necessário configurar um Wallet de visualização, ou "apenas relógio", que lhe permitirá ver o saldo, bem como preparar transacções de recibos para continuar a acumular Sats em segurança.



A partir do Wallet localizado no dispositivo offline, selecionar o menu _Carteira_ -> _Informação_



![image](assets/en/08.webp)



Aparecerá a janela que contém todas as informações do Wallet, onde pode verificar o "caminho de derivação" e a "impressão digital do mestre", por exemplo, para os marcar ao lado das palavras na frase do Mnemonic (fortemente recomendado).



![image](assets/en/09.webp)



Lembre-se que está a obter estes dados a partir de um computador não ligado, pelo que terá de copiar/colar o `zpub` para um ficheiro de texto e guardá-lo numa pen USB.



Agora pode passar para o computador ligado à Internet, para lançar o Electrum e criar um novo Wallet.



No menu _File_, selecione _New/Restore_.



![image](assets/en/10.webp)



O novo Wallet é apenas de visualização, por isso, neste guia, chamar-lhe-emos `watch-only`.



![image](assets/en/12.webp)



No ecrã seguinte, escolha _Carteira normal_ e clique em _Próximo_.



![image](assets/en/13.webp)



Ao escolher o `Keystore` tenha cuidado: para criar o display Wallet selecione _Usar uma chave mestra_. De seguida, avançar com _Próximo_.



![image](assets/en/14.webp)



Cole aqui o `zpub` copiado do Wallet offline e que você trouxe para este computador via mídia usb.



![image](assets/en/15.webp)



Conclua definindo uma palavra-passe forte também para este Wallet, possivelmente diferente da escolhida para o Cold correspondente.



Aparecerá o ecrã Wallet, com um aviso. A mensagem recorda-lhe que se trata de um Wallet apenas para visualização e que não pode, com ele, gastar os fundos associados.



**Nota bem**: **você precisará, portanto, de possuir sempre as chaves privadas para dispor dos UTXOs deste Wallet**. Com um bom sistema de backup, não será difícil para si manter a posse total dos seus Bitcoins.



![image](assets/en/16.webp)



Este aviso aparecerá sempre que abrir este Wallet. Clique em _Ok_ e passemos à etapa de verificação.



## Verificação dos dois Wallet



Como aprendemos no início deste guia, um airgap Wallet e o seu ecrã Wallet são duas carteiras que têm faculdades diferentes mas **partilham os mesmos endereços**.



Se olharmos para as duas carteiras lado a lado, visualmente reparamos que na Wallet airgap existe um símbolo "seed", enquanto na watch-only não existe. Mesmo este pormenor ajudá-lo-á a lembrar-se de que o mostrador Wallet não tem chaves privadas.



![image](assets/en/17.webp)



No entanto, para fazer uma primeira verificação precisa, selecione em ambas as carteiras o menu `Endereços`: uma vez que partilham os mesmos endereços, a lista de endereços deve ser idêntica em ambas.



![image](assets/en/18.webp)



⚠️ **ATENÇÃO**: **não pode haver meio-termo; os endereços têm de ser os mesmos. Se forem diferentes, é necessário apagar todo o trabalho efectuado até agora e começar de novo**.



Agora pode proceder a duas verificações diferentes. Primeiro, tente apagar as duas Carteiras e restaurá-las de raiz, cada uma no computador apropriado. No caso de proceder a esta verificação, os procedimentos para a visualização do Wallet são idênticos aos descritos acima.



Para o Wallet airgap, no entanto, no ecrã `keystore` terá de escolher _Já tenho uma semente_ e introduzir as palavras copiando-as da sua cópia de segurança em papel.



Após o fim do período experimental "sem carregamento", pode tentar efetuar uma transação de um pequeno montante e gastá-lo imediatamente.



## Transacções de receção e de despesa



Para começar a usar o seu Electrum airgap, pode fazer uma transação de recibo com uma pequena quantia e depois gastá-la num Address seu. Poderá então familiarizar-se com o procedimento, verificando que tem o controlo total dos fundos.



**Nota**: Não recomendo que deposite uma grande quantidade de fundos no Wallet antes de ter a certeza de que pode efetuar todas as operações sem problemas.



As etapas explicadas abaixo podem, à primeira vista, parecer complicadas. Não se deixe abater: depois de as tentar pela primeira vez, verá que demoram apenas alguns minutos a concluir.



Para receber os fundos, deve necessariamente utilizar o ecrã Wallet situado no seu computador ligado à Internet. No menu `Receber` clique em _Criar pedido_ para que o Electrum generate seja o primeiro Address disponível e o utilize para nos enviar alguns Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Uma vez propagada a transação, já se pode ver que - como é natural - ela só é visível no visor Wallet e não no airgap Wallet.



![image](assets/en/21.webp)



Depois de a sua transação ter recebido alguma confirmação, pode preparar a despesa e, assim, tentar o procedimento de assinatura a partir do Wallet fora da rede. Em seguida, prepare a transação no watch-only e prima _Preview_ para a verificar



![image](assets/en/22.webp)



A janela de transação avançada permite-lhe ver isso:




- a transação não está assinada (`Status: Unsigned);
- os comandos `Sign` e `Broadcast` são inibidos.



A única coisa que pode fazer é exportar a transação tal como está, levá-la ao Wallet airgap e assiná-la.



Introduza uma unidade flash USB no seu computador e, no menu do canto inferior esquerdo, selecione _Compartilhar_.



![image](assets/en/23.webp)



Em seguida, selecione _Guardar no ficheiro_.



![image](assets/en/24.webp)



Guardar a transação na pen USB.



Notará que Electrum dá ao ficheiro um nome com os primeiros dígitos de transaction ID, e a extensão do ficheiro é `.PSBT`, o que significa `Partially Signed Bitcoin Transaction`.



Extraia o suporte de dados com o ficheiro `.PSBT` e ligue-o ao computador offline.



A partir do Wallet, selecionar o menu _Ferramentas_, depois _Carregar transacção_ e a seguir De ficheiro_.



![image](assets/en/25.webp)



Com o gestor de ficheiros, selecione `.PSBT` a partir da sua localização.



![image](assets/en/29.webp)



O software do computador fora da rede abrirá automaticamente a janela de transação avançada, completamente idêntica à que viu no ecrã do Wallet. O estado é "Não assinado", mas a diferença é que aqui o comando "Assinar" está ativo. E é exatamente isso que terá de executar.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Agora que a transação está assinada, lembre-se que seu Wallet está em uma máquina offline. Portanto - mesmo que você veja o comando `Broadcast` ativo - seu Wallet não será capaz de propagar a transação para a rede Bitcoin.



O que é preciso fazer agora é repetir a operação de exportação da transação assinada para a pen USB, de modo a poder importá-la para um computador ligado à Internet e propagá-la.



No menu inferior esquerdo, selecione novamente _Compartilhar_ e, em seguida, _Guardar em ficheiro_.



![image](assets/en/28.webp)



Agora o ficheiro tem uma extensão diferente: **em vez de `.PSBT` agora a transação tem a extensão `.txn`. De agora em diante é assim que Electrum vai permitir que você reconheça as transações assinadas das não assinadas**.



![image](assets/en/30.webp)



Para a propagação final da transação, retire a pen usb do computador off-line e insira-a no computador ligado à Internet.



A partir do watch-only, repetir o procedimento de importação, ou seja, no menu _Tools_ selecionar _Load transaction_ e finalmente _From file_.



![image](assets/en/31.webp)



Electrum abrirá a janela da transação para você, marcadamente diferente da mostrada anteriormente neste Wallet, pois agora está assinada (`Status: Signed`) e o comando `Broadcast` está acessível.



A última operação que precisa de fazer é exatamente essa:



![image](assets/en/32.webp)



## Conclusões



Os seus testes estão agora terminados. Se seguiste o guia e obtiveste os mesmos resultados, criaste um Wallet Cold com Electrum, em dois computadores diferentes, que podes usar em modo airgap para armazenar os teus Bitcoins.



As únicas coisas a que terá de prestar muita atenção são duas:


1) **nunca utilizar o airgap Wallet para endereços de receção generate**. Uma vez que está offline, oferecer-lhe-á sempre o primeiro Address, que coincide com o que acabou de utilizar para efetuar a transação de teste;



![image](assets/en/33.webp)



como se pode ver na imagem acima, o Wallet offline não conhece a sua própria história do Address. É totalmente cego a este respeito. **A única tarefa que pode fazer por si é armazenar as suas chaves offline e assinar as suas transacções**_.



2) Utilizar uma unidade flash USB dedicada apenas a este fim, **não utilizar um meio que utilize frequentemente**. As ferramentas quotidianas são mais susceptíveis de serem alvo de ciberataques e, involuntariamente, pode atacar até o computador que mantém desligado da rede. Uma pen USB que utilize apenas para este fim tem muito poucas oportunidades de entrar em contacto com o seu PC online, especialmente se for um hodler que não tem de gastar, reduzindo assim a probabilidade de receber e depois transmitir vírus, malware, etc.