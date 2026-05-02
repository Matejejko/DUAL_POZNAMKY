public class idkJustTrying {
    public static void main(String[] args) {
    System.out.println("Hello World");
    System.out.print("text without ln");
    System.out.println(" once again");
    System.out.println(2 * 5);
    //wow a fuc*ing comment

    /*this a 
    multy line comment
     */

    /*types of variables:
        String - stores text, such as "Hello". String values are surrounded by double quotes
        int - stores integers (whole numbers), without decimals, such as 123 or -123
        float - stores floating point numbers, with decimals, such as 19.99 or -19.99
        char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
        boolean - stores values with two states: true or false
     */

// creating them: type variableName = value;

    String kokot = "si kokot?";
    System.out.println(kokot);

    int MyNum;
    MyNum = 11;
    System.out.println(MyNum);

    int MyNum2 =20;
    MyNum2 = 12;         //now its 10 and not 20
    System.out.println(MyNum2);

    final int myNum3 = 13;  //now you wont be able to change it final "constant"
    System.out.println(myNum3);


//To combine both text and a variable, use the + character
    System.out.println(myNum3 + " is a number");

//You can also use the + character to add a variable to another variable
    String firstName = "John ";
    String lastName = "Doe";
    String fullName = firstName + lastName;
    System.out.println(fullName);

//For numeric values, the + character works as a mathematical operator (notice that we use int (integer) variables here):
    int x = 5;
    int y = 6;
    System.out.println(x + y);

//To declare more than one variable of the same type, you can
    int xx = 5, yy = 6, zz = 50;
    System.out.println(xx + yy + zz);

//same value to multiple variables
    int x2, y2, z2;
    x2 = y2 = z2 = 50;
    System.out.println(x2 + y2 + z2);


/*All Java variables must be identified with unique names.

These unique names are called identifiers.

Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume). */


    //D A T A   T Y P E S


    /*Data types are divided into two groups:
    Primitive data types - includes byte, short, int, long, float, double, boolean and char
    Non-primitive data types - such as String, Arrays and Classes 
    
    byte	-   Stores whole numbers from -128 to 127
    short	-   Stores whole numbers from -32,768 to 32,767
    int	    -   Stores whole numbers from -2,147,483,648 to 2,147,483,647
    long	-   Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
    float	-   Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
    double	-   Stores fractional numbers. Sufficient for storing 15 to 16 decimal digits
    boolean	-   Stores true or false values
    char	-   Stores a single character/letter or ASCII values*/

    /*Primitive number types are divided into two groups:

    Integer types stores whole numbers, positive or negative (such as 123 or -456), without decimals. 
    Valid types are byte, short, int and long. Which type you should use, depends on the numeric value.

    Floating point types represents numbers with a fractional part, containing one or more decimals.
    There are two types: float and double. */


    //B o o l e a n   T y p e s

    /*Very often in programming, you will need a data type that can only have one of two values, like:
        YES / NO
        ON / OFF
        TRUE / FALSE
    For this, Java has a boolean data type, which can only take the values true or false: */
    boolean isJavaFun = true;
    boolean isFishTasty = false;
    System.out.println(isJavaFun);     // Outputs true
    System.out.println(isFishTasty);   // Outputs false


    //C H A R A C T E R S
        //The char data type is used to store a single character. The character must be surrounded by single quotes, like 'A' or 'c':
    char myGrade = 'B';
    System.out.println(myGrade);
    //Alternatively, if you are familiar with ASCII values, you can use those to display certain characters:
    char myVar1 = 65;
    System.out.println(myVar1);
    }
}