# Caesar Cipher ROT13 Tool

A command line tool to encode or decode text with the letter substitution cipher also known as Caesar cipher. ROT*n* rotates the letters by _n_ places.
Because there are 26 letter in the basic Latin alphabet, ROT13 is its own inverse. To decode a text encoded by ROT13, simply apply ROT13 on the text again.

## Usage

The rotation is set to 13 as a default but can be changed by giving an argument.
There are three ways to use **caesar**.

### Text as argument

The easiest way to encode or decode text with **caesar** is to simply pass text as an argument in the command line:

```
python3 caesar.py "Hello World!"
```

Output:

```
Rotation: 13
Hello World!
Uryyb Jbeyq!
```

If the text is still encoded you can pass an a second argument after the text to set the rotation:

```
python3 caesar.py "Khoor Zruog!" -3
```

Output:

```
Rotation: -3
Khoor Zruog!
Hello World!
```

### File as argument

You can pass a file with text as an argument to **caesar**:
The file _text.txt_ contains the following text:

```
Why did the chicken cross the road?
Gb trg gb gur bgure fvqr!
```

Decode text:

```
python3 caesar.py text.txt
```

Output:

```
Rotation: 13
Jul qvq gur puvpxra pebff gur ebnq?

To get to the other side!
Increase or set rotation and run again? (yes/no/set)
```

**caesar** will ask you if you want to increase or set a new rotation in case the text is still encoded:

- `yes` : rotation will be increased by 1 and the text will be decoded again.
- `no` : program will quit
- `set` : you will be asked to enter a new rotation and the text will be decoded again.

### Interactive Mode

You can start _Interactive Mode_ by not providing any arguments or passing a hyphen '`-`' as the first argument.
In _Interactive Mode_ any text you enter will be encoded/decoded by the given rotation(default=13).
To exit _Interactive Mode_, simply use the key-combination **`CTRL+C`**.

```
python3 caesar.py
```

Output:

```
--- Interactive Mode --- (Press 'Ctrl + c' to exit)
Rotation: 13
```

Type text to encode/decode and press **`ENTER`**:

```
Hello World!
Uryyb Jbeyq!
```

To quit _Interactive Mode_ use **`CTRL+C`**

```
--- Exit Interactive Mode ---
```

![Visitors](https://api.visitorbadge.io/api/VisitorHit?user=toshydev&repo=caesar&countColor=%237B1E7A)
