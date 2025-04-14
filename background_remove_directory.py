
from rembg import remove, new_session
from PIL import Image
import time
import glob
import shutil
from pathlib import Path
import time 
import os 
#check if folder is there, if not makes it 
#root_path = 'Z:'
root_path = input()

dir= os.path.isdir(f"{root_path}/Process")
dir2= os.path.isdir(f"{root_path}/Process/Background")
dir3= os.path.isdir(f"{root_path}/Process/Processed")

if dir == False:
    os.makedirs(f"{root_path}/Process")

if dir2 == False:
    os.makedirs(f"{root_path}/Process/Background") 
if dir2 == False:
    os.makedirs(f"{root_path}/Process/Processed")

files = glob.glob(f'{root_path}/Process/*.jpg')

#rembg settings, to use tensor and CUDA they must be installed or it will default to CPU 
providers = ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
#if model isn't installed, it should be downloaded when you run for the first time. some to try 'u2net','isnet-general-use','birefnet-dis'
model_name='isnet-general-use'

session = new_session(model_name, providers=providers, gpu=True)

def process():
    for i in files:
            input = i.strip().replace('"', '')
            input_path = input 
            path = Path(input)
            filename = Path(path).name
            path = path.parent

            filename2 = filename.split('.')[0]
            output_path = f"{root_path}/Process/Background/" + filename2 + "_removed.png"  
        
            input_image = Image.open(input_path)
        
        # process the image and time it
            start_time = time.time()
            output_image = remove(input_image, session=session)
            end_time = time.time()
            
            # save the output image
            output_image.save(output_path)
            
            input_image.close()
            shutil.move(i,f"{root_path}/Process/Processed/"+filename)
            print(f"Processing time: {end_time - start_time:.2f} seconds")
            

#checks for new files
while True:
    files_new = glob.glob(f'{root_path}/Process/*.jpg')
     
    if files_new == []:
          print ("No new files")
          time.sleep (60)
    else:
        print("New files added")
        files = glob.glob(f'{root_path}/Process/*.jpg')  
        process()