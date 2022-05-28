# VR_Pupper_Control
Code Package to remotely control the Stanford Pupper with Virtual Reality

To stream the camera feed to the viewmaster via the Pi's local IP Address, run rpi_camera_streaming.py which is based on what http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming did for surveilance. 

Once the VRduino is connected to the pi and the robot has done its default boot up, run karel-pupper-api/StanfordQuadroped/programs/imu_data.py to sync head movement on the viewmaster to the pupper. We use the Karel Pupper API to abstract some control functionality of the robot - take a look over here: https://github.com/stanfordroboticsclub/karel-pupper-api.
