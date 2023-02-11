from flask import Flask, render_template, url_for, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://sparta:test@cluster0.rqyqkq1.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/quiz', methods=["GET"])
def quiz():
    quiz = list(db.QUIZ.find({}, {'_id': False}))
    return jsonify({'result': quiz})

@app.route('/result', methods=["GET"])
def result():
    result = list(db.RESULT.find({}, {'_id': False}))
    return jsonify({'result': result})

@app.route('/final')
def final():
    arg = request.args.get('total_score')
    return render_template('final.html', total_score=arg)
# total_score=num

@app.route('/final/score', methods=["POST"])
def final_score():
    results = request.form["score_give"]
    num = results
    # db에 점수를 가지고 조회해서 알맞는 결과 문장 가져오는 코드 작성
    return jsonify({'result': num})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)