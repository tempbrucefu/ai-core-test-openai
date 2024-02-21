from flask import Flask, request, jsonify
import openai
import logging
import os

openai.api_type = "azure"
openai.api_version = "2023-05-15" #"2022-12-01"

app = Flask(__name__)
testVcap = os.getenv("VCAP_SERVICES","not setting")
logging.info(f"vcap = {testVcap}")

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
    
@app.route("/v2/vcap", method=["GET"])
def get_vcap():
    return testVcap
