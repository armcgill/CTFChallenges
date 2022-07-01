# CTFChallenges

*Shhh! It's a secret:*

Type: Cryptography

Difficulty: Medium 

Prompt: 

```
A new cryptographic exchange method used in RFC 2409 is supposedly unbreakable. There is something 
about this that looks familiar - I wonder if you can discover the shared secret between them. 

p = 9839 
g = 823


A = 6781
B = 6030


Note: Submit the secret wrapped in flag{}
```

Walkthrough: 

Step 1: 
From looking at the variables given, (or referring to RFC 2409) it can be easily deduced that Diffie Hellman is the cryptography scheme being used. Fortunately we have both parties public keys and the p value is small enough for us to brute force it with a simple script. 

Step 2:
We can write a python script that tries every value from 1 - p to solve for the secret value. From there we can determine the shared secret they used to communicate with. 
```
for i in range(1,9839):
    if (823 ** i) % 9839 == 6781:
        print(str((6030 ** i) % 9839))
        exit()
```
Step 3: 
Congratulations you have found the flag {8431}

