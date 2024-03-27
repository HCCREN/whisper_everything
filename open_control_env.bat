@echo off
cd /D D:\python\env\whisper_env\Scripts
call activate
cd /D D:\Github\whisper_everything
cmd.exe /K
set path = C:\Windows\System32\DriverStore\FileRepository\nvaci.inf_amd64_30e446a72214201b\nvidia-smi.exe
set path = C:\Users\e10929\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin\ffmpeg.exe
call nvidia-smi