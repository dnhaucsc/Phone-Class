# Dustin Ha
# Assignment 10.1: Your Own Class
# Acknowledgements: Hari's Lecture Video and Notes and Textbook
# Time module: https://docs.python.org/3/library/time.html#time.sleep
# The purpose of this assignment is to implement our own class based on a real-world object


from time import sleep

class Phone:

    numberList = []

    def __init__(self, number):
        # uses the strip method defined below to create consistent formatting of phone numbers.
        self.__number = Phone.strip(number)

        # If the number is already in the class variable of number lists; raise an error.
        if self.__number in Phone.numberList:
            raise ValueError('{} is already being used as a number!'.format(self.__number))
        
        # tests if our number is valid using the is_valid_number defined below
        Phone.is_valid_number(self.__number)

        # add this phone number to the number list.
        Phone.numberList.append(self.__number)

        # set the battery to 100; the voicemail to the default voicemail; and the phone's blocked list to an empty list.
        self.__battery = 100
        self.__voicemail = "Your call has been forwarded to the voicemail for {}. No one is available to take your call. At the tone, please record your message. When you've finished recording, you may hang up or press the # key for more options.".format(self.get_number())
        self.__blocked = []


    # this takes in a string, and replcaes all hypdens, parenthesis, and spaces with nothing. Essentially, stripping a phone number to just the numbers.
    def strip(string):
        return string.replace('-','').replace('(','').replace(')','').replace(' ','')

    # gets your number
    def get_number(self):
        return 'Phone Number: {}'.format(self.__number)

    # gets ONLY the phone number without the string text before it.
    def get_raw_number(self):
        return self.__number

    # Changes the phone number
    def change_number(self, newNumber):
        # first, strips the user input.
        newNumber = Phone.strip(newNumber)
        # then, tests of the stripped input is a valid phone number.
        Phone.is_valid_number(newNumber)

        # if the new number is the same, raise an error
        if newNumber == self.__number:
            raise ValueError('{} is already the number for this phone'.format(newNumber))

        # if the new number is an already existing number, raise an error,
        elif newNumber in Phone.numberList:
            raise ValueError('{} is currently being used by another phone'.format(newNumber))

        # remove the current number from the list
        Phone.numberList.remove(self.__number)
        # set the current number to the new number
        self.__number = newNumber
        # add it to the list
        Phone.numberList.append(self.__number)

    # tests if a number consists of only integers. If not; raises an error.
    def is_valid_number(number):
        for i in number:
            try:
                int(i)
            except:
                raise ValueError('{} is not a valid phone number'.format(number))

    # Returns the battery precentage of the phone
    def get_battery(self):
        return 'Battery: {}%'.format(self.__battery)

    # returns only the numerical value of the battery.
    def get_raw_battery(self):
        return self.__battery

    # charges the battery at a rate of 1% per 2 minutes.
    def charge_battery(self, time):
        # If the time charged is negative, return an error
        if time < 0:
            raise ValueError('Cannot charge for a negative amount of minutes')
        self.__battery += time * 0.5
        # If the battery goes above 100; set it to 100.
        if self.__battery >= 100:
            print("Battery Full")
            self.__battery = 100

    # sets the new voicemail for the phone object.
    def set_voicemail(self, newVoicemail):
        self.__voicemail = newVoicemail

    # calls another phone.
    def call(self, other):
        # if the battery is dead; raise and error
        if self.__battery == 0:
            raise KeyError('Cannot call. phone is dead')

        # if the other phones battery is dead, raise an error
        elif other.get_raw_battery() == 0:
            raise RuntimeError('Attempted to call a dead phone')

        # or if the other phone is blocked, raise an error
        elif other.get_raw_number() in self.__blocked:
            raise ValueError('{} is blocked'.format(other.get_raw_number()))

        # or if the other phone has blocked the caller
        elif self.get_raw_number() in other.get_block_list():
            raise ValueError('Could not call {}'.format(other.get_raw_number()))

        # otherwise, drain the battery by 5% and return the voicemail of the other phone ( no one picks up your calls D: )
        else:
            self.__battery -= 5
            # after the battery is drained 5%, if it is below 0: set the battery to 0 and print a message stating that the phone is dead.
            if self.__battery < 0:
                self.__battery = 0
                print('This phone is now dead. Please charge it to continue using')
            return other.__voicemail

    # add a number to your blocked list.
    def block(self, other):
        self.__blocked.append(other.get_raw_number())

    # unblock a number
    def unblock(self, other):
        try: 
            self.__blocked.remove(other.get_raw_number())
        #unless it is not in the phones blocked list; then raise an error.
        except:
            raise ValueError('{} not in blocked list'.format(other.get_raw_number()))

    # returns the blocked list of the phone
    def get_block_list(self):
        return self.__blocked

    # deletes a phone object.
    def __del__(self):
        Phone.numberList.remove(self.__number)
        self.__number, self.__battery, self.__voicemail, self.__blocked = None, None, None, None

if __name__ == '__main__':
    while(True):
        command = input("Welome to the Phone class! To access the demo; please input 'demo'. To exit and just mess around with the code, please type in 'exit': ")
        if command.lower() == 'demo':
            print('\nThe Phone class attempts to replicate a real phone. So; let\'s create a new phone named "testPhone" with a phone number of "123-456-7890" using this code:\ntestPhone = Phone("123-456-7890")\n')
            testPhone = Phone("1234567890")
            sleep(10)
            print("With just the phone by itself, you can find out it's phone number; get the battery percentage; set it's voicemail and charge it's battery.")
            sleep(10)
            print("\nSo, since this is a new phone, we should expect it's battery to be at 100%, and we should expect our phone number to be 1234567890.")
            sleep(10)
            print("\nLets use the get_battery() and get_number() functions on our object to see if it works")

            print(testPhone.get_battery())

            print(testPhone.get_number())

            sleep(7)

            print("\nI want to change the voicemail to: 'Hey! I couldn't take your call, please call back!'. To do so I will type in:\ntestPhone.set_voicemail('Hey! I couldn't take your call, please call back!')")
            testPhone.set_voicemail("Hey! I couldn't take your call, please call back!")

            sleep(7)
            print('\nSo, we can see that those functions work. We will get back to the voicemail later. If we tried to charge the phone, nothing would happen since we are already at 100%. However, this is pretty much all you can do with a phone by itself.')

            sleep(10)

            print("\nBut, with another phone, we open our doors a little. Lets create another phone object named otherPhone with a phone number of 408-123-4567")

            otherPhone = Phone("4081234567")

            sleep(10)

            print("\nThen, we can actually call this phone. When we call another phone, it will return to us that other phone's voicemail. It will also drain your battery by 5%")

            sleep (10)

            print("\nSo lets call the testPhone by running otherPhone.call(testPhone). We have already set testPhone's voicemail earilier, so we should expect to see it here")

            sleep(5)

            print(otherPhone.call(testPhone))
            sleep(5)

            print("\nFinally, you can block and unblock numbers. I will block otherPhone, and to do so I will run testPhone.block(otherPhone)")

            sleep(7)

            print("\nIf I were to call otherPhone now, it would give an error.")

            sleep(5)

            print("\n And that's it! Thank you for viewing the demo!")

            del(testPhone)
            del(otherPhone)

        elif command.lower() == 'exit':
            break
        else:
            print("I'm sorry, I don't understand that command")