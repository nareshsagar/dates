import configparser

def add_servers_to_serverclass(serverclass_conf_path, serverclass_name, new_server_ips):
    config = configparser.ConfigParser()
    config.read(serverclass_conf_path)

    if serverclass_name not in config.sections():
        print(f"{serverclass_name} class not found in serverclass.conf.")
        return

    existing_servers = set()
    for key, value in config.items(serverclass_name):
        if key.startswith("whitelist"):
            existing_servers.add(value)

    added_servers = []

    for new_server_ip in [ip.strip() for ip in new_server_ips.split(',')]:
        if new_server_ip in existing_servers:
            print(f"Server {new_server_ip} is already mapped to {serverclass_name} class.")
        else: ki
            whitelist_key = f"whitelist.{len(existing_servers) + 1}"
            config.set(serverclass_name, whitelist_key, new_server_ip)
            added_servers.append(new_server_ip)

    with open(serverclass_conf_path, 'w') as configfile:
        config.write(configfile)

    if added_servers:
        print(f"Successfully added {', '.join(added_servers)} to {serverclass_name} class.")


add_servers_to_serverclass("serverclass.conf", "my_serverclass", "host3, host4")


import configparser

def remove_servers_from_serverclass(serverclass_conf_path, serverclass_name, server_ips_to_remove):
    config = configparser.ConfigParser()
    config.read(serverclass_conf_path)

    if serverclass_name not in config.sections():
        print(f"{serverclass_name} class not found in serverclass.conf.")
        return

    existing_servers = config.get(serverclass_name, 'whitelist', fallback='').split(',')

    removed_servers = []

    for server_ip_to_remove in [ip.strip() for ip in server_ips_to_remove.split(',')]:
        if server_ip_to_remove in existing_servers:
            existing_servers.remove(server_ip_to_remove)
            removed_servers.append(server_ip_to_remove)
        else:
            print(f"Server {server_ip_to_remove} is not found in {serverclass_name} class.")

    config.set(serverclass_name, 'whitelist', ','.join(existing_servers))

    with open(serverclass_conf_path, 'w') as configfile:
        config.write(configfile)

    if removed_servers:
        print(f"Successfully removed {', '.join(removed_servers)} from {serverclass_name} class.")


