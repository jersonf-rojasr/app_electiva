import bcrypt

def encryp_pass(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('UTF-8'),salt)
    return hashed

def verify_pass(stored_hash, password):
    return bcrypt.checkpw(password.encode('UTF-8'),stored_hash)
