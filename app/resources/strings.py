# API messages

USER_DOES_NOT_EXIST_ERROR = "user does not exist"
ARTICLE_DOES_NOT_EXIST_ERROR = "article does not exist"
ARTICLE_ALREADY_EXISTS = "article already exists"
USER_IS_NOT_AUTHOR_OF_ARTICLE = "you are not an author of this article"

INCORRECT_LOGIN_INPUT = "incorrect email or password"
USERNAME_TAKEN = "user with this username already exists"
EMAIL_TAKEN = "user with this email already exists"

UNABLE_TO_FOLLOW_YOURSELF = "user can not follow him self"
UNABLE_TO_UNSUBSCRIBE_FROM_YOURSELF = "user can not unsubscribe from him self"
USER_IS_NOT_FOLLOWED = "you don't follow this user"
USER_IS_ALREADY_FOLLOWED = "you follow this user already"

WRONG_TOKEN_PREFIX = "unsupported authorization type"  # noqa: S105
MALFORMED_PAYLOAD = "could not validate credentials"

ARTICLE_IS_ALREADY_FAVORITED = "you are already marked this articles as favorite"
ARTICLE_IS_NOT_FAVORITED = "article is not favorited"

COMMENT_DOES_NOT_EXIST = "comment does not exist"

AUTHENTICATION_REQUIRED = "authentication required"

### Flags

BrokenFunctionLevelAuthorization = "flag{I_aM_Th3_aDm1n_H3r3!}"
BrokenUserAuthentication = "flag{F33l_My_V01t_Tack13!}"
BOLA = "flag{B0lA!!!!!}"
ImproperAssetsManagement = "flag{Impr0peR_Ass3ts_ManAg3m3nt}"
Injection = "flag{1nject10n_Ap1}"
ExcessiveDataExposure = "flag{3xc3ss1v3_daTa_Xp0sur3}"

# Description
DescriptionImproperAssetsManagement = "Old API versions are usually unpatched and are an easy way to compromise " \
                                      "systems without having to fight " \
                                      "state-of-the-art security mechanisms, which might be in place to protect the " \
                                      "most recent API versions. "
DescriptionInjection = "Attackers will feed the API with " \
                       "malicious data through whatever " \
                       "injection vectors are available " \
                       "(e.g., direct input, parameters, " \
                       "integrated services, etc.), " \
                       "expecting it to be sent to an " \
                       "interpreter"
DescriptionExcessiveDataExposure = "Exploitation of Excessive Data " \
                                   "Exposure is simple, and is usually " \
                                   "performed by sniffing the traffic " \
                                   "to analyze the API responses, " \
                                   "looking for sensitive data " \
                                   "exposure that should not be " \
                                   "returned to the user."
DescriptionBOLA = "APIs tend to expose endpoints that handle object identifiers, " \
                  "creating a wide attack surface Level Access Control issue. Object " \
                  "level authorization checks should be considered in every function " \
                  "that accesses a data source using an input from the user."
