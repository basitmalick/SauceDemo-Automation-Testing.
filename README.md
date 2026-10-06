# 🤖 SauceDemo Automation Testing

### 🚀 Selenium + Python + PyTest Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge\&logo=selenium\&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-Testing-0A9EDC?style=for-the-badge)
![POM](https://img.shields.io/badge/Framework-Page%20Object%20Model-orange?style=for-the-badge)
![HTML Report](https://img.shields.io/badge/Report-HTML-purple?style=for-the-badge)

---

## 🚀 Project Overview

**SauceDemo Automation Testing** is an automated web application testing project developed using **Python, Selenium WebDriver, PyTest, and Page Object Model (POM)**.

The project automates important end-to-end user workflows of the SauceDemo e-commerce application.

The framework demonstrates practical skills in:

* 🤖 Test Automation
* 🐍 Python
* 🌐 Selenium WebDriver
* 🧪 PyTest
* 🏗️ Page Object Model
* 📊 HTML Test Reporting
* 🔍 Automated Validation
* 📸 Test Execution Evidence

---

# 🎯 Application Under Test

**Application:** SauceDemo
**Testing Type:** Automation Testing
**Framework:** Selenium WebDriver + PyTest
**Programming Language:** Python

Application URL:

```text
https://www.saucedemo.com/
```

---

# 🏗️ Automation Framework

The project follows the **Page Object Model (POM)** design pattern.

```text
Test Cases
     ↓
Page Objects
     ↓
Selenium WebDriver
     ↓
SauceDemo Application
     ↓
Assertions / Results
     ↓
HTML Report
```

POM helps keep the test code organized, reusable, and easier to maintain.

---

# 🧪 Automated Test Modules

### 🔐 1. Login Automation

Automates:

* Valid username
* Valid password
* Login button
* Successful login validation
* Inventory page verification

Test credentials:

```text
Username: standard_user
Password: secret_sauce
```

---

### 🛍️ 2. Product Automation

Automates verification of:

* Product list
* Product names
* Product descriptions
* Product prices
* Product images
* Product sorting

Sorting options tested:

* A → Z
* Z → A
* Price Low → High
* Price High → Low

---

### 🛒 3. Cart Automation

Automates:

* Add product to cart
* Add multiple products
* Cart item count
* Open cart
* Verify cart products
* Remove product
* Continue shopping
* Add product again

---

### 💳 4. Checkout Automation

Automates the complete checkout workflow:

```text
Login
  ↓
Select Products
  ↓
Add to Cart
  ↓
Open Cart
  ↓
Checkout
  ↓
Enter Customer Information
  ↓
Verify Products
  ↓
Verify Prices
  ↓
Verify Subtotal
  ↓
Verify Tax
  ↓
Verify Total
  ↓
Finish Order
  ↓
Verify Order Confirmation
```

Expected confirmation:

```text
Thank you for your order!
```

---

# 📁 Project Structure

```text
SauceDemo-Automation-Testing/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── Test/
│   ├── __init__.py
│   ├── login_test.py
│   ├── product_test.py
│   ├── cart_test.py
│   └── checkout_test.py
│
├── screenshots/
│   ├── project_structure.png
│   ├── test_execution_passed.png
│   └── automation_report.png
│
├── reports/
│   └── automation_report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# 🧩 Technologies Used

| Technology         | Purpose              |
| ------------------ | -------------------- |
| Python             | Programming Language |
| Selenium WebDriver | Browser Automation   |
| PyTest             | Test Framework       |
| Page Object Model  | Framework Design     |
| PyTest HTML        | Test Reporting       |
| Chrome             | Browser              |
| Git & GitHub       | Version Control      |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate to the project:

```bash
cd SauceDemo-Automation-Testing
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Tests

Run all automation tests:

```bash
pytest Test/ -v
```

Generate HTML report:

```bash
pytest Test/ -v --html=reports/automation_report.html --self-contained-html
```

---

# 📊 Test Report

The project generates an HTML automation report containing:

* Test cases
* Test status
* Execution time
* Passed tests
* Failed tests
* Error details

Example:

```text
========================
3 passed
========================
```

The generated report is available in:

```text
reports/automation_report.html
```

---

# 📸 Test Evidence

Screenshots are included to demonstrate:

* Automation framework structure
* Test execution
* Passed test results
* HTML automation report

---

# 🛠️ Automation Skills Demonstrated

* Selenium WebDriver
* Python Automation
* PyTest
* Page Object Model (POM)
* Web Element Locators
* Explicit Waits
* Assertions
* Test Fixtures
* `conftest.py`
* Test Organization
* End-to-End Testing
* Functional Automation
* Regression Automation
* HTML Reporting
* GitHub Project Documentation

---

# 🎯 Project Objective

The objective of this project is to demonstrate practical **Selenium Web Automation and Software Quality Assurance skills** by building a maintainable automation framework and automating important end-to-end workflows of a real-world e-commerce application.

---

# 👨‍💻 Tester / Automation Engineer

**Abdul Basit**

BS Software Engineering
Software Quality Assurance / Test Automation

---

# ⭐ Project Highlights

✔ Python + Selenium
✔ PyTest Framework
✔ Page Object Model
✔ Login Automation
✔ Product Testing
✔ Cart Testing
✔ Checkout Testing
✔ End-to-End Automation
✔ Explicit Waits
✔ Assertions
✔ HTML Test Reports
✔ GitHub Documentation
✔ Test Execution Screenshots
