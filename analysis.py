"""
Analysis Example
Post to HTTP Route

This analysis simple post to an HTTP route. It's a starting example for you to develop more
complex algorithms.
In this example we get the Account name and print to the console.
"""
import urllib.request

from tagoio_sdk import Analysis


def my_analysis(context, scope: list = None) -> dict:
    account_token = next(
        (item for item in context.environment if item["key"] == "account_token"), None
    )

    if not account_token:
        raise ValueError("Missing 'account_token' in the environment variables")

    url = "https://api.tago.io/info"
    headers = {
        "Authorization": account_token["value"],
    }
    # How to use HTTP QueryString
    # url += "?serie=123"
    #
    # How to send a HTTP Body:
    # data = b'My text body'

    req = urllib.request.Request(url, headers=headers, method="GET")

    try:
        with urllib.request.urlopen(req) as response:
            result = response.read().decode("utf-8")
            print(result)
    except Exception as error:
        print(f"{error}")


# The analysis token in only necessary to run the analysis outside TagoIO
Analysis(params={"token": "MY-ANALYSIS-TOKEN-HERE"}).init(my_analysis)
