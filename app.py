from flask import Flask, render_template ,url_for
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test')
def test():
   return render_template('test.html')

@app.route('/final')
def final():
   return render_template('final.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)