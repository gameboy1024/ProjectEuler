package problems.p10_19;

/**
 * 
 * Longest Collatz sequence Problem 14 The following iterative sequence is
 * defined for the set of positive integers:
 * 
 * n ¡ú n/2 (n is even) n ¡ú 3n + 1 (n is odd)
 * 
 * Using the rule above and starting with 13, we generate the following
 * sequence:
 * 
 * 13 ¡ú 40 ¡ú 20 ¡ú 10 ¡ú 5 ¡ú 16 ¡ú 8 ¡ú 4 ¡ú 2 ¡ú 1 It can be seen that this sequence
 * (starting at 13 and finishing at 1) contains 10 terms. Although it has not
 * been proved yet (Collatz Problem), it is thought that all starting numbers
 * finish at 1.
 * 
 * Which starting number, under one million, produces the longest chain?
 * 
 * NOTE: Once the chain starts the terms are allowed to go above one million.
 * 
 * 
 * Answer: 837799 Completed on Mon, 25 Nov 2013, 21:15
 * http://projecteuler.net/problem=14
 * 
 * @author SBT
 * 
 */

public class Problem14 {
	/**
	 * A Dynamic programming approach: Keep a large int array
	 * (time-space-trade-off) counter[1] = 1; For others, deduct until we have a
	 * number whose slot isn't 0 with currentLen steps Then we add his length to
	 * his slot so others can use it
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		int[] counter = new int[1000000];
		for (int i = 0; i < counter.length; i++) {
			counter[i] = 0;
		}
		counter[1] = 1;
		long target;
		int currentLen;
		for (int i = 2; i < counter.length; i++) {
			target = i;
			currentLen = 0;
			do {
				if (target % 2 == 0) {
					target = target / 2;
				} else {
					target = target * 3 + 1;
				}
				currentLen++;
			// Careful: these 2 conditions in the while condition only work if the compiler calculate
			// the first value before the second and don't calculate the second if the first don't c-
			// omply
			} while (target >= counter.length || counter[(int) target] == 0);
			counter[i] = currentLen + counter[(int) target];
		}

		int maxCount = -1, maxIndex = -1;
		for (int i = 0; i < counter.length; i++) {
			if (counter[i] > maxCount) {
				maxCount = counter[i];
				maxIndex = i;
			}
		}

		System.out.println("Answer is : " + maxIndex);
	}

}
