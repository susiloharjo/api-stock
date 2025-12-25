# yfinance Stock Valuation API

Aplikasi Flask untuk mengambil data saham (harga, volume, dan valuasi) menggunakan yfinance dengan output format JSON.

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

### 2. Stock Data by Ticker
```
GET http://localhost:5000/api/stock/<ticker>
```
Mengambil data lengkap saham (harga, volume, dan valuasi) berdasarkan ticker.

**Contoh penggunaan:**
- `http://localhost:5000/api/stock/BNBR.JK` - Saham Bakrie & Brothers
- `http://localhost:5000/api/stock/BBRI.JK` - Saham Bank BRI
- `http://localhost:5000/api/stock/AAPL` - Saham Apple (NASDAQ)
- `http://localhost:5000/api/stock/TSLA` - Saham Tesla

**Format ticker:**
- Saham Indonesia: `KODE.JK` (contoh: `BNBR.JK`, `BBRI.JK`)
- Saham internasional: `KODE` (contoh: `AAPL`, `TSLA`, `GOOGL`)

## Response Format

Endpoint mengembalikan data dalam format JSON dengan struktur berikut:

```json
{
  "symbol": "BNBR.JK",
  "company_name": "PT Bakrie & Brothers Tbk",
  "current_price": 116.0,
  "volume_shares": 615821000,
  "volume_lot": 6158210.0,
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

**Penjelasan field:**
- `symbol`: Kode ticker saham
- `company_name`: Nama lengkap perusahaan
- `current_price`: Harga terakhir saham (atau harga penutupan jika pasar tutup)
- `volume_shares`: Volume perdagangan dalam lembar saham
- `volume_lot`: Volume perdagangan dalam lot (1 lot = 100 lembar, khusus Indonesia)
- `valuation_metrics`: Metrik valuasi perusahaan

## Testing API

Menggunakan curl:
```bash
# Test root endpoint
curl http://localhost:5000/

# Test stock data (BNBR)
curl http://localhost:5000/api/stock/BNBR.JK

# Test stock data (BBRI)
curl http://localhost:5000/api/stock/BBRI.JK

# Test stock data dengan formatting JSON
curl http://localhost:5000/api/stock/BNBR.JK | python3 -m json.tool
```

Menggunakan browser:
- Buka `http://localhost:5000/` untuk melihat info API
- Buka `http://localhost:5000/api/stock/BNBR.JK` untuk melihat data saham BNBR

## Catatan Penting

**yfinance TIDAK memerlukan API key!** 

yfinance adalah library Python yang mengambil data dari Yahoo Finance secara publik. Tidak ada autentikasi atau registrasi yang diperlukan. Anda bisa langsung menggunakannya setelah diinstall.

## Data yang Tersedia

### Informasi Harga & Volume
- **Harga Terakhir**: Harga saham saat ini atau harga penutupan terakhir
- **Volume (Lembar)**: Volume perdagangan dalam satuan lembar saham
- **Volume (Lot)**: Volume perdagangan dalam satuan lot (1 lot = 100 lembar, khusus Indonesia)

### Metrik Valuasi
- **Market Cap**: Kapitalisasi pasar
- **Enterprise Value**: Nilai perusahaan
- **Trailing P/E**: Price-to-Earnings ratio (trailing 12 months)
- **Forward P/E**: Price-to-Earnings ratio (forward)
- **PEG Ratio**: Price/Earnings to Growth ratio
- **Price/Sales (ttm)**: Price-to-Sales ratio (trailing 12 months)
- **Price/Book (mrq)**: Price-to-Book ratio (most recent quarter)
- **Enterprise Value/Revenue**: Enterprise Value to Revenue ratio
- **Enterprise Value/EBITDA**: Enterprise Value to EBITDA ratio

## Catatan tentang Data

- Data diambil dari Yahoo Finance melalui library yfinance
- Harga dan volume adalah data real-time atau data terakhir yang tersedia
- Beberapa metrik mungkin `null` jika data tidak tersedia untuk saham tertentu
- Volume dalam lot hanya relevan untuk saham Indonesia (format `.JK`)

