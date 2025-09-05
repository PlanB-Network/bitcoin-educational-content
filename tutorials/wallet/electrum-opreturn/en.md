---
name: Electrum OP_RETURN
description: Register a message on the Blockchain Bitcoin with Electrum
---

![cover](assets/cover.webp)



This step-by-step tutorial shows you how to write a message on the Blockchain Bitcoin using the Wallet Electrum. This operation uses the OP_RETURN instruction to insert text into a transaction, publicly visible on the Blockchain. Follow these simple steps for a successful registration.


---
## Prerequisites



- A computer (Windows, macOS or Linux).
- Internet connection.
- A few satoshis (Sats) or bitcoins (BTC) in your Wallet to cover the transaction amount and fees.
- A text-to-hex converter (e.g. an online site) or a dedicated tool such as [this OP_RETURN script generator](https://resources.davidcoen.it/opreturnelectrum/).


---

## Step 1: Download and install Electrum


![image](assets/fr/01.webp)


1. Visit the official Electrum website: [electrum.org](https://electrum.org/).

2. Download the version corresponding to your operating system (Windows, macOS, Linux).

3. Install Electrum according to the installer's instructions.

4. Check the integrity of the downloaded file (optional, but recommended for security reasons) by comparing the file's signature or Hash.


→ More details on the Electrum tutorial :


https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Step 2: Create or import a Wallet


1. Launch Electrum.

2. Choose Create a new Wallet or Restore an existing Wallet if you already have a seed phrase (recovery phrase).

3. Follow the instructions to configure your Wallet :


 - For a new Wallet, make a note of your seed sentence and keep it in a safe place (paper, safe, etc.).
 - For an existing Wallet, enter your seed phrase to restore it.

4. Set a password to secure your Wallet.


→ More details on the Electrum tutorial :


https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Step 3: Check available funds


Make sure your Wallet contains enough bitcoins (BTC) or satoshis (Sats) to :


- Transaction amount (for example, 0.00001 BTC or 1000 Sats).
- Transaction fees, which vary according to the size of the network (generally a few thousand Sats).


Consult the Balance in Electrum to check your funds.


![image](assets/fr/02.webp)


If necessary, transfer BTC or Sats to feed your Wallet. To do this, go to the 'Receive' tab and click on 'Create Request' :


![image](assets/fr/03.webp)


This will show a reception address:


![image](assets/fr/04.webp)


→ More details on the Electrum tutorial :


https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Step 4: Prepare the message to be inscribed


Select the message you wish to enter (e.g. `Thanks Satoshi`). Note: OP_RETURN messages are limited to 80 bytes, i.e. around 80 ASCII characters.


*Take a moment to think: what you write on the Blockchain Bitcoin is eternal and accessible to all, so :*


- leave a beautiful expression of our humanity,*
- avoid entering content you may regret*


*Blockchain space and your bitcoins are precious, use them wisely and with intention*


Convert your message to hexadecimal :


- You can use an [online tool](https://www.rapidtables.com/convert/number/ascii-to-hex.html), but be careful not to process sensitive data there (although, in principle, information intended for publication on Blockchain Bitcoin via a OP_RETURN does not present any confidentiality issues);
- For greater confidentiality, perform the conversion locally using a small Python :


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


Example: `Thanks Satoshi` in ASCII gives `5468616e6b73205361746f736869` in hexadecimal.


Prepare the transaction script. Here's an example of the expected format:


```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```


which is made up of :



- Destination address**: A valid Bitcoin address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. This can be your own address, if you wish to return the transferred funds to yourself;
- Amount transferred**: the amount of the transaction, here `0.00001` BTC. **Please note**: since the unit used in Electrum is BTC, the amount indicated in the transaction script must also be expressed in BTC, and not in Sats ;
- Script OP_RETURN**: The message converted to hexadecimal preceded by script(`OP_RETURN <messsage>), 0`. Here, `5468616e6b73205361746f736869` for the message in hexadecimal.


⚠️ **Caution**: It's very important to indicate `0` after the OP_RETURN, as this opcode marks the script as invalid, making the output permanently unspendable. Network nodes will delete this output from their UTXO set. If you enter a value other than `0`, it will be irretrievably lost: your bitcoins will be considered burnt. You should therefore always enter `0` with a OP_RETURN in order to record the desired data, but without associating funds with it, which would be lost.


Tip: Use the [OP_RETURN Generator] tool (https://resources.davidcoen.it/opreturnelectrum/) to generate the script automatically. Even if this tool suggests entering the amount in BTC, keep the unit configured in Electrum.


![image](assets/fr/05.webp)


To change the unit used by Electrum, in the menu bar find "Preferences", then in the "Units" tab select BTC / mBTC / bits or Sats :


![image](assets/fr/06.webp)



---

## Step 5: Send the transaction


In Electrum, go to the Send tab.


![image](assets/fr/07.webp)


In the "Pay to" field, paste the prepared script (for example, the one above).


![image](assets/fr/08.webp)


The "Pay to" field should be displayed in green, and the transaction amount should appear on the line below.


Check the amount and its unit in the Amount field.


Click on "Pay..." and adjust your transaction fees according to the amount you are willing to pay and the speed at which you want your transaction to be processed by a miner and integrated into a block.


![image](assets/fr/09.webp)


Click OK and confirm the transaction with your password. A confirmation window will appear.



---

## Step 6: Verify registration


Once the transaction has been confirmed (this may take a few minutes), go to the "History" tab.


![image](assets/fr/10.webp)


Right-click on the transaction and select "View on Explorer" to see the details.


Alternatively, copy the destination address (for example, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) and view it on a Blockchain explorer such as [Mempool.space](https://Mempool.space/) or [blockstream.info](https://blockstream.info/).


Look for the OP_RETURN field in the transaction details to see your message.


![image](assets/fr/11.webp)



![image](assets/fr/12.webp)



---

## Tips and best practices



- Test with a small amount: Start with a small transaction (e.g. Sats 1000) to avoid costly errors.
- Make sure that the output containing OP_RETURN is equal to zero, otherwise your bitcoins will be permanently lost.
- Check the unit: Make sure the amount entered corresponds to the unit displayed in Electrum (BTC, mBTC or Sats).
- Transaction fee: If the network is congested, increase the fee for faster confirmation.
- Short message: OP_RETURN entries are limited to 80 bytes. Plan your message accordingly.


---

## Useful resources



- Download Electrum: [electrum.org](https://electrum.org/)
- OP_RETURN script generator: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)