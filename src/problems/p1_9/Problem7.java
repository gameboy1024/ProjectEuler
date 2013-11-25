package problems.p1_9;
/**
 * 10001st prime
 * Problem 7
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * 
 * What is the 10 001st prime number?
 * 
 * 
 * Answer:
 * 104743
 * Completed on Sun, 24 Nov 2013, 19:16
 * http://projecteuler.net/problem=7
 * 
 * @author SBT
 *
 */
public class Problem7 {

	public static void main(String[] args) {
		long prime[] = new long[10001];
		boolean found = false;
		prime[0] = 2;
		prime[1] = 3;
		int count = 1;
		while (count < 10000) {
			label: for (long i = prime[count] + 1;; i++) {
				found = true;
				for (int j = 0; j <= count; j++) {
					if (i % prime[j] == 0) {
						found = false;
					}
				}
				if (found) {
					// System.out.println("Found prime : " + i);
					prime[++count] = i;
					break label;
				}
			}
		}
		System.out.println("Answer is : " + prime[10000]);

	}

}
