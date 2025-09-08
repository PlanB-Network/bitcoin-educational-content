---
name: Graylog
description: Centralize and analyze your logs easily
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian BURNEL published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## Deploying Graylog on Debian 12


### I. Presentation


Graylog is an open source "log sink" solution designed to centralize, store and analyze logs from your machines and network devices in real time. In this tutorial, we'll learn how to install the free version of Graylog on a Debian 12 machine!


Within an information system, each **server**, whether running **Linux** or **Windows**, and each **network device** (switch, router, firewall, etc...) **generates its own logs**, stored locally. With logs stored locally on each machine, event analysis and correlation is very difficult... This is where **Graylog** comes in. It will act as a **log sink**, meaning that **all your machines will send it their logs** (via syslog, for example). Graylog will then **store and index these logs**, while allowing you to perform global searches and create alerts.


Graylog is an analysis and monitoring tool that makes it easier to identify suspicious behavior and various problems (stability, performance, etc.).



![Image](assets/fr/034.webp)


**Note: the free version, **Graylog Open**, is not a SIEM as Wazuh is, especially as it lacks real intrusion detection functions.


### II. Prerequisites


The **stack Graylog** is based on **several components** that we'll need to install and configure. Here, we'll install all the components on the same server, but it is possible to create clusters based on several nodes and distribute the roles across several servers. For the purposes of this tutorial, we'll be installing **Graylog 6.1**, the most recent version to date.



- MongoDB 7**, the current recommended version for Graylog (minimum 5.0.7, maximum 7.x)
- OpenSearch**, an open source Fork of Elasticsearch created by Amazon (minimum 1.1.x, maximum 2.15.x)
- OpenJDK 17**


The **Graylog server** is running on **Debian 12**, but installation is possible on other distributions, including via Docker. The virtual machine is equipped with **8 GB RAM** and **256 GB disk space**, in order to have enough resources for all components (otherwise this can have a significant impact on performance). However, I'm giving this as a rough guide, as **the sizing of the Graylog architecture depends on the amount of information to be processed**. Graylog can process 30 MB or 300 MB of data per day, as well as 300 GB of data per day... It is a **scalable solution** capable of handling **terabytes of logs** (see [this page](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).


![Image](assets/fr/032.webp)


Source: Graylog


Before starting configuration, assign a static IP address to the Graylog machine and install the latest updates. Be sure to set the local machine's time zone and define an NTP server for date and time synchronization. Here's the command to run:


```
sudo timedatectl set-timezone Europe/Paris
```


**Note: **OpenSearch installation is optional** if you use **Graylog Data Node** instead.


### III Step-by-step installation of Graylog


Let's start by updating the package cache and installing the tools we need for what's to come.


```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```


![Image](assets/fr/030.webp)


#### A. Installing MongoDB


Once that's done, we'll start installing MongoDB. Download the GPG key corresponding to the MongoDB repository:


```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```


Then add the MongoDB 6 repository to the Debian 12 machine:


```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```


Next, we'll update the package cache and attempt to install MongoDB:


```
sudo apt-get update
sudo apt-get install -y mongodb-org
```


MongoDB cannot be installed because a dependency is missing: **libssl1.1**. We'll have to install this package manually before we can proceed, because Debian 12 doesn't have it in its repositories.


```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```


We're going to download the DEB package named "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (latest version) with the **wget** command, then install it with the **dpkg** command. This produces the following two commands:


```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```


![Image](assets/fr/028.webp)


Restart MongoDB installation:


```
sudo apt-get install -y mongodb-org
```


Then restart the MongoDB service and enable it to start automatically when the Debian server is launched.


```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```


With MongoDB installed, we can move on to installing the next component.


#### B. Installing OpenSearch


Let's move on to installing OpenSearch on the server. The following command adds the signature key for OpenSearch packages:


```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```


Then add the OpenSearch repository so that we can download the package with **apt** afterwards:


```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```


Update your package cache:


```
sudo apt-get update
```


Then **install OpenSearch**, taking care to **define the default password for your instance's Admin** account. Here, the password is "**IT-Connect2024!**", but replace this value with a strong password. **Avoid weak passwords** like "**P@ssword123**" and use at least **8 characters** with at least one character of each type (lowercase, uppercase, number and special character), otherwise there will be an error at the end of the installation. **This is a prerequisite since OpenSearch 2.12.**


```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```


Please be patient during installation...


When you've finished, take a moment to perform the minimum configuration. Open the configuration file in YAML format:


```
sudo nano /etc/opensearch/opensearch.yml
```


When the file is open, set the following options:


```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```


This OpenSearch configuration is designed to set up a single node. Here are some explanations of the different parameters we use:



