### **Deploy a dash app with gunicorn over HTTS using docker**
####  1. Get a free Certificates
``` 
sudo certbot certonly --standalone -d example.com -d www.example.com
```
####  2. Clone This repo
```
git clone https://github.com/leberber/dash-ssl-gunicorn-docker.git
```
####  3. Build an image
```
docker build  -t my_dash_image .
```
####  4. Create a container
```
docker run -ti --name my_dash_container -p 443:443  -v /home/ubuntu/fullchain.pem:/fullchain.pem -v /home/ubuntu/privkey.pem:/privkey.pem my_dash_image
```
> Note:  The above will exec into the container. if you exit out of the container and want to exec back to it run 
```
docker exec -ti my_dash_container bash
```

####  4. Run Gunicorn 
```
gunicorn -b 0.0.0.0:443 app:server  --certfile=/fullchain.pem --keyfile=/privkey.pem
```
