---
name: Electrum OP_RETURN
description: Registra un messaggio su Blockchain Bitcoin con Electrum
---

![cover](assets/cover.webp)




Questa esercitazione mostra passo dopo passo come scrivere un messaggio sul Blockchain Bitcoin utilizzando il Wallet Electrum. Questa operazione utilizza l'istruzione OP_RETURN per inserire un testo in una transazione, visibile pubblicamente sul Blockchain. Seguite questi semplici passaggi per una registrazione di successo.



---
## Prerequisiti





- Un computer (Windows, macOS o Linux).
- Connessione a Internet.
- Alcuni satoshis (Sats) o bitcoin (BTC) nel vostro Wallet per coprire l'importo della transazione e le spese.
- Un convertitore da testo a esadecimale (ad esempio un sito online) o uno strumento dedicato come [questo generatore di script OP_RETURN](https://resources.davidcoen.it/opreturnelectrum/).



---

## Passo 1: Scaricare e installare Electrum



![image](assets/fr/01.webp)



1. Visitate il sito web ufficiale di Electrum: [electrum.org](https://electrum.org/).


2. Scaricare la versione corrispondente al proprio sistema operativo (Windows, macOS, Linux).


3. Installare Electrum seguendo le istruzioni del programma di installazione.


4. Verificare l'integrità del file scaricato (facoltativo, ma consigliato per motivi di sicurezza) confrontando la firma del file o il Hash.



→ Maggiori dettagli sul tutorial Electrum :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Passo 2: Creare o importare un Wallet



1. Avviare Electrum.


2. Scegliere Crea un nuovo Wallet o Ripristina un Wallet esistente se si dispone già di una frase seed (frase di ripristino).


3. Seguire le istruzioni per configurare il Wallet :




 - Per un nuovo Wallet, annotate la vostra frase seed e conservatela in un luogo sicuro (carta, cassaforte, ecc.).
 - Per un Wallet esistente, inserire la frase seed per ripristinarlo.


4. Impostare una password per proteggere il Wallet.



→ Maggiori dettagli sul tutorial Electrum :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Fase 3: Verifica dei fondi disponibili



Assicuratevi che il vostro Wallet contenga abbastanza bitcoin (BTC) o satoshis (Sats) per :




- Importo della transazione (ad esempio, 0,00001 BTC o 1000 Sats).
- Le commissioni di transazione, che variano a seconda delle dimensioni della rete (generalmente qualche migliaio di Sats).



Consultare il Saldo in Electrum per verificare i propri fondi.



![image](assets/fr/02.webp)



Se necessario, trasferire BTC o Sats per alimentare il Wallet. Per farlo, andare alla scheda "Ricezione" e cliccare su "Crea richiesta":



![image](assets/fr/03.webp)



Questo mostrerà una ricezione Address:



![image](assets/fr/04.webp)



→ Maggiori dettagli sul tutorial Electrum :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Fase 4: preparazione del messaggio da iscrivere



Selezionare il messaggio che si desidera inserire (ad esempio, `Grazie Satoshi`). Nota: i messaggi del OP_RETURN sono limitati a 80 byte, cioè a circa 80 caratteri ASCII.



*Riflettete un attimo: ciò che scrivete sul Blockchain Bitcoin è eterno e accessibile a tutti, perciò :*




- lasciare una bella espressione della nostra umanità,
- evitate di inserire contenuti di cui potreste pentirvi



*Lo spazio Blockchain e i vostri bitcoin sono preziosi, usateli con saggezza e intenzione*



Convertire il messaggio in esadecimale :




- Potete utilizzare uno [strumento online](https://www.rapidtables.com/convert/number/ascii-to-hex.html), ma fate attenzione a non trattarvi dati sensibili (anche se, in linea di principio, le informazioni destinate alla pubblicazione su Blockchain Bitcoin tramite un OP_RETURN non presentano problemi di riservatezza);
- Per una maggiore riservatezza, eseguire la conversione localmente utilizzando un piccolo file Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Esempio: `Grazie Satoshi` in ASCII dà `5468616e6b73205361746f736869` in esadecimale.



Preparare lo script della transazione. Ecco un esempio del formato previsto:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



che si compone di :





- **Destinazione Address**: Un Bitcoin Address valido. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Può essere il proprio Address, se si desidera restituire a se stessi i fondi trasferiti;
- **Importo trasferito**: l'importo della transazione, qui `0,00001` BTC. **Nota bene**: poiché l'unità di misura utilizzata in Electrum è il BTC, anche l'importo indicato nello script della transazione deve essere espresso in BTC e non in Sats ;
- Script **OP_RETURN**: Il messaggio convertito in esadecimale preceduto da script(`OP_RETURN <messaggio>), 0`. Qui, `5468616e6b73205361746f736869` per il messaggio in esadecimale.



⚠️ **Attenzione**: È molto importante indicare `0` dopo il OP_RETURN, poiché questo opcode contrassegna lo script come non valido, rendendo l'output permanentemente non spendibile. I nodi di rete cancelleranno questo output dal loro set UTXO. Se si inserisce un valore diverso da `0`, sarà irrimediabilmente perso: i bitcoin saranno considerati bruciati. È quindi opportuno inserire sempre `0` con un OP_RETURN per registrare i dati desiderati, ma senza associarvi fondi, che andrebbero persi.



Suggerimento: utilizzare lo strumento [OP_RETURN Generator](https://resources.davidcoen.it/opreturnelectrum/) per generate lo script automaticamente. Anche se questo strumento suggerisce di inserire l'importo in BTC, mantenere l'unità configurata in Electrum.



![image](assets/fr/05.webp)



Per cambiare l'unità di misura utilizzata da Electrum, nella barra dei menu trovare "Preferenze", quindi nella scheda "Unità" selezionare BTC / mBTC / bit o Sats :



![image](assets/fr/06.webp)




---

## Passo 5: inviare la transazione



In Electrum, andare alla scheda Invia.



![image](assets/fr/07.webp)



Nel campo "Pay to", incollare lo script preparato (ad esempio, quello sopra).



![image](assets/fr/08.webp)



Il campo "Pagare a" dovrebbe essere visualizzato in Green e l'importo della transazione dovrebbe apparire nella riga sottostante.



Controllare l'importo e la sua unità nel campo Importo.



Cliccate su "Paga..." e regolate le commissioni di transazione in base all'importo che siete disposti a pagare e alla velocità con cui volete che la vostra transazione venga elaborata da un Miner e integrata in un blocco.



![image](assets/fr/09.webp)



Fare clic su OK e confermare la transazione con la password. Verrà visualizzata una finestra di conferma.




---

## Fase 6: verifica della registrazione



Una volta confermata la transazione (potrebbero essere necessari alcuni minuti), andare alla scheda "Cronologia".



![image](assets/fr/10.webp)



Fare clic con il tasto destro del mouse sulla transazione e selezionare "Visualizza su Explorer" per visualizzare i dettagli.



In alternativa, copiare la destinazione Address (ad esempio, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) e visualizzarla su un explorer Blockchain come [Mempool.space](https://Mempool.space/) o [blockstream.info](https://blockstream.info/).



Cercare il campo OP_RETURN nei dettagli della transazione per visualizzare il messaggio.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Suggerimenti e buone pratiche





- Testate con una piccola quantità: Iniziare con una piccola transazione (ad es. Sats 1000) per evitare errori costosi.
- Assicurarsi che l'uscita contenente OP_RETURN sia uguale a zero, altrimenti i bitcoin andranno definitivamente persi.
- Controllare l'unità di misura: Verificare che l'importo inserito corrisponda all'unità visualizzata in Electrum (BTC, mBTC o Sats).
- Costo della transazione: Se la rete è congestionata, aumentare la tariffa per una conferma più rapida.
- Messaggio breve: Le voci di OP_RETURN sono limitate a 80 byte. Pianificare il messaggio di conseguenza.



---

## Risorse utili





- Scaricare Electrum: [electrum.org](https://electrum.org/)
- Generatore di script OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Esploratori Blockchain: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)