import java.lang.reflect.*;
        
public class Reflection {
   public static void main(String args[]) throws Exception{

         // Comment out this block after getting what you need, then uncomment the other section
         Class c = Class.forName(args[0]);
         Method m[] = c.getDeclaredMethods();
         for (int i = 0; i < m.length; i++)
         System.out.println(m[i].toString());

         // Hint h = new Hint();
         // Class c = h.getClass();

         // Method methodcall = c.getDeclaredMethod("superprivatefunction");
         // methodcall.setAccessible(true);
         // h.setLength(1000);
         // methodcall.invoke(h);
   }
}