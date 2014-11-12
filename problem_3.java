package problems.p1_9;
/**
 * Largest prime factor
 * Problem 3
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
 * 
 * 
 * Answer:
 * 6857
 * Completed on Sun, 24 Nov 2013, 16:27
 * http://projecteuler.net/problem=3
 * 
 * @author SBT
 *
 */

public class Problem3 {

	public static void main(String[] args) {
		long number = 600851475143l;
		long middle = (int) Math.sqrt(number);
		long i;
		long factor = 0;
		// handle even numbers:
		if (number % 2 == 0) {
			factor = 2;
			while (number % 2 == 0) {
				number >>= 1;
			}
		}
		for (i = 3; i <= middle; i += 2) {
			if (number % i == 0) {
				number = number / i;
				factor = i;
				while (number % i == 0) {
					number = number / i;
				}
			}
		}
		if (factor == 0) {
			System.out.println("This is a prime number, no answer!");
		} else {
			System.out.println("Answer is : " + factor);
		}
	}
}
