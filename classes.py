class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
       '''Function for setting default variable values
        during module initialization
        '''
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self):
        '''Function for turning the television on and off'''
        self.__status = not(self.__status)            


    def channel_up(self):
        '''Function for increasing the channel of television'''
        if self.__status:
            self.__channel = (self.__channel + 1)%(Television.MAX_CHANNEL +1)


    def channel_down(self):
       '''Function for decreasing the channel of televsion'''
        if self.__status:
            self.__channel = (self.__channel - 1)%(Television.MAX_CHANNEL +1)
     

    def volume_up(self):
       '''Function for increasing the volume of television'''
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1
      

    def volume_down(self):
        '''Function for decreasing the volume of television'''
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1
  

    def __str__(self):
       '''Function to return formatted string displaying television status
       whenever printed'''
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        
