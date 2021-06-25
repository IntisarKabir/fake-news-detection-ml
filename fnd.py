








def remove_noise_from_string(str):
    noise=['\u200c','\u200d','\xa0','\n','\r','\t','\b','\f' , '^',  '~' ]
    ttc=[]
    for ch in str:
        if(ch not in noise):
            ttc+=ch
    return "".join(ttc)






def format_string(str):
    v=str.replace("??", " ? ").replace("।।", " | ").replace("॥", " | ").replace("!!", " ! ").replace("||", " ")
    v=v.replace("…", " ").replace("-", " - ").replace("/", " / ").replace(",", " ")   
    v=v.replace("?", " ? ").replace("'", "_ ").replace("'", " _").replace("/", " ")
    v=v.replace("#", " # ").replace("@", " @ ").replace("$", "$ ").replace("*", " * ").replace("&", " & ")
    v=v.replace("+", " + ").replace("=", " = ").replace("{", "___ ").replace("}", " ___").replace("[", "___ ").replace("]", " ___")
    v=v.replace("(", " ___ ").replace(")", " ___ ")
    v=v.replace(":", " : ") #.replace("য়", "y")  #য়
    v=v.replace("!", " ! ").replace("|", " । ").replace("।", " | ")
    v=v.replace("‘", "_ ").replace("’", " _").replace('“',"__ ").replace('”'," __").replace("`", "_").replace('"', "__ ").replace('"' , " __")
    v=v.split("!|?")
    v=" ".join(v).strip()
    return ' '+v



























































