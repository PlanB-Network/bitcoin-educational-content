---
name: RGB CLI
description: How do I create and exchange smart contracts on RGB?
---
![cover](assets/cover.webp)

In this tutorial, we'll follow the step-by-step process of writing a contract, using the command-line tool `rgb` created by the LNP/BP association. The aim is to show how to install and manipulate the CLI, compile a Schema, import the Interface and Interface Implementation, and then issue an RGB asset. We'll also look at the underlying logic, including compilation and state validation. At the end of this tutorial, you should be able to reproduce the process and create your own RGB contracts.

## RGB protocol reminder

RGB is a protocol that runs on top of Bitcoin and emulates smart contract functionality and digital asset management, without overloading the blockchain on which it is based. Unlike conventional on-chain smart contracts (as on Ethereum, for example), RGB relies on a "*Client-side validation*" system: the majority of data and status histories are exchanged and stored exclusively by the participants involved, whereas the Bitcoin blockchain only hosts small cryptographic commitments (via mechanisms such as *Tapret* or *Opret*). In the RGB protocol, the Bitcoin blockchain therefore only serves as a time-stamping server and double-spending protection system.

An RGB contract is structured like an evolutionary state machine. It starts with a Genesis that defines the initial state (describing, for example, the supply, ticker or other metadata) according to a strictly typed and compiled Schema. State Transitions and, if necessary, State Extensions are then applied to modify or extend this state. Each operation, whether transferring fungible assets (RGB20) or creating unique assets (RGB21), involves *Single-use Seals*. These link Bitcoin UTXOs to off-chain states and prevent double spending, while ensuring confidentiality and scalability.

To learn more about how the RGB protocol works, I recommend you take this comprehensive training course:

https://planb.network/courses/csv402
The internal logic of RGB is based on Rust libraries that you, as developers, can import into your projects to manage the *Client-side Validation* part. In addition, the LNP/BP team is working on bindings for other languages, but this has not yet been finalized. In addition, other entities such as Bitfinex are developing their own integration stacks, but we'll talk about these in another tutorial. For the time being, the `rgb` CLI is the official reference, even if it remains relatively unpolished.

## Installation and presentation of the rgb CLI tool

The main command is simply called `rgb`. It is designed to be reminiscent of `git`, with a set of sub-commands for manipulating contracts, invoking them, issuing assets and so on. Bitcoin Wallet is not currently integrated, but will be in an imminent version (0.11). This next version will enable users to create and manage their wallets (via descriptors) directly from `rgb`, including PSBT generation, compatibility with external hardware (e.g. a hardware wallet) for signing, and interoperability with software such as Sparrow. This will simplify the entire asset issuance and transfer scenario.

### Installation via Cargo

We install the tool in Rust with :

```bash
cargo install rgb-contracts --all-features
```

(Note: the crate is called `rgb-contracts`, and the installed command will be named `rgb`. If a crate named `rgb` already existed, there could have been a collision, hence the name)

The installation compiles a large number of dependencies (e.g. command parsing, Electrum integration, zero-knowledge proofs management, etc.).

Once installation is complete, the :

```bash
rgb
```

Running `rgb` (without arguments) displays a list of available sub-commands, such as `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, etc. You can change the local storage directory (a stash that holds all logs, schematics and implementations), choose the network (testnet, mainnet) or configure your Electrum server.

![RGB-CLI](assets/fr/01.webp)

### First overview of controls

When you run the following command, you'll see that an `RGB20` interface is already integrated by default:

```bash
rgb interfaces
```

If this interface is not integrated, clone the :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compile it:

```bash
cargo run
```

Then import the interface of your choice:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

However, we are told that no schema has yet been imported into the software. Nor is there a contract in the stash. To see it, run the command :

```bash
rgb schemata
```

You can then clone the repository to retrieve certain schematics:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

This repository contains, in its `src/` directory, several Rust files (for example `nia.rs`) which define schemas (NIA for "*Non Inflatable Asset*", UDA for "*Unique Digital Asset*", etc.). To compile, you can then run :

```bash
cd rgb-schemata
cargo run
```

This generates several `.rgb` and `.rgba` files corresponding to the compiled schematics. For example, you'll find `NonInflatableAsset.rgb`.

### Importing Schema and Interface Implementation

You can now import the schematic into `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

This adds it to the local stash. If we run the following command, we see that the schema now appears:

```bash
rgb schemata
```

## Contract creation (issuing)

There are two approaches to creating a new asset:


- Either we use a script or code in Rust that builds a Contract by populating schema fields (global state, Owned States, etc.) and produces a `.rgb` or `.rgba` file;
- Or use the `issue` sub-command directly, with a YAML (or TOML) file describing the token's properties.

You can find examples in Rust in the `examples` folder, which illustrate how you build a `ContractBuilder`, fill in the `global state` (asset name, ticker, supply, date, etc.), define the Owned State (to which UTXO it is assigned), then compile all this into a *contract consignment* that you can export, validate and import into a stash.

