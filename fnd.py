








def remove_noise_from_string(str):
    noise=['\u200c','\u200d','\xa0','\n','\r','\t','\b','\f' , '^',  '~' ]
    ttc=[]
    for ch in str:
        if(ch not in noise):
            ttc+=ch
    return "".join(ttc)








