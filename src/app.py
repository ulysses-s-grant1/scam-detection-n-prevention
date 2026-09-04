import os

from flask import Flask, render_template, request
from analyzer import analyze_message
from explainer import calculate_risk_level, explain_results

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form.get("message", "").strip()

        if not user_message:
            return render_template(
                "index.html",
                error="Please enter a message to analyze.",
            ), 400

        results = analyze_message(user_message)
        risk = calculate_risk_level(results)
        explanations = explain_results(results)

        return render_template(
            "index.html",
            risk_level=risk["level"],
            explanation=" ".join(explanations),
            message=user_message,
        )

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")