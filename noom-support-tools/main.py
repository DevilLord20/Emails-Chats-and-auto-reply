from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get form data
        channel = request.form.get("channel")
        customer_name = request.form.get("customer_name")
        concern_type = request.form.get("concern_type")
        refund_amount = request.form.get("refund_amount")
        weight_months = request.form.get("weight_months")
        weight_price = request.form.get("weight_price")
        premium_months = request.form.get("premium_months")
        premium_price = request.form.get("premium_price")

        # Generate response based on the selected channel
        if channel == "Email":
            response = f"Hi {customer_name},\n\nThis is Saeed from Noom support. "
            response += "I'll be more than happy to assist you with "
        else:  # Chat
            response = ""

        if concern_type == "Refund":
            response += f"the refund that you're concerning about.\n\nWe'll miss working with you, "
            response += "but please know that we appreciate the opportunity to serve you. "
            response += f"I've cancelled your Noom subscription and issued a refund of ${refund_amount}. "
            response += "Please allow 2-5 business days to see the refund credited to your original payment method."

        elif concern_type == "Partial Refund":
            response += f"the refund that you're concerning about.\n\nI'm happy to let you know that "
            response += "I was able to find an exception to our policy for your specific scenario "
            response += f"so I cancelled your Noom subscription and issued a prorated refund of ${refund_amount}. "
            response += "Please allow 2-5 business days to see the refund credited to your original payment method."

        elif concern_type == "Billing/Clarifications":
            response += "your billing inquiry.\n\nAfter reviewing your account, I see that:\n"
            response += f"- {weight_months}-month Noom Weight subscription for ${weight_price}\n"
            response += f"- {premium_months}-month Noom Premium subscription for ${premium_price}\n\n"
            response += "Your subscriptions provide access to various features...\n\n"
            response += "You can access all account information through your Subscription Portal."

        elif concern_type == "Tech Issue":
            response += "your technical issue.\n\nWe're transferring your ticket to our Tech team. "
            response += "Please check your spam folder. Available 7 days/week 7:00 AM - 8:00 PM ET."

        elif concern_type == "Medications":
            response += "your inquiry.\n\nThis would be an excellent question for your Care Coordinators. "
            response += "While we can help with technical issues, we aren't able to assist with INSERT_CUSTOMER_REQUEST. "
            response += "Please contact your Care Coordinators through the app."

        if channel == "Email":
            response += "\n\nDon't hesitate to reach out if you need anything else!\n\nBest regards,\nSaeed\nNoom Support"

        return render_template("index.html", response=response)

    return render_template("index.html", response=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)