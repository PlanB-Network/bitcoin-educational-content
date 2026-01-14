---
name: Coinjoin Coordinator - WabiSabi
description: How to setup and run a coinjoin coordinator following the WabiSabi protocol (used in Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)

---

## Introduction 👋

In this expert guide we will help you set-up a coinjoin coordinator, essentially a server that brings together people that want to save on transaction fees or increase their onchain privacy in collaborative transactions. Since there is no longer a company run coordinator bundled with Wasabi Wallet, users have to find and select their own preferred coordinator server. Only a few coordinators have shown up asking a 0% coordination fee, so the developers of Wasabi Wallet have been working hard to make it as easy as possible to start running your own community coordinator (on hardware as small as a Raspberry Pi5!). The currently active coordinators that ask 0% coordination fee can be found on [LiquiSabi](https://liquisabi.com) and more importantly on [nostr](https://github.com/Kukks/WasabiNostr).

## Requirements 🫴

- VPS (hosted node) or computer/server (self-hosted node)
- Pruned/Full Bitcoin Core node (tested with v29.0)

Optional:
- (sub)Domain forwarding traffic to the node (e.g. coinjoin.[yourdomain].io)

It is recommended to have some experience with commandline prompts and bash, as not all steps can be automated.

Hardware-wise it is adviced to have a system with:
- 4 cores
- 16 GB RAM
- 2 TB SSD or NVMe (for a full-node) / 128 GB SSD (for a pruned-node)

Such requirements can be provided by a Raspberry Pi 5 for just 120 $, excluding the storage which costs around 100 $ for a 2TB NVMe stick.

Cheap VPS typically come with only 1 core and 4GB RAM, which I've found is too little to sync and verify the entire bitcoin blockchain at blockheight 911817.

Storage-wise a full-node will require at minimum a 2TB of disc storage, preferably SSD or NVMe type. When pruning the blockchain a much smaller storage drive is acceptable (e.g. a 128GB SSD).

If you intend to run a coordinator for large (300+ input) coinjoins, it is adviced to choose a system with faster/newer cores with a higher performance for all the signature verifications.

## Installation 🛠️

On the node we want to download and install the latest released version of Wasabi Wallet, which includes a backend and coordinator as standalone executables next to the wallet.

Find the latest version: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) and verify the PGP signature of the release with the keys: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)

The deployment details differ depending on hardware (CPU-architecture) and OS choice, below the different details are given for a Raspberry Pi (ARM-64) with Debian-based RaspiBlitz as starting point. Skip ahead for (X86-64) Ubuntu OS deployment using Nix.

Find the installation instructions here: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)

### RaspiBlitz/Debian deployment

For RaspiBlitz (tested with v1.11) nodes a deployment script building from source code can be used: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)


### Easy deployment

For a minimal deployment you just want to extract the executables for your platform in a folder.
Example commandline codes for Debian/Ubuntu:

```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```

This should result in the following valid signature message:

```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```

And you can proceed to install the downloaded package:

```
sudo apt install ./Wasabi-2.7.2.deb
```


## Configuration 🧾

Before running the coordinator you need to edit the Config.json file with your:
- Bitcoin RPC credentials
- Preferred round parameters
- Coordinator Extended Public Key (create a new SegWit wallet for receiving collected dust) 
**Warning**: Taproot wallet will result in unspendable UTXO's! Use a Native Segwit wallet here.
- Allowed input and output address types
- Announcer configuration for publishing over nostr (name, description, Uri, minimum inputs, nostr relay, nostr private key)

You can run the coordinator accesible only via the .onion address, or use your custom clearnet domain.

Find or create the config file on this path: 

`~/.walletwasabi/coordinator/Config.json`

Edit it with command:

```
sudo nano ~/.walletwasabi/coordinator/Config.json
```

See this example Config.json:

