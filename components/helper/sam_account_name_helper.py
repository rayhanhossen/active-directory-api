from api.models import ADUser
from components.helper import first_name_excluded_list


def create_sam_account_name(first_name, last_name, employee_id):
    SAM_account_name_options = list()
    for name in first_name_excluded_list:
        first_name = first_name.lstrip(name)

    first_first_name = first_name.split()[0]
    first_last_name = last_name.split()[0]
    # Sam account name creation Option
    SAM_account_name_options.append(first_first_name + '.' + first_last_name)
    SAM_account_name_options.append(first_last_name + '.' + first_first_name)
    SAM_account_name_options.append(first_first_name[0] + '.' + first_last_name)
    SAM_account_name_options.append(first_first_name + '.' + first_last_name[0])
    SAM_account_name_options.append(first_name.replace(" ", ""))
    SAM_account_name_options.append(last_name.replace(" ", ""))
    SAM_account_name_options.append(first_first_name + str(employee_id)[-4:])
    SAM_account_name_options.append(first_last_name + str(employee_id)[-4:])

    for option in SAM_account_name_options:
        if not ADUser.objects.filter(SAM_account_name=option).exists():
            return option.lower()

    raise Exception('SAM account name could not be created')
