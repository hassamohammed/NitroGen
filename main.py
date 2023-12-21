from Nitro import NitroGen

def main():
    print(""" $$\                                                                       
    $$ |                                                                      
    $$$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
    $$  __$$\  \____$$\ $$  _____|$$  _____| \____$$\ $$  _$$  _$$\ $$  __$$\ 
    $$ |  $$ | $$$$$$$ |\$$$$$$\  \$$$$$$\   $$$$$$$ |$$ / $$ / $$ |$$ /  $$ |
    $$ |  $$ |$$  __$$ | \____$$\  \____$$\ $$  __$$ |$$ | $$ | $$ |$$ |  $$ |
    $$ |  $$ |\$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$  |
    \__|  \__| \_______|\_______/ \_______/  \_______|\__| \__| \__| \______/ 
                                                            """)
    
    Num = int(input("How many codes to generate and check: "))
    Webhook = input("Webhook (Optional): ")
    Log = input("Log (y/n): ")

    if Log == "y":#Proabably a better way to do this
        Log = True
    else:
        Log = False

    Gen = NitroGen(Num, Webhook, Log)

    Gen.Generate()

if __name__ == '__main__':
    main()