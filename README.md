# VR_Pupper_Control
Code Package to remotely control the Stanford Pupper with Virtual Reality.

To stream the camera feed to the View-Master via the Raspberry Pi's local IP Address, run rpi_camera_streaming.py which is based on what http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming did for surveillance. Follow this link format: http:{your_pi's_ip_address}:8000.

Once the VRduino is connected to the Pupper's Raspberry Pi and the robot has performed its default boot up, run karel-pupper-api/StanfordQuadroped/programs/imu_data.py to sync head movement on the View-Master to the Pupper. We use the Karel Pupper API to abstract some control functionality of the robot - take a look over here: https://github.com/stanfordroboticsclub/karel-pupper-api.

The file final_report is a PDF document explaining this project in detail. A video presentation of this project is available of this google drive link and shows a demo of the working project: https://drive.google.com/file/d/19U1zkn7KY0-_x2a-4Ght_FK0hOb5PoSE/view?usp=sharing.

