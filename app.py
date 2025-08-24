from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_TOKEN = "Bearer 6XLCTKW1ELXA5VPXE91C0OI68HIVRO4RFPBRUUMFEKAIV7TJ0NKZMLLGEGPYQWRS"

# Route: lấy danh sách giao dịch
@app.route("/api/lsgd", methods=["GET"])
def get_transactions():
    try:
        url = "https://my.sepay.vn/userapi/transactions/list"
        headers = {
            "Content-Type": "application/json",
            "Authorization": API_TOKEN
        }
        params = {"limit": 20}

        res = requests.get(url, headers=headers, params=params)
        data = res.json()

        return jsonify({
            "message": "Lấy lịch sử giao dịch thành công!",
            "metadata": data
        }), 200
    except Exception as e:
        return jsonify({"message": "Có lỗi xảy ra", "error": str(e)}), 500


# Route: lấy chi tiết 1 giao dịch (truyền ?id=xxxx)
@app.route("/api/detail-gd", methods=["GET"])
def get_transaction_detail():
    try:
        tx_id = request.args.get("id")  # lấy tham số id trên URL
        if not tx_id:
            return jsonify({"message": "Thiếu id giao dịch"}), 400

        url = f"https://my.sepay.vn/userapi/transactions/details/{tx_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": API_TOKEN
        }

        res = requests.get(url, headers=headers)
        data = res.json()

        return jsonify({
            "message": "Lấy chi tiết giao dịch thành công!",
            "metadata": data
        }), 200
    except Exception as e:
        return jsonify({"message": "Có lỗi xảy ra", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
