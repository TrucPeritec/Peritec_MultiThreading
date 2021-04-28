import threading
import queue
import time
from time import sleep

# Thread Template - begin ------------------------------------------------------------------------------------------------------------------------
class PeritecThreadTemplate(threading.Thread):
    locker = threading.Lock()
    def __init__(self, thread_name, qin):
        threading.Thread.__init__(self)
        self.setName(thread_name)
        self.qin = qin

    def getThreadByName(self, thread_name):
        for thread in threading.enumerate():
            if thread.getName() == thread_name:
                return thread
        return 0

    def enqueue(self, queue, mess, data, sender = ""):
        if queue != 0:
            self.locker.acquire()
            queue.put({"mess": mess, "data": data, "sender": sender})
            self.locker.release()

    def dequeue(self, queue):
        if queue != 0:
            if not queue.empty():
                self.locker.acquire()
                data_queue = queue.get()                
                self.locker.release()
            else:
                data_queue = 0
            return data_queue
        else:
            return 0
# Template thread - end ------------------------------------------------------------------------------------------------------------------------


# Queue Generator --------------------------------------------------------------------------
def queueGenerator(num_of_element):
    return queue.Queue(num_of_element)
# Queue Generator --------------------------------------------------------------------------








# The MultiThreading template definition end here ---------------------------------------------------------------
# The code below is just for test purpose ---------------------------------------------------------------







# User output thread - begin ------------------------------------------------------------------------------------------------------------------------
class UserOutputThread(PeritecThreadTemplate):
    def __init__(self, thread_name, qin):
        PeritecThreadTemplate.__init__(self, thread_name, qin)

    def run(self):
        while(1):
            data_queue = self.dequeue(self.qin)
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    break;
                elif data_queue["mess"] == "print":
                    print(data_queue["data"])
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# User output thread - end ------------------------------------------------------------------------------------------------------------------------

# User input thread - begin ------------------------------------------------------------------------------------------------------------------------
class UserInputThread(PeritecThreadTemplate):
    def __init__(self, thread_name, qin):
        PeritecThreadTemplate.__init__(self, thread_name, qin)

    def run(self):
        while(1):
            user_command = input()
            # ----------------------------------------------------------------------------------
            if user_command == "1":
                if self.getThreadByName("pr_thread") != 0:
                    self.enqueue(self.getThreadByName("pr_thread").qin, "data_from_user_input", 1, self.getName())
                if self.getThreadByName("user_output_thread") != 0:
                    self.enqueue(self.getThreadByName("user_output_thread").qin, "data_from_user_input", 1, self.getName())
                break;
            elif user_command == "2":
                if self.getThreadByName("pr_thread") != 0:
                    self.enqueue(self.getThreadByName("pr_thread").qin, "data_from_user_input", 2, self.getName())
            elif user_command == "3":
                if self.getThreadByName("pr_thread") != 0:
                    self.enqueue(self.getThreadByName("pr_thread").qin, "data_from_user_input", 3, self.getName())
            elif user_command == "4":
                if self.getThreadByName("pr_thread") != 0:
                    self.enqueue(self.getThreadByName("pr_thread").qin, "data_from_user_input", 4, self.getName())
            else:
                pass
            # ----------------------------------------------------------------------------------
            sleep(0.001)
# User input thread - end ------------------------------------------------------------------------------------------------------------------------



# Producer thread - begin ------------------------------------------------------------------------------------------------------------------------
class PrThread(PeritecThreadTemplate):
    def __init__(self, thread_name, qin):
        PeritecThreadTemplate.__init__(self, thread_name, qin)

    def run(self):
        while(1):
            data_queue = self.dequeue(self.qin)
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    if self.getThreadByName("task_0") != 0:
                        self.enqueue(self.getThreadByName("task_0").qin, "data_from_producer", 1, self.getName())
                    if self.getThreadByName("task_1") != 0:
                        self.enqueue(self.getThreadByName("task_1").qin, "data_from_producer", 1, self.getName())
                    break;
                elif data_queue["data"] == 2:
                    if self.getThreadByName("user_output_thread") != 0:
                        self.enqueue(self.getThreadByName("user_output_thread").qin, "print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 3:
                    if self.getThreadByName("task_0") != 0:
                        self.enqueue(self.getThreadByName("task_0").qin, "data_from_producer", 3, self.getName())
                elif data_queue["data"] == 4:
                    if self.getThreadByName("task_1") != 0:
                        self.enqueue(self.getThreadByName("task_1").qin, "data_from_producer", 4, self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Producer thread - end ------------------------------------------------------------------------------------------------------------------------



# Consumer A thread - begin ------------------------------------------------------------------------------------------------------------------------
class CsAThread(PeritecThreadTemplate):
    def __init__(self, thread_name, qin):
        PeritecThreadTemplate.__init__(self, thread_name, qin)

    def run(self):
        while(1):
            data_queue = self.dequeue(self.qin)
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    break;
                elif data_queue["data"] == 2:
                    pass
                elif data_queue["data"] == 3:
                    if self.getThreadByName("user_output_thread") != 0:
                        self.enqueue(self.getThreadByName("user_output_thread").qin, "print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 4:
                    if self.getThreadByName("user_output_thread") != 0:
                        self.enqueue(self.getThreadByName("user_output_thread").qin, "print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Consumer A thread - end ------------------------------------------------------------------------------------------------------------------------

# Consumer B thread - begin ------------------------------------------------------------------------------------------------------------------------
class CsBThread(PeritecThreadTemplate):
    def __init__(self, thread_name, qin):
        PeritecThreadTemplate.__init__(self, thread_name, qin)

    def run(self):
        while(1):
            data_queue = self.dequeue(self.qin)
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    break;
                elif data_queue["data"] == 2:
                    pass
                elif data_queue["data"] == 3:
                    if self.getThreadByName("user_output_thread") != 0:
                        self.enqueue(self.getThreadByName("user_output_thread").qin, "print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 4:
                    if self.getThreadByName("user_output_thread") != 0:
                        self.enqueue(self.getThreadByName("user_output_thread").qin, "print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Consumer B thread - end ------------------------------------------------------------------------------------------------------------------------



def main():
    user_input_thread = UserInputThread("user_input_thread", queueGenerator(10))
    user_input_thread.start()

    user_output_thread = UserOutputThread("user_output_thread", queueGenerator(10))
    user_output_thread.start()

    thread_1 = PrThread("pr_thread", queueGenerator(10))
    thread_1.start()

    thread_2 = CsAThread("task_0", queueGenerator(10))
    thread_2.start()

    thread_2 = CsBThread("task_1", queueGenerator(10))
    thread_2.start()


if __name__ == "__main__":
    main()