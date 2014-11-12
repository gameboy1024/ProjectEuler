package problems.p10_19;

/**
 * 15. Lattice paths
 * 
 * Starting in the top left corner of a 2×2 grid, and only being able to move to
 * the right and down, there are exactly 6 routes to the bottom right corner.
 * 
 * How many such routes are there through a 20×20 grid?
 * 
 * Answer: 137846528820 Completed on Tue, 26 Feb 2014, 09:59
 * http://projecteuler.net/problem=15
 * 
 * @author SBT
 * 
 */
public class Problem15 {

	/**
	 * The simplest way to do this is dynamic programming. There are 2 parts,
	 * the upper left triangle and lower right triangle. We go from lower right
	 * where it's a typical Yanghui triangle: 1 1, 1 2 1, 1 3 3 1, 1 4 6 4 1，etc
	 * with each number meaning the possible path from all the points on the
	 * n-th 45 degree line with x axis. The second part is to merge two by two
	 * the diagonal.
	 */
	public static void main(String[] args) {
		// Dimension - 1 of the grid as input:
		int size = 21;
		// Initiate the two counters
		long[] counter1 = new long[size];
		long[] counter2 = new long[size];
		for (long i : counter1) {
			i = 0;
		}
		for (long i : counter2) {
			i = 0l;
		}
		counter1[0] = 1;
		counter1[1] = 1;

		// Get the 20th Yanghui triangle array value
		for (int i = 0; i < size - 2; i++) {
			if (i % 2 == 0) {
				counter2[0] = counter1[0];
				for (int j = 1; j < size; j++) {
					counter2[j] = counter1[j] + counter1[j - 1];
				}
			} else {
				counter1[0] = counter2[0];
				for (int j = 1; j < size; j++) {
					counter1[j] = counter2[j] + counter2[j - 1];
				}
			}
		}
		System.out.println();
		for (int i = size - 1; i > 0; i--) {
			if (i % 2 != 0) {
				for (int j = 0; j < i; j++) {
					counter2[j] = counter1[j] + counter1[j + 1];
				}
			}else {
				for (int j = 0; j < i; j++) {
					counter1[j] = counter2[j] + counter2[j + 1];
				}
			}
		}
		
		System.out.println(counter2[0]);
	}

}
