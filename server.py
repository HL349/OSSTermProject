from flask import Flask, request, jsonify
import subprocess
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/run_kakao_review', methods=['POST'])
def run_kakao_review():
    query = request.json.get('query', '남대문시장')
    app.logger.debug(f"Received query: {query}")
    try:
        result = subprocess.run(['python3', 'KakaoReview.py', query], capture_output=True, text=True, check=True)
        app.logger.debug(f"Script output: {result.stdout}")
        return jsonify({'output': result.stdout})
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Error running script: {e.stderr}")
        return jsonify({'output': e.stderr}), 500

if __name__ == '__main__':
    app.run(debug=True)
