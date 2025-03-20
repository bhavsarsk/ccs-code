// Function to compute GCD
public static int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to calculate modular exponentiation (base^exp % mod)
public static BigInteger modExp(BigInteger base, BigInteger exp, BigInteger mod) {
    return base.modPow(exp, mod);
}

public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // Taking user input for p and q
    System.out.print("Enter a prime number (p): ");
    int p = scanner.nextInt();
    
    System.out.print("Enter another prime number (q): ");
    int q = scanner.nextInt();

    int n = p * q;      
    int phi = (p - 1) * (q - 1); 

    // Choosing e such that 1 < e < phi and gcd(e, phi) = 1
    int e = 2;
    while (e < phi && gcd(e, phi) != 1) {
        e++;
    }

    // Compute d (modular inverse of e mod phi)
    int d = 1;
    while ((d * e) % phi != 1) {
        d++;
    }

    // Display public and private keys
    System.out.println("\nPublic Key: (" + e + ", " + n + ")");
    System.out.println("Private Key: (" + d + ", " + n + ")");

    // Taking user input for message
    System.out.print("\nEnter a number to encrypt (should be < " + n + "): ");
    int message = scanner.nextInt();

    scanner.close();

    // Encryption
    BigInteger encrypted = modExp(BigInteger.valueOf(message), BigInteger.valueOf(e), BigInteger.valueOf(n));
    System.out.println("Encrypted message: " + encrypted);

    // Decryption
    BigInteger decrypted = modExp(encrypted, BigInteger.valueOf(d), BigInteger.valueOf(n));
    System.out.println("Decrypted message: " + decrypted);
}