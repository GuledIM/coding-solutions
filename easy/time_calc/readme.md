# 🕒 Time Calculator

A simple Python script that calculates the end time of an event, given a **start time** (hours and minutes) and a **duration** in minutes. This solution handles arbitrary durations and wraps around the 24-hour clock correctly.

---

## 🔍 Scenario

You are given:

* A **start time**, represented as two integers:

  * Hours (0–23)
  * Minutes (0–59)
* A **duration** in minutes (can be a large number).

Your task is to compute and print the **end time** in the `HH:MM` format.

---

## ✅ Example

### Sample Input

```
Start Hour:   12  
Start Minute: 17  
Duration:     59
```

### Output

```
13:16
```

### Sample Input

```
Start Hour:   23  
Start Minute: 58  
Duration:     642
```

### Output

```
10:40
```

---

## 🧠 Key Logic

* Total the **start time** in minutes.
* Add the **duration**.
* Convert the resulting total minutes back into hours and minutes.
* Use the modulo operator `%` to handle the 24-hour format and minute wrapping:

  * Hours: `(total_minutes // 60) % 24`
  * Minutes: `total_minutes % 60`

---

## 🧪 Test Data

| Start Hour | Start Minute | Duration | Expected Output |
| ---------- | ------------ | -------- | --------------- |
| 12         | 17           | 59       | 13:16           |
| 23         | 58           | 642      | 10:40           |
| 0          | 1            | 2939     | 1:00            |

---

## 🚀 How to Run

1. Clone or download the repository.
2. Run the script using Python 3:

   ```bash
   python time_calc.py
   ```
3. Follow the prompts or provide input values directly in the script.

---

## 🛠 Notes

* This script assumes all inputs are valid integers.
* No validation is performed for negative inputs or values outside typical ranges.
* The focus is on correctly handling **valid input** and producing the correct output.

---
