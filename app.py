from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1. The Home Page (Login/PIN Screen)
@app.route('/')
def home():
    return render_template('login.html')

# 2. File Upload Page
@app.route('/upload')
def upload_page():
    return render_template('upload.html')

# 3. Checkout / Print Settings Page
@app.route('/checkout')
def checkout_page():
    return render_template('checkout.html')

# 4. Asol API (ETA PORE PI ER SATHE KATHA BOLBE)
@app.route('/verify_pin', methods=['POST'])
def verify_pin():
    data = request.json
    pin = data.get('pin')
    
    # Ekhonkar jonno ekta test PIN: 1234
    if pin == "1234":
        return jsonify({"status": "success", "message": "PIN Matched!"})
    else:
        return jsonify({"status": "error", "message": "Invalid PIN!"}), 400

if __name__ == '__main__':
    # Eta tor laptop e server chalabe (Port 5000)
    app.run(debug=True, port=5000)