# CPU Usage
This project is to build a web server which provides CPU usage of the hosting server and a web client which displays server CPU usage information. 

## Author
Na Lou

## Tech
React, Django REST framework

## License 
MIT

## Demo
https://drive.google.com/file/d/1dhxJI0eXxQNsRG8YAoy3lyBMvQ4139QV/view?usp=sharing

## Run the project locally
git clone project and go to the project root dir

1. Run web server
   requirement: python3, Linux
   - create a virtual env and activate it 
   - pip install -r requirements.txt
   - run web server: 
     python manage.py makemigrations
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py runserver 
     server would run by default on http://127.0.0.1:8000/
     
2. REST API Usage:  
   REQUEST: 
   - get cpu usage data by server id    
     http://127.0.0.1:8000/cpu/<server_id>      
     e.g. http://127.0.0.1:8000/cpu/1   
   - get cpu usage data by server id and timestamp range   
     http://127.0.0.1:8000/cpu/<server_id>/<start_timestamp>/<end_timestamp>   
     e.g. http://127.0.0.1:8000/cpu/1/2021-11-22T00:10:46.771147Z/2021-11-22T00:11:46.826599Z  
  
3. Run web client:
   - npm install
   - npm build
   - yarn start 
   - check http://localhost:3000
   
   The chart would show last 10 mins cpu usage (system usage + user usage)
   
 ## Run test
 python manage.py test
 
 ## Screenshots
 ### RESTAPI
 #### get data with server_id
 <img width="1251" alt="3" src="https://user-images.githubusercontent.com/39046184/142806448-af7d2178-b9f7-4842-bb3e-427b4b327e70.png">
 
 #### get data with server_id and timestamp range
 <img width="1251" alt="2" src="https://user-images.githubusercontent.com/39046184/142806626-5f50d271-5990-4022-b2fc-4a41f2bb3004.png">
 
 #### client 
  <img width="1251" alt="1" src="https://user-images.githubusercontent.com/39046184/142806909-6f7137b1-999a-4db9-8752-7291b0c054c9.png">

## Extend in the future
Migrage to Mongodb. Mongbo is a better candidate in this scenario considering data structure and scalability. Django has libraby "Django" which is consistent with Django ORM. For this project, because by default django use SQLite and it is not necessary to preinstall and setup, it would be easier to run this project locally here. 

 


   
