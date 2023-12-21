import string,random,requests,threading
from time import sleep
from discord_webhook import DiscordWebhook

class NitroGen:
    def __init__(self, Numcodes, webhook = None, Log = False):
        self.FileName = "NitroCodes.txt"
        self.Numcodes = Numcodes
        self.webhook = webhook
        self.Log = Log #Slows down due to calls
        self.Checked = 0

    def RandomCode(self):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for i in range(16))


    def NitroGift(self):
        Code = self.RandomCode()
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{Code}?with_application=false&with_subscription_plan=true"

        response = requests.get(url)
        if response.status_code == 200:

            if self.Log:
                print(f"Valid | {Code} \n")

            #Send Valid Nitro to Webhook
            if self.webhook != None:
                DiscordWebhook(
                    url=self.webhook,
                    content=f"Valid Nitro Code: {Code}"
                ).execute()

            #Write Valid Nitro to File
            with open(self.FileName, "w") as file:
                file.write(Code)

            return Code
        
        if self.Log:
            print(f"Invalid | {Code} \n")

        return None

    def Generate(self):
        #global rate limit of 50 requests per second
        #However its probably using a different ratelimit which needs to be found out
        while self.Checked < self.Numcodes:
            for i in range(50):
                threading.Thread(target=self.NitroGift).start()

                self.Checked += 1
                if self.Checked == self.Numcodes:
                    break
            sleep(1)