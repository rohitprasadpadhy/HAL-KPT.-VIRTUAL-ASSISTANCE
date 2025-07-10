from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# ✅ Load intents.json using UTF-8 to fix UnicodeDecodeError
with open("intents.json", encoding="utf-8") as file:
    intents = json.load(file)

# ✅ Chatbot response logic
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                if isinstance(intent["responses"], list):
                    # Show all steps or lines together
                    return "<br>".join(intent["responses"])
                else:
                    return intent["responses"]
    return "❓ Sorry, I didn't understand that. Try asking something else."

# ✅ Route to render HTML page
@app.route("/")
def index():
    return render_template("chat.html")

# ✅ API route to get chatbot response
@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_response(user_input)
    return jsonify({"response": response})

# ✅ Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
