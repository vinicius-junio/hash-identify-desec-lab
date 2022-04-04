import os
import hashlib
import base64

class Discover:
    #
    # Read Wordlist
    #
    def __init__(self,file: str):
        with open(file, 'r',encoding='utf-8') as f:
            self.words = f.read().splitlines()

class HashConvert:
    #
    # Hash Convert
    #
    def __init__(self, hash: str):
        self.hash = hash.encode('utf-8')

    def __str__(self):
        return str(self.hash)

    def md5_hash(self):
        return hashlib.md5(self.hash).hexdigest().encode()

    def base_64(self, _md5):
        return base64.b64encode(_md5)      

    def sha1(self,_b64):
        return hashlib.sha1(_b64).hexdigest()
    
def main():
    _HASH = "806825f0827b628e81620f0d83922fb2c52c7136"

    directory = os.path.dirname(__file__)
    path = os.path.join(directory, "wordlist", "john_list.txt")
    discover = Discover(path)
    
    for wordlist in discover.words:
        _hash = HashConvert(wordlist)
        _md5 = _hash.md5_hash()
        _b64 = _hash.base_64(_md5)
        _sha1 = _hash.sha1(_b64)
        if(_HASH == _sha1):
            print(wordlist)
            
if __name__ == '__main__':
    main()
