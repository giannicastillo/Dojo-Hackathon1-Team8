from refugeeresourceproject_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


DB = 'project_database_name'

class projectClass:
    def __init__(self, data):
        self.id = data['id']
        pass

    @classmethod
    def save_PLACEHOLDER(cls, data):
        query = "INSERT INTO projectTable (xx, xx, xx) VALUES (%(xx)s, %(xx)s, %(xx)s);"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def show_all_PLACEHOLDER(cls):
        query = "SELECT * FROM projectTable;" # may need an extender for bringing in user data
        projectTable_from_db = connectToMySQL(DB).query_db(query)
        all_projectTable = []
        for x in projectTable_from_db:
            all_projectTable.append(cls(x))
        return all_projectTable

    @classmethod
    def show_PLACEHOLDER(cls, data):
        query = "SELECT * FROM projectTable WHERE projectTable.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        projectTable = cls(result[0])
        return projectTable

    @classmethod
    def update_PLACEHOLDER(cls,data):
        query = "UPDATE projectTable SET xx=%(xx)s, xx=%(xx)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def delete_PLACEHOLDER(cls,data):
        query = "DELETE FROM projectTable WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

# multijoin methods and queries
    @classmethod
    def new_placeholder(cls,data):
        query = 'INSERT INTO skeptics (user_id, sighting_id, skeptic) VALUES (%(user_id)s, %(sighting_id)s, %(skeptic)s);'
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def placeholder_update(cls,data):
        query = 'UPDATE skeptics SET user_id=%(user_id)s, sighting_id=%(sighting_id)s, skeptic=%(skeptic)s, updated_at=NOW() WHERE skeptics.id = %(skeptic_id)s;'
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def get_placeholder(cls,id):
        data = {
            'id': id
        }
        query = 'SELECT users.id AS user_id, skeptics.id AS skeptic_id, CONCAT(users.first_name, " ", users.last_name) AS skeptic_name FROM users LEFT JOIN skeptics ON users.id = skeptics.user_id LEFT JOIN sightings ON skeptics.sighting_id = sightings.id WHERE sightings.id = %(id)s AND skeptics.skeptic = 1;'
        return connectToMySQL(DB).query_db(query,data)

@staticmethod
    def validate_PLACEHOLDER(placeholder):
        is_valid = True
        if not placeholder['placeholder']:
            flash('This is a required field', 'error_placeholder')
            is_valid = False
        elif len(placeholder['placeholder']) < 3:
            flash('Please be more expansive.', 'error_placeholder')
        if not placeholder['placeholder']:
            flash('This is a required field.', 'error_placeholder')
            is_valid = False
        elif len(placeholder['placeholder']) < 5:
            flash('You need to tell us more than that!', 'error_placeholder')
            is_valid = False
        if not placeholder['placeholder']:
            flash('This is a required field.', 'error_when')
        if not placeholder['placeholder']:
            flash('This is a required field.', 'error_placeholder')
            is_valid = False
        elif int(placeholder['placeholder']) < 1:
            flash('There must be at least 1 squatch... WTF?', 'error_placeholder')
            is_valid = False
        return is_valid


# bcrypt.generate_password_hash(password_string) <--- create hash
# bcrypt.check_password_hash(hashed_password, password_string) <--- compare hash to pwd