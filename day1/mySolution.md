### Day-1
- The dial starts with 50 as default.
- then what we can do is have a value counter `zero_counter` which tracks the total number of times the dial is at zero 
---
### Step 0 - Extract the values of the instructions
- this is the can be done by simply putting the instructions in a `input.txt` file then can be read line by line.
- for removing existing blank spaces - just trim it.
- we can choose our increment and decrement after that by knowing the first element of the string or line
- can be done via `if "L" in trimmedLine:` or `if line.startswith("L"):`
- values can be separated via `a = int(line[1:])`

### Step 1 - Making a `Dial` class
- This can be done without making a class, may be even faster.But via making a class this whole thing becomes much simpler.
- So I chose to do it via making a class.
- make a class named `Dial`
- its value `val` is 50 on the time of creation of instance.
- There are 2 methods : one for increment and other for decrement. 



![class](<Screenshot 2025-12-02 at 11.33.36 AM.png>)
---