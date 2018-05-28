import sys
text_list=[]                                                    

fo=open(sys.argv[1],"r", errors="ignore")						
textin=fo.read()
fo.close()                                                     

def func(text):                                                         
        string=""							
        for i in str(text):
                h=str(hex(ord(i)))[2::]				
                if len(h)==1:
                        h="0"+h
                string+=h
        count=0								
        string2=""							
        for j in str(string):
                count+=1						
                string2+=j
                if count%4==0:
                        string2+=" "					
        return string2

def replace_line(word):                                                 
        new_word=""
        for i in str(word):
                if i=="\n":
                        new_word+="."
                else:
                        new_word+=i
        return new_word

def line(val):                                                          
        return "0"*(7-len(str(val)))+str(val)+"0"


text=""
count=0
for i in str(textin):
        text+=i
        count+=1
        if count == 16:
                text_list.append(text)
                count=0
                text=""
else:
        text_list.append(text)
        text=""


for i in range(len(text_list)):
        print(line(i),func(text_list[i]),"\t"+str(replace_line(text_list[i])))   
