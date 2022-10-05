from dadata import Dadata


token = "9b23dbd41e5f143094a94ff6d1ae204b7e702fae"
secret = "a380afa548e2b3c9ce3e4a23fddbba02ccaaf337"
dadata = Dadata(token, secret)
print(dadata.clean("passport", "4509 235857"))