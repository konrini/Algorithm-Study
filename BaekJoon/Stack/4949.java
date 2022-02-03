import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		while (true) {
			String line = br.readLine();
			boolean check = true;
			if (line.equals(".")) {
				break;
			}
			List<String> list = new ArrayList<>();
			for (int i = 0; i < line.length(); ++i) {
				if (line.substring(i, i + 1).equals("(")) {
					list.add("(");
				} else if (line.substring(i, i + 1).equals(")")) {
					if (list.contains("(")) {
						if (list.get(list.size() - 1).equals("(")) {
							list = list.subList(0, list.size() - 1);
						} else {
							bw.write("no\n");
							check = false;
							break;
						}
					} else {
						bw.write("no\n");
						check = false;
						break;
					}
				} else if (line.substring(i, i + 1).equals("[")) {
					list.add("[");
				} else if (line.substring(i, i + 1).equals("]")) {
					if (list.contains("[")) {
						if (list.get(list.size() - 1).equals("[")) {
							list = list.subList(0, list.size() - 1);
						} else {
							bw.write("no\n");
							check = false;
							break;
						}
					} else {
						bw.write("no\n");
						check = false;
						break;
					}
				}
			}
			if (check == true) {
				if (list.size() > 0) {
					bw.write("no\n");
				} else {
					bw.write("yes\n");
				}
			}
		}
		bw.close();
	}
}