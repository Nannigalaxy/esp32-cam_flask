[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Nannigalaxy/esp32-cam_flask/blob/master/LICENSE)  

# ESP32-cam Flask

A simple flask server for esp32-cam to upload captured image.   


## 1. Server Setup

### 1.1. Python package installation  
`$ pip install -r requirements.txt`

### 1.2. Nginx Server
In ubuntu:  
`$ sudo apt-get install nginx`

#### Setup:  
Create a file /etc/nginx/sites-available/esp32 and type the following:  

```
server {  
    location / {  
        proxy_pass http://127.0.0.1:8000;  
    }
}

```  
Create a symbolic link in the sites-enabled directory:  
`$ ln -s /etc/nginx/sites-available/esp32 /etc/nginx/sites-enabled/esp32`   

Restart nginx service:  
`$ sudo service nginx restart`   

### Run Server
`$ cd flask_app`  
`$ gunicorn run:app`

## 2. Client
The esp32-cam/client_image_post/client_image_post.ino sketch is based on project [ESP32-CAM-Arduino-IDE](https://github.com/RuiSantosdotme/ESP32-CAM-Arduino-IDE)  by Rui Santos.

### TODO
- [ ] Gallery UI to view uploaded images
