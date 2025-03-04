class Car:
    def __init__(self, car_id, brand, model, base_price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.base_price_per_day = base_price_per_day
        self.is_available = True

    def calculate_price(self, rental_days):
        return self.base_price_per_day * rental_days

    def rent(self):
        self.is_available = False

    def return_car(self):
        self.is_available = True


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Rental:
    def __init__(self, car, customer, days):
        self.car = car
        self.customer = customer
        self.days = days


class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def rent_car(self, car, customer, days):
        if car.is_available:
            car.rent()
            self.rentals.append(Rental(car, customer, days))
        else:
            print("Car is not available for rent.")

    def return_car(self, car):
        car.return_car()
        rental_to_remove = None

        for rental in self.rentals:
            if rental.car == car:
                rental_to_remove = rental
                break

        if rental_to_remove:
            self.rentals.remove(rental_to_remove)
        else:
            print("Car was not rented.")

    def menu(self):
        while True:
            print("\n===== Car Rental System =====")
            print("1. Rent a Car")
            print("2. Return a Car")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n== Rent a Car ==")
                customer_name = input("Enter your name: ")

                print("\nAvailable Cars:")
                for car in self.cars:
                    if car.is_available:
                        print(f"{car.car_id} - {car.brand} {car.model}")

                car_id = input("\nEnter the car ID you want to rent: ")
                rental_days = int(input("Enter the number of days for rental: "))

                new_customer = Customer(f"CUS{len(self.customers) + 1}", customer_name)
                self.add_customer(new_customer)

                selected_car = next((car for car in self.cars if car.car_id == car_id and car.is_available), None)

                if selected_car:
                    total_price = selected_car.calculate_price(rental_days)
                    print("\n== Rental Information ==")
                    print(f"Customer ID: {new_customer.customer_id}")
                    print(f"Customer Name: {new_customer.name}")
                    print(f"Car: {selected_car.brand} {selected_car.model}")
                    print(f"Rental Days: {rental_days}")
                    print(f"Total Price: ${total_price:.2f}")

                    confirm = input("\nConfirm rental (Y/N): ").strip().lower()
                    if confirm == "y":
                        self.rent_car(selected_car, new_customer, rental_days)
                        print("\nCar rented successfully.")
                    else:
                        print("\nRental canceled.")
                else:
                    print("\nInvalid car selection or car not available for rent.")

            elif choice == "2":
                print("\n== Return a Car ==")
                car_id = input("Enter the car ID you want to return: ")

                car_to_return = next((car for car in self.cars if car.car_id == car_id and not car.is_available), None)

                if car_to_return:
                    rental = next((rental for rental in self.rentals if rental.car == car_to_return), None)

                    if rental:
                        self.return_car(car_to_return)
                        print(f"Car returned successfully by {rental.customer.name}")
                    else:
                        print("Car was not rented or rental information is missing.")
                else:
                    print("Invalid car ID or car is not rented.")

            elif choice == "3":
                print("\nThank you for using the Car Rental System!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    rental_system = CarRentalSystem()

    car1 = Car("C001", "Toyota", "Camry", 60.0)
    car2 = Car("C002", "Honda", "Accord", 70.0)
    car3 = Car("C003", "Mahindra", "Thar", 150.0)

    rental_system.add_car(car1)
    rental_system.add_car(car2)
    rental_system.add_car(car3)

    rental_system.menu()
