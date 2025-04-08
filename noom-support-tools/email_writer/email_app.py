from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        concern_type = request.form.get("concern_type")
        refund_amount = request.form.get("refund_amount")

        # Generate response
        response = f"Hi {customer_name},\n\nThis is Saeed from Noom support. "
        response += f"I'll be more than happy to assist you with {concern_type}.\n"
        response += f"Refund Amount: ${refund_amount}\n\nBest regards,\nSaeed\nNoom Support"

        return render_template("index.html", response=response)

    return render_template("index.html", response=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)