```
{
  "Network": "Main",
  "MainNetBitcoinRpcUri": "http://localhost:8332",
  "TestNetBitcoinRpcUri": "http://localhost:48332",
  "RegTestBitcoinRpcUri": "http://localhost:18443",
  "BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
  "ConfirmationTarget": 21,
  "DoSSeverity": "0.02",
  "DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
  "DoSMinTimeForCheating": "1d 0h 0m 0s",
  "DoSPenaltyFactorForDisruptingConfirmation": 0.2,
  "DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
  "DoSPenaltyFactorForDisruptingSigning": 1.0,
  "DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
  "DoSMinTimeInPrison": "0d 0h 20m 0s",
  "MinRegistrableAmount": "0.000021",
  "MaxRegistrableAmount": "1000.00",
  "AllowNotedInputRegistration": true,
  "StandardInputRegistrationTimeout": "0d 0h 21m 0s",
  "BlameInputRegistrationTimeout": "0d 0h 3m 0s",
  "ConnectionConfirmationTimeout": "0d 0h 1m 0s",
  "OutputRegistrationTimeout": "0d 0h 1m 0s",
  "TransactionSigningTimeout": "0d 0h 1m 0s",
  "FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
  "FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
  "RoundExpiryTimeout": "0d 0h 5m 0s",
  "MaxInputCountByRound": 100,
  "MinInputCountByRoundMultiplier": 0.21,
  "MinInputCountByBlameRoundMultiplier": 0.21,
  "RoundDestroyerThreshold": 375,
  "CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
  "CoordinatorExtPubKeyCurrentDepth": 0,
  "MaxSuggestedAmountBase": "100.00",
  "RoundParallelization": 1,
  "CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
  "AllowP2wpkhInputs": true,
  "AllowP2trInputs": true,
  "AllowP2wpkhOutputs": true,
  "AllowP2trOutputs": true,
  "AllowP2pkhOutputs": true,
  "AllowP2shOutputs": true,
  "AllowP2wshOutputs": true,
  "DelayTransactionSigning": false,
  "AnnouncerConfig": {
    "CoordinatorName": "Your Coordinator Name",
    "IsEnabled": true,
    "CoordinatorDescription": "Privacy is a human right!",
    "CoordinatorUri": "https://coinjoin.yourdomain/",
    "AbsoluteMinInputCount": 21,
    "ReadMoreUri": "https://coinjoin.yourdomain/",
    "RelayUris": [
      "wss://relay.primal.net"
    ],
    "Key": "nsec_your_coordinator_nostr_privatekey"
  },
  "PublishAsOnionService": true,
  "OnionServicePrivateKey": your_onion_service_private_key
}
```
### Tor configuration 🧅

To fill in your OnionServicePrivateKey you likely need to generate one first. 

Wasabi Wallet will generate a private key for you if you run it the first time with ```"PublishAsOnionService": true,``` set in the Config.json file.

Run the coordinator once with command:

```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```

To see your Onion hidden service address, either check the coordinator logs with:

```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```

and you'll find something like:

```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```

The long URL ending in .onion is your hidden service address or CoordinatorUri.

Or check again your coordinator configuration file with:

```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```

Which should automatically be filled in now.

## Running ⚡

Once all the config parameters have been set you can run the coordinator service and start announcing your first round 🕶️ 

Simply start the coordinator with the command:

```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```

You can monitor the current round and number of registered UTXO's/coins by checking (in Tor browser for .onion): 

```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```

![detected](assets/en/01.webp)

### Optional: debugging coordinator server

You can monitor for any issues or errors in the logfile at ```~/.walletwasabi/backend/Logs.txt```

Typical issues include RPC connection issues, this has to be enabled in ```~/.bitcoin/bitcoin.conf``` with:

```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```

### Optional: Running the backend server

Together with the coordinator you can also provide a backend server for users that don't have their own bitcoin node to connect to for fee estimates and blockfilters.

Start this service with command:

```
wbackend
```

## Inviting Wasabi users to your coordinator 🫂

For other users to find your service you can rely on the nostr announcer, or share a magic link with your domain (clearnet) or hidden service (.onion link) and round parameters like this:

```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```

When a user copies the magic link and opens their Wasabi Wallet, the software will automatically show the coordinator dialog with your domain and parameters.

![detected](assets/en/02.webp)

💚🍣 Congratulations on decentralizing bitcoin privacy 🕶️

Remember your training [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet is for defence only 🛡️
