---
name: JoinMarket

description: Guía y tutorial sobre cómo utilizar JoinMarket para hacer CoinJoin sobre Bitcoin a través de la línea de comandos
---

![cover](assets/cover.webp)



---

Si ha encontrado esta página buscando "JoinTmarket" en Internet, le expreso mi más sincero agradecimiento. Sin embargo, has tropezado con una guía que trata un tema completamente diferente, ¡pero extremadamente interesante! 🚬🍁



El objetivo de este tutorial es ilustrar el funcionamiento teórico y práctico de JoinMarket, a través de la línea de comandos. 🐢 💚



## Definición teórica de JoinMarket



Podemos definir JoinMarket como una herramienta, o una Wallet, que permite CoinJoin con otros usuarios de forma totalmente Trustless y sin ningún coordinador central.



Dado que toda la parte teórica de esta herramienta es extremadamente amplia, decidí Address en un episodio específico de mi podcast. Para aquellos que puedan entender el italiano, recomiendo encarecidamente seguir leyendo después de escuchar el episodio, a fin de asimilar mejor los conceptos básicos para utilizar correctamente este programa.



Puede ponerse al día con el episodio en estos enlaces directos:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (aquí puede escucharlo directamente desde el navegador).
- [Antenna pod](https://antennapod.org/) es un gestor de podcasts gratuito y de código abierto que no requiere registro. Para encontrar el episodio descarga la app, añade manualmente mi podcast pegando [este enlace](https://Anchor.fm/s/bd5d5b20/podcast/rss) en la sección _feed rss_, luego busca el episodio dedicado a JoinMarket.



## Instalación



Sistemas operativos:





- Raspiblitz
- Paraguas
- MiNodo
- Raspibolt



## Archivos de configuración



JoinMarket es un software personalizable con un número infinito de ajustes; estos ajustes se especifican en un archivo de configuración ubicado en el directorio principal del programa llamado `Joinmarket.cfg`.



En esta sección vamos a repasar algunos campos que puede resultarte interesante explorar y/o modificar, en función de tus necesidades. Me gustaría destacar que todas las modificaciones que se indican a continuación son útiles de conocer para adaptar el funcionamiento del software a las necesidades personales, sin ser obligatorias.



Primero vamos a la carpeta `joinmarket/scripts` y ejecutamos el comando:



```bash
python wallet-tool.py generate
```


En este punto deberíamos obtener un error, pero hacerlo hará que el software generate un archivo de configuración preestablecido para nosotros. Podemos ir y editar el archivo de configuración desde el terminal con:



```bash
nano joinmarket.cfg
```



o:



```bash
vim joinmarket.cfg
```



una vez abierto observaremos numerosas líneas con diversas configuraciones y su explicación en inglés. En concreto analizaremos a continuación las variables más interesantes:





- `merge_algorithm` en caso de que lo hagamos como fabricante este campo ajusta la agresividad con la que el software consolidará las Salidas no gastadas. En caso de que tengamos muchos UTXOs que consolidar, podría tener sentido cambiar de _gradual_ a _greedy_
- `tx_fees` ajusta como tomador las tasas con las que pagar la transacción, es muy útil cambiar esta configuración en caso de que uses el tumbler a menudo (hablaremos de esto más adelante) ya que si hay un pico en las tasas durante la ejecución de esta, si no configuramos este campo correctamente, nos arriesgamos a gastar muchos Sats por CoinJoin. Si fijamos valores en miles (como 2000), esto equivaldrá a 2 Sats/vBytes, 3500 a 3,5 Sats/vBytes, y así sucesivamente. Yo recomendaría un número entre 1500 y 6000 en función de tus necesidades.
- `max_cj_fee_abs` se utiliza para especificar cuánto estamos dispuestos a pagar en términos absolutos por los makers que elijamos durante CoinJoin. Por defecto este campo para los creadores es de 200 Sats, una buena opción podría ser un número que oscile entre 200 y 1000 Sats por contrapartida (esto se basa en cuánto quieres gastar y cuánto anon-set buscas para tus CoinJoins)
- `max_cj_fee_rel` tiene la misma función que el campo anterior pero especifica las comisiones relativas (porcentajes) que estamos dispuestos a pagar a cada contrapartida. Como se trata de un valor `porcentual`, ten cuidado de no establecer valores altos para evitar costes elevados en CoinJoins con grandes cantidades. El valor por defecto para los makers es _0.00002_, recomiendo un valor similar o ligeramente superior.
- `minimum_makers` es el campo que especifica con cuantas otras contrapartes hacemos CoinJoin, por defecto joinMarket siempre elige de 4 a 9 contrapartes, si queremos, para mayor privacidad, podemos subir este valor a 5 o 6 (aunque encarecerá las transacciones).
- `cjfee_a` especifica, en caso de que actuemos como maker, cuantos Sats en términos absolutos queremos cobrar por alquilar nuestra liquidez. Este campo es totalmente subjetivo, el valor por defecto ya es muy bueno (tendremos así mejor privacidad como maker) podemos considerar llevarlo a 0 si queremos ganar más CoinJoin en menos tiempo.
- igual que en el campo anterior, pero en términos porcentuales y no absolutos. De nuevo recomiendo dejar el valor por defecto o bajarlo para atraer a más tomadores.
- `ordertype` con este campo elegimos desde maker si cobrar de forma absoluta (absoffer) o porcentual (reloffer). Normalmente los tomadores prefieren ofertas absolutas para temas económicos.
- `minsize` si como creador no queremos tener UTXO demasiado pequeños podemos especificar el CoinJoin mínimo para participar. Este campo se expresa en Satoshi y es totalmente subjetivo. Podríamos dejar este campo a 0 o aumentarlo a 500000 (Sats), 1000000 (Sats), y así sucesivamente.



Tenga mucho cuidado de no editar los campos equivocados, algunas de las variables del archivo joinmarket.cfg si se configuran incorrectamente podrían comprometer la funcionalidad del software o aniquilar completamente su privacidad, ¡ojo y precaución al máximo!



## Configuración del entorno de trabajo



Algunos nodos establecen automáticamente los valores correctos para estos campos dentro del archivo joinmarket.cfg, recomiendo volver a comprobarlo manualmente:





- rpc_user = tu-nombre-deusuario-como-en-Bitcoin.conf
- `rpc_password = tu-contraseña-como-en-Bitcoin.conf`
- `rpc_host = localhost #por defecto suele ser correcto`
- `rpc_port = 8332 # por defecto para Mainnet`



En este punto podemos proceder a la creación de nuestro Wallet dentro de JoinMarket:



```bash
python wallet-tool.py generate
```



Este comando nos hará introducir una contraseña con la que encriptar el Wallet y el nombre que queremos darle, cuando te pregunte si quieres o no soportar bonos de fidelidad te recomiendo usar la opción _yes_, la salida devuelta tendrá este aspecto:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


en caso de que aparezca un error lo más probable es que hayamos configurado incorrectamente los 4 campos RPC especificados anteriormente. En caso de que pueda ayudar a seguir [esta guía](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) que se encuentra en la documentación original JoinMarket.



Hemos completado la configuración de nuestro entorno de trabajo y podemos empezar a explorar los comandos que nos serán más útiles. Todos los scripts que discutiremos pueden ser lanzados en la consola seguidos de `--help` para una explicación en profundidad.



Ahora podemos intentar el lanzamiento:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



este comando le mostrará todos los mixdepths de las distintas carteras con las distintas direcciones categorizadas como:




- Nuevo (Address nunca usado)
- Change-out (resto de una transacción anterior)
- Cj-out (salida de un CoinJoin)



he aquí un ejemplo práctico del resultado:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Ahora podemos proceder a depositar nuestros primeros Satoshis dentro de una o más direcciones recordando que independientemente del creador o tomador, el software nunca irá a consolidar UTXO en diferentes mixdepths directamente, de esta manera podemos mantener Satss con diferentes niveles de privacidad separados dentro de Wallet.



## Envío de Bitcoin con CoinJoin Individual



Ahora podemos mover nuestros Satoshis. Uno de los principales comandos de este software es el script:



```bash
pyhton sendpayment.py
```


que nos permitirá enviar transacciones a otras direcciones con o sin CoinJoin. Vamos a ver cómo funciona y algunos ejemplos prácticos. Por defecto el formato del comando es (recuerde sustituir el texto encerrado por los símbolos < y >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



un ejemplo básico de uso podría ser:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


en este caso vamos a enviar al Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc es decir 5000000 Satoshi de nuestro mixdepth 0 (el predeterminado) yendo a elegir de 4 a 9 contrapartidas para CoinJoin (opción por defecto).



Para tener más control sobre cómo y qué UTXOs gastar podemos repasar las opciones adicionales a este comando:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


en este ejemplo hemos añadido dos especificaciones: -N indica con cuántas contrapartidas vamos a mezclar, -m el mixdepth del que vamos a retirar fondos. De hecho, hemos enviado 100.000.000 Sats (1 btc) a la Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c con los fondos en mixdepth 1 y mezclando con 5 contrapartidas.



Si ponemos 0 como valor de envío especificando un mixdepth, joinMarket realizará el llamado `sweep`, es decir, enviará todos los fondos de ese mixdepth consolidándolos entre sí:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



aquí enviamos todos los fondos de mixdepth 0 (podríamos no haberlo especificado porque es el valor por defecto) mezclando con 7 contrapartidas.



El comando sendpayment se utiliza para mover fondos de joinMarket a Wallet externas o para enviar Satoshi a una persona añadiendo una Layer de privacidad entre nosotros y ella. Para obtener un nivel suficiente de privacidad en nuestros UTXOs es más apropiado utilizar el comando tumbler.py que explicaremos más adelante en esta guía.



## Ser fabricante



El script que vamos a cubrir en esta sección es:



```bash
yg-privacyenhanced.py
```



Este programa se utiliza para actuar como maker en el joinMarket. El programa se conectará a nuestro nodo Bitcoin y al mercado interno de la plataforma en el que los makers se presentan como ofertantes de liquidez y los takers buscan contrapartidas. En caso de que desee utilizar un bono de fidelidad puede crear uno con este formato:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



por ejemplo:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



la salida que se nos devolverá será una Bitcoin Address (es decir, aquella en la que tendrá que depositar los fondos que desea asignar a fidelity).



**Precaución**: Hay dos cosas a las que debe prestar mucha atención si va a crear un Bono de Fidelidad (también conocido como FB);





- una vez depositados los fondos, no se pueden volver a mover hasta que caduque. Presta atención a cuántos Satss envías al Address y cómo formateas la fecha. ¡No se admiten errores!
- El bono de fidelidad es fácilmente reconocible onchain, por lo que es recomendable depositar los fondos a través de un CoinJoin y con un origen ajeno a tu identidad. Lo mismo también es recomendable hacer una vez quieras mover el bono de fidelidad caducado fuera de JoinMarket.



Es importante recordar que es posible recargar el bono de fidelidad con una sola transacción, en caso de UTXO múltiples sólo la mayor se considerará válida para FB.



Tratemos ahora el script mencionado al principio de este párrafo, una vez creado el bono de fidelidad (que recordemos es opcional) estamos listos para ejecutar el ejecutable para actuar como maker en joinMarket. Una vez depositados los Satss en las distintas direcciones y mixdepth podemos ejecutar el comando:



```bash
python yg-privacyenhanced.py <wallet name>
```



A partir de este momento (tras unos minutos de conexión a la red) y hasta que detengamos el script, nuestro cliente JoinMarket aparecerá en la lista de makers activos en el protocolo y ofrecerá nuestra liquidez a diversas contrapartidas para realizar CoinJoin. No esperes docenas de CoinJoins al día (a no ser que tengas una gran fidlidad y mucha liquidez depositada en Wallet), recuerda también que factores como las comisiones requeridas y los Satoshis depositados afectan a la frecuencia con la que serás maker.



Ejecutando el siguiente comando podrá ver el historial de todas las transacciones realizadas en Wallet y cualquier ganancia (si es un creador) o gasto por comisiones (si es un tomador) que haya tenido a lo largo de la vida de la cartera.



```bash
python wallet-tool.py <wallet name> history
```



Una vez que tus Satoshis hagan CoinJoins, se moverán de mixdepth en mixdepth hasta llegar al último. Una vez pasado el cuarto volverán a mixdepth 0, depende de ti cuánta privacidad conseguir antes de moverlos a un Cold Wallet, es aconsejable terminar un ciclo completo Wallet.



## Vaso



Por fin llegamos a la parte más jugosa de JoinMarket, ¡el tumbler! Si has escuchado el podcast ya sabes de qué va esto. Una recomendación antes de empezar: **¡Cuidado con las comisiones!** Recuerda establecer los límites en el archivo joinmarket.cfg (como se explica al principio) y considera ejecutar el programa sólo cuando las comisiones onchain sean relativamente bajas (por debajo de 10 Sats/vB).



Para lanzar la secadora es necesario haber detenido el script de maker (si estaba activo), después de eso podemos ejecutar el comando:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Es esencial introducir **al menos** 3 direcciones de salida para la secadora: esto es para asegurar una buena privacidad y no crear enlaces obvios entre UTXOs a lo largo del proceso. Como siempre, añadiendo `--help` al comando puedes ver todos los detalles adicionales. Vamos a ver un ejemplo más complejo con reglas avanzadas:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



En este caso hemos lanzado un script de tumbling que no utilizará el número de contrapartidas por defecto (el parámetro -N indica que necesitamos 7 contrapartidas con una varianza máxima de 2, por lo que un número aleatorio de hacedores de 5 a 9) y con un mayor número de CoinJoin por mixdepth (por defecto este script hace un número aleatorio de CoinJoin por sección de Wallet que va de 1 a 3, utilizando el comando -c 3 1 en su lugar será de 2 A 4). De esta forma gastaremos más Sats en tasas pero tendremos un conjunto de anonimato mayor.



También puede añadir tantas direcciones de salida como desee (mínimo 3, no hay más máximo que el sentido común). Sin embargo, no es posible, por cuestiones de privacidad, decidir cómo se distribuirá Satoshi entre las direcciones especificadas como salida.



Tumbler es un proceso deliberadamente largo, ocasionalmente puede ocurrir que algo deje de funcionar, en la mayoría de los casos esto se resolverá por sí mismo en unas pocas horas. En caso de caída total podemos intentar reiniciarlo con el comando:



```bash
python tumbler.py --restart
```



O simplemente reinicie una nueva orden de volteo. Esto no iniciará la programación de la volteadora anterior pero iniciará un nuevo ciclo de mezcla. En caso de que al cerrar el terminal SSH de su nodo también se detenga el script puede aprovechar el programa `TMUX` que puede instalarse con el comando:



```bash
sudo apt install tmux
```



Si lo ejecutas desde el shell tecleando `tmux` se te abrirá un terminal que permanecerá activo en segundo plano aunque cierres la conexión remota. Cuando te vuelvas a conectar a tu nodo con el comando `tmux attach` volverás a abrir la shell que permanecía activa en segundo plano.



## Conclusión



JoinMarket es un software ilimitado y personalizable. En esta guía hemos descubierto las principales funciones para que sea posible que cualquiera (o al menos yo lo he intentado, soy consciente de que usar este software no es un paseo por el parque) pueda usarlo. Uno de los mayores problemas de JoinMarket es precisamente ese: el número de personas que lo utilizan y que son creadores. Si pocos usuarios se aprovechan de este software, la privacidad general (anon-set) se reduce. Por eso espero que esta guía incentive el uso y te convenza de descargar e instalar mi software favorito para hacer CoinJoin. En caso de que quieras profundizar aún más en algunos aspectos te recomiendo que le des una leída a los diversos docs en profundidad en github, están vermanete bien hechos y los puedes encontrar aquí.



¡Feliz mezcla de tortugas!🐢💚



[Aquí](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) puedes apoyar a Turtlecute