- cluster.name: graylog**: this parameter names the OpenSearch cluster with the name "**graylog**".
- node.name: ${HOSTNAME}**: the node name is set dynamically to match that of the local Linux machine. Even if we only have one node, it's important to name it correctly.
- path.data: /var/lib/opensearch**: this path specifies where OpenSearch stores its data on the local machine, in this case in "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: this path defines where OpenSearch log files are stored, here in "**/var/log/opensearch**".
- discovery.type: single-node**: this parameter configures OpenSearch to work with a single node, hence the choice of the "**single-node**" option.
- network.host: 127.0.0.1**: this configuration ensures that OpenSearch only listens on its Interface local loop, which is sufficient since it's on the same server as Graylog.
- action.auto_create_index: false**: by disabling automatic index creation, OpenSearch will not automatically create an index when a document is sent without an existing index.
- plugins.security.disabled: true**: this option deactivates the OpenSearch security plugin, meaning that there will be no authentication, access management or communication encryption. This setting saves time when setting up Graylog, but should be avoided in production (see [this page](https://opensearch.org/docs/1.0/security-plugin/index/)).


Some options are already present, so you simply need to remove the "#" to activate them, then indicate your value. If you can't find an option, you can declare it directly at the end of the file.


![Image](assets/fr/023.webp)


Save and close this file.


#### C. Configure Java (JVM)


You need to configure the Java Virtual Machine used by OpenSearch in order to adjust the amount of memory this service can use. Edit the following configuration file:


```
sudo nano /etc/opensearch/jvm.options
```


With the configuration deployed here, **OpenSearch will start with 4 GB of allocated memory and can grow up to 4 GB**, so there will be no memory variation during operation. Here, the configuration takes into account the fact that the virtual machine has a total of **8 GB RAM**. Both parameters must have the same value. This means replacing the lines:


```
-Xms1g
-Xmx1g
```


With these lines:


```
-Xms4g
-Xmx4g
```


Here is an image of the modification to be made:


![Image](assets/fr/022.webp)


Close this file after saving it.


In addition, we need to check the configuration of the "**max_map_count**" parameter in the Linux kernel. It defines the limit of memory areas mapped per process, in order to meet the needs of our application. **OpenSearch**, like Elasticsearch**, recommends setting this value to "262144" to avoid memory management errors.


In principle, on a freshly installed Debian 12 machine, the value is already correct. But let's check. Run this command:


```
cat /proc/sys/vm/max_map_count
```


If you get a value other than "**262144**", run the following command, otherwise it's not necessary.


```
sudo sysctl -w vm.max_map_count=262144
```


Finally, enable OpenSearch autostart and launch the associated service.


```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```


If you display your system status, you should see a Java process with 4 GB RAM.


```
top
```


![Image](assets/fr/029.webp)


Next step: the long-awaited installation of Graylog!


#### D. Installing Graylog


To **install Graylog 6.1** in its latest version, run the following 4 commands to **download and install Graylog Server**:


```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```


When this is done, we need to make some changes to Graylog's configuration before trying to launch it.


Let's start by configuring these two options:



- password_secret**: this parameter is used to define a key used by Graylog to secure the storage of user passwords (in the spirit of a salting key). This key must be **unique** and **random**.
- root_password_sha2**: this parameter corresponds to the default administrator password in Graylog. It is stored as a Hash SHA-256.


We'll start by generating a 96-character key for the **password_secret** parameter:


```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```


Copy the returned value, then open the Graylog configuration file:


```
sudo nano /etc/graylog/server/server.conf
```


Paste the key into the **password_secret** parameter, like this:


![Image](assets/fr/027.webp)


Save and close the file.


Next, you need to set the password for the "**admin**" account created by default. In the configuration file, the Hash of the password must be stored, which means it must be calculated. The example below gives the Hash of the password "**LogsWells@**": adapt the value to your password.


```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```


Copy the value obtained as output (without the hyphen at the end of the line).


Open the Graylog configuration file again:


```
sudo nano /etc/graylog/server/server.conf
```


Paste the value into the **root_password_sha2** option like this:


![Image](assets/fr/026.webp)


While you're in the configuration file, set the "**http_bind_address**" option. Specify "**0.0.0.0:9000**" so that Graylog's Interface web can be accessed on port **9000**, via any server IP address.


![Image](assets/fr/024.webp)


Then set the "**elasticsearch_hosts**" option to `http://127.0.0.1:9200` to declare our local OpenSearch instance. This is necessary, as we're not using a **Graylog Data Node**. And without this option, it won't be possible to go any further...


![Image](assets/fr/025.webp)


Save and close the file.


This command activates Graylog so that it starts automatically on next boot, and immediately launches the Graylog server.


```
sudo systemctl enable --now graylog-server
```


Once this is done, try to connect to Graylog from a browser. Enter the server's IP address (or name) and port 9000.


**For your information:**


Not so long ago, an authentication window similar to the one below appeared when you first logged on to Graylog. You had to enter your login "**admin**" and your password. And then you'd be unpleasantly surprised to find that the connection didn't work.


![Image](assets/fr/031.webp)


It was necessary to go back to the command line on the Graylog server and consult the logs. We could then see that **for the first connection**, it is necessary to **use a temporary password**, specified in the logs.


```
tail -f /var/log/graylog-server/server.log
```


![Image](assets/fr/021.webp)


You then had to retry a connection with the user "**admin**" and the temporary password, and this allowed you to log in!


**This is no longer the case. All you have to do is log in with your admin account and the password configured on the command line


![Image](assets/fr/033.webp)


**Welcome to Graylog's Interface!


![Image](assets/fr/019.webp)


#### E. Graylog: create a new administrator account


Rather than using the admin account created natively by Graylog, you can create your own personal administrator account. Click on the "**System**" menu, then on "**Users and Teams**" to click on the "**Create user**" button. Then fill in the form and assign the administrator role to your account.


![Image](assets/fr/020.webp)


A personalized account can contain additional information, such as first and last name and e-mail address, unlike a native admin account. What's more, this ensures better traceability when each person works with a named account.


## Send logs to Graylog with rsyslog


### I. Presentation


In this second part, we'll learn how to configure a Linux machine to send its logs to a Graylog server. To do this, we'll install and configure Rsyslog on the system.


### II. Configuring Graylog to receive Linux logs


We'll start by configuring Graylog. There are three steps to complete:



- The creation of an **Input** to create an entry point allowing Linux machines to **send Syslog logs via UDP**.
- The creation of a new **Index** to store and **index all Linux logs**.
- Creation of a **Stream** to **route** the logs received by Graylog to the new Linux Index.


#### A. Create an Input for Syslog


Log on to Graylog Interface, click on "**System**" in the menu and then on "**Inputs**". In the drop-down list, select "**Syslog UDP**" then click on the button labelled "**Launch new input**". It is also possible to create a TCP Syslog Input, but this requires the use of a TLS certificate: a plus for security, but not covered in this article.


![Image](assets/fr/001.webp)


A wizard will appear on the screen. Start by giving this Input a name, for example "**Graylog_UDP_Rsyslog_Linux**" and choose a port. By default, the port is "**514**", but you can customize it. Here, port "**12514**" is selected.


![Image](assets/fr/016.webp)


You can also check the "**Store full message**" option to store the full log message in Graylog. Click on "**Launch Input**".


![Image](assets/fr/017.webp)


The new Input has been created and is now active. Graylog can now receive Syslog logs on port 12514/UDP, but we haven't finished configuring the application yet.


![Image](assets/fr/018.webp)

**Note: a single Input can be used to store logs from several Linux machines.


#### B. Create a new Linux Index


We need to create an Index in Graylog to store logs from Linux machines. An **index** in Graylog is a storage structure that contains the logs received, i.e. the messages received. Graylog uses OpenSearch as its storage engine, and messages are indexed to enable fast, efficient searches.


From Graylog, click on "**System**" in the menu, then on "**Indices**". On the new page that appears, click on "**Create index set**".


![Image](assets/fr/005.webp)


Name this index, for example "**Linux Index**", add a description and a prefix, before confirming. Here, we'll **store all Linux logs in this index**. It is also possible to create specific indexes to store only certain logs (only [SSH] logs (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), Web service logs, etc.).


![Image](assets/fr/006.webp)


Now we need to create a new stream to route messages to this index.


#### C. Create a Stream


To create a new stream, click on "**Streams**" in Graylog's main menu. Then click on the "**Create stream**" button on the right. In the window that appears, name the stream, for example "**Linux Stream**" and choose the index "**Linux Index**" for the field named "**Index Set**". Confirm your choice.


**Note: messages corresponding to this stream will also be included in the "**Default Stream**", unless you check the "**Remove matches from 'Default Stream'**" option.


![Image](assets/fr/002.webp)


Then, in your steam settings, click on the "**Add stream rule**" button to add a new message routing rule. If you can't find this window, click on "**Streams**" in the menu, then on the line corresponding to your stream, click on "**More**" then "**Manage Rules**".


Choose the "**match input**" type and select the previously created **Rsyslog input in UDP**. Confirm with the "**Create Rule**" button. All messages to our new Input will now be sent to the Index for Linux.


![Image](assets/fr/003.webp)


Your new Stream should appear in the list and it should be in the "**Running**" state. The message bandwidth shows "**0 msg/s**", as we are not currently sending any logs to the Rsyslog UDP input. To view a stream's logs, simply click on its name.


![Image](assets/fr/004.webp)


**Everything's ready on the Graylog side**. The next step is to configure the Linux machine.


### III. Installing and configuring Rsyslog on Linux


Log on to the Linux machine, either locally or remotely, and use a user account with permissions to elevate its privileges (via sudo). Otherwise, use the "root" account directly.


#### A. Installing the Rsyslog package


Start by updating the package cache and installing the package named "**rsyslog**".


```
sudo apt-get update
sudo apt-get install rsyslog
```


Then check the service status. In most cases, it's already running.


```
sudo systemctl status rsyslog
```


#### B. Configuring Rsyslog


Rsyslog has a main configuration file located here:


```
/etc/rsyslog.conf
```


In addition, the "**/etc/rsyslog.d/**" directory is used to store additional configuration files for Rsyslog. In the main configuration file, there is an Include directive to import all "**.conf**" files located in this directory. This makes it possible to have additional files for configuring Rsyslog without modifying the main file.


In this directory, you must use numbers to define the loading order, because files are loaded in alphabetical order. Adding a numerical prefix allows you to manage the priority between several configuration files. Here, we only have one additional file, so it's not a problem.


In this directory, we will create a file called "**10-graylog.conf**":


```
sudo nano /etc/rsyslog.d/10-graylog.conf
```


In this file, insert this line:


```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```


Here's how to interpret this line:



- `*.*`: means send all Syslog logs from the Linux machine to Graylog.
- `@`: indicates that the transport is performed in UDP. You must specify "**@@**" to switch to TCP.
- `192.168.10.220:12514`: indicates the address of the Graylog server, and the port on which logs are sent (corresponding to the Input).
- `RSYSLOG_SyslogProtocol23Format`: corresponds to the format of messages to be sent to Graylog.


When done, save the file and restart Rsyslog.


```
sudo systemctl restart rsyslog.service
```


Following this action, the first messages should arrive on your Graylog server!


### IV. Displaying Linux logs in Graylog


From Graylog, you can click on "**Streams**" and select your new stream to view related messages. Alternatively, click on "**Search**" and select your Steam and launch a search.


Here are some key features of the Interface:


**1** - Select the period for which to display messages. By default, messages from the last 5 minutes are displayed.


**2** - Select the stream(s) to be displayed.


**3** - Enable automatic refresh of the message list (every 5 seconds, for example). Otherwise, it's static and you'll have to refresh it manually.


**4** - Click on the magnifying glass to launch the search after modifying the period, stream or filter.


**5** - Input bar to specify your search filters. Here, I specify "**source:srv\-docker**" to display only the logs of the new machine on which I've just set up Rsyslog.


Logs are sent by the Linux machine:


![Image](assets/fr/015.webp)


### V. Identifying an SSH connection failure


Graylog's strength lies in its ability to index logs and enable searches to be carried out according to various criteria: source machine, timestamp, message content, etc... We could be looking to identify failed SSH connections.


From a remote machine (the Graylog server, for example), try to connect to your Linux server on which you've just configured Rsyslog. For example:


```
ssh [email protected]
```


Then deliberately enter an incorrect **username** and **password**, in order to **generate connection errors**. In the "**/var/log/auth.log**" file, this will generate log messages similar to the following:


```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```


You should find these messages on Graylog.


On Graylog, use the following search filter to display only matching messages:


```
message:Failed password AND application_name:sshd
```


If you have several servers and wish to analyze the logs of a specific server, specify its name in addition:


```
message:Failed password AND application_name:sshd AND source:srv\-docker
```


Here's an overview of the result on a machine where I generated several connection errors, at different times of the day:


![Image](assets/fr/009.webp)


Unsuccessful connection attempts are made from the machine with IP address "**192.168.10.199**". If you want to know more about the activity of this host, you can **search for this IP address**. Graylog will output all logs where this IP address is referenced, on all hosts (for which log sending is configured).


In this case, the filter to be used can be:


```
message:"192.168.10.199"
```


We get additional results (not surprising, since we don't filter on the SSH application):


![Image](assets/fr/008.webp)


### VI. Conclusion


By following this tutorial, you should be able to configure a Linux machine to send its logs to a Graylog server. This way, you'll be able to centralize the logs of your Linux hosts in your log sink!


To go even further, consider creating dashboards and alerts to receive notification when an anomaly is detected.


![Image](assets/fr/007.webp)