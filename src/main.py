from flask import Flask, request, jsonify
import openai
import os

openai.api_type = "azure"
openai.api_version = "2023-05-15" #"2022-12-01"

app = Flask(__name__)
testVcap = os.getenv("VCAP_SERVICES","not setting")
try:
    app.logger.info(f"vcap = {testVcap}")
except Exception as e:
    app.logger.info(f"vcap error {e}")

testRawVcap = os.getenv("vcap","not setting")
try:
    import json
    app.logger.info(f"vcap = {testRawVcap}")
    testVcap2 = json.loads(testRawVcap)
    app.logger.info(f"vcap = {testVcap2}")
except Exception as e:
    app.logger.info(f"vcap error {e}")

@app.route("/v2/completion", methods=["POST"])
def predict_completion():
    try:
        payload = request.json
        if payload:
            completion = openai.Completion.create(**payload)
            if not completion is None:
                return jsonify(completion)
        
        return jsonify({"error": "Malformed Payload"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/v2/chat-completion", methods=["POST"])
def predict_chat_completion():
    try:
        payload = request.json
        if payload:
            completion = openai.ChatCompletion.create(**payload)
            if not completion is None:
                return jsonify(completion)
        
        return jsonify({"error": "Malformed Payload"})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/v2/vcap", methods=["GET"])
def get_vcap():
    try:
        app.logger.info(f"vcap = {testVcap}")
        app.logger.info(f"vcap1 = {testVcap2}")
        return jsonify({"error": str(e)})
    except Exception as e:
        return jsonify({"error": str(e)})
