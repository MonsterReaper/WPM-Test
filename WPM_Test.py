#good luck :)
import time
import pyjokes
class WPM:
    def __init__(self):
        self.joke = pyjokes.get_joke()
        self.count = len(self.joke.split())
        
    def test_now(self):
        print(self.joke)
        while True:
            t0 = time.time()
            input_text = str(input("Enter "))
            t1 = time.time()
            accuracy =  len(set(input_text.split())&set(self.joke.split()))
            accuracy = accuracy/self.count*100
            t = t1-t0
            wpm = self.count/t*100
            print("WPM",wpm,"Accuracy",accuracy,"Timetaken",t)
