---
name: Chim sẻ Wallet - Multisig
description: Tạo danh mục đầu tư đa chữ ký trên Sparrow
---
![cover](assets/cover.webp)



Wallet đa chữ ký (thường được gọi là "*Multisig*") là cấu trúc Bitcoin Wallet yêu cầu một số chữ ký mật mã, từ các khóa khác nhau, để ủy quyền cho một khoản chi. Không giống như Wallet thông thường ("*singlesig*"), trong đó một khóa riêng duy nhất là đủ để mở khóa UTXO, Multisig dựa trên mô hình **m-of-n**: trong số _n_ khóa được liên kết với Wallet, _m_ bắt buộc phải đồng ký mỗi giao dịch.



Cơ chế này cho phép chia sẻ quyền kiểm soát danh mục đầu tư giữa nhiều thực thể hoặc thiết bị. Ví dụ, trong cấu hình 2 trong 3, ba bộ khóa độc lập được tạo ra, nhưng chỉ cần hai bộ để giải phóng tiền. Kiến trúc này làm giảm đáng kể các rủi ro liên quan đến việc xâm phạm hoặc mất khóa: kẻ trộm chỉ có quyền truy cập vào một khóa không thể làm trống Wallet và người dùng bị mất một khóa vẫn có thể truy cập vào tiền của mình bằng hai khóa còn lại.



![Image](assets/fr/01.webp)



Tuy nhiên, tính bảo mật cao hơn này đi kèm với sự phức tạp hơn. Thiết lập Multisig Wallet đòi hỏi phải bảo mật một số cụm từ Mnemonic (một cụm từ cho mỗi yếu tố chữ ký) và khóa công khai mở rộng ("*xpub*"). Thật vậy, nếu bạn đang sử dụng Multisig 2-of-3 Wallet, để truy xuất Wallet, bạn phải có cả ba cụm từ Mnemonic hoặc ít nhất hai trong ba cụm từ. Nhưng nếu bạn chỉ có hai trong ba cụm từ, bạn cũng cần truy cập vào ba *xpub*, nếu không sẽ không thể truy xuất khóa công khai cần thiết để truy cập vào bitcoin mà chúng bảo vệ.



Tóm lại, để phục hồi danh mục đầu tư Multisig, bạn phải:




- Hoặc truy cập tất cả các cụm từ Mnemonic liên quan đến từng yếu tố chữ ký;
- Hoặc có số lượng cụm từ Mnemonic tối thiểu theo ngưỡng yêu cầu để có thể ký và cũng có quyền truy cập vào xpub của tất cả các yếu tố để lấy các khóa công khai cần thiết.



![Image](assets/fr/02.webp)



Việc quản lý sao lưu danh mục đầu tư Multisig này được hỗ trợ bởi *Output Script Descriptors*, nhóm tất cả dữ liệu công khai cần thiết để truy cập vào các quỹ. Tuy nhiên, chức năng này vẫn chưa được triển khai trong tất cả các phần mềm quản lý danh mục đầu tư.



