import time

def moviator2():
    ask = input("What do you need to do? ").lower()
    return f"lets get {ask} started! You got this"

start_time = time.time()




def moviator():
    ask = input("What do you need to do? ").lower()
    if ask == 'dishes':
        print(f"Get scrub daddy on the phone!")
    elif ask == 'laundry':
        print(f'lets just throw it all away and go shopping')
    print(f'YOU NEED TO GET {ask} DONE< WHAT ARE YOU DOING? YOU GOT THIS! JUST LIK SHIA "JUST DO IT" ')

    
end_time = start_time - time.time()

print( start_time, moviator(), end_time )