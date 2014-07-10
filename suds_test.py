# This script tests that the SUDS module for Python
# is installed and working it sends the two values 
# to the web service which sums them and returns the result

from suds.client import Client
client = Client('http://ladonize.org/python-demos/Calculator/soap/description')
 
# Calculate 34+56
result = client.service.add(34,56)
print result