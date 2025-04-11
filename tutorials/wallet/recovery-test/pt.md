---
name: Teste de Recuperação
description: Como testar seus backups para garantir que você não perca seus bitcoins?
---
![cover](assets/cover.webp)

Ao criar uma carteira Bitcoin, é solicitado que você anote uma frase mnemônica, geralmente consistindo de 12 ou 24 palavras. Esta frase permite que você recupere o acesso aos seus bitcoins em caso de perda, dano ou roubo do dispositivo que hospeda sua carteira. Antes de começar a usar sua nova carteira Bitcoin, é muito importante verificar a validade desta frase mnemônica. A melhor maneira de fazer isso é realizando um teste de recuperação em seco.

Este teste envolve simular uma restauração da carteira antes de depositar quaisquer bitcoins nela. Enquanto a carteira estiver vazia, simulamos uma situação em que o dispositivo que hospeda nossas chaves é perdido, e tudo o que nos resta é nossa frase mnemônica para tentar recuperar nossos bitcoins.

![TESTE DE RECUPERAÇÃO](assets/notext/01.webp)

## Qual é o propósito?

Este processo de teste permite verificar se o backup físico da sua frase mnemônica, seja em papel ou metal, é funcional. Uma falha durante este teste de recuperação indica um erro no backup da frase, colocando seus bitcoins em risco. Por outro lado, se o teste for bem-sucedido, confirma que sua frase mnemônica está totalmente operacional, e você pode então assegurar bitcoins com tranquilidade usando esta carteira.

Realizar um teste de recuperação em seco tem uma dupla vantagem. Não só permite verificar a precisão da sua frase mnemônica, mas também oferece a oportunidade de se familiarizar com o processo de recuperação da carteira. Desta forma, você descobrirá potenciais dificuldades antes que uma situação real se apresente a você. No dia em que realmente precisar recuperar sua carteira, você estará menos estressado, pois já conhecerá o processo, reduzindo o risco de erro. É por isso que é importante não negligenciar esta etapa de teste e tomar o tempo necessário para fazê-lo corretamente.

## O que é um teste de recuperação?

O processo do teste é bastante simples:
- Após criar sua nova carteira Bitcoin, e antes de depositar seus primeiros satoshis, anote uma informação testemunha, como um xpub, o primeiro endereço de recebimento, ou até mesmo a impressão digital da chave mestra;
- Em seguida, delete deliberadamente a carteira ainda vazia, por exemplo, redefinindo sua carteira de hardware para as configurações de fábrica;
- Depois, simule uma recuperação da sua carteira usando apenas os backups em papel da sua frase mnemônica e sua passphrase, caso você use uma;
- Finalmente, verifique se a informação testemunha corresponde à da carteira regenerada. Se a informação coincidir, você pode ter certeza da confiabilidade do seu backup físico, e então enviar seus primeiros bitcoins para esta carteira.
Cuidado, durante um teste de recuperação, **você deve usar o mesmo dispositivo destinado à sua carteira final**, a fim de não aumentar a superfície de ataque da sua carteira. Por exemplo, se você criar uma carteira em um Trezor Safe 5, certifique-se de realizar o teste de recuperação neste mesmo Trezor Safe 5. É importante não inserir sua frase de recuperação em nenhum outro software, pois isso comprometeria a segurança fornecida pela sua carteira de hardware, mesmo que a carteira ainda esteja vazia.

## Como realizar um teste de recuperação?

Neste tutorial, explicarei como realizar um teste de recuperação em uma carteira de software Bitcoin, usando o Sparrow Wallet (para uma carteira quente). No entanto, o processo permanece o mesmo para qualquer outro tipo de dispositivo. Novamente, **se você estiver usando uma carteira de hardware, não realize o teste de recuperação no Sparrow Wallet** (veja a seção anterior).
Acabei de criar uma nova carteira quente no Sparrow Wallet. No momento, ainda não enviei nenhum bitcoin para ela. Está vazia.
![RECOVERY TEST](assets/notext/02.webp)

