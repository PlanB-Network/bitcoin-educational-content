---
name: Graylog
description: Tập trung và phân tích nhật ký của bạn một cách dễ dàng
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian BURNEL được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã được chỉnh sửa.*



___



## Triển khai Graylog trên Debian 12



### I. Trình bày



Graylog là một giải pháp "lưu trữ nhật ký" mã nguồn mở được thiết kế để tập trung, lưu trữ và phân tích nhật ký từ máy tính và thiết bị mạng của bạn theo thời gian thực. Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách cài đặt phiên bản miễn phí của Graylog trên máy tính chạy Debian 12!



Trong một hệ thống thông tin, mỗi **máy chủ**, dù chạy **Linux** hay **Windows**, và mỗi **thiết bị mạng** (switch, router, tường lửa, v.v...) **đều tạo nhật ký riêng**, được lưu trữ cục bộ. Với nhật ký được lưu trữ cục bộ trên mỗi máy, việc phân tích và đối chiếu sự kiện rất khó khăn... Đây chính là lúc **Graylog** phát huy tác dụng. Nó sẽ hoạt động như một **bộ thu nhật ký**, nghĩa là **tất cả các máy của bạn sẽ gửi nhật ký** cho nó (ví dụ: thông qua syslog). Sau đó, Graylog sẽ **lưu trữ và lập chỉ mục các nhật ký này**, đồng thời cho phép bạn thực hiện tìm kiếm toàn cục và tạo cảnh báo.



Graylog là một công cụ phân tích và giám sát giúp xác định dễ dàng hơn các hành vi đáng ngờ và nhiều vấn đề khác nhau (tính ổn định, hiệu suất, v.v.).




![Image](assets/fr/034.webp)



**Lưu ý: phiên bản miễn phí, **Graylog Open**, không phải là SIEM như Wazuh, đặc biệt là vì nó thiếu các chức năng phát hiện xâm nhập thực sự.



### II. Điều kiện tiên quyết



**Ngăn xếp Graylog** dựa trên **một số thành phần** mà chúng ta cần cài đặt và cấu hình. Ở đây, chúng ta sẽ cài đặt tất cả các thành phần trên cùng một máy chủ, nhưng có thể tạo các cụm dựa trên nhiều nút và phân phối các vai trò trên nhiều máy chủ. Trong hướng dẫn này, chúng ta sẽ cài đặt **Graylog 6.1**, phiên bản mới nhất cho đến nay.





- MongoDB 7**, phiên bản hiện tại được khuyến nghị cho Graylog (tối thiểu 5.0.7, tối đa 7.x)
- OpenSearch**, một Fork mã nguồn mở của Elasticsearch do Amazon tạo ra (tối thiểu 1.1.x, tối đa 2.15.x)
- OpenJDK 17**



