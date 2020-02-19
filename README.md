###### Installation

`chmod +x python-ssh.py`  
`python3 -m pip install -r requirements.txt`  
put py script in PATH  
  
**Requires at least python 3.6**  



###### AS IS
this task could be done as bash scripts, with finite number of sed and awk commands, but I feel that python is more maintanable 

to run directly from cloned repo:  
`python3 python-ssh.py test.yml server5 `  


###### TO DO
make config work from previously specified locationm, ex. home folder, to avoid specify it every time  
properly validate yaml file  
test connection to the servers in config file  
