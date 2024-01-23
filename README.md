### **Deploy a dash app with nginx/gunicorn over HTTS using docker**
####  1. Get a free Certificates
``` 
sudo certbot certonly --standalone -d example.com -d www.example.com
```
####  2. Clone This repo
```
git clone https://github.com/leberber/dash-ssl-gunicorn-docker.git
```
####  3. run the app
The below is going to run apps
```
docker-compose up --scale app=3 
```

