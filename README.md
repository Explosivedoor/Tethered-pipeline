# Remote Tethered Shooting to Server Background Removal Pipeline
(This is a very niche project that probably only I will ever need but hey, its a project)
This project aims to create an automated workflow for photographers to streamline their image processing and publishing while shooting remotely. The pipeline will:

1. Automatically upload photos to a "local" server remotely
2. Process images to remove backgrounds on that server (or a connected computer)
3. Upload processed images to a public-facing website
4. Store the original photos for later

### Note: Remote computer/Server refers to the one at your 'home' and the local computer will refers to the computer with you. 


## What You Need to Do This Project
 

1. A camera with tethering capabilities
2. Some tethering software that can save the teather captures to a folder (Capture One, Sony's Tether app, etc.)
3. A storage server that can use SMB (for this project the server is running Truenas Scale) or a shared network drive. 
4. (Not required but helps speed) A computer that has a GPU. This can also be your sever if it is powerful enough.
5. Web server (this can also be the same server as your storage server). [not needed if you don't want to show the pictures]
6. A VPN, for this project I am using tailscale as it is very simple to use. This is used to have access to your storage server remotely. 


## Sever Setup for SMB
First you will need to setup an SMB on your server of choice, or share a drive on your remote powerful computer/server. If it is an SMB on a different machine than your powerful one, you will need to map the SMB as a network drive on both your remote and "local" computer. If it is a shared network drive, you will need to map it on your local computer. 

Once you run the python program it will ask you for you root directory. You will enter the drive and whatever folder it is in, if any. For example ```Z:``` or ```Z:/app```
## VPN Setup
VPN setup is pretty straight forward. You just need to install tailscale on your local computer and on the remote computer (and sign-in).
Next you will need to setup the remote computer to be an [exit node](https://tailscale.com/kb/1103/exit-nodes?q=exit) and to allow for [subnet routing](https://tailscale.com/kb/1019/subnets?q=subnets). 

## Background Removal Process
First run the python program on your remote computer. This will create the needed directories when you enter your root directory (eg. your mapped network drive or your shared drive). 
Then, you will setup your tether program on your local computer to save the files to the mapped network drive in the Process folder.
Now just take a photo and watch it work! 
## Python Scripts 

