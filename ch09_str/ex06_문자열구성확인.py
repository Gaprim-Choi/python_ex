print('python'.isalpha())#True

print('Ver. 3.x'.isalpha())#False

print('12345'.isdigit())#True
print('12345abc'.isdigit())#False

print('   '.isspace())#True
print(' 1 '.isspace())#False

print('PYTHON'.isupper())#True
print('Python'.isupper())#False


string1 = 'Python is powerfull. PYTHON IS EASY TO LEARN'
print(string1.lower())
print(string1.upper())