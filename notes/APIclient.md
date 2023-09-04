This client based on Django testClient
can be used to :
+ make requests
+ check results
+ override authentication

# using the ApiClient
+ import `APIClient` from `rest_framework.test`
+ create client `client = APIClient()`
+ make request `resquest = clent.get('/greets/')`
+ check results using `assertEqual`  and similar 'assert' methods
