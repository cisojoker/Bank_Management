# Bank Management System

This is a simple bank management system implemented in Python with MySQL database integration. It provides basic functionalities for managing customer accounts, including adding customers, viewing customer details, depositing and withdrawing money, and closing accounts.

## Features

- **Add Customer**: Add a new customer to the bank database with details such as account number, name, age, occupation, address, mobile number, Aadhaar number, initial balance, and account type.
- **View Customer**: View customer details by searching with criteria such as account number, name, mobile number, or Aadhaar number.
- **Deposit Money**: Deposit money into a customer's account and update the balance accordingly.
- **Withdraw Money**: Withdraw money from a customer's account if sufficient balance is available and update the balance.
- **Close Account**: Close a customer's account permanently by deleting their record from the database.
- **View All Customer Details**: View all customer details along with their total deposited amount and month.

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` library
- `pandas` library

## Usage

1. Clone the repository:


2. Install the required dependencies:


3. Configure MySQL settings in the script:

- Update `host`, `user`, `password`, and `database` variables in the script according to your MySQL server configuration.

4. Run the script:


5. Follow the on-screen prompts to perform various operations.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
