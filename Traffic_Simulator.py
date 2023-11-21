import multiprocessing
import time
import random
import psutil

class Semaphore:
    def __init__(self, lanes):
        """
        Initialize Semaphore object.

        Parameters:
        - lanes: Number of available lanes at the intersection.
        """
        self.semaphore = multiprocessing.Semaphore(value=lanes)
        self.queue = multiprocessing.Queue()
        self.green_light_duration = 5
        self.priority_lane = None

    def acquire(self):
        """Acquire the semaphore and add a car to the queue."""
        self.queue.put(1)
        self.semaphore.acquire()

    def release(self):
        """Release the semaphore and remove a car from the queue."""
        self.semaphore.release()
        self.queue.get()

    def get_number_of_cars_in_queue(self):
        """Get the number of cars in the queue."""
        return self.queue.qsize()

    def adjust_green_light_duration(self):
        """
        Adjust the green light duration based on the number of cars in the queue.

        If more than 5 cars are in the queue, increase green light duration.
        If fewer than 3 cars are in the queue and the current duration is greater than 1, decrease it.
        If there is a priority lane with cars, increase the duration.
        """
        cars_in_queue = self.get_number_of_cars_in_queue()
        if cars_in_queue > 5:
            self.green_light_duration += 1
        elif cars_in_queue < 3 and self.green_light_duration > 1:
            self.green_light_duration -= 1

        if self.priority_lane is not None and cars_in_queue > 0:
            self.green_light_duration += 1

        print(f"Green light duration adjusted to {self.green_light_duration} seconds.")

    def set_priority(self, lane):
        """Set the priority lane for the semaphore."""
        self.priority_lane = lane

    def clear_priority(self):
        """Clear the priority lane for the semaphore."""
        self.priority_lane = None

    def has_priority_lane(self, lane):
        """Check if a lane has priority based on conditions."""
        return lane == "A" and self.get_number_of_cars_in_queue() > 3

class Intersection:
    def __init__(self, semaphore):
        """
        Initialize Intersection object.

        Parameters:
        - semaphore: Semaphore object controlling the intersection.
        """
        self.semaphore = semaphore

    def traverse_intersection(self, car_id, lane):
        """
        Simulate a car crossing the intersection.

        Parameters:
        - car_id: Unique identifier for the car.
        - lane: Lane from which the car is approaching.
        """
        self.semaphore.acquire()
        try:
            if self.semaphore.has_priority_lane(lane):
                print(f"Car {car_id} from lane {lane} has priority!")
                self.semaphore.set_priority(lane)
            else:
                print(f"Car {car_id} approaching the intersection from lane {lane}.")

            arrival_time = random.uniform(0.1, 1.0)
            time.sleep(arrival_time)
            print(f"Car {car_id} arrived at the intersection in {arrival_time:.2f} seconds.")

            if random.random() < 0.1:
                breakdown_time = random.uniform(2.0, 5.0)
                print(f"Car {car_id} broke down! Waiting for a tow truck for {breakdown_time:.2f} seconds.")
                time.sleep(breakdown_time)
                print(f"Tow truck arrived! Car {car_id} is being removed.")
            else:
                wait_time = random.uniform(0.5, 1.5)
                time.sleep(wait_time)
                print(f"Car {car_id} crossed the intersection.")
        finally:
            self.semaphore.release()
            self.semaphore.clear_priority()

    def unexpected_event(self):
        """
        Simulate an unexpected event at the intersection.
        
        There is a 5% chance of an unexpected event occurring.
        """
        if random.random() < 0.05:
            print("Unexpected event: Change in traffic rules!")
            # Logic to handle the unexpected event, if necessary

class Car(multiprocessing.Process):
    def __init__(self, id, intersection, lane):
        """
        Initialize Car object.

        Parameters:
        - id: Unique identifier for the car.
        - intersection: Intersection object the car will traverse.
        - lane: Lane from which the car is approaching.
        """
        super().__init__()
        self.id = id
        self.intersection = intersection
        self.lane = lane

    def run(self):
        """Run the process to simulate a car crossing the intersection."""
        self.intersection.traverse_intersection(self.id, self.lane)

def start_simulation():
    """
    Start the simulation of traffic at the intersection.
    
    The user is prompted to input the number of cars to simulate.
    """
    available_lanes = 2
    semaphore = Semaphore(available_lanes)
    intersection = Intersection(semaphore)

    try:
        number_of_cars = int(input("Enter the number of cars to simulate: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    cars = []
    for i in range(1, number_of_cars + 1):
        lane = random.choice(["A", "B"])
        car = Car(i, intersection, lane)
        cars.append(car)
        car.start()

        intersection.unexpected_event()

    start_time = time.time()

    for car in cars:
        car.join()

    end_time = time.time()
    simulation_time = end_time - start_time

    print("\n===== Efficiency Evaluation =====")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Total simulation time: {simulation_time:.2f} seconds")

def show_credits():
    """Display the credits for the program."""
    print("João Ribeiro")
    print("Rendrick Carreira")

def main():
    """Main function to run the traffic simulation program."""
    while True:
        print("\n===== Traffic Simulator =====")
        print("1 - Start")
        print("2 - Credits")
        print("3 - Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            start_simulation()
        elif choice == "2":
            show_credits()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