Anotei cuidadosamente minha frase mnemônica de 12 palavras em um pedaço de papel. E, como quero aumentar a segurança desta carteira, também configurei uma passphrase BIP39 que salvei em outro pedaço de papel:

```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```

```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```

***Obviamente, você nunca deve compartilhar sua frase mnemônica e sua passphrase na internet, ao contrário do que estou fazendo neste tutorial. Esta carteira de exemplo não será usada e será deletada ao final do tutorial.***

Agora, vou anotar em um rascunho uma peça de informação de testemunha da minha carteira. Você pode escolher diferentes peças de informação, como o primeiro endereço de recebimento, o xpub ou a impressão digital da chave mestra. Pessoalmente, recomendo escolher o primeiro endereço de recebimento. Isso permite verificar se você é capaz de encontrar o caminho completo da primeira derivação que leva a este endereço.

No Sparrow, clique na aba "*Addresses*".

![RECOVERY TEST](assets/notext/03.webp)

Então, anote em um pedaço de papel o primeiro endereço de recebimento da sua carteira. No meu exemplo, o endereço é:

```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```

Após anotar a informação, vá ao menu "*File*", então selecione "*Delete Wallet*". Lembro-lhe mais uma vez que sua carteira Bitcoin deve estar vazia antes de prosseguir com esta operação.

![RECOVERY TEST](assets/notext/04.webp)

Se sua carteira estiver realmente vazia, confirme a exclusão da sua carteira.

![RECOVERY TEST](assets/notext/05.webp)

Agora você precisa repetir o processo de criação da carteira, mas usando nossos backups de papel. Clique no menu "*File*" e depois em "*New Wallet*".

![RECOVERY TEST](assets/notext/06.webp)

Digite novamente o nome da sua carteira.

![RECOVERY TEST](assets/notext/07.webp)

No menu "*Script Type*", você precisa escolher o mesmo tipo de script da carteira que você deletou anteriormente.

![RECOVERY TEST](assets/notext/08.webp)

Então clique no botão "*New or Imported Software Wallet*".

![RECOVERY TEST](assets/notext/09.webp)

Selecione o número correto de palavras para a sua semente.

![RECOVERY TEST](assets/notext/10.webp)

Digite sua frase mnemônica no software. Se uma mensagem "*Invalid Checksum*" aparecer, isso indica que o backup da sua frase mnemônica está incorreto. Você então terá que começar a criação da sua carteira do zero, pois seu teste de recuperação falhou.

![RECOVERY TEST](assets/notext/11.webp)

Se você tem uma passphrase, como no meu caso, também a insira.

![RECOVERY TEST](assets/notext/12.webp)

Clique em "*Create Keystore*", depois em "*Import Keystore*".

![RECOVERY TEST](assets/notext/13.webp)

E finalmente, clique no botão "*Apply*".

![RECOVERY TEST](assets/notext/14.webp)

Você pode agora retornar à aba "*Addresses*".

![RECOVERY TEST](assets/notext/15.webp)
Finalmente, verifique se o primeiro endereço de recebimento corresponde ao que você havia anotado como testemunha em seu rascunho.
![RECOVERY TEST](assets/notext/16.webp)

Se os endereços de recebimento coincidirem, seu teste de recuperação foi bem-sucedido, e você pode usar sua nova carteira Bitcoin. Se eles não coincidirem, isso pode indicar ou um erro na escolha do tipo de script, o que torna o caminho de derivação incorreto, ou um problema com o backup da sua frase mnemônica ou da sua passphrase. Em ambos os casos, eu recomendo fortemente começar do zero e criar uma nova carteira Bitcoin desde o início para evitar qualquer risco. Desta vez, tenha o cuidado de anotar a frase mnemônica sem erros.
Parabéns, você agora está por dentro de como conduzir um teste de recuperação! Aconselho que generalize este processo para a criação de todas as suas carteiras Bitcoin. Se você achou este tutorial útil, eu ficaria grato se você pudesse deixar um joinha abaixo. Sinta-se livre para compartilhar este artigo em suas redes sociais. Muito obrigado!