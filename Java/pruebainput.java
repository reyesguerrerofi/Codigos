package Java;
import java.util.*;

public class pruebainput {
  public static void main(String args[]){

    Scanner entrada = new Scanner(System.in);
    System.out.println("Introducir nombre: ");
    String nombre = entrada.nextLine();

    System.out.println("Tu nombre es: "+ nombre);

    System.out.println("Ahora tu edad: ");
    int edad = entrada.nextInt();
    System.out.println("Tu edad es: "+ edad);

    
  }

}
