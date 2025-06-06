---
name: Configurer un pruned node avec un snapshot de l'UTXO set 
description: Comment déployer un nœud Bitcoin rapidement avec un snapshot UXTO set ? 
---


## Introduction

This guide will walk you through setting up a pruned Bitcoin node on Ubuntu using BTCPayServer's UTXO snapshot. We'll create a dedicated user, configure RPC authentication, and verify the snapshot's authenticity.

Ce tutoriel vous guidera pour déployer un Pruned Bitcoin Node sur Ubuntu en utilisant un snapshot de l'UTXO set mis à disposition par l'équipe de BTCPayServer.
Pour cela, nous allons créer un compte utilisateur sur la machine, installer Bitcoin Core avec un snapshot et configurer l'authentification RPC pour connecter par exemple un portefeuille Bitcoin comme Sparrow. 

Si vous n'avez pas tout compris, ne vous inquiètez pas nous allons voir chaque étape de manière détaillée. 

Vous pouvez considérer que c'est la manière la plus rapide pour déployer un nœud Bitcoin sur votre machine et qui requière le moins de resources au prix d'une confiance sur l'état de l'UTXO set mis à disposition par BTCPayServer. 

Mais avant de commencer qu'est ce que l'UTXO Set et un pruned node ?

En quelques mots, un pruned node est un nœud Bitcoin qui ne garde en mémoire que les N derniers blocs. Cela permet de faire tourner un nœud sur une machine dont la mémoire est limitée. 
L'UTXO set est une structure de données dans un nœud Bitcoin qui liste l'existence de tous les UTXOs (ou Unspent Transaction Outputs) qui sont en circulation. Cette information permet à votre nœud de vérifier pour chaque nouvelle transaction si les UTXOs utilisaient en entrée sont bel et bien disposible et non déjà dépensés. 


À présent voyons les pré-requis pour suivre ce tutoriel.

## Pré-requis

- Ubuntu 22.04 or later
- At least 10GB free disk space
- Stable internet connection
- Root or sudo access

## 1. System Preparation

First, update your system:

```bash
sudo apt update && sudo apt upgrade -y
```

Install required dependencies:

```bash
sudo apt install -y wget gpg curl build-essential libtool autotools-dev automake pkg-config bsdmainutils python3 libevent-dev libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-test-dev libboost-thread-dev libsqlite3-dev libminiupnpc-dev libzmq3-dev libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libqrencode-dev
```

Install keybase

```
curl --remote-name https://prerelease.keybase.io/keybase_amd64.deb
sudo apt install ./keybase_amd64.deb
run_keybase
```

then create an account or login
source: https://keybase.io/docs/the_app/install_linux

## 2. Create Bitcoin User

Create a dedicated user for running the Bitcoin node:

```bash
sudo adduser bitcoin
sudo usermod -aG sudo bitcoin
```

## 3. Download and Verify Bitcoin Core

Switch to the bitcoin user:

```bash
su - bitcoin
```

Download Bitcoin Core (adjust version number as needed):

```bash
wget https://bitcoincore.org/bin/bitcoin-core-28.0/bitcoin-28.0-x86_64-linux-gnu.tar.gz
wget https://bitcoincore.org/bin/bitcoin-core-28.0/SHA256SUMS
wget https://bitcoincore.org/bin/bitcoin-core-28.0/SHA256SUMS.asc
```

Verify the download:

```bash
git clone https://github.com/bitcoin-core/guix.sigs
gpg --import guix.sigs/builder-keys/*
gpg --verify SHA256SUMS.asc
```

Extract Bitcoin Core:

```bash
tar xzf bitcoin-28.0-x86_64-linux-gnu.tar.gz
sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-28.0/bin/*
```

## 4. Configure Bitcoin Core

Create the Bitcoin data directory:

```bash
mkdir ~/.bitcoin
```

Create bitcoin.conf with RPC authentication:

```bash
cat > ~/.bitcoin/bitcoin.conf << EOL
# Network
listen=1
prune=5000

# RPC Configuration
server=1
rpcuser=asi0
rpcpassword=asi0
rpcallowip=127.0.0.1

# Performance
dbcache=2048
maxconnections=40
EOL
```

Make sure to replace `your_rpc_username_here` and `your_secure_password_here` with secure credentials.

## 5. Download and Verify UTXO Snapshot

Install keybase and login (if you haven't):

```bash
keybase login
```

Download the UTXO snapshot:

```bash
cd ~/.bitcoin
wget https://eu2.contabostorage.com/1f50a74c9dc14888a8664415dad3d020:utxosets/utxo-snapshot-bitcoin-mainnet-820852.tar
```

Download and verify the signature:

```bash
mkdir sigs
cd sigs
wget https://github.com/btcpayserver/btcpayserver-docker/blob/master/contrib/FastSync/sigs/NicolasDorier.utxo-sets.asc
curl https://keybase.io/nicolasdorier/pgp_keys.asc | gpg --import

cd ..
keybase pgp verify -i sigs/nicolasdorier.utxo-sets.asc
```

Extract the snapshot:

```bash
tar xf utxo-snapshot-bitcoin-mainnet-820852.tar
```

## 6. Start Bitcoin Core

Start bitcoind:

```bash
bitcoind -daemon
```

Monitor the initial sync:

```bash
watch bitcoin-cli getblockchaininfo
```

## 7. Create Systemd Service (Optional)

Create a systemd service file for automatic startup:

```bash
sudo nano /etc/systemd/system/bitcoind.service
```

Add the following content:

```ini
[Unit]
Description=Bitcoin daemon
After=network.target

[Service]
User=bitcoin
Group=bitcoin
Type=forking
ExecStart=/usr/local/bin/bitcoind -daemon
ExecStop=/usr/local/bin/bitcoin-cli stop
TimeoutStopSec=300
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl enable bitcoind
sudo systemctl start bitcoind
```

## Verification and Monitoring

Check the node status:

```bash
bitcoin-cli getblockchaininfo
```

Monitor the debug log:

```bash
tail -f ~/.bitcoin/debug.log
```

