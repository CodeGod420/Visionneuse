import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class DCMotor():

    """ This class provides an easy use for L293D's DC motor controlled. """

    # for us, declaration of instance variables
    PWMpin: int
    IN1pin: int
    IN2pin: int
    BTNpin: int

    def __init__(self, PWMpin: int, IN1pin: int, IN2pin: int, BTNpin:int) -> None:
        self.PWMpin = PWMpin
        self.IN1pin = IN1pin
        self.IN2pin = IN2pin
        self.BTNpin = BTNpin

        self.initGPIO()


    def initGPIO(self) -> None:
        """ Set up the GPIO of the raspberry pi """

        # setup outputs
        GPIO.setup(self.PWMpin, GPIO.OUT)
        GPIO.setup(self.IN1pin, GPIO.OUT)
        GPIO.setup(self.IN2pin, GPIO.OUT)

        # setup input
        GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.pwm = GPIO.PWM(self.PWMpin, 100)

        self.pwm.start(0)

        GPIO.output(self.IN1pin, True)
        GPIO.output(self.IN2pin, False)

        self.pwm.ChangeDutyCycle(25)

    def setSpeed(self, speed: int) -> None:
        if speed > 100 or speed < 0:
            print("Speed not supported... Please enter a number between 0 and 100.")
        else:
            self.pwm.ChangeDutyCycle(speed)
    

    #def button_callback(self, channel) -> None:
    #    print("Button pushed!")


mot = DCMotor(4, 27, 22, 2)

if __name__ == '__main__':

    while(True):
        #speed = input("Speed: ")
        #mot.setSpeed(int(speed))
        if GPIO.input(2) == GPIO.HIGH:
            print("Button was pushed!")
    