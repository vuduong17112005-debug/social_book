# Ghi chú Nghiên cứu - Tuần 1

## 1. Tìm hiểu về Django Framework
* **Mô hình MVT (Model-View-Template):** * **Model:** Quản lý dữ liệu và logic nghiệp vụ (tương tác với Database).
    * **View:** Xử lý các yêu cầu HTTP và trả về phản hồi (logic điều hướng).
    * **Template:** Giao diện người dùng (HTML/CSS/JS).
* **Virtual Environment (venv):** Hiểu được tầm quan trọng của việc cô lập các thư viện dự án, tránh xung đột phiên bản với hệ thống.

## 2. Cấu trúc Dự án & Cấu hình hệ thống
* **Project vs App:** Một Project Django có thể chứa nhiều App. Trong dự án này, em đã khởi tạo app `core` để quản lý các tính năng chính.
* **Cấu hình Media & Static:** * `STATIC_URL`: Dùng cho các file tĩnh như CSS, JS của hệ thống.
    * `MEDIA_URL`: Dùng cho các file do người dùng tải lên (ảnh đại diện, ảnh bài đăng).
    * Đã nắm vững cách cấu hình `settings.py` và kết nối chúng vào `urls.py`.

## 3. Quản lý mã nguồn với Git
* **.gitignore:** Đã cấu hình để loại bỏ các thư mục không cần thiết như `venv/` và các file dữ liệu nhạy cảm/tạm thời như `db.sqlite3`, `__pycache__`.
* **Cấu trúc Repository:** Đã tổ chức lại thư mục theo hướng dẫn để tách biệt giữa tài liệu nghiên cứu (`docs/`) và mã nguồn thực tế (`src/`).

## 4. Nguồn tham khảo
* Tài liệu chính thống: [Django Documentation](https://docs.djangoproject.com/en/stable/)
* Lộ trình phát triển: [Backend Roadmap - roadmap.sh](https://roadmap.sh/backend)
