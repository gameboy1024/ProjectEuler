package problems;
/**
 * Smallest multiple
 * Problem 5
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 * 
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 * 
 * 
 * Answer:
 * 232792560
 * Completed on Sun, 24 Nov 2013, 18:28
 * http://projecteuler.net/problem=5
 * 
 * @author SBT
 *
 */
public class Problem5 {
	public static void main(String[] args) {
		long result = 2;
		for (long i = 2; i < 20; i++) {
			result = lcm(result, i + 1);
		}
		System.out.println("Answer is : " + result);
	}

	public static long lcm(long a, long b) {
		long tmp, aa = a, bb = b;
		while (bb != 0) {
			tmp = aa % bb;
			aa = bb;
			bb = tmp;
		}
		return a * b / aa;
	}

}
