package problems;


/**
 * Largest palindrome product
 * Problem 4
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 ¡Á 99.
 * 
 * Find the largest palindrome made from the product of two 3-digit numbers.
 * 
 * 
 * Answer:
 * 906609
 * Completed on Sun, 24 Nov 2013, 17:19
 * http://projecteuler.net/problem=4
 * 
 * 
 * @author SBT
 *
 */
public class Problem4 {
	
	public static void main(String [] args) {
		long start = System.currentTimeMillis();
		method1();
		long mid1 = System.currentTimeMillis();
		method2();
		long mid2 = System.currentTimeMillis();
		method3();
		long finish = System.currentTimeMillis();
		System.out.println("Method 1 : " + (mid1 - start));
		System.out.println("Method 2 : " + (mid2 - mid1));
		System.out.println("Method 3 : " + (finish - mid2));
	}
	
	// Here I use number first, to search down from 999 * 999
	public static void method1(){
		int num = 999 * 999;
		for (int i = num; i > 0; i--) {
			if (isPalindrome2(i)) {
				for (int j = 100; j < 1000; j++) {
					if (i % j == 0 && i / j > 100 && i / j < 1000) {
						System.out.println("Answer is : " + i);
						return;
					}
				}
			}
		}
	}
	
	// Another way in the answer page is to go from a = 100 down to 999 and b = 100 down to 999
	// There are improvements to be made
	public static void  method2() {
		int last = 0;
		int a,b;
		a = 100;
		while (a <= 999) {
			b = 100;
			while (b <= 999) {
				if (isPalindrome2(a * b) && a * b > last) {
					last = a * b;
				}
				b++;
			}
			a++;
		}
		System.out.println("Answer is : " + last);
	}
	
	// Fastest solution after test
	public static void  method3() {
		int last = 0;
		int a,b,db;
		a = 1000;
		while (a >= 100) {
			if (a % 11 == 0) {
				b = 999;
				db = 1;
			}else {
				b = 999;
				db = 11;
			}
			while (b >= a) {
				if (a * b <= last) {
					break;
				}
				if (isPalindrome2(a * b)) {
					last = a * b;
				}
				b = b - db;
			}
			a--;
		}
		System.out.println("Answer is : " + last);
	}
	
	public static boolean isPalindrome(int num) {
		char [] numchar = String.valueOf(num).toCharArray();
		int len = numchar.length;
		for (int i = 0; i < len / 2; i++) {
			if (numchar[i] != numchar[len - i - 1]) {
				return false;
			}
		}
		return true;
	}
	// This a better solution...
	public static boolean isPalindrome2(int num) {
		int reverse = 0, original = num;
		while (original > 0) {
			reverse = reverse * 10 + original % 10;
			original = original / 10;
		}
		return reverse == num;
	}
}
