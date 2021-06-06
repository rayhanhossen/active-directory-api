def parse_domain(parent_ou):
    parent_ou_data = parent_ou.split(',')
    domain_data = []
    for x in parent_ou_data:
        found = x.find('dc')
        if found == 0:
            found_data = x.split('=')[1]
            domain_data.append(found_data)
    organization_name = domain_data[0]
    domain_suffix1 = domain_data[1]
    domain = f'@{organization_name}.{domain_suffix1}'
    if len(domain_data) == 3:
        domain_suffix2 = domain_data[2]
        domain = f'{domain}.{domain_suffix2}'
    return domain
