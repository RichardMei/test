from suds.client import Client

url = 'http://localhost:8080/cstc-web/services/msettleTestFacade?wsdl' 
client = Client(url)
count = 0;
with open('filename','r') as f:
	for line in f:
		result = client.service.sendCommitTransJsonInfo(line)
		count = count + 1
		print ('success num:%d, response:%s' % (count, result)) 
