#This Requires Python 3.10 or higher



def handle_command(self, message):
    match message:
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(ident, red, green, blue)
        case _:
            raise InvalidCommand(message)

"""Examples of messages that would be handled by the above code:

command1=['LED', 4, 255, 0, 0]
command2=[ 'BEEPER', 440, 3]

"""
   
