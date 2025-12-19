---
name: Phoenixd
description: Deploy your own minimalist Lightning node with Phoenixd
---

![cover](assets/cover.webp)


Financial autonomy also means controlling your Lightning infrastructure. For developers and companies wishing to integrate Bitcoin Lightning into their applications, **Phoenixd** represents the ideal solution: a minimalist, specialized Lightning node with automatic liquidity management.


Phoenixd is a Lightning server developed by ACINQ, designed specifically for sending and receiving Lightning payments via an HTTP API. Unlike full-featured implementations such as LND or Core Lightning, Phoenixd abstracts all the complexity of channel management while preserving the self-guarding of your funds.


In this tutorial, we'll look at how to install, configure and use Phoenixd to develop Lightning applications with a self-hosted infrastructure and an easy-to-use API.


## What is Phoenixd?


Phoenixd is a minimal, specialized Lightning node developed by ACINQ. It's a solution designed for developers and enterprises wishing to integrate Lightning into their applications without the management complexity of a full node.


### Operating principle


**Phoenixd is a minimal Lightning node that uses ACINQ as its LSP (Lightning Service Provider) for automatic liquidity. When you receive Lightning payments, it automatically opens channels with ACINQ nodes to allocate the necessary incoming capacity. This "on-the-fly" liquidity is instantaneous, but charged at exactly **1% + mining fees** of the amount received.


**Automated management:** The system manages three key elements:


- Lightning** channels: Open, close and manage automatically as needed
- Incoming/outgoing liquidity**: Automatic provisioning via splicing and channel opening
- Fee credit** : Small payments insufficient to justify a channel are stored as a provision for future charges


### Phoenixd benefits


**You control your private keys (12-word seed) and funds. Phoenixd generates your wallet locally without ever sharing your keys.


**Personal infrastructure:** Phoenixd runs on your server, giving you access to detailed logs, configuration and API control. You are no longer dependent on a third-party service for access to your funds.


**Integrated API:** Phoenixd features an HTTP API for integration with other services, native LNURL support and custom application development.


**Ease of integration:** Thanks to its simple REST API, Phoenixd can be integrated into any application or service requiring Lightning payments.


**Important note:** Automatic liquidity still comes from ACINQ as LSP (Lightning Service Provider). Phoenixd uses the same mechanism as Phoenix mobile for automatic channel management.


## Installing Phoenixd


### Prerequisites


Phoenixd requires a Linux environment (Ubuntu/Debian recommended), with some basic command-line skills. For optimum performance, you'll need :



- Linux server**: VPS or local machine with stable connection
- OpenJDK 21** : Java runtime environment
- Stable Internet connection**: For synchronization with the Lightning network
- Domain name** (optional) : For secure HTTPS access to the API


### Download and installation


**1. Download Phoenixd**


