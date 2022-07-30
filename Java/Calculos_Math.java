package Java;

public class Calculos_Math {
  public static void main(String args[]){
    double raiz = Math.sqrt(9.0);
    System.out.println(raiz);

    float a = 1.776584F;
    int resultado = Math.round(a);
    System.out.println(resultado);
    
    //? Refundicion convertir a un tipo de valor
    //? int raiz = (int) Math.round(a)
    
    double b = 1.2354;
    int resultado2 =(int)Math.round(b); //?El programa arroja error si no refundo
    //?Alega que no puede convertir un valor long a int
    //?solo puede hacerlo si recibe el parametro float si lo hace
    //?Por eso lo convierto refundo a int
    System.out.println(resultado2);

    int base=2,exponente=5;
    double resultado3 = Math.pow(base, exponente);

    System.out.println(resultado3);
  }
}
