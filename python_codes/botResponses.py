class BotResponse():
    def __init__(self, dictionary):
        self.dictionary = dictionary    #dictionary that holds user data
        print("BotResponse initialized")

    def getResponse(self, in_message: str) -> str:
        ##check if first character is !, if not, return None
        if in_message[0] != '!':
            return None
        
        message_strings = in_message.lower().split(' ')

        if message_strings[0] == '!help':
            return 'go fuck urself, nick'

        if (len(message_strings) < 2):
            return None
        
        elif message_strings[0] == '!birthday':
            return self.birthday_response(message_strings[1])    #!birthday nick
        
        elif message_strings[0] == "!dicksize":
            return self.dick_size_response(message_strings[1])   #!dicksize nick
        
        return None
        
    def birthday_response(self, in_name):
        for user in self.dictionary['users']:
            if user['name'] == in_name:
                return user['birthday']
        return "User not found"

    def dick_size_response(self, in_name):
        for user in self.dictionary['users']:
            if user['name'] == in_name:
                return user['dicksize']
        return "User not found"