The other way is to manually edit a YAML file to customize the `ticker`, the `name`, the `supply`, and so on. Suppose the file is called `RGB20-demo.yaml`. You can specify :


- `spec`: ticker, name, precision ;
- `terms`: a field for legal notices ;
- `issuedSupply` : the amount of token issued ;
- `assignments`: indicates the Single-use Seal (*seal definition*) and the quantity unlocked.

Here is an example of a YAML file to create:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

Then simply run the command :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

In my case, the unique schema identifier (to be enclosed in single quotes) is `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` and I haven't put any issuer. So my order is :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

If you don't know the schema ID, run the command :

```bash
rgb schemata
```

The CLI replies that a new contract has been issued and added to the stash. If we type the following command, we see that there is now an additional contract, corresponding to the one just issued:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Then, the next command displays the global states (name, ticker, supply...) and the list of Owned States, i.e. allocations (for example, 1 million `PBN` tokens defined in UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Export, import and validation

To share this contract with other users, it can be exported from the stash to a :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

The `myContractPBN.rgb` file can be passed on to another user, who can add it to his stash with the command :

```bash
rgb import myContractPBN.rgb
```

On import, if it's a simple *contract consignment*, we'll get an "`Importing consignment rgb`" message. If it's a larger *state transition consignment*, the command will be different (`rgb accept`).

To ensure validity, you can also use the local validation function. For example, you could run :

```bash
rgb validate myContract.rgb
```

### Stash usage, verification and display

As a reminder, the stash is a local inventory of schemas, interfaces, implementations and contracts (Genesis + transitions). Each time you run "import", you add an element to the stash. This stash can be viewed in detail with the command :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

This will generate a folder with details of the entire stash.

## Transfer and PSBT

To carry out a transfer, you'll need to manipulate a local Bitcoin wallet to manage the `Tapret` or `Opret` commitments.

### Generate an invoice

In most cases, interaction between the participants in a contract (e.g. Alice and Bob) takes place via the generation of an invoice. If Alice wants Bob to execute something (a token transfer, a reissue, an action in a DAO, etc.), Alice creates an invoice detailing her instructions to Bob. So we have :


- Alice** (the issuer of the invoice) ;
- Bob** (who receives and executes the invoice).

Unlike other ecosystems, an RGB invoice is not limited to the notion of payment. It can embed any request linked to the contract: revoke a key, vote, create an engraving (*engraving*) on an NFT, etc. The corresponding operation can be described in the contract interface. The corresponding operation can be described in the contract interface.

The following command generates an RGB invoice:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

With :


- `$CONTRACT`: Contract identifier (*ContractId*) ;
- `$INTERFACE`: the interface to be used (e.g. `RGB20`) ;
- `$ACTION`: the name of the operation specified in the interface (for a simple fungible token transfer, this could be "Transfer"). If the interface already provides a default action, you don't need to enter it again here;
- `$STATE`: the status data to be transferred (for example, an amount of tokens if a fungible token is transferred);
- `$SEAL`: the beneficiary's (Alice's) Single-use Seal, i.e. an explicit reference to an UTXO. Bob will use this info to build the witness transaction, and the corresponding output will then belong to Alice (in *blinded UTXO* or unencrypted form).

For example, with the following commands

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

The CLI will generate an invoice like :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

It can be transmitted to Bob via any channel (text, QR code, etc.).

### Making a transfer

To transfer from this invoice :


- Bob (who holds the tokens in his stash) has a Bitcoin wallet. He needs to prepare a Bitcoin transaction (in the form of a PSBT, e.g. `tx.psbt`) which spends the UTXOs where the required RGB tokens are located, plus one UTXO for currency (exchange) ;
- Bob executes the following command:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- This generates a `consignment.rgb` file which contains :
 - The transition history proving to Alice that the tokens are genuine;
 - The new transition that transfers tokens to Alice's Single-use Seal ;
 - A witness transaction (unsigned).
- Bob sends this `consignment.rgb` file to Alice (by e-mail, a sharing server or an RGB-RPC protocol, Storm, etc.);
- Alice receives `consignment.rgb` and accepts it in its own stash :

```bash
alice$ rgb accept consignment.rgb
```


- The CLI checks the validity of the transition and adds it to Alice's stash. If invalid, the command fails with detailed error messages. Otherwise, it succeeds, and reports that the sample transaction has not yet been broadcast on the Bitcoin network (Bob is waiting for Alice's green light);
- By way of confirmation, the `accept` command returns a signature (*payslip*) which Alice can send to Bob to show him that she has validated the *consignment* ;
- Bob can then sign and publish (`--publish`) his Bitcoin transaction:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- As soon as this transaction is confirmed on-chain, ownership of the asset is considered transferred to Alice. Alice's wallet, monitoring the transaction's mining, sees the new Owned State appear in its stash.

You now know how to issue and transfer an RGB contract. If you found this tutorial useful, I'd be very grateful if you'd put a green thumb below. Please feel free to share this article on your social networks. Thank you very much!

I also recommend this other tutorial in which I explain how to launch an RGB-compatible Lightning node to exchange tokens almost instantaneously:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea