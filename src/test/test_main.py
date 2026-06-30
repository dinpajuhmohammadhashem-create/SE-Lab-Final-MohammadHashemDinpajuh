from fastapi.testclient import TestClient
from src.main import app, students_db

# ساخت یک کلاینت تستی از اپلیکیشن ما
client = TestClient(app)

# این تابع قبل از اجرای هر تست، لیست دانشجویان را خالی می‌کند تا تست‌ها مستقل باشند
def setup_function():
    students_db.clear()

def test_add_student_success():
    """تست مسیر موفق: ثبت یک دانشجوی جدید"""
    # 1. Arrange (آماده‌سازی داده‌ها)
    payload = {
        "id": "111",
        "name": "Test Student",
        "major": "Software Engineering"
    }
    
    # 2. Act (اجرای درخواست)
    response = client.post("/api/students", json=payload)
    
    # 3. Assert (بررسی صحت نتیجه)
    assert response.status_code == 201
    assert response.json()["id"] == "111"

def test_add_student_duplicate_error():
    """تست مسیر خطا: جلوگیری از ثبت دانشجوی تکراری"""
    # 1. Arrange (آماده‌سازی: ابتدا یک دانشجو را ثبت می‌کنیم)
    payload = {
        "id": "222",
        "name": "Ali Ahmadi",
        "major": "IT"
    }
    client.post("/api/students", json=payload)
    
    # 2. Act (اجرای مجدد همان درخواست تکراری)
    response = client.post("/api/students", json=payload)
    
    # 3. Assert (بررسی اینکه آیا سیستم خطای 400 برمی‌گرداند یا خیر)
    assert response.status_code == 400
    assert response.json()["detail"] == "دانشجویی با این شماره قبلاً ثبت شده است"

def test_get_student_by_id_success():
    """تست مسیر موفق: دریافت اطلاعات یک دانشجو با آیدی"""
    # 1. Arrange (آماده‌سازی: یک دانشجو به دیتابیس تستی اضافه می‌کنیم)
    payload = {
        "id": "333",
        "name": "Sara",
        "major": "Computer Science"
    }
    client.post("/api/students", json=payload)
    
    # 2. Act (ارسال درخواست GET برای دریافت همان دانشجو)
    response = client.get("/api/students/333")
    
    # 3. Assert (بررسی بازگشت صحیح داده‌ها)
    assert response.status_code == 200
    assert response.json()["name"] == "Sara"
