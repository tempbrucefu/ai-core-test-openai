from flask import Flask, request, jsonify
import openai
import os

openai.api_type = "azure"
openai.api_version = "2023-05-15" #"2022-12-01"

app = Flask(__name__)

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
        testVcap = os.getenv("VCAP_SERVICES","not setting")
        try:
            import json
            print(f"vcap = {testVcap}")
            testVcap2Obj = json.loads(str(testVcap))
            print(f"vcap = {testVcap2Obj}")
        except Exception as e:
            print(f"vcap error {e}")
        return jsonify({"VCAP_SERVICES": str(testVcap2Obj)})
    except Exception as e:
        return jsonify({"error": str(e)})
