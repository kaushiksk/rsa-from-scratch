## Usage

The code works with mode python2 and python3. Decrypted message in python2 will be a string, as compared to byte string in python3. Other than that there are no major differences.

```python
>>> from rsa import RSA
>>> A = RSA()  # Alice
>>> B = RSA()  # Bob
>>> E = RSA()  # Eve
```

Alice wants to talk to Bob so she will encrypt her message using Bob's public key
```python
>>> ciphertext_B = A.encrypt("Hello Bob", B.public_key)
>>> B.decrypt(ciphertext_B) 
'Hello Bob'
```

If Eve tries to decrypt this
```python
>>> E.decrypt(ciphertext_B)
'\x12\x0eA\x8c\xc5\x1f\xa1\x05\xfe\x80Q\x1e\x1b|\xbb\xb8\xe9\xa6\x84\xc1\xda\x8b:XC\xed\x91\xb8\x12q\x11\xd9'
```

The above result may vary as the keys are randomly generated each time.

The API remains the same for numbers
```python
>>> ciphertext_E = A.encrypt(123456789, E.public_key)
>>> E.decrypt(ciphertext_E)
123456789L
>>> B.decrypt(ciphertext_E)
4081228201739686282145927510867027940582326297585236661320804597753581131993L
```

## Functions Implemented

- [x] Modular exponentiation
- [x] Euler's method for gcd
- [x] Extended Euler's Algorithm
- [x] Modular Multiplicative Inverse
- [x] Sieve of Eratosthenes
- [x] Euler Totient function
- [x] Legendre Symbol
- [x] Jacobi Symbol
 - Primality test
   - [x] Fermat's Primality Test
   - [x] Solovay-Strassen Primality Test
   - [x] Miller Rabin Primality Test
 - RSA
   - [x] Prime number generation/selection
   - [x] Key generation
   - [x] Encryption
   - [x] Decryption
   - [x] Signing
   - [x] Verification
## Extras
 - Integer Factorization
   - [ ] Pollard's Rho method
   - [ ] Pollard's p-1 method
