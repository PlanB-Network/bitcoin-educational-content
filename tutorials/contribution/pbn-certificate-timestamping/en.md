---
name: Timestamping of Plan ₿ Network certificates and diplomas
description: Understand how Plan ₿ Network issues verifiable proofs for your certificates and diplomas
---

![cover](assets/cover.webp)

If you are reading this, there is a high probability that you received either a ₿-CERT test certificate or a diploma of completion for one of the course you attended on planb.network, so congratulation for this achievement!

In this tutorial, we will discover how Plan ₿ Network issues verifiable proofs for your ₿-CERT test certificate or any Diploma regarding Course Completion. Then, in a second part we will describe how to verify the authenticity of these proofs.

# Plan ₿ Network proof mechanism

At Plan ₿ Network, we cryptographically sign certificates and diplomas, and time-stamp them using the Timechain (i.e. The Bitcoin blockchain), through a proof mechanism that relies on two cryptographic operations:

1. A GPG-signature on a text file that synthesizes your achievements
2. The timestamping of the same signed file via [opentimestamps](https://opentimestamps.org/).

The first operation enables you to confirm the issuer of the certificate (or diploma), while the second operation allows you to verify the date of its issuance.
We believe that this simple proof mechanism empowers us to issue certificates and diplomas with undeniable evidence that anyone can independently verify.

![image](./assets/proof-mechanism.webp)

Thanks to this proof mechanism, any attempt to alter even the smallest detail of your certificate or diploma will result in a completely different SHA-256 hash of the signed file, instantly revealing any tampering, as both the signature and the timestamp will no longer be valid. Moreover, if anyone attempts to maliciously forge certificates or diplomas on behalf of Plan ₿ Network, a simple verification of the signature will expose the fraud.

## How does the GPG-signature work?

The GPG signature is generated using an open-source software called GNU Privacy Guard. This software allows users to easily create private keys, sign and verify signatures, and encrypt and decrypt files. For the purposes of this tutorial, it's important to note that Plan ₿ Network uses GPG to create its private/public keys and to sign all ₿-CERT Certificates and Diplomas of Course Completion.

On the other hand, if someone wants to verify the authenticity of a signed file, they can use GPG to import the public key of the issuer and verify it.

For those who are curious and want to learn more about this fantastic software, you can refer to ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## How does time-stamping work?

Anyone can use OpenTimestamps to timestamp a file and obtain verifiable proof of its existence. In other words, it does not provide proof of when the file was created, but rather proof that the file existed no later than a specific moment in time.
OpenTimestamps provides this service for free by utilizing a highly efficient method to store proof in the Bitcoin blockchain. It employs the SHA-256 hash algorithm to create a unique identifier for your file, and constructs a Merkle tree using the hashes of the files submitted by other users. Only the hash of the Merkle tree structure is anchored in an OP_RETURN transaction, ensuring a secure and compact way to verify file existence.
Once this transaction gets into a block, anyone with the initial file and the `.ots` file associated to it can verify the authencity of the timestamping. In the second part of the tutorial, we will see how to verify your Bitcoin Certificate or any Diploma of Course Completion through a teminal and through a graphical interface on the website of OpenTimestamps.

# How to verify a Plan ₿ Network ₿-CERT certificate or Diploma

## Step 1. Download your Certificate or Diploma

Log into your personal/student dashboard on planb.network.

![image](./assets/login.webp)

Go to "Credentials" by clicking on the lefthand-side menu, and select your exam session or your Diploma.

![image](./assets/credential.webp)

Download the zip file.

![image](./assets/download.webp)

Extract the contents by right-clicking on the `.zip` file and selecting "Extract". You will find three different files:

- A signed text file (e.g. certificate.txt)
- An Open timestamp (OTS) file (e.g. certificate.txt.ots)
- A PDF certificate (e.g. certificate.pdf)

## Step 2: How can you verify the Signature of the Text File?

First, go to the folder where you extracted the files and open a terminal (right-click on the folder window and clik on "Open in Teminal"). Then, follow the instructions below.

1. Import Plan ₿ Network public PGP key with the following command:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

You should see a message like the following if you successfully imported the PGP Key

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

NOTE: if you see that 1 key has been processed and 0 keys have been imported, it likely means you have already imported the same key previously, which is perfectly fine.

2. Verify the signature of the certificate or diploma using the following command:

```bash
gpg --verify certificate.txt
```

This command should show you details about the signature, including:

- Who signed it (Plan ₿ Network)
- When it was signed
- Whether the signature is valid or not

This is an example of the result:

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

If you see a message like "BAD signature", that means that the file has been tampered.

## Step 3: Verifying the Open Timestamp

### Verifying via a Graphical Interface

1. Visit the OpenTimestamps website: https://opentimestamps.org/
2. Click on the "Stamp & Verify" tab.
3. Drag and drop the OTS file (e.g. `certificate.txt.ots`) into the designated area.
4. Drag and drop the timestamped file (e.g. `certificate.txt`) into the designated area.
5. The website will automatically verify the open timestamp and display the result.

If you see a message like the following, the timestamp is valid:

![cover](assets/opentimestamp_wegui_verified.webp)

### The CLI Method

NOTE: this procedure **will require a running local Bitcoin node**

1. Install the OpenTimestamps client from the official [repository](https://github.com/opentimestamps/opentimestamps-client) by running the following command:

```
pip install opentimestamps-client
```

2. Navigate to the directory containing the extracted certificate files.

3. Run the following command to verify the open timestamp:

```
ots verify certificate.txt.ots
```

This command will:

- Check the timestamp against the Bitcoin's blockchain
- Show you exactly when the file was timestamped
- Confirm the timestamp's authenticity

### Final results

The verification is successful if **both** the following messages are displayed:

1. The GPG signature is reported as **"Good signature from Plan ₿ Network"**
2. The OpenTimestamps verification shows a specific Bitcoin block timestamp and reports **"Success! Bitcoin block [blockheight] attests data existed as of [timestamp]"**

Now that you know how Plan ₿ Network issues verifiable proofs for any ₿-CERT Certificate and Diploma, you can easily verify the integrity of them.
