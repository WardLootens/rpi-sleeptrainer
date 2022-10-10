# rpi-sleeptrainer

## Web UI
### Start via
````
cd web
./run.sh
````

### Access via
````
http://<ip>:5000/index.html
````

### Install as service
sudo cp web/sleeptrainer-web.service /lib/systemd/system
sudo chmod 644 /lib/systemd/system/sleeptrainer-web.service
sudo systemctl daemon-reload
sudo systemctl enable sleeptrainer-web.service
sudo systemctl start sleeptrainer-web.service
sudo systemctl status sleeptrainer-web.service

## Standalone script

### Usage
````
./sleeptrainer.py [COLOR [LOW_LIGHT] ]
    COLOR       Either 'black', 'grey', 'red', 'orange', 'yellow',
                'green', 'blue' or 'white'.
                Defaults to 'white'.
    LOW_LIGHT   Either 'True' or 'False'. Defaults to 'True'.
````

### Schedule with crontab
````
45 6 * * * ~/Code/rpi-sleeptrainer/sleeptrainer.py orange
0  7 * * * ~/Code/rpi-sleeptrainer/sleeptrainer.py green
15 7 * * * ~/Code/rpi-sleeptrainer/sleeptrainer.py black
````

## Disable status leds
````
# led0 = status indicator, led1 = power indicator
echo 0 | sudo tee /sys/class/leds/led0/brightness > /dev/null
echo 0 | sudo tee /sys/class/leds/led1/brightness > /dev/null
