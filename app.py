from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# 🖨️ Asol Print Command Route
@app.route('/print_document', methods=['POST'])
def print_document():
    data = request.get_json()
    
    payment_id = data.get('payment_id')
    file_name = data.get('file_name')
    copies = data.get('copies', 1)
    color_mode = data.get('color_mode', 'BW')
    
    # Logic: Terminal-e print command execute hobe
    print(f"💰 Payment Verified: {payment_id}")
    
    # 🛑 Raspberry Pi / Linux specific command
    # lp -n [copies] -o monochrome [file_path]
    try:
        # Dummy print command (Uncomment os.system for real printer)
        color_flag = "" if color_mode == "COLOR" else "-o monochrome"
        print_cmd = f"lp -n {copies} {color_flag} './uploads/{file_name}'"
        print(f"Executing: {print_cmd}")
        
        # os.system(print_cmd) 
        
        return jsonify({"status": "success", "message": "Print started!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    # Uploads folder na thakle baniye nibe
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True, host='0.0.0.0', port=5000)