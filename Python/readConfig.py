import configparser

# Create a configparser object and read the configuration file
config = configparser.ConfigParser()
config.read('./connection.ini')

# Read name-value pairs from the 'Database' section
database_host = config.get('Database', 'host')
database_port = config.getint('Database', 'port')
database_username = config.get('Database', 'username')
database_password = config.get('Database', 'password')

# Read name-value pairs from the 'App' section
app_debug = config.getboolean('App', 'debug')

# Print the values
print("Database Configuration:")
print(f"Host: {database_host}")
print(f"Port: {database_port}")
print(f"Username: {database_username}")
print(f"Password: {database_password}")

print("\nApp Configuration:")
print(f"Debug Mode: {app_debug}")
