from flask import Flask, jsonify
import yfinance as yf
import os

app = Flask(__name__)

@app.route('/api/bnbr', methods=['GET'])
def get_bnbr_valuation():
    """
    Endpoint untuk mendapatkan data valuasi saham Bakrie & Brothers (BNBR.JK)
    """
    try:
        # Inisialisasi ticker untuk Bakrie & Brothers (BNBR)
        bnb = yf.Ticker("BNBR.JK")
        
        # Mengambil semua informasi metrik
        info = bnb.info
        
        # Membuat dictionary dengan data valuasi
        valuation_data = {
            "symbol": "BNBR.JK",
            "company_name": info.get('longName', 'N/A'),
            "valuation_metrics": {
                "market_cap": info.get('marketCap'),
                "enterprise_value": info.get('enterpriseValue'),
                "trailing_pe": info.get('trailingPE'),
                "forward_pe": info.get('forwardPE'),
                "peg_ratio": info.get('pegRatio'),
                "price_to_sales_ttm": info.get('priceToSalesTrailing12Months'),
                "price_to_book_mrq": info.get('priceToBook'),
                "enterprise_value_to_revenue": info.get('enterpriseToRevenue'),
                "enterprise_value_to_ebitda": info.get('enterpriseToEbitda')
            }
        }
        
        return jsonify(valuation_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_valuation(ticker):
    """
    Endpoint untuk mendapatkan data valuasi saham berdasarkan ticker
    Contoh: /api/stock/BNBR.JK
    """
    try:
        # Inisialisasi ticker
        stock = yf.Ticker(ticker)
        
        # Mengambil semua informasi metrik
        info = stock.info
        
        # Membuat dictionary dengan data valuasi
        valuation_data = {
            "symbol": ticker,
            "company_name": info.get('longName', 'N/A'),
            "valuation_metrics": {
                "market_cap": info.get('marketCap'),
                "enterprise_value": info.get('enterpriseValue'),
                "trailing_pe": info.get('trailingPE'),
                "forward_pe": info.get('forwardPE'),
                "peg_ratio": info.get('pegRatio'),
                "price_to_sales_ttm": info.get('priceToSalesTrailing12Months'),
                "price_to_book_mrq": info.get('priceToBook'),
                "enterprise_value_to_revenue": info.get('enterpriseToRevenue'),
                "enterprise_value_to_ebitda": info.get('enterpriseToEbitda')
            }
        }
        
        return jsonify(valuation_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    """
    Endpoint utama untuk informasi API
    """
    return jsonify({
        "message": "YFinance Stock Valuation API",
        "endpoints": {
            "/api/bnbr": "Get BNBR stock valuation data",
            "/api/stock/<ticker>": "Get stock valuation data by ticker (e.g., /api/stock/BNBR.JK)"
        }
    }), 200

if __name__ == '__main__':
    # Use debug mode only in development
    debug_mode = os.getenv('FLASK_ENV', 'development') != 'production'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)

