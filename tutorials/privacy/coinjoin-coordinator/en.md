---
name: Coinjoin Coordinator
description: How to setup and run a coinjoin coordinator following the WabiSabi protocol (used in Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)

---

## Introduction

In this expert guide we will help you set-up a coinjoin coordinator, essentially a server that brings together people that want to save on transaction fees or increase their onchain privacy in collaborative transactions. Since there is no longer a company run coordinator bundled with Wasabi Wallet, users have to find and select their own preferred coordinator server. Only a few coordinators have shown up asking a 0% coordination fee, so the developers of Wasabi Wallet have been working hard to make it as easy as possible to start running your own community coordinator (on hardware as small as a Raspberry Pi5!). The currently active coordinators that ask 0% coordination fee can be found on [LiquiSabi](https://liquisabi.com).

## Requirements

- VPS (hosted node) or computer/server (self-hosted node)
- Pruned/Full Bitcoin Core node (tested with v29.0)

Optional:
- (sub)Domain forwarding traffic to the node (e.g. coinjoin.[yourdomain].io)

It is recommended to have some experience with commandline prompts and bash, as not all steps can be automated.

Hardware-wise it is adviced to have a system with:
- 4-cores
- 16GB RAM
- 2TB SSD/NVMe (for full-node) / 128GB SSD (for pruned-node)

which a Raspberry Pi 5 can provide for just 120$, excluding the storage which costs around 100$ for a 2TB NVMe stick.

Cheap VPS's typically come with only 1-core and 4GB RAM, which I've found is too little to sync and verify the entire bitcoin blockchain at blockheight 911817.

Storage-wise a full-node will require at minimum a 2TB of disc storage, preferably SSD or NVMe type. When pruning the blockchain a much smaller storage drive is acceptable (e.g. a 128GB SSD).

If you intend to run a coordinator for large (300+ input) coinjoins, it is adviced to choose a system with faster/newer cores with a higher performance for all the signature verifications.

## Installation

On the node we want to download and install the latest released version of Wasabi Wallet, which includes a backend and coordinator as standalone executables next to the wallet.

Find the latest version: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases)

and verify the PGP signature of the release with the keys: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)

The deployment details differ depending on hardware (CPU-architecture) and OS choice, below the different details are given for a Raspberry Pi (ARM-64) with Debian-based RaspiBlitz as starting point. Skip ahead for (X86-64) Ubuntu OS deployment using Nix.

### RaspiBlitz/Debian deployment:
For RaspiBlitz (tested with v1.11) nodes a deployment script building from source code can be used: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)

