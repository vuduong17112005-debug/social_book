# Ghi chú Nghiên cứu - Tuần 2

## 1. Tìm hiểu về Django Models (Cơ sở dữ liệu)
* **Khái niệm Model:** Trong Django, Model là nơi định nghĩa cấu trúc dữ liệu dưới dạng các class Python. Mỗi class tương ứng với một bảng (table) trong cơ sở dữ liệu.
* **Mối quan hệ One-to-One (1-1):** Tìm hiểu cách dùng `OneToOneField`. Trong dự án này, mỗi `User` (người dùng hệ thống) sẽ chỉ có duy nhất một `Profile` (thông tin mạng xã hội). Việc tách riêng giúp quản lý dữ liệu sạch sẽ hơn.
* **Các kiểu dữ liệu quan trọng:**
    * `CharField`: Dùng cho văn bản ngắn (vị trí, tên).
    * `TextField`: Dùng cho văn bản dài (tiểu sử/bio).
    * `ImageField`: Dùng để quản lý file ảnh (ảnh đại diện). Cần thư viện `Pillow` để xử lý.

## 2. Hệ thống Xác thực (Authentication)
* **User Model mặc định:** Django cung cấp sẵn model `User` với các trường như username, email, password.
* **Quy trình xử lý:**
    * **Signup (Đăng ký):** Sử dụng hàm `User.objects.create_user` để tự động mã hóa mật khẩu trước khi lưu vào database.
    * **Login (Đăng nhập):** Sử dụng hàm `authenticate()` để kiểm tra thông tin và `login()` để tạo phiên làm việc (session).
    * **Logout (Đăng xuất):** Sử dụng hàm `logout()` để hủy phiên làm việc của người dùng.

## 3. Cơ chế Django Signals (Kiến thức nâng cao)
* **Tín hiệu (Signals):** Cho phép các phần khác nhau của ứng dụng nhận thông báo khi có một sự kiện xảy ra.
* **Ứng dụng:** Tìm hiểu về `post_save`. Mục tiêu là khi một `User` mới được tạo ra, hệ thống sẽ tự động tạo một bản ghi `Profile` tương ứng cho người dùng đó mà không cần viết code tạo thủ công trong View.

## 4. Bảo mật dữ liệu
* Tìm hiểu về cách Django bảo vệ mật khẩu người dùng thông qua việc băm (hashing) thay vì lưu văn bản thuần túy, đảm bảo an toàn nếu database bị lộ.

## 5. Nguồn tham khảo chính
* Tài liệu Django Models: https://docs.djangoproject.com/en/stable/topics/db/models/
* Tài liệu User Authentication: https://docs.djangoproject.com/en/stable/topics/auth/default/
