#################### Import test_invoke_http.py ##################################################
from invokes import invoke_http


#################### NearyBy Complex MS Testing ##################################################

#invoke ... microservice to ...
body = {"cust_location":"30 Sembawang Dr, Singapore 757713"}
results = invoke_http("http://localhost:5100/near_by",method="POST",json=body)

#################### Place an Order Complex MS Testing #############################################

# have not yet added @jolene, klarice if needed!


#################### Cancel an Order Complex MS Testing #############################################

# have not yet added @jx, amanda if needed!
results = invoke_http("http://localhost:5500/cancel_order/2",method="POST")


#################### Printing out results created ##################################################

print(type(results))
print()
print(results)