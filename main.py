morse_code={'a':'._','b':'_...','c':"_._.",'d':'_..','e':'.','f':'.._.',
            'g':'__.','h':'....','i':"..",'j':'.___','k':'_._','l':'._..',
            'k':'_._','l':'._..','m':'__','n':'_.','o':'___','p':'.__.','q':'__._','r':'._.','s':'...',
            't':'_','u':'.._','v':'..._','w':'.__','x':'_.._','z':'__..',' ':' ',
            '1':'.____','2':'..___','3':'...__','4':'...._','5':'.....','6':'_....','7':'__...',
            '8':'___..','9':'____.','0':'_____'}


#BOTH ENCODE AND DECODE
def gen(words):
    morse=[]
    for l in words:
        if l in morse_code:
            morse.append(morse_code[l])
        # else:
        #     morse.append(l)
    return (" ".join(morse))

def degen(words):
    demo=[]
    for i in words:
        for k,v in morse_code.items():
            if v==i:
                demo.append(k)
            
    return (" ".join(demo))


def main():
    print("Morse Code Generator!")
    isT=True
    while isT:
        chosse=input("To Generate(g) or Decode(d):").lower()
        if chosse=='g':
            text=input('''Enter text:''').lower()
            print(f"Here is the Morse Code:\n{gen(text)}")
        elif chosse=='d':
            text=input('''Enter text:''').lower()
            print(f"Here is the Decode Morse code:\n{degen(text.split(' '))}")
        else:
            print("Operation Not availabel")
        
        do_you=input("Do you want to use Morse Code Convert Again?y/n:").lower()
        if do_you=='n':
            isT=False

if __name__=='__main__':
    main()
    