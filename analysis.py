# Analysis Example
# Post to HTTP Route

# This analysis simple post to an HTTP route. It's a starting example for you to develop more complex algorithms.
# In this example we get the Account name and print to the console.

from tago import Analysis
import requests

# The function myAnalysis will run when you execute your analysis
def myAnalysis(context,scope):
    # api-endpoint
    URL = "https://api.tago.io/info"
  
    # defining a headers dict for the headers to be sent to the API
    headers = {
      'Authorization': "Your-Account-Token"
    }

    request_get = requests.get(url = URL, headers = headers)

    data = request_get.json() 

    context.log(data)
    context.log("Your account name is: ", data['result']['name'])

# The analysis token in only necessary to run the analysis outside TagoIO
Analysis('MY-ANALYSIS-TOKEN-HERE').init(myAnalysis)
