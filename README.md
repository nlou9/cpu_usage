# CPU Usage
This project is to build a web server which provides CPU usage of the hosting server and a web client which displays server CPU usage information. 

## Author
Na Lou

## Tech
React, Django REST framework

## License 
MIT

## Run the project locally
git clone project and go to the project root dir

1. Run web server
   requirement: python3
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
   
