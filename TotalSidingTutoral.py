## Script to hold all of the siding, papering and window setting steps.
import time  
print('Hello and Welcome to the custome build tutorial for siding houses. ')
time.sleep(3)
#Insert the different files here to explain what section of the job need done. 
print('What step of the house siding process are you in? Paper, Siding, Windows, Soffit, Fascia.')
userAnswer = input()
if userAnswer == 'paper':
    import AppForPapering
elif userAnswer == 'siding':
    import AppForSiding
elif userAnswer == 'windows':
    import AppForWindows
elif userAnswer == 'soffit':
    import AppForSoffit
elif userAnswer == 'fascia':
    import AppforFascia
else:
    print('Well I hope guide helped you understand ')
##I guess now it is time to build this for real.  