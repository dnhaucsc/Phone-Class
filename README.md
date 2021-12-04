# Phone-Class

README

CLASS DESCRIPTION

    The Phone class attempts to replicate a phone by creating different phone objects. 
    Each object has a phone number, a battery, a voicemail, and a blocklist.
    The class itself keeps a list of all the current phone numbers.
    The object is allowed to change its number, voicemail, and blocklist as well as charge its battery; but with restrictions in place.

VARIABLE DESCRIPTIONS

    class var - numberList

        This is a list of all current phone numbers. The point of this list is to prevent 2 objects from sharing a phone number.

    obj var - __number

        This private variable is the phone number of the object.

    obj var - __voicemail

        This private variable is the voicemail string that is returned when another Phone object uses the call method on this one.

    obj var - __battery

        This private variable is the current battery percentage of the object

    obj var - __blocked

        This private variable is the current numbers that this object has blocked.

METHOD DESCRIPTIONS

    strip 
        - This method takes a string and removes all hyphens, parenthesis, and spaces. It is used to create a consistent format for phone numbers.
        - params: any string
        - return: a string with the parenthesis, hypens, and spaces removed.

    get_number
        - This method returns the phone number of an object in a user friendly way by describing what it is outputting with a string beforehand
        - return: A string "Phone Number: " followed by the phone number of the object

    get_raw_number
        -This method just only returns the phone number of the object
        - return: The phone number of the object

    change_number
        -This method will change the phone number of an object if and only if
         The phone number is valid(no letters or other special characters) and it is not already taken.
         It then updates the class variable numberList to reflect this change
        - param: the new phone number

    is_valid_number
        -This method tests to see if the raw phone number consists of only integers, making it valid
        -param: a string (the phone number)
        
    get_battery
        -This method gets the battery percentage of the object.
        - return: The string "Battery: " followed by the battery variable.

    get_raw_battery
        -this method returns just the numerical value of the battery
        - return: Just the numerical value of the battery
    
    charge_battery
        - This method charges your battery for an amount of time; at 1% every 2 minutes.
        - param: the time to charge
    
    set_voicemail
        - This method sets the voicemail of the object to a new voicemail
        - param: the new voicemail
    
    call
        - This method calls another phone object, returning the other objects voicemail
        or raising an error.

        - param: another phone object
        - return: the other objects voicemail

    block
        - This method blocks another phone object
        - param: another phone object

    unblock
        - This method unblocks a currently blocked object, or returns an error
        - param: another phone object.
    
    get_block_list
        - This returns the blocked contacts of the phone
        - return: a list of all blocked numbers

    __del__
        - when deleting a phone object, it sets all variables to None and removes the number from the phone list
        - param: the phone objet to delete.

DEMO PROGRAM DESCRIPTION
    The Phone class replicates a real phone using the number 123-456-7890.
    The sleep() function suspends the execution of the thread by the given seconds.
    Can use the get_battery and get_number to find out if the phone has 100% and expect the phone number to be 1234567890
    It can also set a different voicemail, call another phone and drain the battery, and block phones.

HOW TO RUN DEMO PROGRAM
    call the function by printing the functions and the user inputs the arguments to use the phone class.
