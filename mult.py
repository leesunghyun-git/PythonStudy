import threading
import topscrwaling as top

t1 = threading.Thread(target=top.crwaling, args=(50,))
t2 = threading.Thread(target=top.crwaling, args=(51,))
t3 = threading.Thread(target=top.crwaling, args=(63,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()