Go to the [GitHub releases] page (https://github.com/ACINQ/phoenixd/releases) and download the latest version for your architecture:


```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```


**2. First start-up


Start Phoenixd for initialization:


```bash
./phoenixd
```


On first launch, you will be asked to confirm two important steps by typing "I understand" :


**Message 1 - Backup:**

```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```


**Save these 12 words** - it's your only guarantee of recovery.


**Message 2 - Automatic liquidity:**

```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```


Type `I understand` for each confirmation.


![Premier démarrage](assets/fr/01.webp)


*Phoenixd starts up for the first time: backup confirmations and automatic liquidity*


**3. In-service configuration** (in French only)


For continuous operation, create a systemd :


```bash
sudo nano /etc/systemd/system/phoenixd.service
```


```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```


```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```


![Service systemd](assets/fr/02.webp)


*Phoenixd service active and operational via systemd and `auto-liquidity` at 2m sat*


## Configuration and security


### Configuration file


Phoenixd automatically creates `~/.phoenix/phoenix.conf` with the essential parameters:


```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```


**Key parameters:**


- `auto-liquidity`: Size of automatically opened channels (default: 2M Sats)
- http-password`: Admin password for API (invoice creation AND payment dispatch)
- http-password-limited-access`: Restricted password (invoice creation only)


### Secure access with HTTPS


By default, the Phoenixd API is only accessible via local HTTP (`http://127.0.0.1:9740`). To use your node from outside (mobile applications, other servers, web integrations), you need to configure secure HTTPS access.


**Reverse proxy principle:**

```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```


**Nginx** acts as a **reverse proxy**: it listens to HTTPS requests from the Internet on port 443, redirects them to Phoenixd locally (port 9740), then sends encrypted responses back to the client.


**The SSL/TLS** certificate is a digital file that :


- Prove your server's identity** (prevents man-in-the-middle attacks)
- Enables HTTPS** encryption: all data, including your API passwords, is encrypted during transport
- Issued free of charge** by Let's Encrypt via the certbot tool


This configuration allows you to :


- Secure access to the API from the Internet**
- Encrypt your API** passwords during transport (to prevent them being transmitted in clear text)
- Integrate Phoenixd** into external applications requiring HTTPS
- Compliance with security standards** for financial APIs


Configure this HTTPS reverse proxy with nginx :


**1. Nginx** configuration


```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```


```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```


```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```


**2. SSL** certificate


```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```


### Function test


Check that Phoenixd is working properly:


```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```


These commands should return JSON information on the node's status and balance (initially empty).


![Commandes CLI](assets/fr/03.webp)


*Getinfo and getbalance commands to check node status*


## Using the API


### First reception test


**1. Create a Lightning** invoice


Use the API to create your first invoice:


```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```


### Understanding the automatic liquidity mechanism


**Fundamental principle:** When you receive a Lightning payment, Phoenixd sometimes has to open a new channel to be able to receive it. This channel opening costs a fee which is **automatically deducted** from the amount received.


**Concrete example with 100,000 Sats:**


![Premier test de réception](assets/fr/04.webp)


*First acceptance test: Sats 100k received, final balance of Sats 75.561 after deduction of liquidity costs*


```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```


**Fee calculation:**


- Service charge**: 1% of channel capacity (2,115,000 Sats) = 21,150 Sats
- Mining fees**: ~3,289 Sats (for On-Chain transaction)
- Total**: 24,439 Sats automatically deducted


**Verification with CLI commands:**

```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```


![Nouveau solde après paiement](assets/fr/05.webp)


*Final balance after payment sent: 257 Sats remaining after Lightning shipment*


**Fee credit for small payments:** If you receive payments too small to justify opening a channel (< approx. 25k Sats), they are stored in a non-refundable "fee credit". This credit will be used to pay future channel fees when you receive a sufficient amount.


**2. Follow channel opening**


Watch the Phoenixd logs:


```bash
journalctl -u phoenixd -f
```


You will see the opening of the channel and the automatic deduction of liquidity fees. Fees vary according to Mempool Bitcoin conditions, but always include 1% service charge plus current mining fee.


**3. Check channel**


```bash
./phoenix-cli listchannels
```


This command displays your active channels with their status and balance.


### Complete API operations


Phoenixd exposes a REST API on port 9740 enabling :


**Basic operations:**

```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```


**Important on costs:**


- Receipt**: 1% + mining fee for automatic liquidity
- Shipping**: 0.4% routing fee on the Lightning network


**Webhooks:** Webhooks enable Phoenixd to **automatically notify** your applications when an event occurs (payment received, invoice paid, channel opened, etc.). Instead of constantly asking Phoenixd for updates, your application receives an instant HTTP notification.


**Your online store automatically receives a notification when a customer pays for an order, enabling instant validation of the transaction.


Configuration in `phoenix.conf` :

```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```


## Advanced applications


### LNURL integrations


Phoenixd natively supports LNURL protocols for advanced integration:


**LNURL-Pay:** Pay for LNURL-compatible services

```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```


**LNURL-Withdraw :** Retrieve funds from LNURL services

```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```


**LNURL-Auth:** Authentication via Lightning to access services

```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```


### Integration with LNbits


LNbits can use Phoenixd as a funding source according to its [official documentation](https://docs.lnbits.org/guide/wallets.html):


**LNbits configuration:**

```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```


This integration allows you to create LNbits sub-accounts powered by your Phoenixd node, providing a web-based Interface for managing multiple Lightning wallets.


### Custom applications


Thanks to its comprehensive REST API, you can develop :


**E-commerce:** Direct integration of Lightning payments into your store

**Donation services:** Donation systems with invoices and automatic webhooks

**Social networking bots:** Telegram/Discord bots with tip functions

**Paywall Lightning:** Premium content available for a Lightning fee


## Safety and best practices


### Access protection


**API passwords:** Automatically generated passwords are the keys to your Lightning treasury. Never share them, and change them if in doubt.


**Firewall:** Never leave port 9740 open directly to the Internet. Always use nginx with HTTPS.


**Enhanced authentication:** Consider a VPN or Tailscale to restrict access to your server to authorized devices only.


### Essential backups


**seed recovery:** Save your 12 words in a safe place, off the server. This is your only guarantee of recovery.


*~/.phoenix directory:** Back up this folder regularly (after Phoenixd has been shut down) to preserve channel status and speed up restoration.


**Service recovery codes:** Also keep backup codes for all services where you activate 2FA with your Phoenix.


### Monitoring and maintenance


**Monitoring logs:**

```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```


**Updates:** Watch [GitHub releases](https://github.com/ACINQ/phoenixd/releases) for new versions. Updating is as simple as replacing the binary and restarting the service.


## Comparison with alternatives


### Phoenixd vs Phoenix standard


**Phoenix standard (mobile) :**


- ✅ Immediate installation, zero configuration
- ✅ Interface mobile intuitive
- ✅ Same auto-save as Phoenixd
- ❌ No API for developers
- ❌ No access to detailed logs


**Phoenixd (server) :**


- ✅ HTTP API for integrations
- ✅ Full access to logs
- ✅ Personal infrastructure
- ❌ Requires technical skills
- ❌ Server maintenance required


**Both use ACINQ as their LSP for automatic liquidity.


### Phoenixd vs LND/Core Lightning


**LND/Core Lightning :**


- ✅ Total control, full Lightning protocol
- ✅ Large community, mature ecosystem
- ❌ Complex manual liquidity management
- ❌ Large learning curve


**Phoenixd :**


- ✅ Automatic liquidity management (like Phoenix mobile)
- ✅ API for developers
- ✅ Simplified configuration
- ❌ Uses ACINQ as LSP (no independent routing)
- ❌ Less flexible than complete nodes


## Solving common problems


### API access problems


**Authentication failed" error:**

1. Check the password in the file `~/.phoenix/phoenix.conf`

2. Check authentication format `-u:password`

3. Make sure Phoenixd is running (`./phoenix-CLI getinfo`)


**Connection timeouts:**


- Check that Phoenixd is listening on the correct port (9740)
- Test local access before configuring HTTPS
- Check logs: `journalctl -u phoenixd -f`


### Liquidity problems


**Payments not arriving :**

1. Check that the amount exceeds the minimum threshold (~30k Sats)

2. Consult logs to identify channel errors

3. Restart Phoenixd if necessary


**Balance in "expense credit":**

Small payments are stored as a provision. Receive a larger amount to trigger channel opening and release these funds.


## Conclusion


Phoenixd represents an excellent compromise between ease of use and technical sovereignty for developers. It offers a simple yet powerful Lightning API with automatic liquidity management, eliminating the complexity of traditional Lightning nodes.


This solution is particularly well suited to developers and companies wishing to :


- Integrate Bitcoin Lightning into your applications
- Avoid the complexity of Lightning channel management
- Benefit from a self-hosted infrastructure
- A simple, reliable API


With Phoenixd, you build your own private Lightning infrastructure with a modern REST API and automatic management of technical aspects. It's the ideal solution for democratizing Lightning integration in your projects.


## Useful resources


### Official documentation


- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Source code and releases
- Phoenix Server** site: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Full documentation
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Frequently asked questions


### Community support


- GitHub Issues** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Technical support
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - News and announcements