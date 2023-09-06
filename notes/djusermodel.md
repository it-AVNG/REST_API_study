# Django authentication
Built in authentication system 
framework included basic features:
+ registreation
+ Login
+auth
Integrated with django admin

# Django user Model
+ Foundataion of the auth system it is also the basic Default usermodel
+ problem with default: use username not emai, not easy to customize
+ Create a custom model for project ist the *recommended* approach: use email login and future proofing for later changes

# how to customize:
- Create a mode : base on `AbstractbaseUser` and `PermissionMixin`
- Create custom manage: used for CLI integration
- Set `AUTH_USER-MODEL` in `settings.py`

## AbstractBaseUser:
+ provided features for authentication
+ doesnt include fields

## PermissionMixin:
+ Support for Django permission system
+ Includes fields and methods

## Notes:
+ Running migratio before setting custom model --> need to clear migration and set custom model first
+ avoid typos in config 
+ indentation in manager 

# usermodelDesign
+ email(EmailField)
+ name(CharField)
+ is_active,is_staff(BooleanField)

## UserModel manager
+ used to manage objects
+ custom Logic for creating objects: hashing password
+ used CLI : create Superuser

## baseUserManager:
+ Base class for managing users
+ Usedful helper methods: normalize_email: for storing emails consistently
+ Methods we will define:
    - `create_user`: called when creating user
    - `create_superuser`: Used by the CLI to create superuser
    
