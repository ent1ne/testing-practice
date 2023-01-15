This was the test assignment I've done for a middle QA-manual position in a financial media holding.

TASK:

The task should be completed using Postman with NASA open API
https://api.nasa.gov/

You will need to find some Mars Rover Photos queries
1. Make a query with "Querying by Earth date" using 21.01.2022
2. Pass  the id of the second photo into Postman environment variable using JSON parsing

The solution should contain the query URL and the JS code for passing the variable

SOLUTION:

1. https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-01-21&api_key={{apiKey}}

Inside the Postman environment we create the variable apiKey that contains the API Key we recieve after 
registration on NASA API website. Recieved API Key should be passed into environment over the apiKey variable

2. 
var jsonData = JSON.parse(responseBody);
postman.setEnvironmentVariable("secondPhotoId", jsonData.photos[1].id)

In the body of GET query we find the list with all photos and pass the id of the second element from the list 
into the environment variable 
