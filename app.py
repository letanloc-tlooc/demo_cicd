from flask import Flask, render_template_string, render_template

app = Flask(__name__)

@app.route("/")
def love_message():
    return render_template_string("""
    <html>
      <head>
        <title>To My Love 💖</title>
        <style>
          body {
            font-family: 'Arial', sans-serif;
            background-color: #ffe6f0;
            color: #cc0066;
            text-align: center;
            margin-top: 100px;
          }
          .heart {
            font-size: 64px;
            animation: beat 1s infinite;
          }
          @keyframes beat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
          }
        a.love-button {
            display: inline-block;
            margin-top: 40px;
            padding: 14px 30px;
            background: linear-gradient(45deg, #ff99cc, #ff66b2);
            color: white;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            border-radius: 50px;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.4);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            }

            a.love-button:hover {
            background: linear-gradient(45deg, #ff66b2, #ff3385);
            box-shadow: 0 6px 20px rgba(255, 105, 180, 0.6);
            transform: scale(1.05);
            }
        </style>
      </head>
      <body>
        <div class="heart">💗</div>
        <h1>Gửi em yêu 💌</h1>
        <p>Chúc em một ngày ngọt ngào như nụ cười của em vậy 😘</p>
        <p>Anh luôn ở đây, yêu bé Ngọc của anh 💕</p>
        <a href="{{ url_for('home') }}" class="love-button">💖 Yêu em 💖</a>
      </body>
    </html>
    """)

@app.route('/yeu')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)