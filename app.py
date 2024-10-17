from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''English: Hello, World!<br>
              Spanish: ¡Hola, Mundo!<br> 
              French: Bonjour, le monde!<br>
              German: Hallo, Welt!<br>
              Italian: Ciao, Mondo!<br>
              Portuguese: Olá, Mundo!<br>
              Chinese: 你好，世界！<br> 
              Korean: 안녕하세요, 세계!<br> 
              Russian: Привет, мир!<br>
              Hindi: नमस्ते, दुनिया!<br> 
              Arabic: مرحباً بالعالم!<br>
              Japanese: こんにちは、世界！<br>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    


