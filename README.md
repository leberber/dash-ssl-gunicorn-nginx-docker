### **Deploy a dash app with nginx/gunicorn over HTTS using docker**
####  1. Get a free Certificates
``` 
sudo certbot certonly --standalone -d example.com -d www.example.com
```
####  2. Clone This repo
```
git clone https://github.com/leberber/dash-ssl-gunicorn-docker.git
```
####  3. Edits to `docker-compose` file
Please provide the correct path to the ssl key in the docker-compose file

####  3. Edits to `nginx.conf`
substitute the domain name with your domain name in the nginx.conf file 
####  5. run the app
The below is going to run 3 containers
```
docker-compose up --scale app=3 
```

