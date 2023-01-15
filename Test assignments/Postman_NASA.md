# Postman meets NASA  

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://scontent.ffru8-1.fna.fbcdn.net/v/t1.6435-9/102279727_3549640171717361_7718063278953332736_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=973b4a&_nc_ohc=a9XVQekx0AoAX-eGpNa&_nc_ht=scontent.ffru8-1.fna&oh=00_AfC_7rWdY92t36wm7LB4rRD2Q6CT19XFQYA2j4lcvAe-nw&oe=63EB6A30">
 <source media="(prefers-color-scheme: light)" srcset="https://scontent.ffru8-1.fna.fbcdn.net/v/t1.6435-9/102279727_3549640171717361_7718063278953332736_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=973b4a&_nc_ohc=a9XVQekx0AoAX-eGpNa&_nc_ht=scontent.ffru8-1.fna&oh=00_AfC_7rWdY92t36wm7LB4rRD2Q6CT19XFQYA2j4lcvAe-nw&oe=63EB6A30">
 <img alt="How it could have turned out" src="https://scontent.ffru8-1.fna.fbcdn.net/v/t1.6435-9/102279727_3549640171717361_7718063278953332736_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=973b4a&_nc_ohc=a9XVQekx0AoAX-eGpNa&_nc_ht=scontent.ffru8-1.fna&oh=00_AfC_7rWdY92t36wm7LB4rRD2Q6CT19XFQYA2j4lcvAe-nw&oe=63EB6A30">
</picture>

#### This was the test assignment I've done for a middle manual QA position in a financial media holding  
#### You can check the task and try to solve it by yourself or go straight to the answer

<details><summary>TASK</summary>
<p>

The task should be completed using Postman with NASA open API  

https://api.nasa.gov/

You will need to find some Mars Rover Photos queries:  
 
1. Make a query with «Querying by Earth date» using 21.01.2022
2. Pass  the id of the second photo into Postman environment variable using JSON parsing

The solution should contain the query URL and the JS code for passing the variable

</p>
</details>

<details><summary>SOLUTION</summary>
<p>

1. Inside the Postman environment we create the variable apiKey that contains the API Key we recieve after 
registration on NASA API website. Recieved API Key should be passed into environment over the apiKey variable  
 
```
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-01-21&api_key={{apiKey}}
```
 
2. In the body of GET query we find the list with all photos and pass the id of the second element from the list 
into the environment variable  
 
 ```
  var jsonData = JSON.parse(responseBody);
  postman.setEnvironmentVariable("secondPhotoId", jsonData.photos[1].id)
  ```

</p>
</details>