```
#!/bin/bash

# Wasabi Backend/Coordinator deployment bonus script for RaspiBlitz v1.11.4 (26/01/2025)
WasabiVersion="v2.5.1"

PGPsigner="web-flow"
PGPpubkeyLink="https://github.com/web-flow.gpg"
PGPpubkeyFingerprint="6FB3872B5D42292F59920797856348328949861E"

# command info
if [ $# -eq 0 ] || [ "$1" = "-h" ] || [ "$1" = "-help" ]; then
  echo "Config script to switch Wasabi Coordinator/Backend on or off"
  echo "bonus.wasabi.sh [on|off]"
  echo "enables/disables the coordinator and backend"
  echo "bonus.wasabi.sh [install|uninstall]"
  echo "installs Wasabi Wallet $WasabiVersion"
  echo "To update to the latest release published on github run:"
  echo "bonus.wasabi.sh update"
  echo
  exit 1
fi

source /mnt/hdd/raspiblitz.conf
# get cpu architecture (checked with 'uname -m')
source /home/admin/raspiblitz.info
source <(/home/admin/_cache.sh get state)

function CoordinatorService() {
  echo "# create the wasabicoordinator.service"
  echo "
[Unit]
Description=Wasabi Coordinator daemon
Requires=bitcoind.service
After=bitcoind.service

[Service]
ExecStart=/home/wasabi/dotnet/dotnet run \
 -c Release --project \"/home/wasabi/WalletWasabi/WalletWasabi.Coordinator/WalletWasabi.Coordinator.csproj\"
User=wasabi
Group=wasabi
Type=simple
PIDFile=/run/wasabi/wasabicoordinator.pid
Restart=always
RestartSec=10

# Hardening measures
PrivateTmp=true
ProtectSystem=full
NoNewPrivileges=true
PrivateDevices=true

[Install]
WantedBy=multi-user.target
" | sudo tee /etc/systemd/system/wasabicoordinator.service
  sudo systemctl daemon-reload
}

function BackendService() {
  echo "# create the wasabibackend.service"
  echo "
[Unit]
Description=Wasabi Backend daemon
Requires=bitcoind.service
After=bitcoind.service

[Service]
ExecStart=/home/wasabi/dotnet/dotnet run \
 -c Release --project \"/home/wasabi/WalletWasabi/WalletWasabi.Backend/WalletWasabi.Backend.csproj\"
User=wasabi
Group=wasabi
Type=simple
PIDFile=/run/wasabi/wasabibackend.pid
Restart=always
RestartSec=10

# Hardening measures
PrivateTmp=true
ProtectSystem=full
NoNewPrivileges=true
PrivateDevices=true

[Install]
WantedBy=multi-user.target
" | sudo tee /etc/systemd/system/wasabibackend.service
  sudo systemctl daemon-reload
}

########################################
# INSTALL (just user, code & compile)
########################################

if [ "$1" = "install" ]; then

  # check if code is already installed
  isInstalled=$(compgen -u | grep -c wasabi)
  if [ "${isInstalled}" != "0" ]; then
    echo "# already installed"
    exit 0
  fi

    echo "# create wasabi user"
    sudo adduser --system --group --home /home/wasabi wasabi
    cd /home/wasabi || exit 1

    # Clone repository
    sudo -u wasabi git clone https://github.com/WalletWasabi/WalletWasabi.git

    # Install latest dotnet SDK 8.0
    sudo -u wasabi wget https://download.visualstudio.microsoft.com/download/pr/bb17a3ab-7122-41bd-96cf-33e35b1d4318/7b09327fdd49b7130cf94838f2979aa6/dotnet-sdk-8.0.405-linux-arm64.tar.gz
    
    # Verify download hash
    expectedHash="07988b784bf71913f607ce0ced50434c69980ae715ca62fb6af68f7eaa26810c3f9ffe24df1d8706d1a557c3eb7756143e5357016089cf1508714baa1cce828a"
    actualHash=$(sha512sum dotnet-sdk-8.0.405-linux-arm64.tar.gz | cut -d' ' -f1)
    if [ "$actualHash" != "$expectedHash" ]; then
      echo "Error: Downloaded file hash does not match expected hash."
      exit 1
    fi

    sudo mkdir -p $HOME/dotnet && tar zxf dotnet-sdk-8.0.405-linux-arm64.tar.gz -C $HOME/dotnet
    export DOTNET_ROOT=$HOME/dotnet
    export PATH=$PATH:$HOME/dotnet

    # Remove downloaded tar/zip file
    sudo rm dotnet-sdk-8.0.405-linux-arm64.tar.gz

    # Disable telemetry
    export DOTNET_CLI_TELEMETRY_OPTOUT=1

    # Build Wasabi Backend
    echo "build Wasabi Backend"
    cd /home/wasabi/WalletWasabi/WalletWasabi.Backend/
    sudo -u wasabi $HOME/dotnet/dotnet build -c Release \
      /home/wasabi/WalletWasabi/WalletWasabi.Backend/WalletWasabi.Backend.csproj || exit 1


    # Build Wasabi Coordinator
    echo "build Wasabi Coordinator"
    cd /home/wasabi/WalletWasabi/WalletWasabi.Coordinator
    sudo -u wasabi $HOME/dotnet/dotnet build -c Release \
      /home/wasabi/WalletWasabi/WalletWasabi.Coordinator/WalletWasabi.Coordinator.csproj || exit 1

    echo "# make sure wasabi is member of the bitcoin group"
    sudo /usr/sbin/usermod --append --groups bitcoin wasabi
    exit 0
    echo "Finished installing Wasabi Backend & Coordinator! Happy Co 🕶️"
fi

########################################
# UNINSTALL (remove from system)
########################################

if [ "$1" = "uninstall" ]; then

  isActive=$(sudo ls /etc/systemd/system/wasabicoordinator.service 2>/dev/null | grep -c 'wasabicoordinator.service')
  if [ "${isActive}" != "0" ]; then
    echo "# cannot uninstall if still 'on'"
    exit 1
  fi

  # clear dotnet cache
  /home/wasabi/dotnet/dotnet nuget locals all --clear 2>/dev/null

  # remove dotnet
  sudo rm -rf /usr/share/dotnet 2>/dev/null

  # nuke user
  sudo userdel -rf wasabi 2>/dev/null

  echo "# uninstall done"

  exit 0
fi
########################################
# UPDATE (pull latest master branch)
########################################
echo "# Update Wasabi Wallet"
sudo -r wasabi git pull -p 

########################################
# ON (activate & config)
########################################

if [ "$1" = "1" ] || [ "$1" = "on" ]; then
  CoordinatorService
  sudo systemctl enable wasabicoordinator
  sudo systemctl start wasabicoordinator

  BackendService
  sudo systemctl enable wasabibackend
  sudo systemctl start wasabibackend
fi
########################################
# OFF (deactivate)
########################################

if [ "$1" = "0" ] || [ "$1" = "off" ]; then
  # removing service: wasabicoordinator
  sudo systemctl stop wasabicoordinator
  sudo systemctl disable wasabicoordinator
  sudo rm /etc/systemd/system/wasabicoordinator.service
  # removing service: wasabibackend
  sudo systemctl stop wasabibackend
  sudo systemctl disable wasabibackend
  sudo rm /etc/systemd/system/wasabibackend.service
fi
```

