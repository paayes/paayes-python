from __future__ import absolute_import, division, print_function

import os

import paayes
from flask import Flask, request


paayes.api_key = os.environ.get("PAAYES_SECRET_KEY")
webhook_secret = os.environ.get("WEBHOOK_SECRET")

app = Flask(__name__)


@app.route("/webhooks", methods=["POST"])
def webhooks():
    payload = request.data.decode("utf-8")
    received_sig = request.headers.get("Paayes-Signature", None)

    try:
        event = paayes.Webhook.construct_event(
            payload, received_sig, webhook_secret
        )
    except ValueError:
        print("Error while decoding event!")
        return "Bad payload", 400
    except paayes.error.SignatureVerificationError:
        print("Invalid signature!")
        return "Bad signature", 400

    print(
        "Received event: id={id}, type={type}".format(
            id=event.id, type=event.type
        )
    )

    return "", 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
