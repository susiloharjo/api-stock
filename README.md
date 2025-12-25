# yfinance Stock Valuation API

Aplikasi Flask untuk mengambil data valuasi saham menggunakan yfinance dengan output format JSON.

## Setup

1. Buat virtual environment:
```bash
python3 -m venv venv
```

2. Aktifkan virtual environment:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Menjalankan Script Standalone

```bash
source venv/bin/activate
python3 test_bnbr.py
```

## Menjalankan Flask API

### Menggunakan Virtual Environment (Development)

1. Aktifkan virtual environment:
```bash
source venv/bin/activate
```

2. Jalankan aplikasi Flask:
```bash
python3 app.py
```

Server akan berjalan di `http://localhost:5000`

### Menggunakan Docker (Recommended for Production)

1. Build dan jalankan menggunakan Docker Compose:
```bash
docker-compose up --build
```

2. Atau build dan run menggunakan Docker langsung:
```bash
# Build image
docker build -t yfinance-api .

# Run container
docker run -d -p 5000:5000 --name yfinance-api yfinance-api
```

3. Untuk melihat logs:
```bash
docker-compose logs -f
# atau
docker logs -f yfinance-api
```

4. Untuk stop container:
```bash
docker-compose down
# atau
docker stop yfinance-api && docker rm yfinance-api
```

Server akan berjalan di `http://localhost:5000`

## API Endpoints

### 1. Root Endpoint
```
GET http://localhost:5000/
```
Menampilkan informasi tentang API dan daftar endpoints yang tersedia.

### 2. BNBR Valuation
```
GET http://localhost:5000/api/bnbr
```
Mengambil data valuasi saham Bakrie & Brothers (BNBR.JK).

### 3. Stock Valuation by Ticker
```
GET http://localhost:5000/api/stock/<ticker>
```
Mengambil data valuasi saham berdasarkan ticker. Contoh:
- `http://localhost:5000/api/stock/BNBR.JK`
- `http://localhost:5000/api/stock/BBRI.JK`
- `http://localhost:5000/api/stock/AAPL`

## Response Format

Semua endpoint mengembalikan data dalam format JSON:

```json
{
  "symbol": "BNBR.JK",
  "company_name": "PT Bakrie & Brothers Tbk",
  "valuation_metrics": {
    "market_cap": 20116351746048,
    "enterprise_value": 21177579864064,
    "trailing_pe": null,
    "forward_pe": null,
    "peg_ratio": null,
    "price_to_sales_ttm": 5.2916975,
    "price_to_book_mrq": 5.9716864,
    "enterprise_value_to_revenue": 5.571,
    "enterprise_value_to_ebitda": 116.254
  }
}
```

## Testing API

Menggunakan curl:
```bash
# Test root endpoint
curl http://localhost:5000/

# Test BNBR endpoint
curl http://localhost:5000/api/bnbr

# Test stock by ticker
curl http://localhost:5000/api/stock/BNBR.JK
```

Menggunakan browser:
- Buka `http://localhost:5000/api/bnbr` di browser

## Catatan Penting

**yfinance TIDAK memerlukan API key!** 

yfinance adalah library Python yang mengambil data dari Yahoo Finance secara publik. Tidak ada autentikasi atau registrasi yang diperlukan. Anda bisa langsung menggunakannya setelah diinstall.

## Metrik yang Tersedia

- Market Cap
- Enterprise Value
- Trailing P/E
- Forward P/E
- PEG Ratio
- Price/Sales (ttm)
- Price/Book (mrq)
- Enterprise Value/Revenue
- Enterprise Value/EBITDA

