public class Main {
    public static void main(String[] args) {

        Car car1 = new Car("Toyota", "Camry", 1999);
        Car car2 = new Car("Ford", "Mustang");
        Car car3 = new Car("Volvo");
        Bike mybike1 = new Bike("BMW", "F900", 4, 2019 );
        Bike mybike2 = new Bike("Porsche", "Sportster");    //taktiez 3tia uloha

        System.out.println("Car 1:");
        System.out.println(car1);
        System.out.println("Car 2:");
        System.out.println(car2);
        System.out.println("Car 3:");
        System.out.println(car3);
        System.out.println("Bike 1:");
        System.out.println(mybike1);
        System.out.println("Bike 2:");  //3ka tiez
        System.out.println(mybike2);
    }
}