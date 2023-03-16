# Dicas para instalacao:
 ## Comando para ativar ambiente virutal no powershell:
    1. 
        $ Set-ExecutionPolicy Unrestricted -Scope Process
    2.  
        $ python3 -m venv venv
        $ source ./venv/Scripts/Activate.ps1
        $ pip install -r requeriments.txt 
        
    obs: Utilizei o python na versao 3.7.5, pois tive dificuldade com a lib na versao 3.11, 3.9
    [Python3.7.5 Download](https://www.python.org/downloads/release/python-375/)
 ## Instalacao:
    1. Versao 2.0.0-alpha
        $ pip install https://ms-release.obs.cn-north-4.myhuaweicloud.com/2.0.0a0/MindSpore/unified/aarch64/mindspore-2.0.0a0-cp37-cp37m-linux_aarch64.whl --trusted-host ms-    release.obs.cn-north-4.myhuaweicloud.com -i https://pypi.tuna.tsinghua.edu.cn/simple
    2. Versao 1.10:
        $ pip install mindspore
