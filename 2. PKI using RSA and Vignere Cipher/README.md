# Assignment 2   
A public key infrastructure (PKI) is an arrangement that binds public keys with respective
identities of entities (like people and organizations). The binding is established through a process
of registration and issuance of certificates at and by a certificate authority (CA).The primary role
of the CA is to digitally sign and publish the public key bound to a given user. This is done using
the CA's own private key, so that trust in the user key relies on one's trust in the validity of the
CA's key.   
Consider a mixed encryption scheme, which combines asymmetric key scheme with symmetric
key scheme. We can define a mixed encryption scheme for transmitting a message m by user a A
to a user B, as follows:   
Let m : message,   
k : key of a symmetric key scheme,     
Cs : cipher text obtained after applying key k over m i.e. E(m, k) = Cs.  
skA and pkA be the secret and public keys respectively of public key scheme for user A.

Encryption by user A, works as:
cs <- E(m, k), (c, k') <- E(D(cs, k, skA), pkB)

Decryption by user B, works as:
(cs, k) <- E(D(c, k', skB), pkA), if D(cs, sk) = m then output (m), otherwise reject

Implement the following modules (independent), using RSA as asymmetric key scheme and
Vigenere as symmetric key scheme:

1. Generation of keys: generation of keys by CA for the users, using only strong primes and
    publish the public key, digitally signed by CA, in a directory. Private Key will be handed
    over to the individual user only.
2. Encryption by the sender.
3. Decryption by recipient.

To reduce the computation time use Chinese remainder theorem in applying sk.

You can use download The GNU Multiple Precision Arithmetic Library and include in your
program to handle large integers.


