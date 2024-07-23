# from multiprocessing import Process

# def f(name):
#     print('hello',name)
    
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     ghfhfg
#     ghfhfghfg
    
#     fghfghh
#     fghfgh


# from multiprocessing import Process

# def create_text(text):
#     with open(f"{text}.txt", "w") as file:
        #  file.write(text)
         
#  if __name__ == "__main__":
#      for in in range(100):
#          process = Process         

# from multiprocessing import Process, Queue

# def sender(queue):
#     data = [1,2,3,4,5]
#     for i in data:
#         queue.put(i)
        
# def receiver(queue):
#     while not queue.empty():
#         print(queue.get())
        
# if __name__ == "__main__":
#     q = Queue()
#     process_1 = Process(target=sender, args=(q,))
#     process_2 = Process(target=receiver, args=(q,))     
   
#     process_1.start()
#     process_1.join()     
    
#     process_2.start()
#     process_2.join()   


# from multiprocessing import Process, Pipe
# def get_data(conn):
#     data = [1,2,3,4,5]
#     conn.send(data)
    
# if __name__ == "__main__":
#     blue, green = Pipe()  

import requests
from multiprocessing import Process
import threading

def download_image(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open('image.jpg','wb') as file:
         file.write(response.content)
         print("Downloaded")
    else:
        print("Error")
         
if __name__ == "__main__":
    for i in range(1000):
        thread = threading.Thread(target=download_image, args={str(i)})
        thread.start()
        download_image("https://i.pinimg.com/236x/24/15/21/24152197af38deb718eb730992d441d0.jpg")
  
  
     



    
    
    
    