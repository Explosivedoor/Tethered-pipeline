# Remote Tethered Shooting to Server Background Removal Pipeline
(This is a very niche project that probably only I will ever need but hey, its a project)
This project aims to create an automated workflow for photographers to streamline their image processing and publishing while shooting remotely. The pipeline will:

1.Automatically upload photos to a "local" server remotely
2.Process images to remove backgrounds on that server (or a connected pc)
3.Upload processed images to a public-facing website
4.Store the original photos for later



#What You Need to Do This Project
 

1. A camera with tethering capabilities
2. Some tethering software that can save the teather captures to a folder (Capture One, Sony's Tether app, etc.)
3. A storage server that can use SMB (for this project the server is running Truenas Scale)
4. (Not required but helps speed) A computer that has a GPU. This can also be your sever if it is powerful enough.
5. Web server (this can also be the same server as your storage server).
6. A VPN, for this project I am using tailscale as it is very simple to use. This is used to 


#Sever Setup for SMB
#VPN Setup
#Background Removal Process
#Python Scripts 

