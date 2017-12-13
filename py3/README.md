## Usage

The code works with both python 2 & 3.
For string input, decrypted message in python 2.x will be a string, as compared to a byte string in python 3.x. 
Other than that there are no major differences.

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

You can view anyone's public key but cannot alter it directly.
```python
>>> A.public_key = (2,3)
Exception: You are not allowed to alter generated keys
>> A.public_key
(56618467399119298776135038168667997056624964942029346840873882494861567586229L, 92020774583088837673591629484044516416427751099585188055672485398962861161269L)
```

Digital signatures can be achieved in a similar manner. Alice signs a string or number with her private key.
```python
>>> sign_a = A.sign("Alice's Signature")
```

Bob or Eve can verify this. It can only be verified with Alice's public key.
```python
>>> B.verify(sign_a, A.public_key)
"Alice's Signature"
>>> E.verify(sign_a, A.public_key)
"Alice's Signature"
>>> B.verify(sign_a, E.public_key)
'\x1cv\x04@j\xf2\x04\x83!\xab\x01uN\xd8\x02Y\xc8\xd43\rD\x59c9I@c\x92\x0c)/\xe2\x9c0'
```

The `process_string()` and `recover_string` `@classmethod`s are used to convert between byte strings and long integers. It is a slightly simplified version of the code [here](https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Util/number.py)

```python
>>> RSA.process_string("Hi Bob")
79616349990754
>> RSA.process_string("Hi Bob what's up?")
24640066858828187311071388516817835487295L
>>> RSA.recover_string(79616349990754)
'Hi Bob'
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
