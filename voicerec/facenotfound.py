#if the fce is not recognised we have to set the file name through voice and collect datas
from speech2txt import speakcmd

s='hi'
speakcmd(s)
print(s)
#if (s=='Feel free to command'):
    #print('unrecognised face')
