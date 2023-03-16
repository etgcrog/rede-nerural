# Dicas para instalacao:
 ## Comando para ativar ambiente virutal no powershell:
    1. 
        $ Set-ExecutionPolicy Unrestricted -Scope Process
    2.  
        $ python3 -m venv venv
        $ source ./venv/Scripts/Activate.ps1
        $ pip install -r requeriments.txt 
 ## Instalacao:
    1. Versao 2.0.0-alpha
        $ pip install https://ms-release.obs.cn-north-4.myhuaweicloud.com/2.0.0a0/MindSpore/unified/aarch64/mindspore-2.0.0a0-cp37-cp37m-linux_aarch64.whl --trusted-host ms-    release.obs.cn-north-4.myhuaweicloud.com -i https://pypi.tuna.tsinghua.edu.cn/simple
    2. Versao 1.10:
        $ pip install mindspore
