public class Bike {
    private String make;
    private String model;
    private int wheels;
    private int year;

    public Bike(String make, String model, int wheels, int year) {
        this.make = make;
        this.model = model;	
        this.wheels = wheels;   //toto som pridal pre pocet kolies
        this.year = year;
    }
    //toto som pridal pre 3tiu ulohu
    public Bike(String make, String model) {
        this(make, model, 2, 2025);
    }

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

    public int getWheels() {
        return wheels;
    }

    public void setWheels(int wheels) {
        this.wheels = wheels;
    }    

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    @Override
    public String toString() {
        return "Make: " + make + ", Model: " + model + ", Wheels: " + wheels + ", Year: " + year;
    }
}