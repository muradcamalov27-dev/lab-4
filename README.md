# Django Laboratoriya 4

Bu layihə Django veb çərçivəsinin əsas konsepsiyalarını öyrənmək üçün hazırlanmış bir laboratoriya tapşırığıdır.

## Layihə Strukturu

```
djangolab4/
├── djangolab4/          # Layihə konfiqurasiyası
│   ├── settings.py      # Django ayarları
│   ├── urls.py          # URL marşrutları
│   ├── asgi.py          # ASGI konfiqurasiyası
│   └── wsgi.py          # WSGI konfiqurasiyası
├── myapp/               # Django tətbiqəsi
│   ├── templates/       # HTML şablonları
│   │   └── myapp/
│   │       └── index.html
│   ├── views.py         # View funksiyaları
│   ├── urls.py          # Tətbiqə xas URL-lər
│   ├── models.py        # Məlumatlar bazası modelləri
│   └── admin.py         # Admin paneli konfiqurasiyası
├── manage.py            # Django idarəetmə əmri
└── README.md            # Bu faylı
```

## Quraşdırma

### Tələblər

- Python 3.11+
- Django 5.2.8

### Quraşdırma Addımları

1. **Python Virtual Environment yaratmaq:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # və ya
   venv\Scripts\activate  # Windows
   ```

2. **Django quraşdırmaq:**
   ```bash
   pip install django
   ```

3. **Layihəni çalıştırmaq:**
   ```bash
   python manage.py runserver
   ```

4. **Veb səhifəyə daxil olmaq:**
   ```
   http://localhost:8000/
   ```

## Layihənin Xüsusiyyətləri

### 2. Quraşdırma Addımı

- Python 3.11.0rc1 quraşdırıldı
- Django 5.2.8 quraşdırıldı
- Django layihəsi yaradıldı
- Django tətbiqəsi (myapp) yaradıldı

### 4. Sadə Statik Veb Səhifənin Hazırlanması

- **HTML Şablonu:** `myapp/templates/myapp/index.html`
  - Rəngli və modern dizayn
  - Responsive layout
  - Django haqqında məlumat

- **View Funksiyası:** `myapp/views.py`
  - `index` funksiyası HTML şablonunu render edir

- **URL Konfiqurasiyası:**
  - `myapp/urls.py` - Tətbiqə xas URL marşrutları
  - `djangolab4/urls.py` - Layihə URL marşrutları

## Django MVT Arxitekturası

Django **Model-View-Template (MVT)** arxitekturasından istifadə edir:

- **Model:** Məlumatlar bazası ilə əlaqə
- **View:** Məntiq və məlumatların işlənməsi
- **Template:** İstifadəçiyə göstərilən HTML səhifə

## Faydalı Əmrlər

```bash
# Layihəni çalıştırmaq
python manage.py runserver

# Migrasyonları tətbiq etmək
python manage.py migrate

# Admin panelində super istifadəçi yaratmaq
python manage.py createsuperuser

# Admin panelinə daxil olmaq
# http://localhost:8000/admin/
```

## Qeydlər

- Bu layihə laboratoriya tapşırığının 2-ci və 4-cü addımlarını əhatə edir
- Layihə sadə statik veb səhifə ilə başlayır
- Gələcəkdə modelləri, formları və daha mürəkkəb funksiyaları əlavə etmək mümkündür

## Müəllif

Lab User

## Tarix

2025-11-24
