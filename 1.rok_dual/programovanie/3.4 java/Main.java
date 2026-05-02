// Main.java
public class Main {
    public static void main(String[] args) {
        // Instantiate two Car objects with different parameters
        Car car1 = new Car("Toyota", "Camry", 1999);
        Car car2 = new Car("Ford", "Mustang", 2020);
        Car car3 = new Car("Volvo");
        Car car4 = new Car();
        Car car5 = new Car(2008);

        // Print information about the cars
        System.out.println("Car 1:");
        System.out.println(car1);
        System.out.println("Car 2:");
        System.out.println(car2);
        System.out.println("Car 3:");
        System.out.println(car3);
        System.out.println("Car 4:");
        System.out.println(car4);
        System.out.println("Car 5:");
        System.out.println(car5);
    }
}