import configparser

def add_servers_to_serverclass(serverclass_conf_path, serverclass_name, new_server_hosts):
    config = configparser.ConfigParser()
    config.read(serverclass_conf_path)

    if serverclass_name not in config.sections():
        print(f"{serverclass_name} class not found in serverclass.conf.")
        return

    existing_hosts = set(config.get(serverclass_name, 'whitelist', fallback='').split(','))

    added_hosts = []

    for new_server_host in [host.strip() for host in new_server_hosts.split(',')]:
        if new_server_host in existing_hosts:
            print(f"Host {new_server_host} is already mapped to {serverclass_name} class.")
        else:
            existing_whitelist = config.get(serverclass_name, 'whitelist', fallback='')
            updated_whitelist = f"{existing_whitelist},{new_server_host}" if existing_whitelist else new_server_host
            config.set(serverclass_name, 'whitelist', updated_whitelist)
            added_hosts.append(new_server_host)

    with open(serverclass_conf_path, 'w') as configfile:
        config.write(configfile)

    if added_hosts:
        print(f"Successfully added {', '.join(added_hosts)} to {serverclass_name} class.")

# Example usage
serverclass_conf_path = 'serverclass.conf'
serverclass_name = 'role_power'
new_server_hosts = 'host1, host2, host3'

add_servers_to_serverclass(serverclass_conf_path, serverclass_name, new_server_hosts)
