import queue
import threading
import time
import random

# Create a queue for requests
request_queue = queue.Queue()
stop_event = threading.Event()

# Add a requests
def generate_request():
    request_id = 1
    while not stop_event.is_set():
        # Simulate time for creating new requests
        time.sleep(random.randint(1, 3))
        request = f"Request №{request_id}"
        request_queue.put(request)
        print(f"{request} is added to the queue.")
        request_id += 1

# Process a request
def process_request():
    while not stop_event.is_set() or not request_queue.empty():
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Now processing {request}...")
            # Simulate time for processing the request
            time.sleep(random.randint(1, 3))
            print(f"{request} is processed.")
        else:
            print("Queue is empty, waiting for new requests...")
            time.sleep(2)

        # Show the length of the queue
        print(f"Queue length: {request_queue.qsize()}")

def main():
    # Create separate threads for generating and processing requests
    generator_thread = threading.Thread(target=generate_request)
    processor_thread = threading.Thread(target=process_request)

    # Start the threads
    generator_thread.start()
    processor_thread.start()

    # Wait until the user wants to stop the program
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping request generation...")
        stop_event.set()
        generator_thread.join()
        processor_thread.join()
        print("All requests processed. Program terminated.")

if __name__ == "__main__":
    main()
