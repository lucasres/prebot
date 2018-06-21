from prebot import prebotFacade

class app():
    def __init__(self):
        """
        Construct of classe
        """
        self._prebot = prebotFacade()
        self._name = "BotName"

    def init(self):
        """
        Build a your init chatterbot
        :return:
        """
        pass


    def engine(self,userInput):
        """
        Build your engine conversation
        :param userInput: String
        :return: String
        """
        pass

    def command(self,pInput):
        """
        Execute command
        :param input: String
        :return:
        """
        if(pInput == "!sair"):
            exit(0)

    def conversation(self):
        """
        Call this method for start conversation
        :return:
        """
        while(True):
            userInput = input("User>")
            self.command(userInput)
            response = self.engine(userInput)
            print(self._name+">"+response)

bot = app()
bot.conversation()