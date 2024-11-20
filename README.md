# Questions
1. Please explain Big-O notation in simple terms.    
   Big O notation is a mathematical notation used by computer scientists to describe an algorithm's space or run time requirements. The notation specifically captures what happens to the algorithm as the input size grows. Often times you will see the notation use the variable n, in this case n is representing the input size and we often conceptualize it as growing towards infinity.  
2. What are the most important things to look for when reviewing another team member's code?    
  The most important things to look for are functionality and design. Functionality means the code is executing as described and there are no obvious flaws in the logic or cases that have been missed. Design means that the code is structured in a way that makes sense and fits with the standards of the codeback. It also encompasses code that is easy for other developers to read and modify.  
3. Describe a recent interaction with someone who was non-technical. What did you need to communicate and how did you do it?    
  In a recent ticket that was assigned to me I didn't quite understand the workflow the artists were using to encounter the issue they were reporting. I reached out to the technical artist that submitted the ticket on teams and asked her to clarify and walk we through the workflow. After asking a few more follow up questions I was able to understand the problem. If I was still struggling after reaching out via teams I would have asked to schedule a meeting where she could have shown me exactly what the workflow was. 
4. Implement a simple priority queue. Assume an incoming stream of dictionaries containing two keys; command to be executed and priority. Priority is an integer value [0, 10], where work items of the same priority are processed in the order they are received.    

### Assumptions: 
* a lower number indicates higher priority
* the dictionary's two keys are called "priority" and "command"
* commands are strings representing executable commands

To run the tests for question 4:
1. Clone the project
2. Navigate to the interview-questions directory on your terminal
3. Create a virtual environment, in this case I called mine pytest-env `python3 -m venv pytest-env`
4. Activate your virtual environment `source pytest-env/bin/activate`
5. Install pytest dependancies using `pip install -r requirements.txt`
6. Run `pytest test_priority_queue.py`. Pytest will print the results of running the tests

### PriorityQueue vs HeapPriorityQueue
`priority_queue.py` contains my initial apporach to the question. It runs in O(n) for space and time complexity, with inserts taking O(n) and removal taking O(1). After I wrote it I felt like there must be a faster solution and did some research. Using a binary heap implementation came up as the faster approach. So I wrote a binary min heap implementation of the priority queue in `heap_priority_queue.py`. This has a space complexity of O(n) but a time complexity of O(logn) where inserts take O(logn) and removals take O(logn). I decided to write the implementation from scratch rather than use python's built in heapq because I felt it was more in the spirit of the question. Tests for both implementations of the priority queues run in `test_priority_queue.py`. 
