# SpicyScopes

SpicyScopes is a command-line interface (CLI) tool that retrieves in-scope domains from the HackerOne API.

## Installation

1. Ensure that Python 3 is installed on your system.
2. Clone the SpicyScopes repository:

   ```shell
   git clone https://github.com/k0nf/spicyscopes.git
   ```

3. Navigate to the project directory:

   ```shell
   cd spicyscopes
   ```

4. Install the project dependencies using `pip`:

   ```shell
   pip install -r requirements.txt
   ```

5. (Optional) If you want to install SpicyScopes as a system-wide command, run the following command:

   ```shell
   python setup.py install
   ```

   This will install the `spicyscopes` command globally, allowing you to use it from anywhere on your system.

## Usage

To use SpicyScopes, open a terminal or command prompt and navigate to the project directory.

The general syntax of the command is as follows:

```shell
spicyscopes --program <programId> --api-key <apiKey>
```

- `<programId>`: The ID of the HackerOne program.
- `<apiKey>`: Your HackerOne API key.

Examples:

```shell
# Retrieve in-scope domains for program with ID 123
spicyscopes --program 123 --api-key <yourApiKey>

# Retrieve in-scope domains for program with ID 456
spicyscopes --program 456 --api-key <yourApiKey>
```

The results will be displayed in the terminal, and the in-scope domains will be saved to a TXT file and the asset details will be saved to a JSON file.

For more information and available options, use the `--help` option:

```shell
spicyscopes --help
```

## Uninstalling

To uninstall SpicyScopes from your system, you can use the `pip` package manager:

```shell
pip uninstall spicyscopes
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Please update the README file as needed to reflect the specific details and options of your SpicyScopes project.