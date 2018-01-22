#Calculate Kineti Energy
print("This program calculates the kinetic energy of a moving object.")

#Data input
mass_object = float(raw_input("Enter the object's mass in kilograms: "))
speed_object = float(raw_input("Enter the object's speed in meters per second: "))

#Output calculation
energy = 0.5 * mass_object * speed_object**2

#Result output
print("The object has " + str(energy) + "joules of energy.")