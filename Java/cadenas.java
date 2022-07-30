package Java;

public class cadenas {
  public static void main(String args[]){
    String nombre = "Antonio";//? Con comilla doble
    System.out.println("Hola mi nombre es " + nombre);

    //System.out.println("\n El tamagno de mi nombre es " + nombre.length());
    //System.out.println(("\n La primera letra del nombre es: " + nombre.charAt(0) ));

    String cadena_larga = "Alla en la fuente habia un chorrito se hacia grandote, se hacia chiquito";
    String que_hacia = cadena_larga.substring(55, cadena_larga.length());

    System.out.println(que_hacia);

    String nombre1 = "Emiliana",nombre2="emilian4",nombre3="Antonio",nombre4="Antonio";
    System.out.println(nombre1.equals(nombre2));
    System.out.println(nombre3.equals(nombre4));

    String nombre5="Emi",nombre6="emi";//Ignora mayus y minus
    System.out.println(nombre5.equalsIgnoreCase(nombre6));

  }
}
