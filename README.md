# pycipher
### Simple caesar cipher script

Usage: python3 caesar_cipher.py [message] [rotations] [back=False]

### Example

encrypt message:
```
$ python3 caesar_cipher.py "how you doin'?" 5
> "back" parameter set to [False] by default
> how you doin'? ---> mtb dtz itns'?
```
decrypt message:
```
$ python3 caesar_cipher.py "mtb dtz itns'?" 5 True
> mtb dtz itns'? ---> how you doin'?
```
