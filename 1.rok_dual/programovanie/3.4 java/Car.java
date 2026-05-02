// Car.java

public class Car {
    // Attributes of a car
    private String make;
    private String model;
    private int year;

    // Default constructor
    public Car() {
        this.make = "Unknown";
        this.model = "Unknown";
        this.year = 2024;
    }

    // Explicit constructor with additional initialization logic
    public Car(String make) {
        this.make = make;
        this.model = "Unknown";
        this.year = 2025; // Default year if not provided
    }

    // Explicit constructor with additional initialization logic
    public Car(String make, String model) {
        this.make = make;
        this.model = model;
        this.year = 2022; // Default year if not provided
    }

    // Explicit constructor with full initialization
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public Car(int year) {
        this.make = "Unknown";
        this.model = "Unknown";
        this.year = year;
    }

    // Getters and setters
    public String getMake() {
        return make;
    }

    public void setMake(String make) {
        this.make = make;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    // toString method to print car information
    // Add the @Override annotation to indicate that we are overriding the default toString method
    @Override
    public String toString() {
        return "Make: " + make + ", Model: " + model + ", Year: " + year;
    }
}