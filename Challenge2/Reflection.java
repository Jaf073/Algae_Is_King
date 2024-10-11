import java.lang.reflect.*;
        
// class A {}

public class Reflection {
   private double d;
   public static final int i = 37;
   String s = "testing";
        
   public static void main(String args[]) {
      try {
         Class c = Class.forName(args[0]);
         Method m[] = c.getDeclaredMethods();

         for (int i = 0; i < m.length; i++)
         System.out.println(m[i].toString());

         Field fieldlist[] = c.getDeclaredFields();
         for (int i = 0; i < fieldlist.length; i++) {
            Field fld = fieldlist[i];
            System.out.println("name = " + fld.getName());
            System.out.println("decl class = " + fld.getDeclaringClass());
            System.out.println("type = " + fld.getType());
            int mod = fld.getModifiers();
            System.out.println("modifiers = " + Modifier.toString(mod));
            System.out.println("-----");         
         }



         // Class cls = Class.forName("A");
         // boolean b1 = cls.isInstance(new Integer(37));
         // System.out.println(b1);
         // boolean b2 = cls.isInstance(new A());
         // System.out.println(b2);
      } catch (Throwable e) { System.err.println(e); }
   }
}