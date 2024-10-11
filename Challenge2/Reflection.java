import java.lang.reflect.*;
        
public class Reflection {
   public static void main(String args[]) throws Exception{
         Hint h = new Hint();

         Class c = h.getClass();

         Method methodcall = c.getDeclaredMethod("superprivatefunction");
         methodcall.setAccessible(true);
         methodcall.invoke(h);
   }
}