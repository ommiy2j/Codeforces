import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int m = scn.nextInt();
        ArrayList < String > paths = getMazePaths(1, 1, n, m);
        System.out.print(paths);

    }

    // sr - source row
    // sc - source column
    // dr - destination row
    // dc - destination column
    public static ArrayList < String > getMazePaths(int sr, int sc, int dr, int dc) {
        if (sr == dr && sc == dc) {
            ArrayList < String > bres = new ArrayList < > ();
            bres.add("");
            return bres;
        }
        ArrayList < String > paths = new ArrayList < > ();
        for (int i = 1; i <= dc - sc; i++) {
            ArrayList < String > hpath = getMazePaths(sr, sc + i, dr, dc);
            for (String path: hpath) {
                paths.add("h" + i + path);
            }
        }
        for (int i = 1; i <= dr - sr; i++) {
            ArrayList < String > vpath = getMazePaths(sr + i, sc, dr, dc);
            for (String path: vpath) {
                paths.add("v" + i + path);
            }
        }
        for (int i = 1; i <= dc - sc && i <= dr - sr; i++) {
            ArrayList < String > dpath = getMazePaths(sr + i, sc + i, dr, dc);
            for (String path: dpath) {
                paths.add("d" + i + path);
            }
        }
        return paths;
    }

}