import threading

a = 20
b = 50

condition = threading.Condition()
ready = False

def thread1():
    global ready

    with condition:
        print("Before Swapping:")
        print("a =", a)
        print("b =", b)

        ready = True
        condition.notify()

def thread2():
    global a, b

    with condition:
        while not ready:
            condition.wait()

            temp = a
            a = b
            b = temp

            print("\nAfter Swapping:")
            print("a =", a)
            print("b =", b)

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t2.start()
t1.start()

t1.join()
t2.join()