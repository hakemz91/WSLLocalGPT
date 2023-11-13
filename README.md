# WSLLocalGPT

This is minor fork of localGPT focusing only installation in Windows WSL2 and some minor addition. If you can use WSL2 for installation then it is sane to do this because it is using full GPU and blazing fast, not like if you install in Windows native Anaconda which is although it uses full GPU, but it is really slow as slow as using CPU. So there is no point you install it using native Anaconda in Windows.


## Features

1. Easy to use with simple options.
2. Option to auto shutdown the PC after the ingestion is done. (useful for overnight bulk file ingestion) 
3. Simple logging of start time and finish time.

![Alt text](https://github.com/hakemz91/WSLLocalGPT/blob/main/intro_image_WSLLGPT.png)

## How to install

1. Git clone this repo to anywhere in your windows.

2. Go to the link at the end of this sentence and download the installer Anaconda3-2023.07-2-Linux-x86_64.sh file. I don't recommmend download the latest version since it using python3.11 and will have problem, unless you know how to install python3.11. So for the peace of mind just use link here: (https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Linux-x86_64.sh). You then place the Anaconda3-2023.07-2-Linux-x86_64.sh file into folder called "anaconda_installer" in the repo that you had clone before.

3. Enable the WSL for your Windows and use command the command below to update the wsl kernel to wsl2 (older wsl kernel might work and I am not tested it yet):

```
wsl --update
```

4. Install your Ubuntu distro from Microsoft Store and after that opened it and fill the username and password. After everything set up, close your wsl windows. Then get your Ubuntu distro name by using below command in normal cmd:

```
wsl --list
```

for example my distro id name is Ubuntu-18.04
Keep this for later instruction

5. Right click the launcher.bat and replace the distro id name to the one you used and saved it, for example in this case is Ubuntu-18.04

6. Lauch the launcher.bat file and it will automatically enter the for example Ubuntu-18.04

7. Now in the WSL windows, run the below command one at a time:

```
sudo apt update -y
sudo apt upgrade -y 
sudo apt install build-essential -y
cd anaconda_installer
bash Anaconda3-2023.07-2-Linux-x86_64.sh
```

Then you will need to press enter a lot in order to proceed downwards and need to accept yes for license term in order to install anaconda. If you just accidently skipped license term confirmation, just run the above command again to enter the installation windows. Then just type yes and enter, and enter again to proceed with installation. And after that it will ask "Do you wish the installer to initialize Anaconda3" so just type yes again and enter.

8. After anaconda is installed, close the wsl windows and then launch the launcher.bat again to enter it. It will now enter (base) anaconda environment. 

9. Now run the below command one at a time:

```
conda create -n WSLLocalGPT python=3.10.0 -y

python update_bashrc.py 

conda activate WSLLocalGPT

pip install -r requirements.txt

CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python==0.1.83 --no-cache-dir
```

10. Done install! Now just close the wsl windows and then lauch again the launcher.bat. Choose which option number you want and then type it and press enter. First run will take some time because of downloading the model. After finish the selected option processing, it will ask if you want to run another command. If you do, let say after ingestion you want to run the chatting, just answer y and press enter and it will ask you again the available option.

## How to customize the model and launch command

It is so easy. Just edit the model id and name in the constants.txt to the model that you want. But do not forget to replace the --model_type flag according to your model in bashrc file in wsl. Just use command (nano .bashrc) in your wsl. The default one is for mistral based model. If you want to use llama model for example, change to llama in the .bashrc file in run commands function at the end. Just change mistral to llama. That's it:

```
python run_localGPT.py --model_type llama
```

## How to reset the vector database

Just delete the db folder and reingesting back using option 3 or 4.

## Forked from awesome original LocalGPT
https://github.com/PromtEngineer/localGPT
