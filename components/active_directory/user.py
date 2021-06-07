from components.active_directory.connect import Connect
from components.helper.domain_helper import parse_domain
from components.helper.password_helper import get_random_password
from decouple import config


class UserManager:

    def __init__(self):
        self.connect = Connect(config('AD_SERVER_ADDRESS'), config('AD_USER_NAME'),
                               config('AD_PASSWORD')).connect_server()

    def create_user(self, employee):
        current_user = 'cn=' + employee.SAM_account_name + ',' + employee.parent_OU
        domain = parse_domain(employee.parent_OU)
        # concat variable for add user
        user_principle = employee.SAM_account_name + domain
        display = employee.first_name + "/" + employee.division + "/" + employee.full_name + "(Email: " + user_principle + ")"
        department = employee.department + "|" + employee.division
        ad_name = employee.first_name + "_" + employee.division + "_" + employee.designation + "_" + employee.full_name
        attribute = {
            'objectClass': 'User',
            'cn': ad_name,
            'profilePath': employee.parent_OU,
            'sAMAccountName': employee.SAM_account_name,
            'pager': employee.pager,
            'displayName': display,
            'userPrincipalName': user_principle,
            'department': department,
            'givenName': employee.first_name,
            'sn': employee.last_name,
            'description': employee.description,
            'title': employee.job_title,
            'mobile': employee.phone_number,
            'physicalDeliveryOfficeName': employee.office,
            'streetAddress': employee.address1,
            'postOfficeBox': employee.address2,
            'l': employee.address3,
            'postalCode': employee.PO,
            'st': employee.state,
            'co': employee.country
        }
        if employee.manager:
            attribute['manager'] = f'CN={employee.manager},{employee.parent_OU}'
        self.connect.add(current_user, attributes=attribute)
        ad_response = self.connect.result
        print(f'ADD User Response- {ad_response}')
        # add password for user
        self.generate_ad_password(current_user)

        return user_principle, ad_response

    def disable_user(self, ad_users):
        self.connect.modify('cn=' + ad_users.SAM_account_name + ',' + ad_users.parent_OU, {'userAccountControl': [('MODIFY_REPLACE', 2)]})
        ad_response = self.connect.result
        print(f'Disable User Response- {ad_response}')
        return ad_response

    def add_user_in_group(self):
        pass

    def generate_ad_password(self, user_dn):
        # get random password
        random_password = get_random_password(10)
        # set user password
        self.connect.extend.microsoft.modify_password(user_dn, random_password)
        print(f'ADD Password Response- {self.connect.result}')