### Ubuntu+Nix deployment: 
#TODO Update for Bitcoin Core v29.0 instead of Knots
and use latest Wasabi Wallet release (including onion service)

```
sudo apt update -y && apt upgrade -y

sudo apt-get install software-properties-common

sudo add-apt-repository ppa:luke-jr/bitcoinknots

sudo apt update

sudo apt install bitcoind

sudo apt install tor

sudo apt install curl

sh <(curl -L https://nixos.org/nix/install) --daemon

reboot

cd /

nix --extra-experimental-features nix-command --extra-experimental-features flakes build github:/WalletWasabi/WalletWasabi 

```
**WORKINGDIRECTORY, EXECSTART, AND ENVIRONMENT MUST BE MODIFIED**
For environment, look in /nix/store and use
```ls -d *-openssl*
ls -d *-zlib*
ls -d *-icu4c*
```
Set environment to the lib path of each (concatenated with colons, encapsulated by quotes, set equal to LD_LIBRARY_PATH)
```

nano /etc/systemd/system/walletwasabi-backend.service
                    
[Unit]
Description=WalletWasabi Backend API
After=network.target

[Service]
ExecStart=/bin/bash -x /result/bin/WalletWasabi.Backend
WorkingDirectory=/result/bin/
Restart=always
SyslogIdentifier=walletwasabi-backend
User=root
Environment="LD_LIBRARY_PATH=/nix/store/1w90l4fm5lzhlybipfilyjij2das6w98-openssl-3.0.14/lib:/nix/store/2k9k3q1vk8z6w7743k6nb22vnb05xv06-zlib-1.3.1/lib:/nix/store/80pnfsbljcznzz90jlqi52mk4sfspd08-icu4c-74.2/lib"
Requires=tor.service
Requires=bitcoind.service

[Install]
WantedBy=multi-user.target


nano /etc/systemd/system/bitcoind.service



[Unit]
Description=Bitcoin daemon
Documentation=https://github.com/bitcoin/bitcoin/blob/master/doc/init.md

# https://www.freedesktop.org/wiki/Software/systemd/NetworkTarget/

After=network-online.target

Wants=network-online.target


[Service]
ExecStart=/usr/bin/bitcoind -pid=/run/bitcoind/bitcoind.pid \
                            -conf=/etc/bitcoin/bitcoin.conf \
                            -datadir=/var/lib/bitcoind

# Make sure the config directory is readable by the service user
PermissionsStartOnly=true
ExecStartPre=/bin/chgrp bitcoin /etc/bitcoin

# Process management
####################

Type=forking
PIDFile=/run/bitcoind/bitcoind.pid
Restart=on-failure
TimeoutStartSec=infinity
TimeoutStopSec=600

# Directory creation and permissions
####################################

# Run as bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/bitcoind
RuntimeDirectory=bitcoind
RuntimeDirectoryMode=0710

# /etc/bitcoin
ConfigurationDirectory=bitcoin
ConfigurationDirectoryMode=0710

# /var/lib/bitcoind
StateDirectory=bitcoind
StateDirectoryMode=0710

# Hardening measures
####################

# Provide a private /tmp and /var/tmp.
PrivateTmp=true

# Mount /usr, /boot/ and /etc read-only for the process.
ProtectSystem=full

# Deny access to /home, /root and /run/user
ProtectHome=true

# Disallow the process and all of its children to gain
# new privileges through execve().
NoNewPrivileges=true

# Use a new /dev namespace only populated with API pseudo devices
# such as /dev/null, /dev/zero and /dev/random.
PrivateDevices=true

# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target


nano /etc/bitcoin/bitcoin.conf 

rpcworkqueue=384
rpcthreads=24
txindex=1
daemon=1
rpcuser=bitcoin
rpcpassword=set_a_secure_password
debug=rpc
whitebind=127.0.0.1:8333
softwareexpiry=0

#### This makes mempool policy the same as Bitcoin Core defaults.
corepolicy=1
#mempoolreplacement=fee,optin



apt install nginx certbot python3-certbot-nginx


certbot --nginx -d coinjoin.domain --register-unsafely-without-email
```

