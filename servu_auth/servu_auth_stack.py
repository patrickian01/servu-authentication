from aws_cdk import core, aws_cognito


class ServuAuthStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        servu_userpool = aws_cognito.UserPool(
            self,
            'servu-userpool',
            user_pool_name='ServU Users',
            sign_in_aliases=aws_cognito.SignInAliases(email=True),
            standard_attributes=aws_cognito.StandardAttributes(
                email=aws_cognito.StandardAttribute(required=True, mutable=True),
                fullname=aws_cognito.StandardAttribute(required=True, mutable=True),
                address=aws_cognito.StandardAttribute(required=True, mutable=True),
                phone_number=aws_cognito.StandardAttribute(required=True, mutable=True)
            ),
            password_policy=aws_cognito.PasswordPolicy(
                min_length=8,
                require_digits=True,
                require_lowercase=True,
                require_symbols=True,
                require_uppercase=True,
                temp_password_validity=core.Duration.days(1)
            ),
            sign_in_case_sensitive=False
        )

        servu_userpool_web_client = aws_cognito.UserPoolClient(
            self,
            'servu-userpool-web-client',
            user_pool=servu_userpool,
            auth_flows=aws_cognito.AuthFlow(
                custom=True,
                refresh_token=True,
                user_srp=True
            ),
            user_pool_client_name='ServU Web Client'
        )

        # TODO: Manually configure the domain and callback URLs. Look at CFN for the Pool ID and Client ID
        core.CfnOutput(
            self,
            'servu-userpool-id',
            value=servu_userpool.user_pool_id,
            export_name='servu-userpool-id'
        )

        core.CfnOutput(
            self,
            'servu-userpool-client-id',
            value=servu_userpool_web_client.user_pool_client_id,
            export_name='servu-userpool-client-id'
        )