**Máy chủ Graylog** đang chạy trên **Debian 12**, nhưng có thể cài đặt trên các bản phân phối khác, bao gồm cả thông qua Docker. Máy ảo được trang bị **8 GB RAM** và **256 GB dung lượng ổ đĩa** để có đủ tài nguyên cho tất cả các thành phần (nếu không, điều này có thể ảnh hưởng đáng kể đến hiệu suất). Tuy nhiên, tôi chỉ đưa ra hướng dẫn sơ bộ, vì **kích thước của kiến trúc Graylog phụ thuộc vào lượng thông tin cần xử lý**. Graylog có thể xử lý 30 MB hoặc 300 MB dữ liệu mỗi ngày, cũng như 300 GB dữ liệu mỗi ngày... Đây là một **giải pháp có khả năng mở rộng**, có khả năng xử lý **hàng terabyte nhật ký** (xem [trang này](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Nguồn: Graylog



Trước khi bắt đầu cấu hình, hãy gán địa chỉ IP tĩnh Address cho máy Graylog và cài đặt các bản cập nhật mới nhất. Đảm bảo thiết lập múi giờ của máy cục bộ và xác định máy chủ NTP để đồng bộ hóa ngày giờ. Sau đây là lệnh cần chạy:



```
sudo timedatectl set-timezone Europe/Paris
```



**Lưu ý: **Cài đặt OpenSearch là tùy chọn** nếu bạn sử dụng **Graylog Data Node**.



### III Cài đặt Graylog từng bước



Hãy bắt đầu bằng cách cập nhật bộ đệm gói và cài đặt các công cụ cần thiết cho những việc sắp tới.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Cài đặt MongoDB



Sau khi hoàn tất, chúng ta sẽ bắt đầu cài đặt MongoDB. Tải xuống khóa GPG tương ứng với kho lưu trữ MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Sau đó thêm kho lưu trữ MongoDB 6 vào máy Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Tiếp theo, chúng ta sẽ cập nhật bộ đệm gói và thử cài đặt MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



Không thể cài đặt MongoDB vì thiếu gói phụ thuộc: **libssl1.1**. Chúng ta sẽ phải cài đặt gói này theo cách thủ công trước khi có thể tiếp tục, vì Debian 12 không có gói này trong kho lưu trữ.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Chúng ta sẽ tải xuống gói DEB có tên "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (phiên bản mới nhất) bằng lệnh **wget**, sau đó cài đặt bằng lệnh **dpkg**. Thao tác này sẽ tạo ra hai lệnh sau:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Khởi động lại cài đặt MongoDB:



```
sudo apt-get install -y mongodb-org
```



Sau đó khởi động lại dịch vụ MongoDB và cho phép nó tự động khởi động khi máy chủ Debian được khởi chạy.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Sau khi cài đặt MongoDB, chúng ta có thể chuyển sang cài đặt thành phần tiếp theo.



#### B. Cài đặt OpenSearch



Chúng ta hãy chuyển sang cài đặt OpenSearch trên máy chủ. Lệnh sau sẽ thêm khóa chữ ký cho các gói OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Sau đó thêm kho lưu trữ OpenSearch để chúng ta có thể tải xuống gói bằng **apt** sau đó:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Cập nhật bộ nhớ đệm gói của bạn:



```
sudo apt-get update
```



Sau đó, **cài đặt OpenSearch**, lưu ý **đặt mật khẩu mặc định cho tài khoản Quản trị viên** của bạn. Ở đây, mật khẩu là "**IT-Connect2024!**", nhưng hãy thay thế giá trị này bằng một mật khẩu mạnh. **Tránh sử dụng mật khẩu yếu** như "**P@ssword123**" và sử dụng ít nhất **8 ký tự** với ít nhất một ký tự thuộc mỗi loại (chữ thường, chữ hoa, số và ký tự đặc biệt), nếu không sẽ xảy ra lỗi khi kết thúc quá trình cài đặt. **Đây là điều kiện tiên quyết kể từ OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Hãy kiên nhẫn trong quá trình cài đặt...



Khi hoàn tất, hãy dành chút thời gian để thực hiện cấu hình tối thiểu. Mở tệp cấu hình ở định dạng YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Khi tệp được mở, hãy thiết lập các tùy chọn sau:



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



Cấu hình OpenSearch này được thiết kế để thiết lập một nút duy nhất. Sau đây là một số giải thích về các tham số khác nhau mà chúng tôi sử dụng:





- cluster.name: graylog**: tham số này đặt tên cho cụm OpenSearch bằng tên "**graylog**".
- node.name: ${HOSTNAME}**: tên nút được đặt động để khớp với tên của máy Linux cục bộ. Ngay cả khi chúng ta chỉ có một nút, việc đặt tên chính xác vẫn rất quan trọng.
- path.data: /var/lib/opensearch**: đường dẫn này chỉ định nơi OpenSearch lưu trữ dữ liệu của mình trên máy cục bộ, trong trường hợp này là "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: đường dẫn này xác định nơi lưu trữ các tệp nhật ký OpenSearch, tại đây là "**/var/log/opensearch**".
- discovery.type: single-node**: tham số này cấu hình OpenSearch để hoạt động với một nút duy nhất, do đó lựa chọn tùy chọn "**single-node**".
- network.host: 127.0.0.1**: cấu hình này đảm bảo rằng OpenSearch chỉ lắng nghe trên vòng lặp cục bộ Interface của nó, điều này là đủ vì nó nằm trên cùng một máy chủ với Graylog.
- action.auto_create_index: false**: bằng cách vô hiệu hóa tính năng tạo chỉ mục tự động, OpenSearch sẽ không tự động tạo chỉ mục khi tài liệu được gửi mà không có chỉ mục hiện có.
- plugins.security.disabled: true**: tùy chọn này sẽ vô hiệu hóa plugin bảo mật OpenSearch, nghĩa là sẽ không có xác thực, quản lý truy cập hoặc mã hóa giao tiếp. Cài đặt này giúp tiết kiệm thời gian khi thiết lập Graylog, nhưng nên tránh sử dụng trong môi trường sản xuất (xem [trang này](https://opensearch.org/docs/1.0/security-plugin/index/)).



Một số tùy chọn đã có sẵn, vì vậy bạn chỉ cần xóa dấu "#" để kích hoạt chúng, sau đó chỉ định giá trị của bạn. Nếu không tìm thấy tùy chọn nào, bạn có thể khai báo trực tiếp ở cuối tệp.



![Image](assets/fr/023.webp)



Lưu và đóng tập tin này.



#### C. Cấu hình Java (JVM)



Bạn cần cấu hình Máy ảo Java được OpenSearch sử dụng để điều chỉnh lượng bộ nhớ mà dịch vụ này có thể sử dụng. Chỉnh sửa tệp cấu hình sau:



```
sudo nano /etc/opensearch/jvm.options
```



Với cấu hình được triển khai ở đây, **OpenSearch sẽ bắt đầu với 4 GB bộ nhớ được phân bổ và có thể tăng lên đến 4 GB**, do đó sẽ không có sự thay đổi bộ nhớ trong quá trình hoạt động. Ở đây, cấu hình tính đến thực tế là máy ảo có tổng cộng **8 GB RAM**. Cả hai tham số phải có cùng giá trị. Điều này có nghĩa là phải thay thế các dòng:



```
-Xms1g
-Xmx1g
```



Với những dòng này:



```
-Xms4g
-Xmx4g
```



Sau đây là hình ảnh về sự thay đổi cần thực hiện:



![Image](assets/fr/022.webp)



Đóng tệp này sau khi lưu.



Ngoài ra, chúng ta cần kiểm tra cấu hình của tham số "**max_map_count**" trong nhân Linux. Tham số này xác định giới hạn vùng nhớ được ánh xạ cho mỗi tiến trình, nhằm đáp ứng nhu cầu của ứng dụng. **OpenSearch**, giống như Elasticsearch**, khuyến nghị đặt giá trị này thành "262144" để tránh lỗi quản lý bộ nhớ.



Về nguyên tắc, trên máy Debian 12 mới cài đặt, giá trị này đã chính xác. Nhưng hãy kiểm tra lại. Chạy lệnh này:



```
cat /proc/sys/vm/max_map_count
```



Nếu bạn nhận được giá trị khác "**262144**", hãy chạy lệnh sau, nếu không thì không cần thiết.



```
sudo sysctl -w vm.max_map_count=262144
```



Cuối cùng, hãy bật tính năng tự động khởi động OpenSearch và khởi chạy dịch vụ liên quan.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Nếu bạn hiển thị trạng thái hệ thống, bạn sẽ thấy một tiến trình Java có RAM 4 GB.



```
top
```



![Image](assets/fr/029.webp)



Bước tiếp theo: cài đặt Graylog đã được mong đợi từ lâu!



#### D. Cài đặt Graylog



Để **cài đặt Graylog 6.1** phiên bản mới nhất, hãy chạy 4 lệnh sau để **tải xuống và cài đặt Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Khi thực hiện xong, chúng ta cần thực hiện một số thay đổi đối với cấu hình của Graylog trước khi thử khởi chạy nó.



Chúng ta hãy bắt đầu bằng cách cấu hình hai tùy chọn này:





- password_secret**: tham số này được dùng để xác định khóa được Graylog sử dụng để bảo mật việc lưu trữ mật khẩu người dùng (theo tinh thần của khóa salting). Khóa này phải **duy nhất** và **ngẫu nhiên**.
- root_password_sha2**: tham số này tương ứng với mật khẩu quản trị viên mặc định trong Graylog. Nó được lưu trữ dưới dạng Hash SHA-256.



Chúng ta sẽ bắt đầu bằng cách tạo khóa 96 ký tự cho tham số **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Sao chép giá trị trả về, sau đó mở tệp cấu hình Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Dán khóa vào tham số **password_secret** như sau:



![Image](assets/fr/027.webp)



Lưu và đóng tệp.



Tiếp theo, bạn cần đặt mật khẩu cho tài khoản "**admin**" được tạo mặc định. Trong tệp cấu hình, mã Hash của mật khẩu phải được lưu trữ, nghĩa là mã này phải được tính toán. Ví dụ dưới đây cho mã Hash của mật khẩu "**LogsWells@**": hãy điều chỉnh giá trị cho phù hợp với mật khẩu của bạn.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Sao chép giá trị thu được dưới dạng đầu ra (không có dấu gạch nối ở cuối dòng).



Mở lại tệp cấu hình Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Dán giá trị vào tùy chọn **root_password_sha2** như thế này:



![Image](assets/fr/026.webp)



Khi đang ở trong tệp cấu hình, hãy đặt tùy chọn "**http_bind_address**". Chỉ định "**0.0.0.0:9000**" để có thể truy cập web Interface của Graylog trên cổng **9000**, thông qua bất kỳ IP máy chủ nào Address.



![Image](assets/fr/024.webp)



Sau đó, đặt tùy chọn "**elasticsearch_hosts**" thành `http://127.0.0.1:9200` để khai báo phiên bản OpenSearch cục bộ của chúng ta. Điều này là cần thiết, vì chúng ta không sử dụng **Graylog Data Node**. Và nếu không có tùy chọn này, chúng ta sẽ không thể tiến xa hơn nữa...



![Image](assets/fr/025.webp)



Lưu và đóng tệp.



Lệnh này kích hoạt Graylog để nó tự động khởi động khi khởi động lần tiếp theo và ngay lập tức khởi chạy máy chủ Graylog.



```
sudo systemctl enable --now graylog-server
```



Sau khi hoàn tất, hãy thử kết nối với Graylog từ trình duyệt. Nhập IP Address (hoặc tên) và cổng 9000 của máy chủ.



**Để bạn tham khảo:**



Cách đây không lâu, một cửa sổ xác thực tương tự như bên dưới đã xuất hiện khi bạn đăng nhập lần đầu vào Graylog. Bạn phải nhập tên đăng nhập "**admin**" và mật khẩu. Và rồi bạn sẽ ngạc nhiên đến khó chịu khi thấy kết nối không hoạt động.



![Image](assets/fr/031.webp)



Cần phải quay lại dòng lệnh trên máy chủ Graylog và tham khảo nhật ký. Sau đó, chúng tôi có thể thấy rằng **đối với kết nối đầu tiên**, cần phải **sử dụng mật khẩu tạm thời** được chỉ định trong nhật ký.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Sau đó, bạn phải thử lại kết nối với người dùng "**admin**" và mật khẩu tạm thời, và điều này cho phép bạn đăng nhập!



**Điều này không còn đúng nữa. Tất cả những gì bạn phải làm là đăng nhập bằng tài khoản quản trị viên và mật khẩu được cấu hình trên dòng lệnh.



![Image](assets/fr/033.webp)



**Chào mừng đến với Interface của Graylog!



![Image](assets/fr/019.webp)



#### E. Graylog: tạo tài khoản quản trị viên mới



Thay vì sử dụng tài khoản quản trị viên được tạo sẵn bởi Graylog, bạn có thể tạo tài khoản quản trị viên cá nhân. Nhấp vào menu "**Hệ thống**", sau đó vào "**Người dùng và Nhóm**" để nhấp vào nút "**Tạo người dùng**". Sau đó, điền vào biểu mẫu và gán vai trò quản trị viên cho tài khoản của bạn.



![Image](assets/fr/020.webp)



Tài khoản cá nhân hóa có thể chứa thông tin bổ sung, chẳng hạn như họ tên và email (Address), không giống như tài khoản quản trị viên gốc. Hơn nữa, điều này đảm bảo khả năng truy xuất nguồn gốc tốt hơn khi mỗi người làm việc với một tài khoản được chỉ định.



## Gửi nhật ký đến Graylog bằng rsyslog



### I. Trình bày



Trong phần thứ hai này, chúng ta sẽ tìm hiểu cách cấu hình máy Linux để gửi nhật ký đến máy chủ Graylog. Để thực hiện việc này, chúng ta sẽ cài đặt và cấu hình Rsyslog trên hệ thống.



### II. Cấu hình Graylog để nhận nhật ký Linux



Chúng ta sẽ bắt đầu bằng cách cấu hình Graylog. Có ba bước cần hoàn thành:





- Việc tạo **Đầu vào** để tạo điểm vào cho phép máy Linux **gửi nhật ký Syslog qua UDP**.
- Tạo **Chỉ mục** mới để lưu trữ và **lập chỉ mục cho tất cả nhật ký Linux**.
- Tạo **Luồng** để **định tuyến** các bản ghi được Graylog nhận được đến Linux Index mới.



#### A. Tạo đầu vào cho Syslog



Đăng nhập vào Graylog Interface, nhấp vào "**Hệ thống**" trong menu, sau đó nhấp vào "**Đầu vào**". Trong danh sách thả xuống, chọn "**Syslog UDP**" rồi nhấp vào nút có nhãn "**Khởi chạy đầu vào mới**". Bạn cũng có thể tạo Đầu vào TCP Syslog, nhưng điều này yêu cầu sử dụng chứng chỉ TLS: một điểm cộng về bảo mật, nhưng không được đề cập trong bài viết này.



![Image](assets/fr/001.webp)



Một trình hướng dẫn sẽ xuất hiện trên màn hình. Bắt đầu bằng cách đặt tên cho Đầu vào này, ví dụ: "**Graylog_UDP_Rsyslog_Linux**" và chọn một cổng. Theo mặc định, cổng là "**514**", nhưng bạn có thể tùy chỉnh. Ở đây, cổng "**12514**" được chọn.



![Image](assets/fr/016.webp)



Bạn cũng có thể chọn tùy chọn "**Lưu toàn bộ tin nhắn**" để lưu toàn bộ tin nhắn nhật ký vào Graylog. Nhấp vào "**Khởi chạy Đầu vào**".



![Image](assets/fr/017.webp)



Đầu vào mới đã được tạo và hiện đang hoạt động. Graylog hiện có thể nhận nhật ký Syslog trên cổng 12514/UDP, nhưng chúng tôi vẫn chưa hoàn tất việc cấu hình ứng dụng.



![Image](assets/fr/018.webp)


**Lưu ý: có thể sử dụng một Đầu vào duy nhất để lưu trữ nhật ký từ nhiều máy Linux.



#### B. Tạo một Linux Index mới



Chúng ta cần tạo một Chỉ mục (Index) trong Graylog để lưu trữ nhật ký từ các máy Linux. **Chỉ mục** trong Graylog là một cấu trúc lưu trữ chứa các nhật ký nhận được, tức là các tin nhắn đã nhận. Graylog sử dụng OpenSearch làm công cụ lưu trữ, và các tin nhắn được lập chỉ mục để cho phép tìm kiếm nhanh chóng và hiệu quả.



Từ Graylog, nhấp vào "**Hệ thống**" trong menu, sau đó nhấp vào "**Chỉ mục**". Trên trang mới xuất hiện, nhấp vào "**Tạo bộ chỉ mục**".



![Image](assets/fr/005.webp)



Đặt tên cho chỉ mục này, ví dụ: "**Linux Index**", thêm mô tả và tiền tố trước khi xác nhận. Tại đây, chúng tôi sẽ **lưu trữ tất cả nhật ký Linux trong chỉ mục này**. Bạn cũng có thể tạo các chỉ mục cụ thể để chỉ lưu trữ một số nhật ký nhất định (chỉ nhật ký [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), nhật ký dịch vụ web, v.v.).



![Image](assets/fr/006.webp)



Bây giờ chúng ta cần tạo một luồng mới để định tuyến tin nhắn đến chỉ mục này.



#### C. Tạo một luồng



Để tạo một luồng mới, hãy nhấp vào "**Streams**" trong menu chính của Graylog. Sau đó, nhấp vào nút "**Create stream**" ở bên phải. Trong cửa sổ xuất hiện, hãy đặt tên cho luồng, ví dụ: "**Linux Stream**" và chọn chỉ mục "**Linux Index**" cho trường "**Index Set**". Xác nhận lựa chọn của bạn.



**Lưu ý: các tin nhắn tương ứng với luồng này cũng sẽ được đưa vào "**Luồng mặc định**", trừ khi bạn chọn tùy chọn "**Xóa kết quả trùng khớp khỏi 'Luồng mặc định'**".



![Image](assets/fr/002.webp)



Sau đó, trong cài đặt Steam, hãy nhấp vào nút "**Thêm quy tắc luồng**" để thêm quy tắc định tuyến tin nhắn mới. Nếu bạn không tìm thấy cửa sổ này, hãy nhấp vào "**Luồng**" trong menu, sau đó trên dòng tương ứng với luồng của bạn, nhấp vào "**Thêm**" rồi "**Quản lý Quy tắc**".



Chọn loại "**match input**" và chọn **Rsyslog input đã tạo trước đó trong UDP**. Xác nhận bằng nút "**Create Rule**". Tất cả thông báo đến Input mới của chúng ta sẽ được gửi đến Index for Linux.



![Image](assets/fr/003.webp)



Luồng mới của bạn sẽ xuất hiện trong danh sách và ở trạng thái "**Đang chạy**". Băng thông tin nhắn hiển thị "**0 msg/s**", vì hiện tại chúng tôi không gửi bất kỳ nhật ký nào đến đầu vào UDP của Rsyslog. Để xem nhật ký của luồng, chỉ cần nhấp vào tên luồng.



![Image](assets/fr/004.webp)



**Mọi thứ đã sẵn sàng trên Graylog**. Bước tiếp theo là cấu hình máy Linux.



### III. Cài đặt và cấu hình Rsyslog trên Linux



Đăng nhập vào máy Linux, cục bộ hoặc từ xa, và sử dụng tài khoản người dùng có quyền để nâng cao đặc quyền (thông qua sudo). Nếu không, hãy sử dụng trực tiếp tài khoản "root".



#### A. Cài đặt gói Rsyslog



Bắt đầu bằng cách cập nhật bộ đệm gói và cài đặt gói có tên "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Sau đó kiểm tra trạng thái dịch vụ. Trong hầu hết các trường hợp, dịch vụ đã hoạt động.



```
sudo systemctl status rsyslog
```



#### B. Cấu hình Rsyslog



Rsyslog có tệp cấu hình chính nằm ở đây:



```
/etc/rsyslog.conf
```



Ngoài ra, thư mục "**/etc/rsyslog.d/**" được sử dụng để lưu trữ các tệp cấu hình bổ sung cho Rsyslog. Trong tệp cấu hình chính, có một lệnh Include để nhập tất cả các tệp "**.conf**" nằm trong thư mục này. Điều này cho phép thêm các tệp để cấu hình Rsyslog mà không cần sửa đổi tệp chính.



Trong thư mục này, bạn phải sử dụng số để xác định thứ tự tải, vì các tệp được tải theo thứ tự bảng chữ cái. Việc thêm tiền tố số cho phép bạn quản lý thứ tự ưu tiên giữa nhiều tệp cấu hình. Ở đây, chúng ta chỉ có một tệp bổ sung, nên không thành vấn đề.



Trong thư mục này, chúng ta sẽ tạo một tệp có tên "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Trong tập tin này, chèn dòng này:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Sau đây là cách diễn giải dòng này:





- `*.*`: có nghĩa là gửi tất cả nhật ký Syslog từ máy Linux tới Graylog.
- `@`: biểu thị việc truyền tải được thực hiện qua UDP. Bạn phải chỉ định "**@@**" để chuyển sang TCP.
- `192.168.10.220:12514`: chỉ ra Address của máy chủ Graylog và cổng mà nhật ký được gửi (tương ứng với Đầu vào).
- `RSYSLOG_SyslogProtocol23Format`: tương ứng với định dạng của tin nhắn sẽ được gửi tới Graylog.



Khi hoàn tất, hãy lưu tệp và khởi động lại Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Sau hành động này, những tin nhắn đầu tiên sẽ đến máy chủ Graylog của bạn!



### IV. Hiển thị nhật ký Linux trong Graylog



Từ Graylog, bạn có thể nhấp vào "**Streams**" và chọn luồng mới của mình để xem các tin nhắn liên quan. Hoặc, nhấp vào "**Search**" và chọn Steam của bạn rồi bắt đầu tìm kiếm.



Sau đây là một số tính năng chính của Interface:



**1** - Chọn khoảng thời gian hiển thị tin nhắn. Theo mặc định, tin nhắn trong 5 phút gần nhất sẽ được hiển thị.



**2** - Chọn luồng sẽ được hiển thị.



**3** - Bật tính năng tự động làm mới danh sách tin nhắn (ví dụ: cứ sau 5 giây). Nếu không, danh sách sẽ tĩnh và bạn sẽ phải làm mới thủ công.



**4** - Nhấp vào kính lúp để bắt đầu tìm kiếm sau khi sửa đổi thời kỳ, luồng hoặc bộ lọc.



**5** - Thanh nhập liệu để chỉ định bộ lọc tìm kiếm. Ở đây, tôi chỉ định "**source:srv\-docker**" để chỉ hiển thị nhật ký của máy mới mà tôi vừa cài đặt Rsyslog.



Nhật ký được gửi bởi máy Linux:



![Image](assets/fr/015.webp)



### V. Xác định lỗi kết nối SSH



Điểm mạnh của Graylog nằm ở khả năng lập chỉ mục nhật ký và cho phép thực hiện tìm kiếm theo nhiều tiêu chí khác nhau: máy nguồn, Timestamp, nội dung tin nhắn, v.v... Chúng ta có thể tìm cách xác định các kết nối SSH bị lỗi.



Từ một máy tính từ xa (ví dụ: máy chủ Graylog), hãy thử kết nối đến máy chủ Linux mà bạn vừa cấu hình Rsyslog. Ví dụ:



```
ssh [email protected]
```



Sau đó, cố tình nhập **tên người dùng** và **mật khẩu** không chính xác để **gỡ lỗi kết nối generate**. Trong tệp "**/var/log/auth.log**", điều này sẽ ghi lại các thông báo nhật ký generate tương tự như sau:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Bạn có thể tìm thấy những thông báo này trên Graylog.



Trên Graylog, hãy sử dụng bộ lọc tìm kiếm sau để chỉ hiển thị những tin nhắn phù hợp:



```
message:Failed password AND application_name:sshd
```



Nếu bạn có nhiều máy chủ và muốn phân tích nhật ký của một máy chủ cụ thể, hãy chỉ định thêm tên của máy chủ đó:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Sau đây là tổng quan về kết quả trên một máy mà tôi tạo ra nhiều lỗi kết nối vào nhiều thời điểm khác nhau trong ngày:



![Image](assets/fr/009.webp)



Các nỗ lực kết nối không thành công được thực hiện từ máy có IP Address "**192.168.10.199**". Nếu bạn muốn biết thêm về hoạt động của máy chủ này, bạn có thể **tìm kiếm IP Address này**. Graylog sẽ xuất tất cả nhật ký có tham chiếu đến IP Address này, trên tất cả các máy chủ (mà tính năng gửi nhật ký được cấu hình).



Trong trường hợp này, bộ lọc được sử dụng có thể là:



```
message:"192.168.10.199"
```



Chúng tôi nhận được kết quả bổ sung (không có gì ngạc nhiên vì chúng tôi không lọc theo ứng dụng SSH):



![Image](assets/fr/008.webp)



### VI. Kết luận



Bằng cách làm theo hướng dẫn này, bạn sẽ có thể cấu hình máy Linux để gửi nhật ký đến máy chủ Graylog. Bằng cách này, bạn sẽ có thể tập trung nhật ký của các máy chủ Linux vào bộ lưu trữ nhật ký của mình!



Để tiến xa hơn nữa, hãy cân nhắc việc tạo bảng thông tin và cảnh báo để nhận thông báo khi phát hiện ra bất thường.



![Image](assets/fr/007.webp)