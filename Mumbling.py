'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

'''

def accum(s):
    #define as variaveis para trabalhar nos loops
    str_output=[]
    iCount = 0
    for iStr in s: # loop para cada caracter na string s
        if iStr.isupper()==False: #se o caracter não for maiusculo
            if iCount==0: # se for o primeiro caracter
                str_output.append(iStr.capitalize()) #faz um append na string de saida com o caracter em maiusculo
                iCount+=1 # mais um no iterator
            else:
                str_output.append((iStr.capitalize())+(iStr*(iCount))) #se não for o 1° caracter, faz um appenda na string do 1° em maiusculo mais iCount vezes o caracter
                iCount+=1 # aumentar o interator
        else: #se o primeiro caracter for maiusculo
            if iCount==0: #se for o primeiro caracter da string
                str_output.append(iStr) #append o caracter na saida
                iCount+=1 #mais um no iterator
            else: #não é o primeiro caracter
                str_output.append(iStr+(iStr.lower())*iCount) #coloca o primeiro caracter mais iCount vezes o caracter minúsculo
                iCount+=1 # aumenta o iterator
    str_FinalOutput = "-".join(str_output)  #junta a saida
    return str_FinalOutput #retorna a string final
    
    #could just be
    #def accum(s):
    #    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
