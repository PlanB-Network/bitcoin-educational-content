---
name: バーチャルボックス
description: Windows 11にVirtualBoxをインストールし、最初のVMを作成する。
---
![cover](assets/cover.webp)



___



*このチュートリアルは、[IT-Connect](https://www.it-connect.fr/)に掲載されたFlorian Burnel氏のオリジナルコンテンツに基づいています。ライセンス[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文に変更が加えられている可能性があります。



___




## I.プレゼンテーション



このチュートリアルでは、Windows 10、Windows 11、Windows Server、またはLinuxディストリビューション（Debian、Ubuntu、Kali Linuxなど）を実行する仮想マシンを作成するために、Windows 11にVirtualBoxをインストールする方法を学びます。



このVirtualBox入門チュートリアルは、Oracle社が開発したこのオープンソースの仮想化ソリューションを使い始めるのに役立ちます。後日、他のチュートリアルもオンラインで公開される予定です。



プロジェクトの一環としてのテスト目的であれ、ITの勉強中であれ、ワークステーションを仮想化する場合、VirtualBoxは明らかに良いソリューションだ。また、Windows 10とWindows 11（およびWindows Server）に統合されているHyper-Vや、VMware Workstation（有料）／VMware Workstation Player（個人使用は無料）といった他のソリューションの代替にもなる。



私の構成： **VirtualBoxをインストールするWindows 11ワークステーション**だが、LinuxだけでなくWindows 10（または古いバージョン）にもVirtualBoxをインストールできる。仮想マシンに関する限り、VirtualBoxはWindows（Windows 10、Windows 11、Windows Server 2022など）、Linux（Debian、Rocky Linux、Ubuntu、Fedoraなど）、BSD（PfSense）、macOSなど、幅広いシステムをサポートしている。



## II.Windows 11用VirtualBoxのダウンロード



WindowsマシンにインストールするためのVirtualBoxをダウンロードするには、唯一の良いAddressがあります：[VirtualBox公式ウェブサイト](https://www.virtualbox.org/wiki/Downloads)の "**Downloads**"セクションです。Windows hosts "をクリックするだけで、100MB強の実行ファイルのダウンロードが始まります。



![Image](assets/fr/025.webp)



## III.Windows 11へのVirtualBoxのインストール



### A.VirtualBoxのインストール



VirtualBox**のインストールは簡単で、どのバージョンのWindowsでも同じ手順で行えます。ダウンロードしたVirtualBoxの実行ファイルを起動し、"**Next**"をクリックします。



![Image](assets/fr/026.webp)



このインストールはカスタマイズ可能だが、すべての機能をインストールすることをお勧めする：デフォルト選択の場合である。下の画像では、.NET Frameworkを含む様々なElementsを見ることができる：





- VirtualBox USB Support**： VirtualBoxがUSBデバイスをサポートできるようにする。
- VirtualBox Bridged Network** 「ブリッジ」モードでのネットワークサポートを統合（仮想マシンはローカルネットワークに直接接続可能）
- VirtualBox Host-Only Network** 「ホストのみ」モードでのネットワーク サポートを統合します (このモードでは、仮想マシンは Windows 11 物理ホストおよび他の仮想マシンのみと通信できます)。



次へ**」をクリックして進みます。



![Image](assets/fr/001.webp)



VirtualBoxがブリッジモードを含むさまざまなネットワークタイプをサポートするためにネットワークの変更を実行する間、**Windows 11マシン上でネットワークがしばらくの間中断される**ことを念頭に置いて、"**Yes**"をクリックします。



![Image](assets/fr/002.webp)



確認後、インストールが開始されます。そして「**このデバイスソフトウェアをインストールしますか**」という通知が表示されます。Always trust software from Oracle Corporation**"にチェックを入れ、"**Install**"をクリックします。VirtualBoxは実際にあなたのコンピュータにいくつかのドライバをインストールする必要があります。



![Image](assets/fr/003.webp)



これでインストールは完了です！インストール後、Oracle VM VirtualBox 6.1.34を起動する**"にチェックを入れ、"**クリック**"をクリックするとソフトウェアが起動します。



![Image](assets/fr/004.webp)



### B.拡張パックを追加する



VirtualBoxの公式サイト（前のリンクを参照）では、"**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" セクションの "**All supported platforms**" リンクをクリックすると、公式の拡張パックをダウンロードできます。このパックを使用すると、VirtualBoxに追加機能を追加することができます！例えば、VMでのUSB 3.0のサポート、ウェブカメラのサポート、ディスクの暗号化などが含まれます。



VirtualBoxを開き、メニューの "**File**"から "**Settings**"をクリックします。



![Image](assets/fr/005.webp)



左側の「**拡張機能**」をクリックし(1)、右側の「**+**」ボタンをクリックして(2)、ダウンロードしたVirtualBox**拡張機能パックをロードします(3)。



![Image](assets/fr/006.webp)



インストール**」ボタンをクリックして確認します。



![Image](assets/fr/007.webp)



OK**"をクリックします。これで公式拡張パックがVirtualBoxインスタンスにインストールされます！



![Image](assets/fr/008.webp)



最初の仮想マシンの作成に移ろう。



## IV.最初のVirtualBox VMの作成



VirtualBoxで新しい仮想マシンを作成するには、"**New**"ボタンをクリックするだけで、VM作成ウィザードが起動する。VirtualBoxを起動するのは初めてだと思うので、Interfaceや他のボタンについてもう少し詳しく説明したい。





- 設定**：VirtualBoxの一般的な設定（デフォルトのVMフォルダ、アップデート管理、言語、NATネットワーク、拡張機能など）
- Import**：OVF形式で仮想アプライアンスをインポートする
- Export**：既存の仮想マシンをOVF形式でエクスポートし、仮想アプライアンスを作成する。
- Add**：既存の仮想マシンを VirtualBox のインベントリに追加します。VirtualBox の標準形式（.vbox）または XML 形式です。



左側の "**Tools**"セクションから、**高度な機能、特に仮想ネットワークの管理、VMストレージの管理**にアクセスできます。この "**Tools**"の下に仮想マシンが追加されます。



![Image](assets/fr/009.webp)



### A.VM作成プロセス



**VirtualBoxはWindows、Linux、BSDを含む多数のオペレーティング・システムをサポートしています。この例では、Windows 11用の仮想マシンを作成します。いくつかのフィールドを埋める必要があります：





- Name**：仮想マシン名（VirtualBoxで表示される名前です）
- Machineフォルダ**：仮想マシンを格納する場所。この場所にVM名のサブフォルダが作成される。
- タイプ**：インストールするOSに応じたオペレーティング・システムのタイプ
- バージョン**：インストールしたいシステムのバージョン、この場合はWindows11なので "**Windows11_64**"



次へ**」をクリックして進みます。



![Image](assets/fr/010.webp)



前のステップで選択したオペレーティング・システムに応じて、**VirtualBoxは仮想マシンに割り当てるリソースの推奨を行います**。ここでは、VMに割り当てるRAMについて話しています。Windows 11では4GBが推奨されているため4GBとしておきますが、リソースが足りない場合は代わりに2GBを指定してください。 **続ける



*注***：仮想マシンに割り当てられたリソースは、後で変更することができる。



![Image](assets/fr/011.webp)



仮想Hardディスクに関する限り、我々はゼロから始めるので、VMがオペレーティング・システムをインストールし、データを保存するためのストレージ・スペースを持つように、"**Create virtual Hard disk now**"を選択する必要がある。Create**"をクリックする。



![Image](assets/fr/012.webp)



VirtualBoxは仮想Hardディスクに3つの異なるフォーマットをサポートしており、これはVMwareやHyper-Vなどの他のソリューションと比較して大きな違いである。選べるフォーマットは3つ：





- VDI**、VirtualBoxの公式フォーマット
- VHD**はHyper-Vの公式フォーマットだが、最近は新しいVHDXフォーマットがよく使われている。
- VMDX**は、VMware WorkstationとVMware ESXiの両方に対応するVMwareの公式フォーマットです。



このVirtualBoxインスタンス上でのみ使用する仮想マシンを作成するには、"**VDI**"を選択します。一方、仮想Hardディスクを後日Hyper-Vホストにアタッチする場合は、変換の手間を省くためにVHDフォーマットで始めるのがよいでしょう。Next**"をクリックしてください。



![Image](assets/fr/013.webp)



**仮想ディスクのサイズは、動的または固定**のいずれかです。動的な場合、**仮想ディスクを表すファイル（ここでは.vdiファイル）は、データがディスクに書き込まれるにつれて**最大サイズになるまで大きくなるが、データが削除されても縮小することはない。逆に固定サイズの場合、**全ストレージ領域が即座に割り当てられる（つまり予約される）***ため、パフォーマンスが若干向上するが、仮想ディスクを最初に作成するときに時間がかかる。



個人的には、VirtualBoxのテスト用仮想マシンでは、"**Dynamically allocated**"モードで十分だと考えている。



![Image](assets/fr/014.webp)



**次のステップでは、仮想ディスクのサイズを指定します**。デフォルトでは、ディスクはVMディレクトリに保存されることを念頭に置いてください（この段階で変更可能です）。Windows 11の要件に準拠するために64GBのサイズを指定したが、ここでももっと小さいサイズを指定することができる。Create**」をクリックしてVMを作成する！



![Image](assets/fr/015.webp)



この時点では、VMはインベントリにあり、設定されているが、オペレーティング・システムはインストールされていない。VMを起動する前に、VMのコンフィギュレーションを確定する必要がある。



### B.VirtualBoxのVMにISOイメージを割り当てる



ウィンドウズ11やその他のシステムをインストールするには、インストールソースが必要だ。ほとんどの場合、オペレーティング・システムをインストールするにはISO形式のディスク・イメージを使用する。 **Windows11のISOイメージをVMの仮想DVDドライブにロードする必要がある。



VirtualBox のインベントリで VM をクリックし (1)、"**Configuration**" ボタンをクリックします (2)。このメニューは、リソースの管理（RAM の増設、CPU の設定など）に使用します。左側の "**Storage**"をクリックし(3)、DVDドライブの "**Empty**"と表示されている箇所をクリックします(4)。



![Image](assets/fr/016.webp)



インストールしたいオペレーティング・システムのISOイメージを選択し、OKをクリックする。こうなります：



![Image](assets/fr/017.webp)



VMの "**コンフィギュレーション**"セクションに留まり、まだいくつか説明しなければならないことがある。



### C.VMネットワーク接続



左側の「**Network**」セクションに移動します。このセクションでは、仮想マシンのネットワークを管理します：仮想ネットワークインターフェイスの数（VMごとに最大4つ）、MAC Address、ネットワークアクセスモード（NAT、ブリッジアクセス、内部ネットワークなど）。 **仮想マシンをインターネットにアクセスさせたい場合は、"NAT "または "ブリッジアクセス "**を選択します。



注：ネットワークの部分については、また別の記事で詳しく触れたいと思う。



![Image](assets/fr/018.webp)



### D.仮想プロセッサの数



物理的なコンピューターと同様に、仮想マシンが機能するにはRAM、Hardディスク、プロセッサーが必要だ。VMを作成する際、ウィザードにプロセッサー・コンフィギュレーションが含まれていないことに気づいたかもしれない。しかし、これは "**System**"タブの "**Processor**"からいつでも設定することができ、そこで仮想プロセッサの数を選択することができる。



注：ネストされた仮想化には、"**Enable VT-x/AMD-v nested**"オプションが必要です。



私の場合、仮想マシンには2つの仮想プロセッサがある：



![Image](assets/fr/019.webp)



**コンフィギュレーション・メニューの他のセクションもご覧ください。



### E.最初の起動とOSのインストール



仮想マシンを起動するには、インベントリで仮想マシンを選択し、"**Start**" ボタンをクリックします。2つ目のウィンドウが開き、仮想マシンの概要が表示されます。



![Image](assets/fr/020.webp)



痛い！厄介なエラーが出て、仮想マシンが起動しない！エラーは "Login failed for virtual machine... "で、詳細は以下の通り：



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



実は、これは**私のコンピュータでは仮想化機能が有効になっていない**ため、正常なことなのです！この問題を解決するには、コンピュータを再起動してBIOSにアクセスし、仮想化を有効にする必要があります。



![Image](assets/fr/021.webp)



待つことなくコンピュータを再起動し、**ASUSマザーボードのBIOS**にアクセスするために「SUPPR」キーを押す（キーはマシンによって異なり、例えばF2かもしれない）。仮想化を有効にするには、私の場合、「SVMモード」を有効にしなければならない。ここでもまた、マザーボードによって、メーカーによって、名前が変わることがある。AMD-V**（AMD製CPUの場合）または**Intel VT-x**（Intel製CPUの場合）を指す機能を探してください。



![Image](assets/fr/022.webp)



これが完了したら、変更を保存して物理マシンを再起動します。今度は、**VirtualBoxが仮想マシン**を起動し、Windows ISOイメージをロードしてオペレーティングシステムをインストールできます。



![Image](assets/fr/023.webp)



VirtualBoxがインストールされているWindows 11物理ホスト上で、Windows 11仮想マシンフォルダに様々なファイルが含まれていることがわかる。





- VMの構成（RAM、CPUなど）に対応するVBOX**ファイル（XML形式）。
- VBOX-PREV**ファイルは、以前のコンフィギュレーションのバックアップです。
- VDI**ファイルは、ダイナミックモードの仮想Hardディスクに対応するため、最大サイズが64GBであるのに対し、現在は13GBしかない。
- NVRAM**ファイルには、仮想マシンのBIOS状態が含まれており、これは物理マシンの不揮発性メモリに相当する



![Image](assets/fr/024.webp)



## V.結論



**これでVirtualBoxがWindows 11の物理マシンで稼働するようになった！あとは、これを活用して仮想マシンを作成するだけだ！** VirtualBox VMへのWindows 11のインストールについては、また別の記事で紹介しよう。Windows 10、Windows Server、Linuxディストリビューション（Ubuntu、Debianなど）については、私たちにお任せください！