Multisig đặc biệt phù hợp với những người dùng bitcoin đang tìm kiếm sự bảo mật nâng cao hoặc quản lý tập thể các quỹ: công ty, hiệp hội, gia đình hoặc người dùng cá nhân nắm giữ một lượng lớn bitcoin. Nó có thể được sử dụng để tạo ra các chương trình quản trị phi tập trung, ví dụ, để phân phối quyền ký kết giữa một số người quản lý hoặc thành viên nhóm.



Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách tạo và sử dụng Wallet đa chữ ký cổ điển với **Sparrow Wallet**. Nếu bạn muốn tạo danh mục đầu tư đa chữ ký tùy chỉnh với khóa thời gian, tôi khuyên bạn nên sử dụng Liana thay thế:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Điều kiện tiên quyết



Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách tạo Multisig bằng [phần mềm quản lý danh mục đầu tư Sparrow Wallet](https://sparrowwallet.com/download/). Nếu bạn chưa cài đặt phần mềm này, vui lòng cài đặt ngay. Nếu bạn cần trợ giúp, chúng tôi cũng có hướng dẫn chi tiết về cách cấu hình Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Để thiết lập Wallet đa chữ ký, bạn sẽ cần các ví phần cứng khác nhau. Ví dụ, đối với Multisig 2-de-3, bạn có thể sử dụng:




- Trezor Model One;
- Ledger Linh hoạt;
- Một chiếc Coldcard MK3.



![Image](assets/fr/03.webp)



Tốt nhất là sử dụng các loại Hardware Wallet khác nhau trong cấu hình Multisig của bạn. Điều này đảm bảo rằng nếu một mẫu cụ thể gặp phải sự cố nghiêm trọng, nó sẽ không ảnh hưởng đến sự an toàn chung của Multisig của bạn. Hơn nữa, nó cho phép bạn hưởng lợi từ những lợi thế cụ thể của từng thiết bị. Ví dụ, trong cấu hình của tôi:





- Trezor Model One hoàn toàn là mã nguồn mở, giúp xác minh được thế hệ seed. Tuy nhiên, vì không được trang bị Secure Element nên nó vẫn dễ bị tấn công vật lý;





- Ngược lại, Ledger Flex được hưởng lợi từ phần mềm độc quyền không thể xác minh nhưng tích hợp Yếu tố bảo mật cung cấp khả năng bảo vệ vật lý tuyệt vời;





- Coldcard được trang bị Secure Element và mã của nó có thể tìm kiếm được. Đây là lựa chọn thú vị cho cấu hình của chúng tôi vì nó cung cấp các tính năng xác minh không có trên các mẫu khác.



Trước khi cấu hình Multisig Wallet của bạn, hãy đảm bảo rằng mỗi Hardware Wallet được cấu hình đúng (tạo và lưu Mnemonic, định nghĩa mã PIN). Để biết hướng dẫn chi tiết, bạn có thể tham khảo hướng dẫn của chúng tôi cho từng Hardware Wallet, ví dụ:



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Như chúng ta sẽ thấy sau trong hướng dẫn này, bạn cũng có thể tích hợp vào cấu hình Multisig của mình một yếu tố không liên quan đến Hardware Wallet, nhưng có khóa riêng được lưu trữ trên PC của bạn. Phương pháp này rõ ràng kém an toàn hơn so với việc sử dụng độc quyền ví phần cứng, nhưng nó có thể phù hợp trong một số trường hợp nhất định. Ví dụ, đối với Multisig 2-de-3, bạn có thể chọn hai ví phần cứng và một Software Wallet.



## Tạo danh mục đầu tư Multisig



Mở Sparrow Wallet, nhấp vào tab "*File*", sau đó chọn "*New Wallet*".



![Image](assets/fr/04.webp)



Đặt tên cho danh mục đầu tư đa chữ ký của bạn, sau đó nhấp vào "*Tạo Wallet*" để xác nhận.



![Image](assets/fr/05.webp)



Trong menu thả xuống "*Loại chính sách*", chọn tùy chọn "*Nhiều chữ ký*".



![Image](assets/fr/06.webp)



Ở góc trên bên phải, giờ đây bạn có thể xác định tổng số chìa khóa trong Multisig của mình, cũng như số người đồng ký cần thiết để ủy quyền chi phí. Trong ví dụ của tôi, đây là chương trình 2 trong 3.



![Image](assets/fr/07.webp)



Ở dưới cùng của cửa sổ, Sparrow Wallet hiển thị ba "*Keystore*". Mỗi cái đại diện cho một bộ khóa. Ở đây, tôi đang sử dụng ba danh mục phần cứng, vì vậy mỗi "*Keystore*" tương ứng với một trong số chúng. Bây giờ chúng ta sẽ cấu hình chúng.



Tôi bắt đầu với Coldcard. Trong tab "*Keystore 1*", tôi chọn tùy chọn "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Trên Coldcard, sau khi thiết bị được mở khóa, tôi vào menu "*Cài đặt*", sau đó đến "*Ví Multisig*".



![Image](assets/fr/09.webp)



Menu này cho phép bạn quản lý danh mục Multisig mà Coldcard tham gia. Tôi muốn tạo một danh mục mới, vì vậy tôi chọn "*Xuất XPUB*".



![Image](assets/fr/10.webp)



Đối với trường "*Số tài khoản*", nếu bạn chỉ quản lý một tài khoản, bạn có thể để trống và xác thực trực tiếp bằng cách nhấn nút xác nhận.



![Image](assets/fr/11.webp)



Sau đó, Coldcard sẽ generate một tập tin chứa xpub của bạn, được lưu trên thẻ Micro SD.



![Image](assets/fr/12.webp)



Lắp thẻ Micro SD này vào máy tính của bạn. Trong Sparrow Wallet, nhấp vào nút "*Nhập tệp...*" bên cạnh "*Coldcard Multisig*", sau đó chọn tệp do Coldcard tạo trên thẻ.



![Image](assets/fr/13.webp)



xpub của bạn đã được nhập thành công. Bây giờ chúng ta sẽ lặp lại quy trình với hai ví phần cứng khác.



![Image](assets/fr/14.webp)



Đối với Ledger Flex, tôi chọn "*Keystore 2*", sau đó nhấp vào "*Connected Hardware Wallet*". Đảm bảo Ledger được kết nối với máy tính, đã mở khóa và ứng dụng Bitcoin đang mở.



![Image](assets/fr/15.webp)



Sau đó nhấp vào nút "*Quét...*".



![Image](assets/fr/16.webp)



Bên cạnh tên danh mục phần cứng của bạn, hãy nhấp vào "*Nhập kho khóa*".



![Image](assets/fr/17.webp)



Người ký thứ hai hiện đã được đăng ký chính xác trong Sparrow Wallet.



![Image](assets/fr/18.webp)



Tôi lặp lại chính xác quy trình tương tự với Trezor One để hoàn thiện cấu hình Multisig.



![Image](assets/fr/19.webp)



Trong cấu hình của tôi, chúng tôi không đề cập đến trường hợp này, nhưng nếu bạn muốn thêm chữ ký thông qua Software Wallet trong Sparrow (Hot Wallet) vào Multisig, chỉ cần nhấp vào nút "*Software Wallet mới hoặc đã nhập*".



Bây giờ tất cả các thiết bị chữ ký của bạn đã được nhập vào Sparrow Wallet, bạn có thể hoàn tất việc tạo Multisig bằng cách nhấp vào "*Áp dụng*".



![Image](assets/fr/20.webp)



Chọn mật khẩu mạnh để bảo mật quyền truy cập vào Sparrow Wallet Wallet của bạn. Mật khẩu này bảo vệ khóa công khai, địa chỉ, nhãn và lịch sử giao dịch của bạn khỏi sự truy cập trái phép.



Hãy nhớ lưu mật khẩu này ở nơi an toàn, chẳng hạn như trình quản lý mật khẩu, để tránh bị mất.



![Image](assets/fr/21.webp)



## Sao lưu danh mục đầu tư Multisig



Bây giờ chúng ta sẽ lưu *Mô tả tập lệnh đầu ra* trên Coldcard (điều này chỉ áp dụng cho người dùng có Coldcard trong Multisig của họ) và trên hết, chúng ta sẽ lưu bản sao lưu của nó trên một phương tiện độc lập.



*Descriptor* chứa tất cả các xpub trong danh mục Multisig của bạn, cũng như các đường dẫn phái sinh được sử dụng để generate các khóa. Hãy nhớ những gì chúng ta đã thấy trong Phần 1: để khôi phục danh mục Multisig, bạn phải có **tất cả** các cụm từ Mnemonic hoặc chỉ số lượng tối thiểu cần thiết để đạt đến ngưỡng chữ ký. Tuy nhiên, trong trường hợp sau, điều cần thiết là phải có **xpub** của những người ký tên còn thiếu. *Descriptor* chứa tất cả các xpub của Multisig của bạn.



Nếu bạn không hiểu rõ, hãy nhớ điều này: để lấy Multisig, bạn cần số lượng cụm từ Mnemonic tối thiểu cho mỗi Hardware Wallet được sử dụng, tùy thuộc vào ngưỡng (trong trường hợp của tôi: 2 cụm từ) cũng như *Mô tả*.



*Descriptor* này không chứa khóa riêng tư, chỉ có khóa công khai. Điều này có nghĩa là nó không cấp quyền truy cập vào tiền. Do đó, nó không quan trọng bằng cụm từ Mnemonic, cụm từ này cấp quyền truy cập đầy đủ vào bitcoin của bạn. Rủi ro với *Descriptor* chỉ liên quan đến tính bảo mật: trong trường hợp bị xâm phạm, bên thứ ba có thể theo dõi tất cả các giao dịch của bạn, nhưng không thể chi tiêu tiền của bạn.



Tôi thực sự khuyên bạn nên tạo nhiều bản sao của *Descriptor* này và giữ chúng với mỗi thiết bị ký trên Multisig của bạn. Ví dụ, trong trường hợp của tôi, tôi in *Descriptor* trên giấy và giữ một bản sao với Coldcard, một bản sao khác với Trezor và một bản sao với Ledger. Tôi cũng lưu *Descriptor* này dưới dạng tệp PDF trên ba ổ USB, mỗi ổ được lưu trữ với một trong các danh mục phần cứng. Theo cách này, tôi tối đa hóa cơ hội không bao giờ mất *Descriptor* này và tôi chắc chắn có hai bản sao (một bản vật lý và một bản kỹ thuật số) với mỗi thiết bị.



Sau khi danh mục Multisig của bạn được tạo, Sparrow sẽ tự động cung cấp cho bạn *Mô tả* này. Nhấp vào nút "*Lưu PDF...*" để lưu dưới dạng văn bản và mã QR.



![Image](assets/fr/22.webp)



Sau đó, bạn có thể in tệp PDF này và sao chép vào ổ USB của mình.



![Image](assets/fr/23.webp)



Chúng tôi cũng sẽ đăng ký *Descriptor* này trong Coldcard (nếu bạn sử dụng một trong cấu hình của mình). Điều này sẽ cho phép Coldcard xác minh rằng mỗi giao dịch được ký sau đó tương ứng với Wallet gốc: xpubs đúng, định dạng Address đúng, đường dẫn phái sinh đúng... Nếu không có *Descriptor* được nhập này, Coldcard không thể xác nhận rằng các địa chỉ Exchange chưa bị chiếm đoạt hoặc PSBT chưa bị giả mạo.



Đây là điều khiến Coldcard trở nên thú vị trong Multisig: nó cung cấp các biện pháp kiểm tra bổ sung chống lại một số cuộc tấn công tinh vi mà các ví phần cứng khác không cho phép (tất nhiên là với điều kiện là bạn sử dụng nó để ký).



Trong Sparrow, truy cập menu "*Cài đặt*", sau đó nhấp vào "*Xuất...*".



![Image](assets/fr/24.webp)



Bên cạnh tùy chọn "*Coldcard Multisig*", hãy nhấp vào "*Xuất tệp...*" và lưu tệp văn bản vào thẻ Micro SD.



![Image](assets/fr/25.webp)



Sau đó, lắp thẻ vào Coldcard. Vào menu "*Cài đặt*", sau đó vào "*Ví Multisig*", và chọn "*Nhập từ SD*".



![Image](assets/fr/26.webp)



Chọn tệp thích hợp và xác nhận nhập.



![Image](assets/fr/27.webp)



Nhấp vào tên Multisig mới nhập của bạn.



![Image](assets/fr/28.webp)



Kiểm tra thông số cấu hình Multisig, sau đó xác nhận đăng ký.



![Image](assets/fr/29.webp)



Multisig của bạn hiện đã được lưu chính xác trong Coldcard của bạn. Nếu bạn có nhiều Coldcard trong cùng một Multisig, hãy lặp lại quy trình này cho từng Coldcard.



Ngoài việc lưu *Descriptor*, đừng quên đặc biệt chú ý đến việc lưu cụm từ Mnemonic cho từng thiết bị chữ ký của bạn. Nếu bạn mới bắt đầu, tôi thực sự khuyên bạn nên tham khảo hướng dẫn khác này để biết cách lưu và quản lý chúng đúng cách:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Trước khi nhận bitcoin đầu tiên trên Multisig của bạn, **Tôi thực sự khuyên bạn nên thực hiện một bài kiểm tra khôi phục rỗng**. Ghi lại một số thông tin tham khảo, chẳng hạn như Address đầu tiên nhận được, sau đó đặt lại ví phần cứng của bạn trong khi Wallet vẫn còn rỗng. Tiếp theo, hãy thử khôi phục Multisig Wallet của bạn trên Ví phần cứng bằng cách sử dụng bản sao lưu giấy cụm từ Mnemonic của bạn, sau đó trên Sparrow bằng cách sử dụng *Descriptor*. Kiểm tra xem Address đầu tiên được tạo sau khi khôi phục có khớp với Address đầu tiên mà bạn đã viết ra ban đầu không. Nếu khớp, bạn có thể yên tâm rằng bản sao lưu giấy của bạn là đáng tin cậy.



Để tìm hiểu thêm về cách thực hiện thử nghiệm phục hồi, tôi khuyên bạn nên tham khảo hướng dẫn khác này:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Nhận bitcoin trên Multisig của bạn



Wallet của bạn hiện đã sẵn sàng để nhận bitcoin. Trong Sparrow, hãy nhấp vào tab "*Nhận*".



![Image](assets/fr/30.webp)



Trước khi sử dụng Address do Sparrow Wallet tạo ra, hãy dành thời gian kiểm tra trực tiếp trên màn hình ví phần cứng của bạn. Điều này sẽ đảm bảo rằng Address không bị thay đổi và thiết bị của bạn giữ các khóa riêng cần thiết để chi tiêu các khoản tiền liên quan. Điều này giúp bảo vệ bạn khỏi một số vectơ tấn công.



Để thực hiện việc này, hãy nhấp vào "*Hiển thị Address*" để hiển thị Address trên Trezor hoặc Ledger của bạn khi được kết nối bằng cáp.



![Image](assets/fr/31.webp)



Với Coldcard, việc xác minh này có thể được thực hiện mà không cần bất kỳ tương tác nào với Sparrow. Chỉ cần mở menu "*Address Explorer*", sau đó chọn Multisig của bạn ở dưới cùng.



![Image](assets/fr/32.webp)



Sau đó, bạn sẽ thấy các địa chỉ tiếp nhận được tạo ra bởi Multisig.



![Image](assets/fr/33.webp)



Kiểm tra xem Address hiển thị trên mỗi Hardware Wallet có tương ứng chính xác với Wallet trong Sparrow không. Nên thực hiện việc này ngay trước khi chia sẻ Address với người trả tiền để đảm bảo tính toàn vẹn của nó.



Sau đó, bạn có thể gán "*Nhãn*" cho Address này để chỉ ra nguồn gốc của bitcoin nhận được. Đây là một cách tốt để tổ chức quản lý UTXO của bạn.



![Image](assets/fr/34.webp)



Sau khi xác minh xong, bạn có thể sử dụng Address để nhận bitcoin.



![Image](assets/fr/35.webp)



## Gửi bitcoin bằng Multisig của bạn



Bây giờ bạn đã nhận được Satss đầu tiên trên Multisig Wallet của mình, bạn cũng có thể chi tiêu chúng! Trong Sparrow, hãy vào tab "*Gửi*" để tạo giao dịch mới.



![Image](assets/fr/36.webp)



Nếu bạn muốn sử dụng *Coin Control*, tức là chọn thủ công các UTXO bạn muốn chi tiêu, hãy chuyển đến tab "*UTXOs*". Chọn các UTXO bạn muốn chi tiêu, sau đó nhấp vào "*Gửi mục đã chọn*". Bạn sẽ được tự động chuyển hướng đến tab "*Gửi*", với các UTXO đã được điền sẵn.



![Image](assets/fr/37.webp)



Nhập đích Address. Có thể thêm nhiều địa chỉ bằng cách nhấp vào "*+ Thêm*".



![Image](assets/fr/38.webp)



Thêm "*Nhãn*" để mô tả mục đích của khoản chi phí này, giúp bạn theo dõi các giao dịch dễ dàng hơn.



![Image](assets/fr/39.webp)



Nhập số tiền cần gửi đến Address đã chọn.



![Image](assets/fr/40.webp)



Điều chỉnh tốc độ sạc theo điều kiện mạng hiện tại. Ví dụ, hãy tham khảo [Mempool.space](https://Mempool.space/) để chọn mức sạc phù hợp.



Sau khi kiểm tra tất cả các thông số giao dịch, hãy nhấp vào "*Tạo giao dịch*".



![Image](assets/fr/41.webp)



Nếu bạn hài lòng với mọi thứ, hãy nhấp vào "*Hoàn tất giao dịch để ký*".



![Image](assets/fr/42.webp)



Ở cuối màn hình, bạn sẽ thấy Sparrow đang chờ 2 chữ ký. Điều này là bình thường: Wallet được sử dụng ở đây là Multisig 2-de-3.



![Image](assets/fr/43.webp)



Tôi bắt đầu ký bằng Coldcard của mình. Để thực hiện, tôi lắp thẻ Micro SD vào máy tính, sau đó nhấp vào "*Lưu giao dịch*".



![Image](assets/fr/44.webp)



Có 3 cách để truyền giao dịch cần ký đến Hardware Wallet của bạn, sau đó lấy lại từ Sparrow. Cách đầu tiên là sử dụng thẻ Micro SD, như chúng ta sẽ làm ở đây cho Coldcard. Cách thứ hai là thông qua kết nối cáp, chúng ta sẽ sử dụng cho chữ ký thứ hai (Ledger và Trezor). Cuối cùng, có thể sử dụng giao tiếp mã QR, cho các thiết bị được trang bị camera như Coldcard Q, Jade Plus hoặc Passport V2.



Sau khi lưu PSBT (*Partially Signed Bitcoin Transaction*) trên thẻ Micro SD, tôi lắp thẻ vào Coldcard MK3, sau đó chọn menu "*Sẵn sàng ký*".



![Image](assets/fr/45.webp)



Trên màn hình Hardware Wallet của bạn, hãy kiểm tra cẩn thận các thông số giao dịch: Address của người nhận, số tiền đã gửi và các khoản phí. Sau khi giao dịch được xác nhận, hãy xác thực để tiến hành ký.



![Image](assets/fr/46.webp)



Sau đó trả lại Micro SD vào máy tính của bạn và nhấp vào "*Load Transaction*" trong Sparrow. Chọn PSBT được Coldcard ký từ các tệp của bạn.



![Image](assets/fr/47.webp)



Bạn có thể thấy chữ ký Coldcard đã được thêm vào. Bây giờ tôi sẽ sử dụng thiết bị thứ hai, trong trường hợp này là Ledger, để thực hiện chữ ký thứ hai cần thiết. Tôi kết nối nó, mở khóa nó, sau đó nhấp vào "*Sign*" trên Sparrow.



![Image](assets/fr/48.webp)



Nhấp vào "*Ký*" bên cạnh tên Hardware Wallet của bạn.



![Image](assets/fr/49.webp)



Lần đầu tiên bạn sử dụng Ledger với Multisig này, Sparrow sẽ yêu cầu bạn xác minh khóa công khai mở rộng (xpub) của người đồng ký. Cũng giống như Coldcard, bước này ngăn bạn ký một cách mù quáng sau này. Để xác thực thông tin này, hãy so sánh xpub hiển thị trên màn hình Ledger với những xpub do các ví phần cứng khác của bạn cung cấp trực tiếp.



![Image](assets/fr/50.webp)



Kiểm tra mẫu Address của người nhận, số tiền chuyển và phí giao dịch, sau đó ký xác nhận giao dịch.



![Image](assets/fr/51.webp)



Nhấn vào màn hình để ký.



![Image](assets/fr/52.webp)



Sparrow hiện có hai chữ ký cần thiết để giải phóng tiền từ danh mục đầu tư Multisig. Kiểm tra giao dịch lần cuối và nếu mọi việc diễn ra tốt đẹp, hãy nhấp vào "*Phát sóng giao dịch*" để phát sóng qua mạng.



![Image](assets/fr/53.webp)



Bạn sẽ tìm thấy giao dịch này trong tab "*Giao dịch*" của Sparrow Wallet.



![Image](assets/fr/54.webp)



Xin chúc mừng, giờ bạn đã biết cách thiết lập và sử dụng Wallet đa chữ ký trên Sparrow. Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Vui lòng chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn vì đã chia sẻ!



Để đi sâu hơn, tôi khuyên bạn nên tham khảo hướng dẫn này về một phương pháp khác để tăng cường tính bảo mật cho Bitcoin Wallet của bạn, passphrase BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7