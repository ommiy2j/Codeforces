import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn=new Scanner(System.in);
        String s=scn.next();
        printSS(s,"");

    }

    public static void printSS(String str, String ans) {
        if(str.length()==0)
        {
            System.out.println(ans);
            return;
        }
        char ch=str.charAt(0);
        String ques=str.substring(1);
        printSS(ques,ans+ch);
        printSS(ques,ans+"");
    }

}