## Configuration

Before running the coordinator you need to edit the Config.yaml file with your:
- Bitcoin RPC credentials
- Preferred round parameters
- Coordinator Extended Public Key (create a new SegWit wallet for receiving collected dust) 
<br>Warning: Taproot wallet will result in unspendable UTXO's!
- Allowed input and output address types
- Announcer configuration for publishing over nostr (name, description, Uri, minimum inputs, nostr relay, nostr private key)

You can run the coordinator accesible only via the .onion address, or use your custom domain.

In that case the traffic has to be forwarded to your node for this service in nginx, which can be done with this example:

```
server {
    listen        80;
    listen        [::]:80;
    listen        443 ssl;
    listen        [::]:443 ssl;
    server_name coinjoin.domain; #Edit to your domain
    access_log /var/log/nginx/reverse-access.log;
    error_log /var/log/nginx/reverse-error.log;

    root /var/www/coinjoin;
    index index.html; #Design your own landing page for clearnet

    location /wabisabi/human-monitor {
    proxy_pass http://localhost:37128;
    }

    location / {
        # Browser is redirected to info page.
        if ( $http_user_agent != "" ) {
                return 301 https://coinjoin.domain/index.html; #Edit to your domain
        }
        # Wallets are redirected to coordinator server.
        proxy_pass http://localhost:37128;
        proxy_redirect off;
        proxy_set_header Host $http_host;
    }

    location = /index.html {
        root /var/www/coinjoin;
        index index.html;
    }

    location @fallback {
        return 301 https://coinjoin.domain/index.html; #Edit to your domain
        internal;
    }

    ssl_certificate /etc/letsencrypt/live/coinjoin.domain/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/coinjoin.domain/privkey.pem;
}
```

For the new nginx configuration to load, restart the nginx service using command:

```sudo systemctl restart nginx.service```

In home networks you also have to setup port forwarding of clearnet traffic on port 80 to the local IP of your node.

## Running

Once all the parameters have been set you can run the coordinator service and start announcing your first round 🕶️

---