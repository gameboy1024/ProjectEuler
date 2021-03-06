package problems.p10_19;

/**
 * Summation of primes Problem 10 The sum of the primes below 10 is 2 + 3 + 5 +
 * 7 = 17.
 * 
 * Find the sum of all the primes below two million.
 * 
 * 
 * Answer: 142913828922 Completed on Sun, 24 Nov 2013, 22:35
 * http://projecteuler.net/problem=10
 * 
 * @author SBT
 * 
 */
public class Problem10 {
	public static void main(String[] args) {
		final int LENGTH = 2000000 / 2;
		boolean[] numbers = new boolean[LENGTH];
		for (int i = 0; i < numbers.length; i++) {
			numbers[i] = true;
		}
		numbers[0] = false;
		int limit = (int) Math.sqrt(2 * LENGTH);
		for (int i = 3; i < limit; i++) {
			for (int j = 2 * i; j < 2 * LENGTH; j += i) {
				if (j % 2 == 1) {
					numbers[(j - 1) / 2] = false;
				}
			}
		}
		// Made mistake here... int_max is 10 digit
		long sum = 2;
		for (int i = 1; i < numbers.length; i++) {
			if (numbers[i]) {
				sum += 2 * i + 1;
			}
		}
		System.out.println("Answer is : " + sum);
	}

	// Way too slow... Need some trade-offs
	/*
	 * public static void main(String[] args) { int i = 2, sum = 0; while (i <
	 * 2000000) { if (isPrime(i)) { sum += i; } }
	 * 
	 * System.out.println("Answer is : "); }
	 * 
	 * public static boolean isPrime(int num) { int last = (int) Math.sqrt(num);
	 * for (int i = 2; i < last; i++) { if (num % i == 0) { return false; } }
	 * return true; }
	 */
}
