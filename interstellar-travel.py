
# Create the function fuel_gage here
def fuel_gauge(fuel):
    print(f"You have {fuel} gallons of fuel left!")

# Create the function calculate_fuel here
def calculate_fuel(planet):
    fuel = 0
    if planet == "Venus":
        fuel = 300000
    elif planet == "Mercury":
        fuel = 500000
    elif planet == "Mars":
        fuel = 700000
    else:
        fuel = 0
    return fuel

# Create the function greet_planet here
def greet_planet(planet):
    print(f"Hello passengers, we are currently at {planet}!")

# Create the function cant_fly here
def cant_fly():
    print("We do not have the available fuel to fly there.")

# Create the function fly_to_planet here
def fly_to_planet(planet, fuel):
    fuel_remaining, fuel_cost = 0, 0
    fuel_remaining = fuel
    fuel_cost = calculate_fuel(planet)
    if fuel_remaining >= fuel_cost:
        greet_planet(planet)
        fuel_remaining -= fuel_cost
    elif fuel_cost > fuel_remaining:
        cant_fly()
    return fuel_remaining

# Create the main function here
def main():
    planet_choice = "Venus"
    fuel = 0

    fuel = fly_to_planet(planet_choice, fuel)
    fuel_gauge(fuel)



if __name__ == "__main__":
    main()