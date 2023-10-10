<p align="center">
<img src="https://github.com/rubikproxy/ServerMonPy/assets/84948167/033af428-8b97-4ed4-ae69-795f2be7d174" width="200" height="200"></img>
</p>
<h1 align="center">ServerMonPy - Welcome to ServerMonPy - Real-time Server Monitoring 2023</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Version-2.3.1-green?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-rubikproxy-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-lightblue?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-darkcyan?style=flat-square">
</p>

- Download: https://pypi.org/project/ServerMonPy/
- Source: https://github.com/rubikproxy/ServerMonPy
- Docs: https://rubikproxy.github.io/ServerMonPy/
- GUI : https://github.com/rubikproxy/ServerMonPy/releases

In an increasingly interconnected world, the reliable and efficient operation of servers and remote machines is paramount. 
Whether you are managing a critical infrastructure, a cloud-based application, or a personal server, 
having real-time insights into system performance is invaluable. That's where ServerMonPy comes into play.

Features
========

ServerMonPy is a powerful Python package and command-line tool designed to empower system administrators, 
DevOps professionals, and developers with the ability to monitor remote servers and machines in real-time, 
effortlessly. It leverages the simplicity and security of SSH (Secure Shell) connections to provide you with critical 
insights into the performance and health of your systems.

1. Real-Time Monitoring
ServerMonPy excels at real-time monitoring, delivering vital information about your remote server's performance as it happens. With just a few simple commands, you can gain immediate insights into CPU usage, memory utilization, network activity, and more.

2. Secure Authentication
Authentication is a cornerstone of secure server management. ServerMonPy ensures your credentials are protected by utilizing SSH for secure and encrypted connections. Your login credentials remain confidential throughout the monitoring process.

3. User-Friendly Interfaces
The command-line interface of ServerMonPy is designed for simplicity and ease of use. Anyone, from beginners to seasoned professionals, can quickly grasp its functionality and start monitoring servers with confidence.

4. Customizable Monitoring
We understand that different users have unique monitoring needs. ServerMonPy provides customization options, allowing you to tailor monitoring intervals and parameters to match your specific requirements.

Installing
==========
The tool will prompt you for the hostname or public IP, your username, and securely obtain your password. Once authenticated, 
real-time monitoring begins, displaying a wealth of information about your remote server's performance.

``pip install ServerMonPy``

Project Information
===================

Project documentation can be found
`here <http://ServerMonPy-mail.readthedocs.org/>`__

## Fork and Contribute

We welcome and encourage contributions from the open-source community. If you find a bug, have a feature request, or want to improve **ServerMonPy**, here's how you can contribute:

1. **Fork the Repository**: Click the "Fork" button at the top-right corner of this repository to create your own copy.

2. **Clone your Fork**: Use `git clone` to clone your forked repository to your local machine.

    ```bash
    git clone https://github.com/rubikproxy/ServerMonPy.git
    ```

3. **Create a New Branch**: Create a new branch for your changes.

    ```bash
    git checkout -b feature-or-fix-name
    ```

4. **Make Changes**: Make your desired changes or additions to the code.

5. **Test**: Ensure that your changes don't introduce new issues and pass existing tests.

6. **Commit Changes**: Commit your changes with clear and concise commit messages.

    ```bash
    git commit -m "Add feature: YourFeatureName"
    ```

7. **Push to Your Fork**: Push your changes to your fork on GitHub.

    ```bash
    git push origin feature-or-fix-name
    ```

8. **Open a Pull Request**: Go to the [original repository](https://github.com/rubikproxy/ServerMonPy) and open a pull request from your branch to the `main` branch of the original repository.

9. **Discuss and Review**: Collaborate with other contributors and maintainers to review your changes. Be open to feedback and address any necessary adjustments.

10. **Merge**: Once your pull request is approved, it will be merged into the main project.

11. **Congratulations**: You've successfully contributed to **ServerMonPy**! Your changes will now be part of this open-source project.
Thank you for helping improve **ServerMonPy**! Your contributions are valuable to the community.

Source
------

You can find the source on GitHub:

[click here](https://github.com/rubikproxy/ServerMonPy)

Advanced Usage 
------

For advanced users and developers, ServerMonPy can be integrated into your own Python projects. 
Import the main function and incorporate server monitoring into your scripts and applications, 
giving you even more flexibility and control.

```
from ServerMonPy import main

if __name__ == "__main__":
    main()
```

License
-------

ServerMonPy is released under the MIT License , which can be found [click here](https://github.com/rubikproxy/ServerMonPy/blob/main/LICENSE)

## Testing
-------

We take testing seriously to maintain the reliability and quality of **ServerMonPy**. To contribute effectively or use the tool with confidence, it's crucial to understand how to run tests and ensure everything is working as expected.

### Running Tests

To run the project's tests locally, follow these steps:

1. **Clone the Repository**: If you haven't already, clone the **ServerMonPy** repository to your local machine.

    ```bash
    git clone https://github.com/OriginalRepoOwner/ServerMonPy.git
    ```

2. **Install Dependencies**: Ensure you have the required dependencies installed. You can install them using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Navigate to the Tests Directory**: Change your working directory to the `tests` folder.

    ```bash
    cd ServerMonPy/tests
    ```

4. **Run the Tests**: Execute the test suite using your preferred test runner, typically `unittest` or `pytest`.

    For `unittest`:

    ```bash
    python -m unittest test_main.py
    ```

    For `pytest`:

    ```bash
    pytest test_main.py
    ```

### Writing New Tests

Contributions that include new functionality or bug fixes should ideally include corresponding tests. These tests help maintain and improve code quality.

1. **Create a New Test File**: If necessary, create a new test file in the `tests` directory. Test files should have names following the convention `test_*.py`.

2. **Write Your Tests**: Add test cases using the testing framework of your choice (e.g., `unittest`, `pytest`). Ensure your test cases cover the intended behavior.

3. **Run Your Tests**: Execute your new tests to ensure they pass and do not introduce new issues.

4. **Submit a Pull Request**: When you submit your changes, include your new tests in the pull request. This helps reviewers understand the purpose and functionality of your code.

### Continuous Integration (CI)

Our project uses continuous integration (CI) to automatically run tests on every pull request. This ensures that changes are tested in a controlled environment and helps maintain code quality.

### Reporting Issues

If you encounter any issues while running tests or have questions about testing procedures, please [open an issue](https://github.com/rubikproxy/ServerMonPy/issues). We'll be happy to assist you.

By contributing to testing and maintaining test coverage, you play a vital role in the ongoing reliability and stability of **ServerMonPy**.

Thank you for your commitment to quality and your contributions to the project!


Development
===========

ServerMonPy is written entirely in Python and runs on Python 3. It should hopefully
run on any platform that supports Python and has Unix semantics.

If you find yourself lost in source code, just yell.

PEP-8 should be followed where possible, but feel free to ignore the 80
character limit it imposes (120 is a good marker IMO).

## Contributors
1. [LOGU](https://www.linkedin.com/in/logu-k/)
2. [GANESAN](https://www.linkedin.com/in/ganesan-perumal/)
3. [SURESH](https://github.com/SureshGitLab)
4. [HEMACHANDERAN-R](https://www.linkedin.com/in/hemachandran-r-4b409a255/)
5. [SANJAY KUMAR](https://www.linkedin.com/in/rubikproxy/)
