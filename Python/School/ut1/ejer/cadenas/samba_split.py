# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    third_slash = smb_path[2:].index('/') + 2
    host = smb_path[2:third_slash]
    path = smb_path[third_slash:]

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')
