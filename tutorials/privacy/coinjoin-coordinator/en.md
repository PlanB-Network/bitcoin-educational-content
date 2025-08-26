---
name: Coinjoin Coordinator
description: How to setup and run a coinjoin coordinator following the WabiSabi protocol (used in Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)

---

## Introduction

In this expert guide we will help you set-up a coinjoin coordinator, essentially a server that brings together people that want to save on transaction fees or increase their onchain privacy in collaborative transactions. Since there is no longer a company run coordinator bundled with Wasabi Wallet, users have to find and select their own preferred coordinator server. Only a few coordinators have shown up asking a 0% coordination fee, so the developers of Wasabi Wallet have been working hard to make it as easy as possible to start running your own community coordinator (on hardware as small as a Raspberry Pi5!).

## Requirements

- VPS (hosted node) or computer/server (self-hosted node)
- Pruned/Full Bitcoin Core node (tested with v29.0)
- (sub)Domain forwarding traffic to the node (e.g. coinjoin.[yourdomain].io)

## Installation

On the node we want to download and install the latest released version of Wasabi Wallet, which includes a backend and coordinator

## Configuration

Before running the coordinator you need to edit the Config.yaml file with your:
- Bitcoin RPC credentials
- Preferred round parameters
- Coordinator Extended Public Key (create a new wallet for receiving collected dust)
- Allowed input and output address types
- Announcer configuration for publishing over nostr (name, description, Uri, minimum inputs, nostr relay, nostr private key)

Also the traffic has to be forwarded to your node for this service in nginx, which can be done with this example:

`this is code`

For the new nginx configuration to load, restart the nginx service.

## Running

Once all the parameters have been set you can run the coordinator service and start your first round 🕶️

---