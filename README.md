# Brandon-API
An API used mainly by me and friends. 
The username/name and token determine which database the data is uploaded to. 

## SSL:
``Let's Encrypt`` Works SUPER welll, and is free. 

## Index:
1. [Temperature API](#Temperature)

All APIs can be accesed at http://api.brandon.net.za/
All APIs return JSON formats. 
# Documentation:
## <ins>/</ins>
### Parameters:
None
### Return:
Status, owner.

## <ins>/requests</ins>
### Parameters:
None
### Return:
Total requests made to API while online.

# Temperature
## <ins>/temp_upload</ins>
### Parameters:
|args|Value|
|----|-----|
|name| Name of user using the API|
|token| Token of that user, will also determine the database that will be used|
|probe_id| ID of the temperature probe being used|
|temp| Temperature value to be uploaded|

### Return:
Status value.
Possible outputs:
|Value|Reason|
|----|-----|
|200|ok|
|500|server error|
|404|no datasets found|
|400| incorrect token|

## <ins>/temp_collect</ins>
### Parameters:
|args|Value|
|----|-----|
|name| Name of user using the API|
|token| Token of that user, will also determine the database that will be used|
|probe_id| ID of the temperature probe being used|
|amount| Number of data points|

### Return:
Status value.
Possible outputs:
|Value|Reason|
|----|-----|
|200|ok|
|500|server error|
|404|no datasets found|
|400| incorrect token|

