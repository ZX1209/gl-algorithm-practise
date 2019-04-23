import java.io.*;
import java.util.*;

public class Solution {
	public static void main(String[] args) {
//        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

		File input = new File(args[0]);
		File output = new File(args[1]);
		
		Scanner in = null;
		try {
			in = new Scanner(input);
		}
		catch(FileNotFoundException e) {
			e.printStackTrace();
		}
		
		FileWriter print = null;
		try {
			print = new FileWriter(output);
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		PrintWriter out = new PrintWriter(print);
	
		int t = in.nextInt(); 
    	in.nextLine();
        for (int num = 1; num <= t; ++num) {

        	int L = in.nextInt();
        	in.nextLine();
        	String A = in.nextLine(), B = in.nextLine();
        	HashSet<String> visited = new HashSet<>();
        	int[][][] buf = new int[L][L][26];
        	for(int j = 0; j < L; ++j) {
        		int curr = B.charAt(j) - 'A';
        		for(int i = 0; i <= j; ++i) {
        			if(i < j) buf[i][j] = buf[i][j-1].clone();
        			else buf[i][j] = new int[26];
        			++buf[i][j][curr];
        			visited.add(convert(buf[i][j]));
        		}
        	}
        	int ans = 0;
        	buf = new int[L][L][26];
        	for(int j = 0; j < L; ++j) {
        		int curr = A.charAt(j) - 'A';
        		for(int i = 0; i <= j; ++i) {
        			if(i < j) buf[i][j] = buf[i][j-1].clone();
        			else buf[i][j] = new int[26];
        			++buf[i][j][curr];
        			if(visited.contains(convert(buf[i][j]))) ++ans;
        		}
        	}
        	out.println("Case #" + num + ": " + ans);
        }
        
        in.close();
        out.close();
    }
	
	private static String convert(int[] B) {
		StringBuilder ans = new StringBuilder("");
		for(int b: B) ans.append(b).append(',');
		return ans.toString();
	}
}

