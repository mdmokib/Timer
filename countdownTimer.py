import time

my_time=int(input("Enter your time in seconds : "))

for x in range (my_time, 0, -1):
    second = x % 60
    min=int(x/60)%60
    hr=int(x/3600)
    print(f"{hr:02}:{min:02}:{second:02}")
    time.sleep(1)
print("Time is UP!")    
