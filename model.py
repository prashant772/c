from flask_restful_swagger_2 import Schema


class EmailModel(Schema):
    type = 'string'
    format = 'email'




    


class doctorSignupModel(Schema):
    type = 'object'
    properties = {
        'userID': {
            'type': 'varchar',
           
        },
        'name': {
            'type': 'string'
        },
        'email': EmailModel,
        'age': {
            'type': 'integer',
            'format': 'int32',
        },
        'password':{'type':'varchar'},
        'speciality':{'type':'string'},
        'qualification':{'type':'string'},
        'experience':{'type':'varchar'},
        'previously':{'type':'string'}
    }
    required = ['name,userID,email']





class doctorupdateProfileModel(Schema):
    type = 'object'
    properties = {
        'userID': {
            'type': 'varchar',
           
        },
        'name': {
            'type': 'string'
        },
        'email': EmailModel,
        'age': {
            'type': 'integer',
            'format': 'int32',
        },
        'speciality':{'type':'string'},
        'qualification':{'type':'string'},
        'experience':{'type':'varchar'},
        'previously':{'type':'string'}
    }
    required = ['name,userID,email']






class patientSignupModel(Schema):
    type = 'object'
    properties = {
        'userID': {
            'type': 'varchar',
           
        },
        'name': {
            'type': 'string'
        },
        'email': EmailModel,
        'age': {
            'type': 'integer',
            'format': 'int32',
        },
        'password':{'type':'varchar'},
        'dob':{'type':'string'},
        'address':{'type':'string'},
        'gender':{'type':'string'},
        'pincode':{'type':'string'},
        'first':{'type':'string'},
        'healthIssue':{'type':'string'}
    }
    required = ['name,userID,email']




class patientupdateProfileModel(Schema):
    type = 'object'
    properties = {
        'userID': {
            'type': 'varchar',
           
        },
        'name': {
            'type': 'string'
        },
        'email': EmailModel,
        'age': {
            'type': 'integer',
            'format': 'int32',
        },
       
        'dob':{'type':'string'},
        'address':{'type':'string'},
        'gender':{'type':'string'},
        'pincode':{'type':'string'},
        'first':{'type':'string'},
        'healthIssue':{'type':'string'}
    }
    required = ['name,userID,email']






class doctorLoginModel(Schema):
    type = 'object'
    properties = {
        'password': {
            'type': 'varchar',
           
        },
        'name': {
            'type': 'string'
        }
        
    }
    required = ['name,password']




class doctorProfileModel(Schema):
    type = 'object'
    properties = {
        'userID': {
            'type': 'varchar',
           
        }
    }
    required = ['userID']


class patientLoginModel(Schema):
    type = 'object'
    properties = {
        'password': {
            'type': 'varchar',
           
        },
        'name': {
            'type': 'string'
        }
        
    }
    required = ['name,password']




class patientProfileModel(Schema):
    type = 'object'
    properties = {
        'userID': {
            'type': 'varchar',
           
        }
    }
    required = ['userID']




class ErrorModel(Schema):
    type = 'object'
    properties = {
        'message': {
            'type': 'string'
        }
    }
