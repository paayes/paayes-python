from __future__ import absolute_import, division, print_function

import os

import paayes
from flask import Flask, request, redirect


paayes.api_key = os.environ.get("PAAYES_SECRET_KEY")
paayes.client_id = os.environ.get("PAAYES_CLIENT_ID")

app = Flask(__name__)


@app.route("/")
def index():
    return '<a href="/authorize">Connect with Paayes</a>'


@app.route("/authorize")
def authorize():
    url = paayes.OAuth.authorize_url(scope="read_only")
    return redirect(url)


@app.route("/oauth/callback")
def callback():
    code = request.args.get("code")
    try:
        resp = paayes.OAuth.token(grant_type="authorization_code", code=code)
    except paayes.oauth_error.OAuthError as e:
        return "Error: " + str(e)

    return """
<p>Success! Account <code>{paayes_user_id}</code> is connected.</p>
<p>Click <a href="/deauthorize?paayes_user_id={paayes_user_id}">here</a> to
disconnect the account.</p>
""".format(
        paayes_user_id=resp["paayes_user_id"]
    )


@app.route("/deauthorize")
def deauthorize():
    paayes_user_id = request.args.get("paayes_user_id")
    try:
        paayes.OAuth.deauthorize(paayes_user_id=paayes_user_id)
    except paayes.oauth_error.OAuthError as e:
        return "Error: " + str(e)

    return """
<p>Success! Account <code>{paayes_user_id}</code> is disconnected.</p>
<p>Click <a href="/">here</a> to restart the OAuth flow.</p>
""".format(
        paayes_user_id=paayes_user_id
    )


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
