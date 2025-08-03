import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Приложение работает!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting app on port {port}")  # Лог в консоль
    app.run(host='0.0.0.0', port=port)
