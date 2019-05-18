#!/bin/bash
ps -ef | grep python3 | cut -c 9-15| xargs kill -s 9
ps -ef | grep homebridge | cut -c 9-15| xargs kill -s 9
echo "Kill Complete"
python3 /home/pi/Scripts/GetFromArduino.py &
sleep 10
echo "GetFromArduino.py Started"
python3 /home/pi/AlarmSysLocal/manage.py runserver 0.0.0.0:8000 &
sleep 5
echo "Django Started"
DEBUG=* homebridge -D -P home/pi/plugin_test/homebridge-httpalarm/ -I &
sleep 30
echo "homebridge Started"
python3 /home/pi/Scripts/DataToServer.py &
sleep 5
echo "DataToServer.py Started"
python3 /home/pi/Scripts/SceneToServer.py &
sleep 30
echo "SceneToServer.py Started"
python3 /home/pi/Scripts/Scene.py &
echo "Scene.py Started"