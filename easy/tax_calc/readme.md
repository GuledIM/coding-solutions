# 🧾 Personal Income Tax (PIT) Calculator – Python

## 📜 Scenario

In a fictional land of milk and honey, citizens are required to pay an annual **Personal Income Tax (PIT)** based on their yearly income. The tax system is progressive and uses a two-tier formula:

* If **income ≤ 85,528 thalers**:

  * Tax = **18% of income – 556.02 thalers (tax relief)**
* If **income > 85,528 thalers**:

  * Tax = **14,839.02 + 32% of income exceeding 85,528 thalers**

This tax calculator implements the logic above.

---

## 💡 Features

* Accepts a single input: annual income (float).
* Applies the appropriate tax rule based on income.
* Uses `round()` to round the final tax to the nearest whole thaler.
* Ensures tax is never negative (minimum value is 0).

---

## 🧮 Example Calculations

| Income (thalers) | Tax Calculation                        | Final Tax (rounded) |
| ---------------- | -------------------------------------- | ------------------- |
| 50,000           | (18% × 50,000) – 556.02 = 8,443.98     | 8,444               |
| 100,000          | 14,839.02 + (32% × (100,000 – 85,528)) | 18,700              |
| 10,000           | (18% × 10,000) – 556.02 = 1,243.98     | 1,244               |
| 2,000            | (18% × 2,000) – 556.02 = –196.02 → 0   | 0                   |

---

## 🧪 How to Run

```bash
python tax_calc.py
```

Then enter an income value when prompted, e.g.:

```
Enter your annual income: 50000
Your tax is: 8444 thalers
```

---

## 🛠 Technologies Used

* Python 3.x
* Built-in `round()` function
* Basic control flow (`if` / `else`)

---

## 📁 File Structure

```
tax_calculator.py       # Main Python file with tax calculation logic
README.md               # This documentation
```

---

## 📌 Notes

* The calculator assumes all values are in **thalers**.
* Negative tax values are adjusted to zero, as per the rules of the fictional country.
* This is a beginner-friendly exercise meant to strengthen conditional logic and mathematical reasoning.

---
