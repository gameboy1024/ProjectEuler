package problems;
/**
 * Special Pythagorean triplet
 * Problem 9
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 * 
 * a2 + b2 = c2
 * For example, 32 + 42 = 9 + 16 = 25 = 52.
 * 
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 * 
 * 
 * Answer:
 * 31875000
 * Completed on Sun, 24 Nov 2013, 19:57
 * http://projecteuler.net/problem=9
 * 
 * @author SBT
 *
 */

public class Problem9 {
	public static void main(String[] args) {
		int a, b, c;
		for (c = 500; c >= 250; c--) {
			for (b = 1; b < 1000 - c; b++) {
				a = 1000 - c - b;
				if (a * a + b * b == c * c) {
					System.out.println("Answer is : " + a * b * c);
					return;
				}
			}
		}
	}
}
