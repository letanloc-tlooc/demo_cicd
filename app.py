from flask import Flask, render_template_string

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
        </style>
      </head>
      <body>
        <div class="heart">💗</div>
        <h1>Gửi em yêu 💌</h1>
        <p>Chúc em một ngày ngọt ngào như nụ cười của em vậy 😘</p>
        <p>Anh luôn ở đây, yêu bé Ngọc của anh 💕</p>
      </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)