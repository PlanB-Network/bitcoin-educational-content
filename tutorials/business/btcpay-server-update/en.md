---
name: Updating BTCPay Server
description: Apply a security update to your BTCPay Server instance and rotate the credentials that matter
---

![cover](assets/cover.webp)

Running your own payment processor means you are also your own security team. When the BTCPay Server maintainers publish a security release, nobody will patch your instance for you: the update, the verification, and the credential rotation that follows are yours to perform.

This tutorial walks through the whole procedure, whatever way you deployed BTCPay Server: check the running version, apply the update on your deployment type, verify that it actually landed, and rotate the secrets that an attacker may have captured while your instance was vulnerable.

If you have not deployed BTCPay Server yet, start with the installation guide:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## The August 2026 critical vulnerability

⚠️ **Critical security alert (7 August 2026):** a critical vulnerability affecting BTCPay Server is being actively exploited and can lead to a loss of funds. Update your instance to **version 2.4.2** immediately via `Admin Dashboard > Server > Maintenance > Update`, then check that the footer displays `2.4.2`. If you cannot update straight away, shut down your BTCPay Server. Once updated, you must also completely refresh your macaroons and your `macaroons.db`, completely refresh the authentication strings of any other Lightning backend, and, if you generated a hot on-chain wallet inside BTCPay Server, move those funds and recreate the wallet. Integrators should also update NBXplorer to version 2.6.10. Source: [BTCPay Server 2.4.2 release notes](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Version 2.4.2 was published on 7 August 2026. The release notes state that it fixes a critical vulnerability that was already being exploited in the wild, reported by `brunoerg` and `benthecarman` through the Bitcoin Red Team effort. The same release also fixes a TOTP two-factor authentication bypass through Greenfield Basic authentication, and disables Greenfield Basic authentication by default five minutes after account creation.

Two consequences follow from "actively exploited":

- **Updating is not optional and not something to schedule for next week.** An unpatched instance that is reachable from the internet must be either updated or switched off.
- **Updating is not enough on its own.** If your instance was compromised before you patched, the attacker may already hold copies of your Lightning credentials and of any hot wallet key material BTCPay Server generated for you. Those secrets stay valid after the update until you rotate them. The rotation section below is the part people skip, and it is the part that actually protects your funds.

## Step 1 — Find out which version you are running

Log in to your BTCPay Server and look at the **footer of any page**: the version string is displayed there. You can also open `Admin Dashboard > Server > Maintenance`, which shows the current version and the update controls.

If your instance exposes the Greenfield API, `GET /api/v1/server/info` returns the version as well.

Anything below `2.4.2` is vulnerable.

## Step 2 — Update

### Self-hosted Docker deployment (the standard install)

This covers the official Docker deployment, which is what you get from the BTCPay Server documentation, from the LunaNode one-click launcher, and from most VPS installs.

The simplest path is the web interface:

1. Go to `Admin Dashboard > Server > Maintenance`.
2. Click **Update**.
3. Wait for the containers to be pulled and restarted. The interface will be unavailable for a few minutes.

If the web interface is unreachable, or you prefer to see the logs, do it over SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

On a default install `$BTCPAY_BASE_DIRECTORY` is `/root`, so the directory is `/root/btcpayserver-docker`. The script pulls the latest images, recreates the containers, and prints the resulting versions.

The Docker deployment ships NBXplorer alongside BTCPay Server, so a standard update also brings NBXplorer to the recommended `2.6.10`. If you run NBXplorer separately — typical for integrators and for custom stacks — update it explicitly.

### Umbrel

Open the Umbrel dashboard, go to the **App Store**, find BTCPay Server and apply the update if one is offered.

⚠️ **Important:** app-store packages are repackaged by the Umbrel team and can lag behind upstream by hours or days. Check the version in the BTCPay Server footer after updating. If it is still below `2.4.2`, **stop the app** from the Umbrel dashboard and wait for the packaged release rather than leaving a vulnerable instance running.

The dedicated Umbrel guide covers the app itself:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Same logic: update BTCPay Server from the StartOS marketplace, then verify the version in the footer. If the packaged version is not yet `2.4.2`, stop the service until it is.

### Managed and third-party hosting

If someone else operates your instance (a hosting provider, an association, a friend's server), you still need the confirmation. Ask the operator for the version string shown in the footer, and ask explicitly whether the post-update credential rotation described below has been performed. "We updated" is not the same answer as "we rotated your macaroons".

## Step 3 — Verify the update actually landed

Reload the BTCPay Server interface and read the version in the footer. It must show `2.4.2` or higher.

Do not rely on the update command exiting without an error: on constrained machines an image pull can fail silently and leave the previous container running. Read the version, every time.

## Step 4 — Rotate your credentials

This is the step that turns "patched" into "safe". Because the vulnerability was being exploited before the fix shipped, treat every secret your instance held as potentially known to an attacker.

### Lightning: LND

Regenerate the macaroons **and** the `macaroons.db` file. Deleting the macaroon files alone is not enough — LND derives macaroons from the root key stored in `macaroons.db`, so an attacker holding a copy of an old macaroon keeps access until that database is recreated.

The procedure is: stop LND, remove `macaroons.db` and the `*.macaroon` files from the network directory (for mainnet, `data/chain/bitcoin/mainnet/` inside the LND data directory), then restart and unlock LND, which recreates them. Back up the directory first, and re-pair every application that used the old macaroons — BTCPay Server itself, Zeus, Thunderhub, RTL, Alby, and any script you wrote.

If you also expose LND over the internet, review its TLS certificate and any `lnd.conf` credentials at the same time.

### Lightning: other backends

Anything that authenticates to your node with a string must get a new string:

- **Core Lightning**: regenerate the rune or the access credentials used by the connection.
- **Phoenixd**: rotate the HTTP password.
- **LNbits and similar**: revoke and reissue the admin and invoice keys.
- **Remote node connection strings** stored in BTCPay Server store settings: rewrite them with the new secrets.

### Hot on-chain wallet generated inside BTCPay Server

If you let BTCPay Server generate an on-chain wallet for you — as opposed to connecting a hardware wallet or importing an xpub whose keys never touched the server — that seed lived on the machine.

Consider it burned:

1. Create a new wallet, ideally with a hardware wallet so the keys never sit on the server again.
2. Sweep the funds from the old wallet to the new one.
3. Replace the derivation scheme in the store settings with the new wallet.
4. Never reuse the old seed.

Watch-only setups (xpub or hardware wallet) do not need this: the private keys were never on the server. This is exactly why the installation guide recommends them.

### BTCPay Server accounts and API keys

While you are at it:

- Change the passwords of every user account on the instance.
- Revoke and reissue all Greenfield **API keys**.
- Re-enroll two-factor authentication, given that 2.4.2 fixes a 2FA bypass.
- Open `Admin Dashboard > Server > Users` and check that no unexpected account exists.
- Review recent **payouts**, **pull payments** and **refunds** for entries you did not create.
- Review your webhooks and their secrets.

## Step 5 — Stay informed for the next one

Security releases only help the operators who hear about them:

- Watch the [BTCPay Server releases on GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub can email you on every new release of a repository.
- Follow the project's announcement channels and the [official blog](https://blog.btcpayserver.org/).
- Keep your instance on a version you can update quickly: the further behind you are, the more painful an emergency update becomes.

Self-hosting gives you sovereignty over your payments. The cost of that sovereignty is exactly this: reading release notes and being the one who patches.
