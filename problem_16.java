package problems.p10_19;

/**
 * 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
 * What is the sum of the digits of the number 2^1000?
 * 
 * Answer: 1366 Completed on Thu, 27 Feb 2014, 09:53
 * http://projecteuler.net/problem=16
 * 
 * @author SBT
 *
 */
public class Problem16 {

	/**
	 * Let's simulate the power operation and then sum up...
	 */
	public static void main(String[] args) {
		// lg(2^1000) = 1000 * lg2 < 303 so 303 is enough. 
		int [] counter = new int[303];
		for (int i : counter) {
			i = 0;
		}
		counter[0] = 1;
		
		int carry = 0;
		for (int i = 0; i < 1000; i++) {
			for (int j = 0; j < counter.length; j++) {
				counter[j] = counter[j] * 2 + carry;
				carry = 0;
				if (counter[j] >= 10) {
					carry = counter[j] / 10;
					counter[j] %= 10;
				}
			}
		}
		
		int sum = 0;
		for (int i : counter) {
			sum += i;
		}
		System.out.println(sum);
	}
}