import math

def calculate_rover_time():

    try:
        #  Get input
        origin = input("Enter Origin (x1 y1): ")
        destination = input("Enter Destination (x2 y2): ")

        x1, y1 = map(float, origin.split())
        x2, y2 = map(float, destination.split())

        
        v0 = float(input("Initial Velocity: "))
        a = float(input("Acceleration: "))
        v_max = float(input("Top Speed: "))

        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        
        t_accel = (v_max - v0) / a

        
        d_accel = v0 * t_accel + 0.5 * a * t_accel * t_accel

        
        if d_accel >= distance:
            
            time = (-v0 + math.sqrt(v0*v0 + 2*a*distance)) / a

        else:
            #  max speed
            remaining_distance = distance - d_accel
            cruise_time = remaining_distance / v_max
            time = t_accel + cruise_time

        #  print result
        print("\nDistance:", round(distance, 1), "m")
        print("Time:", round(time, 1), "seconds")

    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("Acceleration cannot be zero.")



calculate_rover_time()
