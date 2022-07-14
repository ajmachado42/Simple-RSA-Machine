print("Welcome back! Arendt is pleased to see you, again. Please enter your encryption list - no brackets, please:")
z = input()



z = list(map(int, z.split(',')))
p = 13 # integer greater than or equal to 13
q = 17 # integer greater than or equal to 17
n = p * q # public key
e = 5 # public key
i = 2



def f(n):
    
    """phi function of n
    Argument: n
    Output: p*q-p-q+1"""
    
    return int((p - 1)*(q - 1))



d = int(((i * f(n)) + 1) / e) # private key



num_caps_alpha = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z", 27:" "}



def e_decryption(list):
    
    """
    To return the decrypted list of integers representing the cyphered user input
    Argument: encryption list
    Output: cypher list"""
    
    e_to_d= []
    for number in list:
        decrypted = int((number**d)%n)
        e_to_d.append(decrypted)
        
    return e_to_d

decryption = e_decryption(z)



def reverse_cypher(decryption):
    
    """To send the decrypted message back through the cypher and get the original message as a string
    Argument: Decryption list
    Output: Decyphered list"""
    
    d_to_l = []
    for int in decryption:
        letter = num_caps_alpha.get(int)
        d_to_l.append(letter)
    return d_to_l

r_cypher = reverse_cypher(decryption)



cypher_string = ""
print("Your original input text was: ", cypher_string.join(r_cypher))
print("ET VOILÀ!!!")
