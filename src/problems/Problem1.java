package problems;

/**
 * Multiples of 3 and 5
 * Problem 1
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * 
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * 
 * Answer:
 * 233168
 * Completed on Sun, 24 Nov 2013, 15:52
 * 
 * http://projecteuler.net/problem=1
 * 
 * @author SBT
 *
 */

public class Problem1 {

	public static void main(String[] args) {
		int sum = 0;
		for (int i = 999; i > 0; i--) {
			if (i%5 == 0 || i % 3 == 0) {
				sum += i;
			}
		}
		System.out.println("Answer is : " + sum);
	}

}
