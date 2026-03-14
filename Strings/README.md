# Valid Palindrome

## Problem

Given a string `s`, determine if it is a **palindrome**, considering only **alphanumeric characters** and ignoring **cases**.

A palindrome reads the same **forward and backward**.

---

## Example

### Example 1

Input

```
s = "A man, a plan, a canal: Panama"
```

Output

```
true
```

Explanation
After removing non-alphanumeric characters and converting to lowercase:

```
amanaplanacanalpanama
```

This reads the same forward and backward.

---

### Example 2

Input

```
s = "race a car"
```

Output

```
false
```

---

## Approach

1. Remove all **non-alphanumeric characters**.
2. Convert the remaining characters to **lowercase**.
3. Compare the cleaned string with its **reverse**.
4. If both are equal → the string is a palindrome.

---

## Python Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]
```

---

## Explanation

```
cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
```

* `isalnum()` → keeps only letters and numbers
* `lower()` → converts characters to lowercase
* `join()` → builds the cleaned string

```
cleaned[::-1]
```

* Reverses the string using Python slicing.

Then we compare:

```
cleaned == cleaned[::-1]
```

If both are the same → palindrome.

---

## Complexity Analysis

Time Complexity

```
O(n)
```

Space Complexity

```
O(n)
```

Where `n` is the length of the string.

---

## Tags

* String
* Two Pointers
* Palindrome
