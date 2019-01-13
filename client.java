
package javaapplication1;

import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;


public class client extends Thread{
     Socket s;
     String mas,recv;
    public static void main(String[] args) {
        try {
            
           client c= new client();
           c.s=new Socket("localhost",5023);
            Scanner sc=new Scanner(System.in);
            
            PrintStream inp=new PrintStream(c.s.getOutputStream());
            System.out.println("enter your name :-");
            c.mas=sc.nextLine();
           
            inp.println(c.mas);
            c.start();
            while(true)
            {
                c.mas=sc.nextLine();
                 inp.println(c.mas);
            }
            
            
        } catch (IOException ex) {
            Logger.getLogger(client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    @Override
    public void run()
    {
         try {
             while(true)
             {
                 
             Scanner rec= new Scanner(s.getInputStream());
             recv=rec.nextLine();
             System.out.println(recv);
             }
         } catch (IOException ex) {
             System.out.println("out from recv");
         }
    }
    
}
